# Source: https://learn.sparkfun.com/tutorials/tfmini---micro-lidar-module-qwiic-hookup-guide

## Introduction

[![SparkFun Qwiic Logo](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png)](https://www.sparkfun.com/qwiic)

\
**Heads up!** This tutorial is for the [**Qwiic**](https://www.sparkfun.com/qwiic) enabled TFMini. Serial data is output via I^2^C. If you are using the TFMini that outputs serial data via UART \[ [SEN-14588](https://www.sparkfun.com/products/14588) \], please refer to the [TFMini - Micro LiDAR Module Hookup Guide](https://learn.sparkfun.com/tutorials/tfmini---micro-lidar-module-hookup-guide).

The [TFMini](https://www.sparkfun.com/products/14786) is a ToF (Time of Flight) LiDAR sensor capable of measuring the distance to an object as close as 30 cm and as far as 12 meters! The TFMini allows you to integrate LiDAR into applications traditionally reserved for smaller sensors such as the SHARP GP-series infrared rangefinders. With the added Qwiic feature, you can quickly connect to the sensor via I2C! In this tutorial, you will learn how to connect to the TFMini using an Arduino microcontroller with the [Qwiic system](https://www.sparkfun.com/qwiic).

[![TFMini - Micro LiDAR Module (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/4/2/14786-TFMini_-_Micro_LiDAR_Module__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14786)

### [TFMini - Micro LiDAR Module (Qwiic)](https://www.sparkfun.com/products/14786) 

[ SEN-14786 ]

The TFMini is a ToF, Qwiic-enabled LiDAR sensor capable of measuring the distance to an object as close as 30 centimeters and...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Beefy 3 - FTDI Basic Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/7/6/13746-01.jpg)](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html)

### [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html) 

[ DEV-13746 ]

This is SparkFun Beefy 3 FTDI Basic Breakout for the FTDI FT231X USB to serial IC. The pinout of this board matches the FTDI ...

[ [\$18.95] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

**Tip:** You could also use RedBoard Qwiic. It\'s basically a RedBoard with additional features. The board includes the same AP2112K 3.3V voltage regulator that is populated on the Beefy 3 and Qwiic connector on the board. This would reduce the amount of components and time soldering headers to the board. Additionally, a USB port can provide up to about 500mA so the TFMini may want to pull more power when auto ranging for longer distances.\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

#### Tools

Depending on your setup, you will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

## Hardware Overview

**Note:** This product does not use laser light for ranging. Instead it contains an LED and optics. Many such systems are being marketed under the name \"LiDAR,\" although it may be more appropriate to think of this device as a \"Time-of-Flight Infrared Rangefinder\". It differs significantly from traditional IR rangefinders in that it uses ToF to determine range and not triangulation --- as is performed by the Sharp GP-series devices.

The sensor works by sending a modulated near-infrared light out. The light that is reflected from the object returns to the sensor\'s receiver. The distance between the two can be converted using the sensor by calculating the time and phase difference. The distance measured may vary depending on the environment and the reflectivity of object.

### Input Power

According to the [datasheet (pg 1)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/SJ-GU-TFmini-I__C-01__A01_-_V1.pdf), the input voltage is **5V**. In this tutorial, we will be using the included boost converter by applying a 3.3V input voltage from the Qwiic side to boost power to 5V on the TFMini side.

[![Benewake TFMini Boost Converter](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TFMini-BoostConverter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TFMini-BoostConverter.jpg)

**Current Draw:** According to the datasheet, TFMini may pull up to **\~800mA** at peak current. You may want to consider providing a sufficient power supply when using the sensor in a project. Remember, a USB port can only provide up to about 500mA. Data can be observed on the serial monitor when objects are within the \"intermediate distance\" from the Qwiic TFMini. However, you will need an external power supply as the sensor auto ranges to detect objects after a certain distance.

**⚡ Warning:** Since the Qwiic system uses 3.3V for power, the Qwiic enabled TFmini with boost circuit can exceed the maximum output rating of the 3.3V voltage regulator on the RedBoard powered by Arduino. This causes 3.3V voltage regulator to enter thermal shutdown and the RedBoard to restart. As a result, you will not be able to read the TFMini\'s output on an Arduino serial monitor.\
\

[![Insufficient 3.3V Regulator on the RedBoard for the Qwiic enabled TFMini](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/13975-04_RedBoard_3.3V_VoltageRegulator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/13975-04_RedBoard_3.3V_VoltageRegulator.jpg)

\
\
Make sure to use either the [Beefy 3](https://www.sparkfun.com/products/13746) with a 3.3V Arduino Pro Mini, [RedBoard Qwiic](https://www.sparkfun.com/products/15123), or the [LD1117V33 3.3V voltage regulator](https://www.sparkfun.com/products/526) to provide sufficient current for the TFMini. You may need to power the Qwiic TFMini with an external power supply.

### Logic Levels

While the sensor can be powered at 5V, the I2C pins are only **3.3V logic**. Make sure to use a logic level converter when reading the sensor with a 5V microcontroller.

### Pinout

There is a marking next to the polarized connector to indicate the polarity as \"**J1**\" as indicated in the image below. This is useful when referencing sensor\'s pinout. As opposed to the original TFMini, the green and white wires for the Qwiic enabled TFMini uses an I^2^C serial. The default address of the TFMini is **0x10**.

[![TFMini Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/14588-TFMini_-_Micro_Infrared_Module-03_Pinout_Qwiic_I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/14588-TFMini_-_Micro_Infrared_Module-03_Pinout_Qwiic_I2C.jpg)

  Pin Number   Wire Color   Qwiic TFMini Pinout   Wire Color
  ------------ ------------ --------------------- ------------
  1            Green        SCL (**3.3V TTL**)    Yellow
  2            White        SDA (**3.3V TTL**)    Blue
  3            Red          **5V**                Red
  4            Black        GND                   Black

## Hardware Hookup

If you haven\'t yet [assembled your 3.3V Pro Mini](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v#assembly), now would be the time to head on over to that tutorial to [solder the header pins](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). Once soldered, connect the power and I^2^C pins between the Arduino Pro Mini 3.3V/8MHz and Qwiic adapter.

  Arduino Pins   Qwiic Adapter Pins   Wire Color
  -------------- -------------------- ------------
  A5 (SCL)       SCL (**3.3V TTL**)   Yellow
  A4 (SDA)       SDA (**3.3V TTL**)   Blue
  **3.3V**       **3.3V**             Red
  GND            GND                  Black

Then connect the Qwiic cable that was included in the **Power Input** side between the Qwiic adapter and the boost circuit. On the other side, insert the second cable that was included in the **Power Output** side between from the boost circuit to the TFMini. The connectors are different on each side of the boost converter so it should not be Finally, power the circuit up with a micro-B USB cable and the Beefy 3. The connection should look like the image below.

[![Qwiic Enabled TFMini with Beefy 3 and 3.3V Arduino Pro Mini](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial_-_Hardware_Hookup_Arduino_Pro_Mini.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial_-_Hardware_Hookup_Arduino_Pro_Mini.jpg)

**Tip:** Looking to reduce the number of components? Try using the SparkX BlackBoard or RedBoard Qwiic is an alternative to connecting to the Qwiic enabled TFMini. The trade off is that the BlackBoard is larger than the Arduino Pro Mini.\
\

[![SparkX Hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial_-_Hardware_Hookup_Arduino_BlackBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial_-_Hardware_Hookup_Arduino_BlackBoard.jpg)

**Tip:** Remember, powering from a USB port can only provide about 500mA. When testing this between short and intermediate distances, the Beefy3 was sufficient enough to power both the Arduino Pro Mini 3.3V and Qwiic TFMini. You may need an external power supply when powering both at longer distances.\
\
If you are using a SparkX BlackBoard or RedBoard Qwiic with a USB cable, try powering the boards with a 9V wall adapter in addition to USB. Don\'t worry, it is acceptable to connect both a barrel jack and a USB connector at the same time. The boards have power-control circuitry to automatically select the best power source.\
\

[![Wall Adapter Power Supply - 9VDC 650mA](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/5/00298-01a.jpg)](https://www.sparkfun.com/products/298)

### [Wall Adapter Power Supply - 9VDC 650mA](https://www.sparkfun.com/products/298) 

[ TOL-00298 ]

High quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for Spark Fun Electronics. T...

**Retired**

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Grab a micro-B USB cable and connect the Arduino to your computer. Copy, paste, and upload the code below. Make sure to use the correct COM port and board selection.

    language:c
    /*
      LidarTest.ino
      Written in collaboration by Nate Seidle and Benewake

      Example sketch for the Qwiic Enabled TFMini
      (https://www.sparkfun.com/products/14786)
    */

    #include <Wire.h>

    uint16_t distance = 0; //distance
    uint16_t strength = 0; // signal strength
    uint8_t rangeType = 0; //range scale
    /*Value range:
     00 (short distance)
     03 (intermediate distance)
     07 (long distance) */

    boolean valid_data = false; //ignore invalid ranging data

    const byte sensor1 = 0x10; //TFMini I2C Address

    void setup()
    

    void loop()
    
        else 
      }
      else 
      delay(50); //Delay small amount between readings
    }

    //Write two bytes to a spot
    boolean readDistance(uint8_t deviceAddress)
    
      Wire.requestFrom(deviceAddress, (uint8_t)7); //Ask for 7 bytes

      if (Wire.available())
      
            else if (incoming == 0x01)
            
          }
          else if (x == 2)
            distance = incoming; //LSB of the distance value "Dist_L"
          else if (x == 3)
            distance |= incoming << 8; //MSB of the distance value "Dist_H"
          else if (x == 4)
            strength = incoming; //LSB of signal strength value
          else if (x == 5)
            strength |= incoming << 8; //MSB of signal strength value
          else if (x == 6)
            rangeType = incoming; //range scale
        }
      }
      else
      

      return (true);
    }

Once uploaded, try moving an object in front of the sensor to test. In the example below, a third hand was used to hold the TFMini when detecting an object at a certain distance away from the sensor. Since the sensor is not able to detect an object when less than 11.8 inches (or 30cm = 0.3m) away, the object under test was placed at 20 inches and 30 inches.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial-Distance-_20_Inches.jpg "TFMini Reading an Object at 20 Inches")](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial-Distance-_20_Inches.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial-Distance-_30_Inches.jpg "TFMini Reading an Object at 30 Inches")](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/3/TF_Mini_Qwiic_Tutorial-Distance-_30_Inches.jpg)
  *Qwiic Enabled TFMini Reading an Object at 20 Inches*                                                                                                                                                                                                                 *Qwiic Enabled TFMini Reading an Object at 30 Inches*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Opening the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200**, you may see an output similar to the values printed below. Using a yard stick, the values responded as expected when moving an object between 30 inches and 20 inches. The Qwiic enabled TFMini indicated that the object was at an \"intermediate distance\".

    TFMini I2C Test
    Data valid:         Dist[72]    strength[274]   mode[3]
    Data valid:         Dist[72]    strength[275]   mode[3]
    Data valid:         Dist[73]    strength[267]   mode[3]
    Data valid:         Dist[72]    strength[265]   mode[3]
    Data valid:         Dist[71]    strength[275]   mode[3]
    Data valid:         Dist[70]    strength[284]   mode[3]
    Data valid:         Dist[68]    strength[305]   mode[3]
    Data valid:         Dist[67]    strength[311]   mode[3]
    Data valid:         Dist[65]    strength[329]   mode[3]
    Data valid:         Dist[65]    strength[335]   mode[3]
    Data valid:         Dist[65]    strength[341]   mode[3]
    Data valid:         Dist[65]    strength[361]   mode[3]
    Data valid:         Dist[64]    strength[367]   mode[3]
    Data valid:         Dist[64]    strength[383]   mode[3]
    Data valid:         Dist[64]    strength[387]   mode[3]
    Data valid:         Dist[64]    strength[386]   mode[3]
    Data valid:         Dist[64]    strength[385]   mode[3]
    Data valid:         Dist[64]    strength[384]   mode[3]
    Data valid:         Dist[64]    strength[386]   mode[3]
    Data valid:         Dist[64]    strength[394]   mode[3]
    Data valid:         Dist[64]    strength[398]   mode[3]
    Data valid:         Dist[64]    strength[400]   mode[3]
    Data valid:         Dist[64]    strength[402]   mode[3]