# Source: https://learn.sparkfun.com/tutorials/single-supply-logic-level-converter-hookup-guide

## Introduction

The [Single Supply Logic Level Converter](https://www.sparkfun.com/products/14765) combines a boost converter (TPS61200), adjustable voltage regulator (MIC5205), and logic level translator (TXB0104) into one board. It provides 5V to the high side of the TXB0104 and the low side is programmable to 3.3V, 2.5V and 1.8V. The default low side voltage is 3.3V. With this device you can use your 5V microcontroller with 3.3V sensors and vice versa without the need for a second power supply!

[![SparkFun Logic Level Converter - Single Supply](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/0/1/0/14765-SparkFun_Logic_Level_Converter_-_Single_Supply-01.jpg)](https://www.sparkfun.com/sparkfun-logic-level-converter-single-supply.html)

### [SparkFun Logic Level Converter - Single Supply](https://www.sparkfun.com/sparkfun-logic-level-converter-single-supply.html) 

[ PRT-14765 ]

The SparkFun Single Supply Logic Level Converter is logic level and power supply translator in one small package.

[ [\$18.95] ]

What makes this logic level converter truly special is the fact that you can supply it with 3.3V and it will boost it to 5V - meaning you can use your 3.3V system, and convert directly to another 5V sensor - and even power your sensor or other board! We will use a 3.3V microcontroller and a 5V sensor for the example. However, you can use still this board with a 5V microcontroller and a 3.3V sensor.

### Required Materials

To follow along with this project tutorial, you will need the following materials to level shift between a 3.3V microcontroller with a 5V sensor. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

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

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

## Hardware Overview

Before we discuss hooking up the breakout, let's go over some of the features of this board.

[![Top View of Single Supply Logic Level Converter](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_-_Single_Supply-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_-_Single_Supply-02.jpg)

### Pinout

The following table describes the pins that are broken out.

  ----------------------------------------------------------------------------------------------------------
  Pin                                 Description
  ----------------------------------- ----------------------------------------------------------------------
  VIN                                 Input Supply Voltage (**3V - 5.5V**)

  GND                                 Ground

  VOUT, 5V                            Boost Converter\'s Voltage Output Set to **5V**

  VOUT, 3.3V                          Regulated Voltage Output Set to **3.3V**\
                                      *(can be adjusted depending on resistor*)

  A1-A4                               Programmable VCCA Port for Lower TTL Logic Levels - *Default = 3.3V*

  B1-B4                               VCCB Port for Higher TTL Logic Levels - *Set to 5V*
  ----------------------------------------------------------------------------------------------------------

### Logic Level Shifter

The Single Supply Logic Level Converter breaks out Texas Instrument\'s TXB0104 module. The TXB0104 is a 4-bit, noninverting, bi-directional voltage-level translator with automatic direction sensing.

[![TXB0104 Highlighted on the board with Low and High Side TTL pins ](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_TXB0104.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_TXB0104.jpg)

Each pin on this module is broken out for you to easily access ports A and B. Port A (A1-A4) is for low side TTL levels. This device\'s VCCA is set to 3.3V by default but can easily be programmable with a resistor to 2.5V and 1.8V. Port B (B1-B4) is for high side TTL levels. VCCB is hard wired to 5V. VCCA should not exceed VCCB. Depending on which voltage is chosen for VCCA the data rate may vary.

#### Adjusting the Lower Voltage Side (i.e. VCCA)

To adjust the reference voltage for the low side, you will need an associated resistor value to adjust the MIC5205\'s output voltage. Below is a table of calculated resistor values that can be used. For more information, check out [equation 4-7 on page 11 of the datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/20005785A.pdf).

VCCA

Resistor Value

**3.3V**

**Default = 13kΩ**

2.5V

22kΩ

1.8V

49kΩ

[] **Heads up!** While the datasheet states that the TXB0104 can translate voltages on the low side for VCCA between \"*1.2V to 3.6V*\" and high side for VCCB between \"*1.65V to 5.5V*\", the board is only capable of translating a minimum of about **1.58V** on the low side due to the adjustable voltage regulator on the board.

Simply remove the default surface mount resistor with a blob of solder so that heat can be transferred to both terminals. Once heated, the surface mount resistor can be removed with tweezers or a [gentle sweep of a soldering iron](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering#advanced-techniques-and-troubleshooting). Once removed, a resistor of your choice can be used to adjust the VCCA\'s reference voltage.

[![Resistor to Modify When Adjusting the Low Side Voltage Reference Pin ](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_Adjustable_VCCA.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_Adjustable_VCCA.jpg)

**Note:** Depending on the resistor value, you may need to add some resistors in [series](https://learn.sparkfun.com/tutorials/resistors#series-and-parallel-resistors) to achieve the exact resistor value. If necessary, try using heat shrink, wires, and the snappable protoboard when adding the resistors in series.\
\

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun Snappable Protoboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/8/9/13268-01.jpg)](https://www.sparkfun.com/sparkfun-snappable-protoboard.html)

### [SparkFun Snappable Protoboard](https://www.sparkfun.com/sparkfun-snappable-protoboard.html) 

[ PRT-13268 ]

Sometimes it\'s nice to have a protoboard that\'s super long and skinny, super small, or just a bunch of holes. The SparkFun Sn...

[ [\$13.50] ]

[![Heat Shrink Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/2/3/09353-01.jpg)](https://www.sparkfun.com/heat-shrink-kit.html)

### [Heat Shrink Kit](https://www.sparkfun.com/heat-shrink-kit.html) 

[ PRT-09353 ]

We love heat shrink! We use it for all sorts of handy projects. Use it to reinforce connections, protect devices, and electri...

[ [\$10.95] ]

[![Hook-up Wire - Yellow (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/4/08024-01a.jpg)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html)

### [Hook-up Wire - Yellow (22 AWG)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html) 

[ PRT-08024 ]

Standard 22 AWG solid Yellow hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes...

[ [\$3.25] ]

### Power Supply and Voltage Regulator

The TPS61200 buck/boost converter on the Single Supply Logic Level Converter takes an input between **3V - 5.5V** (most likely from your microcontroller\'s VCC pin) and regulates it to 5V. This output is also connected to the high side on VCCB for reference.

[![Input Voltage Pins](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VIN.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VIN.jpg)

The output current of the TPS61200 depends on the input to output voltage ratio. The TPS61200 provides output currents up to **600 mA at 5V**. The maximum average input current is limited to 1.5A. For more information, check out the [datasheet](https://www.sparkfun.com/datasheets/Prototyping/tps61200.pdf).

[![Components Highlighted on the Single Supply Logic Level Converter for a Buck/Boost Voltage of 5V](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VOUT_TPS61200.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VOUT_TPS61200.jpg)

The regulated 5V is then further regulated to **3.3V**, which is connected to the low side on VCCA for reference. There is an option to reprogram VCCA\'s voltage using an external PTH resistor as explained earlier.

[![Components Highlighted on the Single Supply Logic Level Converter for Regulated 3.3V](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VOUT_MIC5205_3.3V.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply_VOUT_MIC5205_3.3V.jpg)

#### VCCA Reference Ground

⚡ [] **Warning:** The reference GND that you choose can affect the serial data being sent depending on how far your device is from the rest of the ground plane. You may notice some data not being sent correctly between your devices (like some gibberish or garbage data on a serial UART). It is recommended to use the GND pin by the lower VCCA side above the A1-A4 pins when you are referencing ground on the low side.\
\

[![VCCA Reference Ground](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply-VCCA_Reference_Ground.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/14765-SparkFun_Logic_Level_Converter_Single_Supply-VCCA_Reference_Ground.jpg)

### Timing Requirements

Not all logic level converters are the same! Compared to the lower cost [bi-directional logic level converter with BSS138](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide), the single supply logic level converter with TXB0104 is able to achieve higher data rates. The speed is dependent on the reference voltage that is used for the low side voltage on VCCA. This is indicated by the table below and was taken from the datasheet. For more information, check out [page 8 of the datasheet](https://cdn.sparkfun.com/assets/3/9/8/a/5/txb0104.pdf).

  VCCA   Data Rate   Pulse Duration
  ------ ----------- ----------------
  1.5V   40 Mbps     25 ns
  1.8V   60 Mbps     17 ns
  2.5V   100 Mbps    10 ns
  3.3V   100 Mbps    10 ns

[] **Heads up!** Remember, the single supply logic level converter can translate down to about 1.58V due to the voltage regulator attached to the VCCA\'s reference pin. You may get slightly above 40Mbps if you are referencing VCCA with about 1.58V.

## Hardware Hookup

Grab some straight header pins, break the pins apart, and [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) them to the single supply logic level converter.

[![Soldered Single Supply Logic Level Converter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/1/SparkFun_Logic_Level_Converter_-_Single_Supply_Headers_Soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/SparkFun_Logic_Level_Converter_-_Single_Supply_Headers_Soldered.jpg)

This would also be a good time to solder headers to the 3.3V/8MHz Arduino Pro Mini if you have not already done so!

[![Soldered Arduino Pro Mini](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/3/GoodProMini1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/3/GoodProMini1.jpg)

### Circuit Diagram

Ready to start hooking everything up? Check out the circuit diagram below to connect the components together.

[![Fritzing Diagram of Example Circuit to Translate 5V Sensor Data to a 3.3V Arduino Microcontroller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/1/SingleSupplyLogicLevelConverter_Arduino_Ultrasonic_Sensor_Buzzer_bb_Fritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/SingleSupplyLogicLevelConverter_Arduino_Ultrasonic_Sensor_Buzzer_bb_Fritzing.png)

*Having a hard time seeing the circuit? Click on the image for a closer look.*

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

The single supply logic level converter can be used to shift data in either direction. In this example, we are going to shift levels from a 3.3V Arduino microcontroller and a 5V sensor.

### Level Shifting Between a 3.3V Microcontroller w/ 5V Sensor

Copy the code below and paste it into the Arduino IDE. Since we are using an Arduino Pro Mini 3.3V/8MHz, make sure that you are selecting the correct board. Additionally, make sure to have the correct COM port selected when uploading. When ready, upload the example code!

    language:c
    /*
    Single Supply Logic Level Converter Hookup Guide

    This project will beep continuosly with a frequency proportional
    to distance. As objects get closer, the beep gets faster.

    Hardware:
     HC-SR04 Ultrasonic Sensor
     Arduino Pro Mini 3.3V/8MHz
     SparkFun Single Supply Logic Level Converter
     Piezo Buzzer

    */

    #define TRIG_PIN 10
    #define ECHO_PIN 11
    #define Beep 3

    void setup() 

    void loop() 
      else 
    }

**Heads up!** We found that when using this code with an ATmega32U4 (like the Pro Micro 3.3V/8MHz), it requires the user to toggle the reset button after a power cycle. The initial current draw to the boost converter is enough to cause the Pro Micro brown out.

After uploading, place your hand in front of the ultrasonic sensor. When your hand is within a certain range, the buzzer will begin beeping! As you move your hand toward the sensor, the buzzer will beep faster. Moving your hand away from the sensor will slow down the beeping until you are out of range.

[![Circuit for shifting logic between a 3.3V microcontroller and 5V sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/1/SparkFun_Logic_Level_Converter_-_Single_Supply_Ultrasonic_Arduino_Buzzer.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/1/SparkFun_Logic_Level_Converter_-_Single_Supply_Ultrasonic_Arduino_Buzzer.jpg)

**Troubleshooting Warning:** HVAC systems in offices and schools have been known to interfere with the performance of the ultrasonic distance sensor. If you are experiencing sporadic behavior from your circuit, check your surroundings. If there are numerous air ducts in the room you are using, try moving to a different room that does not have ducts. The airflow from these ducts can interfere with the waves sent from the sensor, creating noise and resulting in bad readings.