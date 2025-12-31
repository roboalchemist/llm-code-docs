# Source: https://learn.sparkfun.com/tutorials/sparkfun-gps-breakout---xa1110-qwiic-hookup-guide

## Introduction

The [XA1110 GPS module](https://www.sparkfun.com/products/14414) from GTOP is a rare bird indeed. GPS modules are hard to come by, but an I^2^C GPS+GLONASS module? Now we\'re cooking with peanut oil! This small module also utilizes the MediaTek MT3333 chipset, loaded with specialized SparkFun firmware that enables both I^2^C and Serial ports simultaneously. Using I^2^C means you won\'t have to tie up your serial port with GPS, leaving it open to other possibilities.

[![SparkFun GPS Breakout - XA1110 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/4/0/14414-SparkFun_GPS_Breakout_-_XA1110__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-xa1110-qwiic.html)

### [SparkFun GPS Breakout - XA1110 (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-xa1110-qwiic.html) 

[ GPS-14414 ]

The SparkFun XA1110 GPS Breakout is a small I2C-supported module built for easy hookup, thanks to our Qwiic Connect System. E...

[ [\$35.95] ]

This module is configured with an on-board RTC battery that enables a warm-start functionality. (Giving the XA1110 just five seconds to first fix) A U.FL connector gives you the option to hook up an [external antenna](https://www.sparkfun.com/products/464) via a [U.FL cable](https://www.sparkfun.com/products/9145)

This hookup guide will show you how to get started figuring out where on Earth you are. You\'ll also learn how to change the update rate of the GPS up to 10 Hz as well as change the baud rate.

### Required Materials

To get started, you\'ll need a microcontroller to, well, control everything.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

[![Raspberry Pi 3](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/1/8/13825-01.jpg)](https://www.sparkfun.com/products/13825)

### [Raspberry Pi 3](https://www.sparkfun.com/products/13825) 

[ DEV-13825 ]

Everyone knows and loves Raspberry Pi, but what if you didn\'t need additional peripherals to make it wireless. The Raspberry ...

**Retired**

Now to get into the Qwiic ecosystem, the key will be one of the following Qwiic shields to match your preference of microcontroller:

[![SparkFun Qwiic HAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/5/14459-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html)

### [SparkFun Qwiic HAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html) 

[ DEV-14459 ]

The SparkFun Qwiic HAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still u...

[ [\$6.95] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

You will also need a Qwiic cable to connect the shield to your GPS module, choose a length that suits your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

## Hardware Overview

Below is a table listing all of the hardware features and specs for the XA1110.

  **Characteristic**    **Range**
  --------------------- ---------------------------------------------------------------------------------------------------
  Operating Voltage     3.3V: **Regulated to 1.8V - 3.6V**
  Current               25 mA (typical)
  Hot/Warm/Cold Start   1/5/15 seconds
  Update Rate           1 Hz (default), 0.1-10 Hz
  I^2^C Interface       100kHz & 400kHz (3.3V)
  I^2^C Address         0x10
  UART                  9600 bps (default), 4800-115200 bps (3.3V)
  Position Accuracy     \<3.0m, \<2.5m with SBAS enabled
  Satellites            99 during search, 33 during tracking
  Sensitivity           -148dBm Acquisition, -165dBm Tracking
  Max Altitude          80km (the mesosphere) using the example configuration sketch to enable high-altitude balloon mode
  RTC Battery           5.5mAh, enables warm start for 15 days without power

### Pins

The following table lists all of the XA1110\'s pins and their functionality.

  Pin                                        Description                                                                             Direction
  ------------------------------------------ --------------------------------------------------------------------------------------- -----------
  GND                                        Ground                                                                                  In
  3.3V                                       Power                                                                                   In
  SDA                                        Data                                                                                    In
  SCL                                        Clock                                                                                   In
  [INT]   Interrupt, goes low when NMEA data is ready, after packet is read, the pin pulls high   Out
  Wake                                       Wake up                                                                                 In
  [RST]   Pulling low will reset the module                                                       In
  PPS                                        Provides one pulse-per-second signal                                                    Out
  RX                                         UART receiver; to receive commands                                                      In
  TX                                         UART transmitter; outputs GPS information                                               Out

## Optional Features

The XA1110 breakout has several optional features. The first of which is the option to disable the pulse-per-second LED. This can be done by slicing the connection on the JP5 jumper with a hobby knife. If multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by removing the solder on the pull up resistor jumper highlighted below. Both jumpers are shown in the below image.

[![pull up resitor jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/1/jumpers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/1/jumpers.png)

There is also a U.FL connector on the board, outlined below, which can be used in conjunction with the [U.FL cable](https://www.sparkfun.com/products/9145) to connect to an [external antenna](https://www.sparkfun.com/products/464)

[![U.FL connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/1/antenna.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/1/antenna.png)

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the XA1110 breakout, the other into the Qwiic Shield and you\'ll be ready to upload a sketch and figure out where you are. It seems too easy, but thats why we made it this way!

[![XA1110 plugged into shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/1/Qwic_Titan_X1_GPS_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/1/Qwic_Titan_X1_GPS_Hookup_Guide-01.jpg)

## Library Overview 

First, you\'ll need to download and install the Sparkfun I^2^C GPS library, this can be done using the button below or by using the Arduino Library Manager.

[Download the SparkFun I2C GPS Library](https://github.com/sparkfun/SparkFun_I2C_GPS_Arduino_Library/archive/master.zip)

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Before we get started developing a sketch, let\'s look at the available functions of the library.

- `boolean begin(TwoWire &wireport = Wire, uint32_t i2cSpeed = I2C_SPEED_STANDARD);` \-\-- `begin()` is used to start the GPS, it runs sort of like this:
  - Starts running the I^2^C port at the given port and clock speed
  - Pings the module and checks for a response
  - Returns `TRUE` if the response is received, `FALSE` if not.
- `void check();` \-\-- Checks the module for new data.
- `uint8_t available();` \-\-- Returns the available number of bytes. Will call check() if zero is available.
- `uint8_t read();` \-\-- Returns the next available byte.
- `void enableDebugging(Stream &debugPort = Serial);` \-\-- Outputs various messages to assist in debugging.
- `void disableDebugging();` \-\-- Pretty self explanatory, turns off debugging.
- `boolean sendMTKpacket(String command);` \-\-- Can be used to send a command or configuration to the GPS module.
  - The input buffer on the MTK is 255 bytes, so strings must be shorter than 255 bytes.
  - After ending a transmission, give the module 10 ms to process the message.
- `String createMTKpacket(uint16_t packetType, String dataField);` \-\-- Creates a config sentence (String) from a packetType and any settings. See [\'MTK NMEA Packet\'](https://cdn.sparkfun.com/assets/parts/1/2/2/8/0/PMTK_Packet_User_Manual.pdf) datasheet for more info.
- `String calcCRCforMTK(String sentence);` \-\-- XORs bytes to create MTK packet.

**Note:** Due to a new QZSS satellite recently launched by the Japanese, users in the Asia-Pacific region (Longitude 70 to -160 degrees East) can experience huge drifts in location over the course of 2 hours. In order to remedy this, two options are available. The first is to simply reset the module every 2 hours. The second option is to disable the QZSS feature entirely. To do this, simply use the following command in your setup loop. sendMTKpacket(\$PMTK352,1\*2B);

## Example Code

You should have downloaded the SparkFun I^2^C GPS Library in the previous step, if not, go back and click the button to download it. Within should be contained the library along with five examples. We\'re going to get you started with the first two examples.

Upload the following example to the microcontroller of your choice.

    language:c
    #include "SparkFun_I2C_GPS_Arduino_Library.h"
    I2CGPS myI2CGPS; //Hook object to the library

    void setup()
    
      Serial.println("GPS module found!");
    }

    void loop() //Writes GPS data to the Serial port with a baud rate of 115200
    
    }

This first example outputs the raw [NMEA sentences](http://www.gpsinformation.org/dale/nmea.htm). Which look something like this:

[![NMEA output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/1/Example1-output.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/1/Example1-output.PNG)

If your GPS doesn\'t have a satellite fix, you will simply get zeroes instead of numbers. These NMEA sentences may be a little hard to wrap your head around if you don\'t fluently speak GPS, so let\'s move onto the second example, which will take this data, and use the TinyGPS library to transform it into some sensible latitude and longitude data. The second example requires the TinyGPS library, which can be downloaded using the button below.

[Download the Tiny GPS Library](https://github.com/mikalhart/TinyGPSPlus/archive/master.zip)

The below example code will take these NMEA sentences and use the `displayInfo()` function to output some nice and friendly latitude and longitude readings.

    language:c
    #include <SparkFun_I2C_GPS_Arduino_Library.h> //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_I2C_GPS_Arduino_Library
    I2CGPS myI2CGPS; //Hook object to the library

    #include <TinyGPS++.h> //From: https://github.com/mikalhart/TinyGPSPlus
    TinyGPSPlus gps; //Declare gps object

    void setup()
    
      Serial.println("GPS module found!");
    }

    void loop()
    

      if (gps.time.isUpdated()) //Check to see if new GPS info is available
      
    }

    //Display new GPS info
    void displayInfo()
    
      else
      

      if (gps.location.isValid())
      
      else
      
    }

The output of this code in the serial monitor should look similar to the below image. If the module does not yet have a fix, you will see `Location not yet valid` instead of a latitude and longitude reading.

[![long lat output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/1/Example2-output.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/1/Example2-output.PNG)