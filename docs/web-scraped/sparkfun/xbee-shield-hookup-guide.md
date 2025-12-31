# Source: https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide

## Introduction

**Heads up!** Originally, this tutorial was written to configure an XBee Series 1 to communicate in transparency mode. However, this can apply to the XBee Series 3 module as long as you configure the firmware to the legacy 802.15.4 protocol. For more information, check out the [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) tutorial.

The [XBee Shield](https://www.sparkfun.com/products/10854) gives your Arduino a seamless interface to [XBee](https://www.sparkfun.com/categories/111) \-- one of the most popular wireless platforms around. With XBee, instead of being tied down by a serial cable \-- inches away from a paired device \-- your Arduino can pass data over the air to another device hundreds of feet away.

[![SparkFun XBee Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/9/6/9/7/12847-SparkFun_XBee_Shield-01_.jpg)](https://www.sparkfun.com/sparkfun-xbee-shield.html)

### [SparkFun XBee Shield](https://www.sparkfun.com/sparkfun-xbee-shield.html) 

[ WRL-12847 ]

The SparkFun XBee Shield mates directly with any dev board that has an Arduino standard footprint and equips it with wireless...

[ [\$21.50] ]

[![SparkFun XBee 3 Wireless Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/5/7/8/15936-SparkFun_XBee_3_Wireless_Kit-02.jpg)](https://www.sparkfun.com/sparkfun-xbee-3-wireless-kit.html)

### [SparkFun XBee 3 Wireless Kit](https://www.sparkfun.com/sparkfun-xbee-3-wireless-kit.html) 

[ KIT-15936 ]

Inside this kit you will find two XBee Modules, one XBee Explorer, one Xbee Shield and a set of Arduino R3 headers to solder ...

[ [\$87.95] ]

Part of what makes XBee so popular is its simplicity. XBees are controlled over a [serial UART interface](https://learn.sparkfun.com/tutorials/serial-communication) \-- in the most basic operation they can be used as a **wireless serial cable**. Setting up XBee networks and addresses is also simplified with Digi\'s free software \-- XCTU \-- which we explain in a [separate tutorial](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu).

### Covered In This Tutorial

The goal of this tutorial is to set up wireless XBee communication between a computer and an Arduino/XBee Shield combo. Then, using a [terminal program](https://learn.sparkfun.com/tutorials/terminal-basics), we can remotely send data to an Arduino, or read data off of it.

[![Communication example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/0/communication-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/communication-example.png)

We\'ll begin by examining the [schematics and hardware](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide/hardware-overview) of the XBee Shield, then move on to example code. First we\'ll set up a [test program](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide/example-communication-test) to make sure our XBees are communicating with each other. Then we\'ll move on to the [remote control Arduino](https://learn.sparkfun.com/tutorials/xbee-shield-hookup-guide/example-remote-control-arduino) sketch.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

- **1x [XBee Shield](https://www.sparkfun.com/products/10854)** \-- The star of this tutorial.
  - You\'ll also need **headers** to install into your shield. We recommend [stackable headers](https://www.sparkfun.com/products/11417).

- **1x Arduino** \-- The XBee Shield should work with any Arduino-compatible board \-- [Uno](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/11575), [Mega](https://www.sparkfun.com/products/11061), you name it.

- **2x XBees** \-- XBees exist in a variety of **series**, **frequencies**, and **ranges**. If you\'re just getting started with XBee, we highly recommend going with **Series 1** models \-- either with a [trace antenna](https://www.sparkfun.com/products/11215), [wire antenna](https://www.sparkfun.com/products/8665) or [u.fl connector](https://www.sparkfun.com/products/8666).

  - For more help picking an XBee, check out our [XBee Buying Guide](https://www.sparkfun.com/pages/xbee_guide).

  ::: 
  **Heads up!** While this tutorial was written for XBee Series 1, you can still follow along using XBee Series 3 modules. Just make sure to configure it with the 802.15.4 (Series 1) firmware. For more information, check out the [Exploring XBees and XCTU](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) tutorial.
  :::

- **1x Explorer** \-- The Explorer board allows you to connect an XBee to your computer. You can use either the [Explorer USB](https://www.sparkfun.com/products/11812), [Explorer USB Dongle](https://www.sparkfun.com/products/11697), or [Explorer Serial](https://www.sparkfun.com/products/9111).
  - Depending on which explorer you have, you may also need a matching [mini-B USB](https://www.sparkfun.com/products/11301) or [serial cables](https://www.sparkfun.com/products/65).

- At least one **computer with [X-CTU](http://www.digi.com/products/wireless-wired-embedded-solutions/zigbee-rf-modules/xctu)** installed.
  - The latest version of X-CTU is available for both Mac and Windows!

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

Before reading through this tutorial, we highly recommend checking out the [Exploring XBees and XCTU tutorial](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu).

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

March 12, 2015

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

That tutorial will introduce you to XCTU and explain how to configure XBee networks and addresses. In addition to that tutorial, we also recommend checking these guides out:

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication) \-- Serial communication is critical to controlling and managing XBees.
- [Arduino Shields](https://learn.sparkfun.com/tutorials/arduino-shields-v2) \-- The basics of Arduino Shields, including how to assemble a shield.
- [XBee Buying Guide](https://www.sparkfun.com/pages/xbee_guide) \-- We highly recommend **Series 1** XBee\'s, if this is your first time playing with them. If you\'re curious about other XBee classes, check out this guide!

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

## Hardware Overview

Here\'s a quick overview of the most components of the XBee Shield:

[![Annotated XBee Shield](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/shield-annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/shield-annotated.png)

Below we\'ll go more in-depth on the most important components of the shield.

### UART/Software Serial Switch

One of the most important components on the XBee Shield is the DLINE/UART switch. This switch controls which Arduino pins interface with the XBee.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/dline-switch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/dline-switch.png)

The Arduino Uno has a single hardware UART, which is usually either used for **programming** (via the Arduino\'s serial bootloader) or communication with the **serial monitor**. That serial port can only be used to communicate with one device at any time, lest you run into problems of [bus contention](https://learn.sparkfun.com/tutorials/serial-communication/common-pitfalls#busContention). There\'s also a chance that, during program upload, spurious \-- even harmful \-- data might be sent to any device attached to the Arduino\'s hardware UART.

So to avoid any problems that might arise from connecting the XBee to the Arduino\'s hardware UART, we usually take advantage of the [Software Serial library](http://arduino.cc/en/Reference/SoftwareSerial), connecting the XBee\'s RX and TX pins to a pair of free digital pins on the Arduino.

To select between software and hardware serial, the XBee Shield includes a small, surface-mount slide switch. This switch allows you to select between the hardware serial port (UART position) and a software serial port connected to pins 2 (Arduino-side RX) and 3 (Arduino-side TX).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/0/switch-schematic.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/switch-schematic.png)

*The switch configuration from the [XBee Shield schematic](http://cdn.sparkfun.com/datasheets/Dev/Arduino/Shields/xbeeshield-v14.pdf). \"D_TX\" connects to Arduino pin 3, and \"D_RX\" connects to Arduino pin 2.*

For all of our example sketches we\'ll assume the switch is in the **DLINE position**. At the very least, **make sure the switch is in the \"DLINE\" position when uploading sketches**.

### Status LED Indicators

There are 5 LEDs on the XBee Shield. Each of these LEDs connects to a pin on the XBee, which does most of the LED driving. Here\'s a table explaining the operation of each LED:

  LED Label   LED Color   XBee Pin Connection   Default Operation Notes
  ----------- ----------- --------------------- --------------------------------------------------------------------------------
  PWR         Red         3.3V                  Indicates power is present.
  DIO5        Green       Associate/DIO5        Associated indicator \-- blinks when the XBee is associated with another XBee.
  DOUT        Red         DOUT                  Indicates wireless data is being received.
  DIN         Green       DIN                   Indicates wireless data is being transmitted.
  RSSI        Green       PWM0/RSSI             Indicates relative signal strength (RSSI) of last received transmission.

These LEDs can be very useful for debugging. The DIO5/Associate indicator should blink when the XBee is paired with a compatible device. The RSSI LED is actually PWM\'d so it will be brighter when the paired XBee is closer (sending a stronger signal).

### Assembly Tips

Before you can use the XBee Shield with your Arduino, you\'ll need to solder in some headers.

[![Xbee Shield Header Install](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/0/assembly.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/assembly.png)

Check out the [assembly page of our Shield tutorial](https://learn.sparkfun.com/tutorials/arduino-shields-v2/installing-headers-preparation) for all of the tips and tricks related to header installation.

### XBee Socket

There is some white silkscreen on the Shield PCB to help orient your XBee as you\'re plugging it in. Make sure to match up the XBee\'s two diagonal edges with the two diagonal lines on the PCB.

[![XBee on XBee Shield](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/shield-assembled.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/shield-assembled.png)

With everything installed, you\'re ready for the next step! Time to code\...

## Example: Communication Test

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Double-Check Your XBee Network

**Heads up!** Make sure that the XBees are configured correctly to communicate with each other in the network.

Before continuing with this example, you\'ll need to make sure your XBee\'s are configured correctly \-- they need to be on the **same network** and have compatible **destination and MY addresses**. By default, XBees will all be compatibly configured, but we recommend setting up unique network ID\'s and addresses. Check out the [Configuring Networks](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu/configuring-networks) page of our [Exploring XBee\'s and XCTU tutorial](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu) for help with that.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

March 12, 2015

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

This example assumes you have [XCTU installed](http://www.digi.com/products/wireless-wired-embedded-solutions/zigbee-rf-modules/xctu) and two compatibly-configured XBees \-- one connected to your computer via a [USB Explorer](https://www.sparkfun.com/products/8687) (or [Dongle](https://www.sparkfun.com/products/9819), or [Serial Explorer](https://www.sparkfun.com/products/9111)) and another plugged into the Shield/Arduino.

[![XBee Shield and XBee USB Explorer](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/XBee-Pairs-plugged-in.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/XBee-Pairs-plugged-in.jpg)

### The Arduino Sketch

Let\'s start simple. In this section, we\'ll upload a sketch which passes data between your serial monitor and the XBe using the serial UART. This sketch can be use to create a \"portal of communication\" between your Arduino\'s serial monitor, and another XBee (connected to a computer via a USB Explorer). The first uses software serial defined pins on an Arduino. The second example uses the native hardware serial defined pins.

#### Software Serial Passthrough

Here\'s the sketch we\'ll use. It makes use of the [SoftwareSerial library](http://arduino.cc/en/Reference/SoftwareSerial), which is included with all of the recent Arduino releases. Before uploading this sketch, **make sure the switch on the Shield is in the \"DLINE\" position**!

Copy and upload the sketch below.

    language:c
    /*****************************************************************
    XBee_Serial_Passthrough.ino

    Set up a software serial port to pass data between an XBee Shield
    and the serial monitor.

    Hardware Hookup:
      The XBee Shield makes all of the connections you'll need
      between Arduino and XBee. If you have the shield make
      sure the SWITCH IS IN THE "DLINE" POSITION. That will connect
      the XBee's DOUT and DIN pins to Arduino pins 2 and 3.

    *****************************************************************/
    // We'll use SoftwareSerial to communicate with the XBee:
    #include <SoftwareSerial.h>

    //For Atmega328P's
    // XBee's DOUT (TX) is connected to pin 2 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 3 (Arduino's Software TX)
    SoftwareSerial XBee(2, 3); // RX, TX

    //For Atmega2560, ATmega32U4, etc.
    // XBee's DOUT (TX) is connected to pin 10 (Arduino's Software RX)
    // XBee's DIN (RX) is connected to pin 11 (Arduino's Software TX)
    //SoftwareSerial XBee(10, 11); // RX, TX

    void setup()
    

    void loop()
    
      if (XBee.available())
      
    }

[](#softwareserialpins)

#### Software Serial Note

The demo code was originally designed for the ATmega328P on the Arduino Uno. Not all the pins can support change interrupts for a serial Rx pin depending on what Arduino microcontroller is used. If you were using it with ATmega2560 (i.e. Arduino Mega 2560) or ATmega32U4 (i.e. Arduino Leonardo, Pro Micro 5V/16MHz, Pro Micro 3.3V/8Mhz, FioV3, etc.), you would need to re-define the software serial pin definitions, remove the solder jumpers for pin 3 & 2, and reroute the pins. For more information about the limitations, try looking at the Arduino reference language for the Software Serial library.\
\

[Arduino Software Serial Library](https://www.arduino.cc/en/Reference/SoftwareSerial)

##### Pin Definitions

To use re-define the software serial pins on an Arduino Mega 2560 or Arduino Leonardo, you would just need to [comment out the line](https://www.arduino.cc/reference/en/language/structure/further-syntax/singlelinecomment/) where it says:\
\

        SoftwareSerial XBee(2, 3); // RX, TX

and uncomment out the line here:\
\

        //SoftwareSerial XBee(10, 11); // RX, TX

##### Reroute Pins

To reroute the pins, on an Arduino Mega 2560 or Leonardo, you would need to remove the solder jumper and reroute pads to the respective pins.\
\

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Pins Rerouted for Arduino Mega 2560 R3](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Mega_Fritzing_bb.png "Click to Enlarge Circuit")](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Mega_Fritzing_bb.png)   [![Pins Rerouted for Arduino Leonardo w/ ATmega32U4](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Leonardo_Fritzing_bb_2.png "Click to Enlarge  Circuit")](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/SparkFun_XBee_Serial_Passthrough_Serial_UART_Jumper_Disconnected_Arduino_Leonardo_Fritzing_bb_2.png)
  *Pins Rerouted for ATmega2560-Based Arduino*                                                                                                                                                                                                                                                                                                                                                 *Pins Rerouted for ATmega32U4-Based Arduino*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] **Warning for Users *NOT* Using the Arduino Serial Monitor!** If you are using Digi\'s X-CTU or a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows) to configure or connect to an XBee by using a RedBoard/Arduino Uno as a serial passthrough, you may need to add a jumper wire between the RST and 5V pin to prevent the Arduino from resetting.\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/3/0/SparkFun_XBee_Shield_Serial_Passthrough_Serial_UART_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/SparkFun_XBee_Shield_Serial_Passthrough_Serial_UART_Fritzing_bb.png)

\
Basically when the XCTU or serial terminal opens a COM port to the Arduino, computer resets the microcontroller while looking for the XBee. Therefore, it can't communicate with the XBee because the Arduino is rebooting.

#### Hardware Serial Passthrough

This example is for those trying to use the hardware UART on an ATmega32U4-based Arduino. Copy and upload the sketch below. You can also download it [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/Leonardo_XBee_Serial_Passthrough.zip).

    language:c
    /*****************************************************************
    Leonardo_XBee_Serial_Passthrough.ino

    Set up a serial port to pass data between an XBee Shield
    and the serial monitor.

    Hardware Hookup:
      The XBee Shield makes all of the connections you'll need
      between Arduino and XBee. If you have the shield make
      sure the SWITCH IS IN THE "UART" POSITION. That will connect
      the XBee's DOUT and DIN pins to Arduino pins 0 and 1.
    *****************************************************************/

    // Leonardo Serial  is the USB port
    // Leonardo Serial1 is pins 0 and 1

    void setup()
    

    void loop()
    
      if (Serial1.available())   //XBee/UART1/pins 0 and 1
      
    }

**Note:** If you are using an Arduino Leonardo (or any ATmega32U4-based Arduino) and not a Arduino Uno, make sure to change the switch to the **hardware \"UART\"** position. In this case, do not need to add a jumper wire between the RST and GND pin.\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/2/3/0/SparkFun_XBee_Shield_Arduino_Leonardo_ATmega32U4_Fritzing_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/SparkFun_XBee_Shield_Arduino_Leonardo_ATmega32U4_Fritzing_bb.png)

\

------------------------------------------------------------------------

### What You Should See

After you\'ve uploaded the code, follow this series of steps to verify that everything is working:

1.  Open the Arduino\'s **Serial Monitor**. Make sure the baud rate is set to **9600**.
2.  Switch to XCTU and click over to **console mode**.
3.  Type something in the console view, it should show up on the Serial Monitor.
4.  Type something into the Serial Monitor (and press \"Send\"), it should show up in the console view.
5.  Yay!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/0/serial_example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/serial_example.png)

You can use this setup to create a chat system. If you have another computer nearby, try to see how far your XBees can be from each other while still reliably communicating.

If your XBee\'s aren\'t communicating with each other, try getting them closer together (if they were far apart to begin with). Otherwise, check out our [troubleshooting section](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu/troubleshooting) of the Exploring XBee tutorial.

## Example: Remote Control Arduino

Setting up a chat system is fun, but where XBees and the XBee Shield really shine is in passing data to and from an Arduino, so you can remotely control it or receive data from it. In this example, we\'ll create a simple serial interface, which can be used to set and read analog and digital pins.

### Example Sketch

Here\'s the sketch. Copy and paste from below, or [click here to download it](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/XBee_Remote_Control.zip).

    language:c
    /*****************************************************************
    XBee_Remote_Control.ino
    Write your Arduino's pins (analog or digital) or read from those
    pins (analog or digital) using a remote XBee.
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: May 7, 2014

    This sketch requires an XBee, XBee Shield and another XBee tied to
    your computer (via a USB Explorer). You can use XCTU's console, or
    another serial terminal program (even the serial monitor!), to send
    commands to the Arduino. 

    Example usage (send these commands from your computer terminal):
        w#nnn - analog WRITE pin # to nnn
          e.g. w6088 - write pin 6 to 88
        d#v   - digital WRITE pin # to v
          e.g. ddh - Write pin 13 High
        r#    - digital READ digital pin #
          e.g. r3 - Digital read pin 3
        a#    - analog READ analog pin #
          e.g. a0 - Read analog pin 0

        - Use hex values for pins 10-13
        - Upper or lowercase works
        - Use 0, l, or L to write LOW
        - Use 1, h, or H to write HIGH

    Hardware Hookup:
      The Arduino shield makes all of the connections you'll need
      between Arduino and XBee. Make sure the SWITCH IS IN THE 
      "DLINE" POSITION.

    Development environment specifics:
        IDE: Arduino 1.0.5
        Hardware Platform: SparkFun RedBoard
        XBee Shield & XBee Series 1 1mW (w/ whip antenna)
            XBee USB Explorer connected to computer with another
              XBee Series 1 1mW connected to that.

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, please 
    buy us a round!

    Distributed as-is; no warranty is given.
    *****************************************************************/
    // SoftwareSerial is used to communicate with the XBee
    #include <SoftwareSerial.h>

    SoftwareSerial XBee(2, 3); // Arduino RX, TX (XBee Dout, Din)

    void setup()
    

    void loop()
    
      }
    }

    // Write Digital Pin
    // Send a 'd' or 'D' to enter.
    // Then send a pin #
    //   Use numbers for 0-9, and hex (a, b, c, or d) for 10-13
    // Then send a value for high or low
    //   Use h, H, or 1 for HIGH. Use l, L, or 0 for LOW
    void writeDPin()
    

    // Write Analog Pin
    // Send 'w' or 'W' to enter
    // Then send a pin #
    //   Use numbers for 0-9, and hex (a, b, c, or d) for 10-13
    //   (it's not smart enough (but it could be) to error on
    //    a non-analog output pin)
    // Then send a 3-digit analog value.
    //   Must send all 3 digits, so use leading zeros if necessary.
    void writeAPin()
    

    // Read Digital Pin
    // Send 'r' or 'R' to enter
    // Then send a digital pin # to be read
    // The Arduino will print the digital reading of the pin to XBee.
    void readDPin()
    

    // Read Analog Pin
    // Send 'a' or 'A' to enter
    // Then send an analog pin # to be read.
    // The Arduino will print the analog reading of the pin to XBee.
    void readAPin()
    

    // ASCIItoHL
    // Helper function to turn an ASCII value into either HIGH or LOW
    int ASCIItoHL(char c)
    

    // ASCIItoInt
    // Helper function to turn an ASCII hex value into a 0-15 byte val
    int ASCIItoInt(char c)
    

    // printMenu
    // A big ol' string of Serial prints that print a usage menu over
    // to the other XBee.
    void printMenu()
    

Upload that, then switch over to your XCTU console window. You\'ll use the XBee connected to your computer to control and read data from your Arduino.

All of the XBee magic occurs in serial prints and reads. To send data from the Arduino XBee, `XBee.print()` and `XBee.println()`\'s are used to write strings and other data. To read data from the computer XBee, we can use `XBee.read()`, adding `XBee.available()` tests to check if data has come in. That\'s all there is to it!

Check out the comments in the code for a line-by-line dissection.

### Remote Controlling/Receiving

When the Arduino sketch first starts up, it will print a helpful usage menu. After that\'s printed, follow the directions to send commands to your Arduino. To control pins 10, 11, 12, and 13, send the [hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal) equivalent characters (A, B, C, and D).

- `w#nnn` \-- **analog write** pin `#` to `nnn`. Use leading zeros for single- and double-digit values.
  - Example: `w6088` will write pin 6 to 88
- `d#v` \-- **digital write** pin `#` to `v`. `v` can be 1, h, or H for HIGH, and 0, l, or L for LOW.
  - Example: `ddh` will write pin 13 High
- `r#` - **digital read** digital pin `#`
  - Example: `r3` will digtally read from pin 3.
- `a#` \-- **analog read** analog pin `#`
  - Example: `a0` will read analog pin 0

In each case, the Arduino will respond with the action it\'s taken after you\'ve sent a viable string.

As an initial test, try turning the D13 LED on and off, by sending `dd1` and `dd0`.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/remote-control-console.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/0/remote-control-console.png)

Then try setting analog values, or reading from pins. Maybe try making it more advanced \-- have a button press trigger an XBee communication. Or send an alert when an analog input rises past a certain threshold.

------------------------------------------------------------------------

This example barely scrapes the surface of what the Arduino-XBee combination is capable of. XBee\'s allow you to [remotely control your robot](https://www.sparkfun.com/products/12697) from the comfy confines of your computer. Or you can set up a network of XBees to monitor [carbon-monoxide](https://www.sparkfun.com/products/9403) conditions in every room, while logging to a single computer.

The power of XBees comes from their simplicity \-- they make your projects wireless by simply \"serial printing\".