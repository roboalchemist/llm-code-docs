# Source: https://learn.sparkfun.com/tutorials/tfmini---micro-lidar-module-hookup-guide

## Introduction

**Heads up!** This tutorial is for the TFMini that outputs serial data via UART. If you are using the Qwiic enabled TFMini that outputs serial data via I^2^C \[ [SEN-14786](https://www.sparkfun.com/products/14786) \], please refer to the [TFMini - Micro LiDAR Module (Qwiic) Hookup Guide](https://learn.sparkfun.com/tutorials/tfmini---micro-lidar-module-qwiic-hookup-guide).

The [TFMini](https://www.sparkfun.com/products/14588) is a ToF (Time of Flight) LiDAR sensor capable of measuring the distance to an object as close as 30 cm and as far as 12 meters! The TFMini allows you to integrate LiDAR into applications traditionally reserved for smaller sensors such as the SHARP GP-series infrared rangefinders. In this tutorial, you will learn how to connect to the TFMini using an Arduino microcontroller.

[![TFMini - Micro LiDAR Module](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/4/2/14588-TFMini_-_Micro_Infrared_Module-04.jpg)](https://www.sparkfun.com/products/14588)

### [TFMini - Micro LiDAR Module](https://www.sparkfun.com/products/14588) 

[ SEN-14588 ]

The TFMini is a ToF (Time of Flight) LiDAR sensor capable of measuring the distance to an object as close as 30 centimeters a...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun Logic Level Converter - Bi-Directional](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/2/2/12009-06.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html)

### [SparkFun Logic Level Converter - Bi-Directional](https://www.sparkfun.com/sparkfun-logic-level-converter-bi-directional.html) 

[ BOB-12009 ]

The SparkFun bi-directional logic level converter is a small device that safely steps down 5V signals to 3.3V AND steps up 3....

[ [\$3.95] ]

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

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![SparkFun USB Mini-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/6/9/8/0/11301-01.jpg)](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html)

### [SparkFun USB Mini-B Cable - 6 Foot](https://www.sparkfun.com/sparkfun-usb-mini-b-cable-6-foot.html) 

[ CAB-11301 ]

This is a USB 2.0 type A to Mini-B 5-pin cable. You know, the mini-B connector that usually comes with USB Hubs, Cameras, MP3...

[ [\$5.50] ]

#### Tools

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

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

## Hardware Overview

**Note:** This product does not use laser light for ranging. Instead it contains an LED and optics. Many such systems are being marketed under the name \"LiDAR,\" although it may be more appropriate to think of this device as a \"Time-of-Flight Infrared Rangefinder\". It differs significantly from traditional IR rangefinders in that it uses ToF to determine range and not triangulation --- as is performed by the Sharp GP-series devices.

The sensor works by sending a modulated near-infrared light out. The light that is reflected from the object returns to the sensor\'s receiver. The distance between the two can be converted using the sensor by calculating the time and phase difference. The distance measured may vary depending on the environment and the reflectivity of object.

### Input Power

According to the [datasheet (pg 4)](https://cdn.sparkfun.com/assets/5/e/4/7/b/benewake-tfmini-datasheet.pdf) the input voltage is between *4.5V-6V*. In this tutorial, we will be applying **5V** to the sensor.

**Current Draw Testing and Analysis:** According to the datasheet, TFMini may pull up to **\~800mA** at peak current. Testing with a multimeter set to measure current and a 5V/2A power supply, the sensor was pulling about *66mA-68mA* by itself. When using a 5V Arduino, logic level converter, and the sensor, the sensor was pulling about *98mA-92mA*. For basic tests, 5V/500mA from a USB port should suffice.\
\
You may want to consider providing a sufficient power supply when using the sensor in a project.

### Logic Levels

While the sensor can be powered at 5V, the serial UART pins are only **3.3V logic**. Make sure to use a logic level converter when reading the sensor with a 5V microcontroller.

### Pinout

There is a marking next to the polarized connector to indicate the polarity as \"**J1**\" as indicated in the image below. This is useful when referencing sensor\'s pinout.

[![TFMini Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/2/14588-TFMini_-_Micro_Infrared_Module-03_Pinout_small.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/2/14588-TFMini_-_Micro_Infrared_Module-03_Pinout_small.png)

  Pin Number   TFMini Pinout            Wire Color
  ------------ ------------------------ ------------
  1            UART_TX (**3.3V TTL**)   Green
  2            UART_RX (**3.3V TTL**)   White
  3            **5V**                   Red
  4            GND                      Black

## Hardware Hookup

**Advanced Users:** For those that have experience with Arduino, you could go smaller and use a [5V/16MHz Arduino Pro Mini](https://www.sparkfun.com/products/11113)! Just make sure to also power the TFMini with 5V and use a [logic level converter](https://www.sparkfun.com/products/12009).

For the purpose of this tutorial, we will be using a 5V Arduino. A microcontroller and logic level converter is required in order to read the sensor values through the serial UART pins. Make sure to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the [male header pins](https://www.sparkfun.com/products/116) to the converter before making the connections on a breadboard. Begin by making a connection from an Arduino\'s high side and following the connection to the TFMini. Then continue to make the rest of the connections by following the hookup table listed below.

  ---------------------------------------------------------------------------------------------------------------------------
  5V Arduino w/ Atmega328P   Logic Level Converter *(High Side)*   Logic Level Converter *(Low Side)*   TFMini
  -------------------------- ------------------------------------- ------------------------------------ ---------------------
  Software Serial RX\        HV1                                   LV1                                  UART_TX (3.3V TTL)\
  *(Pin 10)*                                                                                            *(Pin 1)*

  Software Serial TX\        HV4                                   LV4                                  UART_RX (3.3V TTL)\
  *(Pin 11)*                                                                                            *(Pin 2)*

  3.3V                                                             LV                                   

  5V                         HV                                                                         Vin (4.5V-6V)\
                                                                                                        *(Pin 3)*

  GND                        GND                                   GND                                  GND\
                                                                                                        *(Pin 4)*
  ---------------------------------------------------------------------------------------------------------------------------

Once we are finished, it should look like the image below.

[![Connecting the TFMini with Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/2/TFMini_HardwareHookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/2/TFMini_HardwareHookup.jpg)

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Download and install Peter Jansen\'s **Arduino TFMini library** using the library manager. You can also manually install it from the [GitHub Repository](https://github.com/opensensinglab/tfmini) by downloading the library from the button below.

[Download TFMini Arduino Library (ZIP)](https://github.com/opensensinglab/tfmini/archive/master.zip)

Grab a mini-USB cable and connect the Arduino to your computer. Upload the **BasicReading.ino** that was included in the library\'s examples to your Arduino. Make sure to use the correct COM port and board selection.

Once uploaded, try moving an object in front of the sensor to test. In the example below, a third hand was used to hold the TFMini when detecting an object at a certain distance away from the sensor. Since the sensor is not able to detect an object when less than 11.8 inches (or 30cm = 0.3m) away, the object under test was placed at 20 inches and 30 inches.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/2/TFMini_Distance_20Inches.jpg "TFMini Reading an Object at 20 Inches")](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/2/TFMini_Distance_20Inches.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/2/TFMini_Distance_30Inches.jpg "TFMini Reading an Object at 30 Inches")](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/2/TFMini_Distance_30Inches.jpg)
  *TFMini Reading an Object at 20 Inches*                                                                                                                                                                                           *TFMini Reading an Object at 30 Inches*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Opening the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200**, you may see an output similar to the values printed below. Using a yard stick, the values responded as expected when moving an object between 20 inches and 30 inches.

    Initializing...
    54 cm      sigstr: 457
    54 cm      sigstr: 456
    54 cm      sigstr: 456
    54 cm      sigstr: 456
    55 cm      sigstr: 456
    54 cm      sigstr: 456
    54 cm      sigstr: 456
    54 cm      sigstr: 457
    67 cm      sigstr: 340
    70 cm      sigstr: 315
    71 cm      sigstr: 315
    77 cm      sigstr: 283
    77 cm      sigstr: 283
    77 cm      sigstr: 283
    77 cm      sigstr: 283
    77 cm      sigstr: 284
    78 cm      sigstr: 281
    78 cm      sigstr: 281
    78 cm      sigstr: 282
    78 cm      sigstr: 282
    78 cm      sigstr: 283

**Troubleshooting:** If you are receiving an error similar to the output below, it could be due to a few reasons.\
\

    TF Mini error: too many measurement attempts
    Last error:
    ERROR_SERIAL_NOHEADER
    65535 cm      sigstr: 65535

This may be caused by your Arduino not properly communicating with the TFMini. For example, the [maximum baud an Arduino at 8MHz can handle with the software serial library is 57600 baud](https://forum.arduino.cc/index.php?topic=54623.msg391081#msg391081). If you are using a 3.3V/8MHz Arduino Pro Mini with a baud rate of 115200, it is probably too high which can cause unreliable readings. It is recommended to use a 5V/16MHz Arduino if you are using the software serial library to communicate with the sensor at 115200.\
\
As an alternative to check if the TFMini is still functioning at small distances, you can try using the [TFMini\'s GUI](http://www.benewake.com/en/down.html) with a [USB-to-Serial cable](https://www.sparkfun.com/products/9717). Just make sure that you are providing 5V for Vcc and communicating with 3.3V logic levels.