# Source: https://learn.sparkfun.com/tutorials/sending-sensor-data-over-lora

## Introduction

We are on mission here at SparkFun to demonstrate the simplest ways to send sensor data using different wireless solutions. So far together we have explored [sending sensor data over wifi](https://learn.sparkfun.com/tutorials/sending-sensor-data-over-wifi/all), but what about longer range projects? Sure, we could create a mesh network of lots of boards talking to one another and it *would* be super rad, but for **long range**, why not use LoRa! In this tutorial we're going to check out what it takes to send sensor data and output that data to a screen by using two [SparkFun LoRa Thing Plus - expLoRaBLE](https://www.sparkfun.com/products/17506) development boards, and a couple of really nifty antennas; let us away!

![Sensor and LoRa Hardware](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/lora-transmitter-receiver.jpg)

*Hardware not to scale*

 

## Required Materials

Below you can find all of the parts you'll need to follow along with this tutorial; you can add what you need or if you don't have any of these parts already, you can click to the wishlist provided and purchase it all in one go! I included two USB-C cables with this list, as I found it really helpful to have them to monitor both the transmitter and receiver, but it would work fine with just one (with the receiver powered by the battery and monitored from the OLED screen). Additionally, the LoRa Fiberglass Antenna does come with an interface N to RP-SMA cable included, but I went ahead and added the part to the wishlist for reference.

**Note:** For demonstration purposes we are using the [Atmospheric Sensor Breakout](https://www.sparkfun.com/products/15440). However, this sensor could be swapped out with many of our other [sensors](https://www.sparkfun.com/categories/23). In most cases, you can find code in our product hookup guides to modify the code given below if you would like to use a different sensor.

 

 

## Hardware Hookup

This project was put together to be as simple as possible and requires two separate hardware hookups; one being the transmitter and the other the receiver. There is no soldering needed since we are utilizing our [Qwiic Connect System](https://www.sparkfun.com/qwiic) for the sensor and the OLED screen to output the data. In the photos below, we are using a USB-C connector for power but depending on your needs you can also connect a battery to the on-board JST-PH connector.

### Hooking up the LoRa Transmitter

First thing to do here is to simply connect one end of your Qwiic cable to your transmitter expLoRaBLE board, and the other to the atmospheric sensor. For the antenna you'll first need to attach the U.FL to SMA interface cables to your expLoRaBLE's U.FL connection. This connection can be a bit tricky to hook up so if this is your first time using U.FL you may want to reference [Three Quick Tips About Using U.FL](https://learn.sparkfun.com/tutorials/three-quick-tips-about-using-ufl). I *highly* recommend that you run this cable through the hole on the board (as shown below) if you aren't using it for mounting. This will add a lot of stability to your connection to the antenna and greatly reduce the risk of damaging the U.FL connectors.

[![LoRa Transmitter](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRA-transmitter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRA-transmitter.jpg)

*Very simple hardware hookup for the data transmitter.*

Once you feel confident that your interface cable isn't going anywhere, you'll be able to screw on the second interface cable, which will then attach to the end of the fiberglass antenna.

 

[![Fiberglass Antenna for LoRa](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-antenna-setup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-antenna-setup.jpg)

### Hooking up the LoRa Receiver

In a very similar fashion to the transmitter, you\'ll start by connecting one end of your Qwiic cable to your receiver expLoRaBLE board and the other end to the Micro OLED Breakout. The only difference of hooking up this antenna is that it attaches directly to the U.FL interface cable (as shown below).

[![LoRa Receiver with Antenna](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-receiver-with-antenna.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-receiver-with-antenna.jpg)

*That\'s it! About as easy as it gets.*

 

## Software Setup and Programming

To run this project, you'll need to install the following libraries:

1.  **[RadioLib](https://github.com/jgromes/RadioLib/archive/refs/heads/master.zip)** Arduino library
2.  **[SparkFun Micro OLED](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library/archive/main.zip)** library
3.  **[SparkFun BME280](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/master.zip)** Library

Aside from the above libraries you\'ll need to install the **SparkFun Apollo3 Boards** board definitions: If you need help, we\'ve put together a quick video to show how this is done.

**Note:** If you don\'t see the **SparkFun Apollo3 Boards** when searching in the boards manager, below is the `.json` file link for the SparkFun Ambiq Apollo3 Arduino Core referenced in the video above.

[`https://raw.githubusercontent.com/sparkfun/Arduino_Apollo3/master/package_sparkfun_apollo3_index.json`](https://raw.githubusercontent.com/sparkfun/Arduino_Apollo3/master/package_sparkfun_apollo3_index.json)

 

## Transmit/Receive Code

Once the libraries are installed, go ahead and open up two separate blank sketches in Arduino. One sketch will house the transmitter program, while the other will be for our receiver:

    // Peer to Peer: Monitor Sensor Data using LoRa - Transmitter
    // SparkFun Electronics, Mariah Kelly, November 2022
    // Original transmit file can be found here: https://cdn.sparkfun.com/assets/learn_tutorials/1/4/9/4/Transmit-v3.ino

    // Include necessary libraries
    #include <RadioLib.h>         // Transmit & receive - https://github.com/jgromes/RadioLib/archive/refs/heads/master.zip
    #include "SparkFunBME280.h"   // Qwiic Atmospheric Sensor library - https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/master.zip

    // SX1262 has the following connections:
    // NSS pin:   D36
    // DIO1 pin:  D40
    // NRST pin:  D44
    // BUSY pin:  D39
    SX1262 radio = new Module(D36, D40, D44, D39, SPI1);
    BME280 mySensor;

    void setup() 

      // Initialize SX1262 with default settings
      Serial.print(F("[SX1262] Initializing ... "));

      int state = radio.begin(915.0, 250.0, 7, 5, 0x34, 20, 10, 0, false);;

      if (state == RADIOLIB_ERR_NONE)  else 
    }

    void loop()  else if (state == RADIOLIB_ERR_PACKET_TOO_LONG)  else if (state == RADIOLIB_ERR_TX_TIMEOUT)  else 

      // Wait for a second before transmitting again
      delay(1000);
    }

Once your transmitter is up and running, and you're getting readings from your atmospheric sensor, we can move on to the receiver!

    // Peer to Peer: Monitor Sensor Data using LoRa - Receiver
    // SparkFun Electronics, Mariah Kelly, November 2022
    // Original receive file can be found here: https://cdn.sparkfun.com/assets/learn_tutorials/1/4/9/4/Receive-v3.ino

    // Include necessary libraries
    #include <RadioLib.h>
    #include <Wire.h>
    #include <SFE_MicroOLED.h>  // Include the SFE_MicroOLED library

    #define PIN_RESET 9
    #define DC_JUMPER 1
    MicroOLED oled(PIN_RESET, DC_JUMPER);    // I2C declaration

    // SX1262 has the following connections:
    // NSS pin:   10
    // DIO1 pin:  2
    // NRST pin:  3
    // BUSY pin:  9
    //SX1262 radio = new Module(10, 2, 3, 9);
    SX1262 radio = new Module(D36, D40, D44, D39, SPI1);

    void setup()  else 
    }

    void loop()  else if (state == RADIOLIB_ERR_RX_TIMEOUT)  else if (state == RADIOLIB_ERR_CRC_MISMATCH)  else 
    }

Now that our transmitter and receiver are chatting with each other, we can go out and test how far the signal will reach! Feel free to play around with your settings a bit, just remember to change them in both the transmitter and receiver settings AND to check your [regional LoRa Frequency Band parameters](https://resources.lora-alliance.org/technical-specifications/rp002-1-0-4-regional-parameters) (for the U.S. this range is 902 - 928MHz).

We managed to get 0.3 miles away before we had to turn around because of the highway, but were still getting a decent signal from there! Let us know how far you can go!

[![Exploring with LoRa](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-setup-with-oled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/8/LoRa-setup-with-oled.jpg)

 

## Troubleshooting

**Getting a CRC Error?**

As you explore the range of your device, you may get a "CRC Error" on your screen, meaning the packet was corrupted in some way and was not received and/or sent properly. It doesn't necessarily mean that you are out of range of your transmitter and you may still be able to receive data after seeing this error. Give it a second or two to update again to know for sure if you are out of range!