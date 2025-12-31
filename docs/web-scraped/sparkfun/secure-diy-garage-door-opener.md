# Source: https://learn.sparkfun.com/tutorials/secure-diy-garage-door-opener

## Introduction

If you\'d like to increase the security of your garage door, or you are just interested in learning more about cryptography, then read on! At its core, this project is simply about a secure wireless button. This could be used to trigger any number of things, so we hope it can inspire message security on many other future projects.

*Project showcase video.*

I was surprised to learn that even if your garage door is fairly new, then you may still be vulnerable to [man-in-the-middle](https://www.beenverified.com/crime/what-is-a-man-in-the-middle-attack/) or [roll-jam](https://www.wired.com/2015/08/hackers-tiny-device-unlocks-cars-opens-garages/) attacks. With this tutorial, you can achieve an extremely high level of security utilizing ECC signatures and the [SparkFun Cryptographic Co-processor](https://www.sparkfun.com/products/15573).

If you\'d like to read more about garage doors, here are two great articles about hacking and history.

- [Garage Door Hacking: What\'s the Deal?](https://www.garageautomatics.com/garage-door-hacking/)

- [A (Very) Short History of the Garage Door Opener](https://www.garageautomatics.com/garage-door-opener-history/)

During my research for this project, I also came across an interesting story about garage doors in San Francisco. In 2004, military radio signals were jamming garage door openers. It seems that most garage door openers at the time were operating on the same frequency as a new military communications system (390 MHz). For more details, check out this [CBS News article](https://www.cbsnews.com/news/military-jams-garage-doors-openers/). After learning this, I was glad to know that my new setup is operating on 915MHz, and so it shouldn\'t be effected.

Most communication channels are exposed to the world. Whether it\'s a hard wired connection or a wireless signal flying through the air, anyone can listen in and try to intercept, record, and/or impersonate your signal. So how do we protect ourselves against these malicious attacks? Surprisingly, you can make a very robust solution with a couple of Pro RFs and our Cryptographic Co-processors.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend you read over these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide)

### SparkFun SAMD21 Pro RF Hookup Guide 

Using the super blazing, nay blinding, fast SAMD21 whipping clock cycles at 48MHz and the RFM96 module to connect to the Things Network (and other Radio woodles).

[](https://learn.sparkfun.com/tutorials/qwiic-single-relay-hookup-guide)

### Qwiic Single Relay Hookup Guide 

Get started switching those higher power loads around with the Qwiic Single Relay.

[](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl)

### Three Quick Tips About Using U.FL 

Quick tips regarding how to connect, protect, and disconnect U.FL connectors.

[](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide)

### Cryptographic Co-Processor ATECC508A (Qwiic) Hookup Guide 

Learn how to use some of the standard features of the SparkFun Cryptographic Co-processor.

## The Secure Solution

We are going to use digital signatures to add security to our system. If you want to learn more about how to use the Cryptographic Co-processor, check out the [hookup guide](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide) and associated [video](https://youtu.be/_MjjF211BM8). These will show you the fundamental ideas behind digital signatures, walk you through how to setup each co-processor.

[](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide)

### Cryptographic Co-Processor ATECC508A (Qwiic) Hookup Guide 

October 17, 2019

Learn how to use some of the standard features of the SparkFun Cryptographic Co-processor.

For the secure garage door opener example shown here, we are going to do something very similar to [Example 6](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/example-6-challenge) in the Arduino Library. A complete cycle will follow these steps:

1.  User presses button on remote to engage cycle.
2.  Remote sends a \"request for token\".
3.  Base generates a new random token (32-bytes).
4.  Base sends token to remote.
5.  Remote creates ECC signature on token (using its unique private key).
6.  Remote sends ECC signature to base.
7.  Base verifies signature using remote\'s public key.
8.  If verified, base opens garage.

What makes this so secure is the fact that the only place in the world that can create a valid signature is inside the remote\'s co-processor. This is because the private key was generated randomly during configuration and will never leave the IC. If you don\'t have that actual piece of hardware (the remote co-processor), you will never be able to create a signature.

Also, the fact that the base creates a new random token for each cycle, allows us to prevent against [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) and [roll-jam](https://www.wired.com/2015/08/hackers-tiny-device-unlocks-cars-opens-garages/) attacks.

Wahoo! That\'s one heck of a secure wireless button!

## Hardware Overview

For this project, we need to build up two separate circuits. One will be the remote control (that lives in my car or bike), and the second will be the base transceiver that lives inside my garage (listening for the ECC signature, and then engaging the garage door button).

### Remote Control

- Pro RF
- Duck Antennae
- Cryptographic Co-processor (for creating the ECC signature)
- Enclosure
- Button
- 400mAh Lipo Battery
- Qwiic Cable (QTY:1)

### Base Transceiver

- Pro RF
- Wire antennae
- Cryptographic Co-processor (for creating the TTL token, and verifying the ECC signature)
- SparkFun Qwiic Single Relay
- Wire antennae
- USB wall wart
- Qwiic Cable (QTY:2)

For easy one click ordering, here is a wish list. Be sure to read the entire tutorial, and then adjust as necessary.

## Hardware Hookup

All of these boards use Qwiic, so that made things much easier and faster to hookup.

### The Remote

For the remote control, there are only 4 connections that need to be made:

  ----- ------------------- --------------------------- ----------------------------
        **From/Device 1**   **Connection Type**         **To/Device 2**
  1\.   Pro RF              Qwiic Cable                 Cryptographic Co-processor
  2\.   LiPo Battery        JST                         Pro RF
  3\.   Duck Antennae       U.FL to SMA adapter cable   Pro RF
  4\.   Button              Wire                        Switch Headers on Pro RF
  ----- ------------------- --------------------------- ----------------------------

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/IMG_3093.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/IMG_3093.jpg)

*The remote control all wired up.*

### The Base Transceiver

The Base Transceiver also requires hooking up just 4 connections:

  ----- ---------------------------- --------------------- ----------------------------
        **From/Device 1**            **Connection Type**   **To/Device 2**
  1\.   Power adapter                USB                   Pro RF
  2\.   Pro RF                       Qwiic Cable           Cryptographic Co-processor
  3\.   Cryptographic Co-processor   Qwiic Cable           Relay
  4\.   Relay COM & NO               Wire                  Garage door button
  ----- ---------------------------- --------------------- ----------------------------

Note, the order of boards in the qwiic system didn\'t matter, but I put the relay last so I could position it for easier access. I also [soldered to the PTH pins](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) on the bottom of the screw pin terminal, but you could choose to do a solderless connection if you like.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/IMG_3122.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/IMG_3122.jpg)

*The Base Transceiver all wired up.*

## Integration

To engage the garage door, I opted to emulate what a human does (press the button on the wall inside). I opened up the wall-mounted controller and saw this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/button1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/button1.jpg)

*The wall-mounted garage door button opened up.*

Aha! I recognize those [mini push button switches](https://www.sparkfun.com/products/97).Upon further inspection, I saw that there are various passive components involved:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/button_closeup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/button_closeup.jpg)

*Backlight exposes the copper. Hmm\... What is going on here?*

Pretty neat how they are able to get three button control from simply two wires. I wonder if there is an ADC involved? Or maybe some sort of pulsing and time sensitive digital reads? Maybe an AC signal? What do you think?

For this project, I was only concerned with the lower momentary switch (aka the \"big button\"). From looking at the circuit board with backlight as shown above, I was able to see that the lower button simply connects the two leads together directly without any extra passives involved. With this in mind, I decided to use a relay and run it in parallel with the switch. I used a [SparkFun Qwiic Single Relay](https://www.sparkfun.com/products/15093) to engage this button from my Arduino. I know this is probably overkill for the amount of current this will ever see, but I liked that this solution would be very easy to connect/control using Qwiic and was a sure bet in emulating the button.

For the connection to the garage door wall-mounted button, I chose to open it up and solder to the connection points on either side of the button. After doing so, I actually realized that you could \"tap\" into the two wires out to the button anywhere in the line and potentially use the screw pin terminals on the relay for a solder-less connection point. Nevertheless, I used a couple [XT-60 connectors](https://www.sparkfun.com/products/10474) on the lines, and this makes it pretty easy to take apart if necessary for re-programming.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/IMG_3123.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/IMG_3123.jpg)

*Some slight hacking necssary to gain access to the garage door button*

## Power Considerations

In order to save power on the remote control, I opted to put a momentary push button in series on the power input. This way, power would only be connected when I wanted to open the garage door. Otherwise, it would remain completely off. Also, with a more traditional DPST switch, we\'d be more likely to accidentally leave it switched on and drain the battery. Luckily, the ProRF has a couple headers already in the design for an external switch.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/switch_highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/switch_highlight.jpg)

*These switch headers made it easy to integrate the momentary power switch.*

Now I wanted to consider how much power is actually being used during each attempt to open the garage door. I hooked up an [SparkFun RedBoard Artemis](https://www.sparkfun.com/products/15444) and a [Zio Current and Voltage Sensor - INA219 (Qwiic)](https://www.sparkfun.com/products/15176), and I had some data streaming in no time!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/IMG_3094.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/IMG_3094.jpg)

*The Zio qwiic current setup to measure current draw on the system.*

Here is what a complete cycle looked like on the serial plotter and monitor:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/3/Annotation_2020-01-09_131555.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/3/Annotation_2020-01-09_131555.png)

*Serial plotter showing the current used during a complete cycle.*

Each reading is precisely 100ms apart, so adding them all up I can see that it will use 0.065mAh per cycle.

21 readings (2100ms) at 36mA = 0.021mAh

1 reading (100ms) at 56mA = 0.002mAh

20 readings (2000ms) at 76mA = 0.042mAh

Total: 0.065mAh

Battery capacity is 400mAh

400mAh / 0.065mAh = 6,153

So according to my rough math, I think I can press this button 6153 times with this single battery. At 2 times a day, 300 days a year (600/year), that\'s 10 years. Even with capacity loss during storage in my car (let\'s say 10% each year), it\'ll still should last\... let\'s see\...

Year: capacity : -10% - yearly use for cycles (600 \* 0.065 = \~40mAh)

Year 1 : 400 - 40 - 40 = 320

Year 2 : 320 - 32 - 40 = 248

Year 3 : 248 - 25 - 40 = 183

Year 4 : 183 - 18 - 40 = 125

Year 5 : 125 - 13 - 40 = 72

Year 6 : 72 - 7 - 40 = 25

Wahoo! Six years is pretty good. Now I just need to make sure it doesn\'t get squashed somewhere in my car.

## Arduino Code

There are two separate sketches: one for the remote control and a second for the base transceiver. You can see both sketches in the project GitHub repository located here:

[Project Github Repository (firmware)](https://github.com/lewispg228/securebutton)

The code used in this project was kept fairly clean by using three Arduino Libraries:

- [SparkFun_ATECCX08a_Arduino_Library](https://github.com/sparkfun/SparkFun_ATECCX08a_Arduino_Library)
- [SparkFun Qwiic Relay Arduino Library Github Repo](https://github.com/sparkfun/SparkFun_Qwiic_Relay_Arduino_Library)
- [Radiohead Arduino Library](https://github.com/PaulStoffregen/RadioHead)

For help with installing each necessary Arduino library, see the individual hookup guides for the [Qwiic Relay]() and [Cryptographic Co-processor](https://learn.sparkfun.com/tutorials/cryptographic-co-processor-atecc508a-qwiic-hookup-guide/introduction). But you can also check out a more general tutorial on [Arduino library installation here](https://learn.sparkfun.com/tutorials/installing-an-arduino-library):

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

January 11, 2013

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

Also, to use the SparkFun Pro RF, you will need to install the SAMD board packages. For more information on how to do that, you can take a look at [this section of the Pro RF Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide#setting-up-arduino). Now let\'s take a closer look at each individual sketch.

### Remote Control Sketch

This sketch basically does everything inside its `setup()`. This is because, it will actually remain un-powered for most of its life. When I want to power it up and begin an entire attempt cycle, I will press the momentary button on the enclosure and this will supply power.

After setting up the RF module, the cryptographic co-processor and button, the most important thing to note is that it calls \"attempt_cycle\" at the very end of `setup()`. All the good stuff happens in there!

The `attempt_cycle()` function does essentially four things:

- Engages a cycle by sending \"\$\$\$\".
- Receives 64-byte token.
- Creates the ECC signature.
- Sends Signature back to the base.

[]()

    language:c
        /*
      Remote Control
      This sketch is used to create a cryptographically secure wireless controller to open you garage.
      The complete system uses SparkFun Pro RF modules, Cryptographic Co-processors, and the qwiic relay.
      Note, it also requires a base transceiver setup with separate sketch.

      See the complete tutorial here:
      https://learn.sparkfun.com/tutorials/secure-diy-garage-door-opener

      By: Pete Lewis
      SparkFun Electronics
      Date: January 13th, 2020
      License: This code is public domain but you can buy me a beer if you use this and we meet someday (Beerware license).

      Feel like supporting our work? Please buy a board from SparkFun!
      https://www.sparkfun.com/products/15573

      Some of this code is a modified version of the example provided by the Radio Head
      Library which can be found here:
      www.github.com/PaulStoffregen/RadioHeadd

      Some of this code is a modified version of the example provided by the SparkFun ATECCX08a
      Arduino Library which can be found here:
      https://github.com/sparkfun/SparkFun_ATECCX08a_Arduino_Library
    */

    #include <SPI.h>

    //Radio Head Library:
    #include <RH_RF95.h>

    // We need to provide the RFM95 module's chip select and interrupt pins to the
    // rf95 instance below.On the SparkFun ProRF those pins are 12 and 6 respectively.
    RH_RF95 rf95(12, 6);

    int LED = 13; //Status LED is on pin 13

    int packetCounter = 0; //Counts the number of packets sent
    long timeSinceLastPacket = 0; //Tracks the time stamp of last packet received

    // The broadcast frequency is set to 921.2, but the SADM21 ProRf operates
    // anywhere in the range of 902-928MHz in the Americas.
    // Europe operates in the frequencies 863-870, center frequency at 868MHz.
    // This works but it is unknown how well the radio configures to this frequency:
    //float frequency = 864.1;
    float frequency = 921.2; //Broadcast frequency

    //////////////crypto stuff

    #include <SparkFun_ATECCX08a_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_ATECCX08a
    #include <Wire.h>

    ATECCX08A atecc;

    uint8_t token[32]; // time to live token, created randomly each authentication event

    /////////////

    byte buf[RH_RF95_MAX_MESSAGE_LEN];

    void setup()
    
      else 

      // Set frequency
      rf95.setFrequency(frequency);

      // The default transmitter power is 13dBm, using PA_BOOST.
      // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
      // you can set transmitter powers from 5 to 23 dBm:
      // Transmitter power can range from 14-20dbm.
      rf95.setTxPower(14, false);

      pinMode(5, INPUT_PULLUP);

      Wire.begin();

      if (atecc.begin() == true)
      
      else
      

      attempt_cycle();

    }

    void loop()
    
      delay(10); // button debounce
    }

    void printBuf64()
    
      SerialUSB.println("};");
      SerialUSB.println();
    }

    void printToken()
    
      SerialUSB.println("};");
      SerialUSB.println();
    }

    // Note, in Example4_Alice we are printing the signature we JUST created,
    // and it lives inside the library as a public array called "atecc.signature"
    void printSignature()
    
      SerialUSB.println("};");
      SerialUSB.println();
    }

    void attempt_cycle()
    
        else 
      }
      else 
      delay(500);
    }

### Base Transceiver Sketch

This sketch is very similar to the first Example Sketch in our hookup guide for the Pro RF: [Point to Point Radio Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-samd21-pro-rf-hookup-guide#point-to-point-radio-arduino-examples). In fact, that\'s were I started from. And then I added in the necessary libraries for the Cryptographic chip and the Qwiic relay. And then I stole some code from each of their initial examples. A whole lot of copy/paste going on. Isn\'t that convenient, Gromit!

Inside the main loop, the Base does the following:

- Listens to incoming messages.
- If it receives a \"\$\$\$\", then create a new random token and send it to remote.
- Listens for a signature from remote.
- Receives 64-byte signature.
- Verifies signature.
- If valid, trigger relay to \"close\" for 500ms, emulating a button press.
- If success hasn\'t happened within 1 second, destroy token. This protects against repeater attacks.

Note, whenever the Base hears *any* message come in, it checks for the \"\$\$\$\". This will tell it if the message is an request or a signature. If it doesn\'t see \"\$\$\$\" then it pulls in the next 64 bytes and attempts to verify the signature.

    language:c
    /*
      Base Transceiver
      This sketch is used to create a cryptographically secure wireless controller to open you garage.
      The complete system uses SparkFun Pro RF modules, Cryptographic Co-processors, and the qwiic relay.
      Note, it also requires a remote control setup with separate sketch.

      See the complete tutorial here:
      https://learn.sparkfun.com/tutorials/secure-diy-garage-door-opener

      By: Pete Lewis
      SparkFun Electronics
      Date: January 13th, 2020
      License: This code is public domain but you can buy me a beer if you use this and we meet someday (Beerware license).

      Feel like supporting our work? Please buy a board from SparkFun!
      https://www.sparkfun.com/products/15573

      Some of this code is a modified version of the example provided by the Radio Head
      Library which can be found here:
      www.github.com/PaulStoffregen/RadioHeadd

      Some of this code is a modified version of the example provided by the SparkFun ATECCX08a
      Arduino Library which can be found here:
      https://github.com/sparkfun/SparkFun_ATECCX08a_Arduino_Library

      Some of the code is a modified version of the example provided by the SparkFun Qwiic
      Relay Arduino Library which can be found here:
      https://github.com/sparkfun/SparkFun_Qwiic_Relay_Arduino_Library
    */

    #include <SPI.h>

    //Radio Head Library:
    #include <RH_RF95.h>

    // We need to provide the RFM95 module's chip select and interrupt pins to the
    // rf95 instance below.On the SparkFun ProRF those pins are 12 and 6 respectively.
    RH_RF95 rf95(12, 6);

    int LED = 13; //Status LED on pin 13

    int successLED = 3; // green
    int failLED = 4; // red
    int statLED = 2; // blue

    int packetCounter = 0; //Counts the number of packets sent
    long timeSinceLastPacket = 0; //Tracks the time stamp of last packet received
    // The broadcast frequency is set to 921.2, but the SADM21 ProRf operates
    // anywhere in the range of 902-928MHz in the Americas.
    // Europe operates in the frequencies 863-870, center frequency at
    // 868MHz.This works but it is unknown how well the radio configures to this frequency:
    //float frequency = 864.1;
    float frequency = 921.2;

    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];

    ////////////////relay

    #include "SparkFun_Qwiic_Relay.h"

    #define RELAY_ADDR 0x18 // Alternate address 0x19

    Qwiic_Relay relay(RELAY_ADDR);

    ////////////////

    /////////////////crypto

    #include <SparkFun_ATECCX08a_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_ATECCX08a
    #include <Wire.h>

    ATECCX08A atecc;

    uint8_t token[32]; // time to live token, created randomly each authentication event

    uint8_t signature[64]; // incoming signature from Alice

    int headerCount = 0; // used to count incoming "$", when we reach 3 we know it's a good fresh new message.

    // Alice's public key.
    // Note, this will be unique to each co-processor, so your will be different.
    // copy/paste Alice's true unique public key from her terminal printout in Example6_Challenge_Alice.

    uint8_t AlicesPublicKey[64] = ;

    void setup()
    
      else 

      rf95.setFrequency(frequency);

      // The default transmitter power is 13dBm, using PA_BOOST.
      // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then
      // you can set transmitter powers from 5 to 23 dBm:
      // rf95.setTxPower(14, false);

      Wire.begin();

      if (atecc.begin() == true)
      
      else
      

      if (!relay.begin())
      
      else
      

    }

    void loop()
    

            rf95.send(token, sizeof(token));
            rf95.waitPacketSent();
            SerialUSB.println("Sent token");
            digitalWrite(LED, LOW); //Turn off status LED
          }
          else // this means Alice just sent us a signature
          
            else
            
          }

        }
        else
          SerialUSB.println("Recieve failed");
      }
      //Turn off status LED if we haven't received a packet after 1s
      if (millis() - timeSinceLastPacket > 1000) 
      }
    }

    void printSignature()
    
      SerialUSB.println("};");
      SerialUSB.println();
    }

    void printBuf64()
    
      SerialUSB.println("};");
      SerialUSB.println();
    }

    void clearBuf()
    

    void blinkStatus(int LED)