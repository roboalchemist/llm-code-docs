# Source: https://learn.sparkfun.com/tutorials/lidar-lite-v3-hookup-guide

## Introduction

**Note:** While this guide was written primarily for the LIDAR-Lite v3, it can be used for the LIDAR-Lite v3HP.

The LIDAR-Lite Series - the [v3](https://www.sparkfun.com/products/14032) and [v3HP](https://www.sparkfun.com/products/14599) - are compact optical distance measurement sensors, which are ideal for drones and unmanned vehicles.

[![LIDAR-Lite v3](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/4/9/14032-01.jpg)](https://www.sparkfun.com/lidar-lite-v3.html)

### [LIDAR-Lite v3](https://www.sparkfun.com/lidar-lite-v3.html) 

[ SEN-14032 ]

This is the LIDAR-Lite v3, a compact optical distance measurement sensor. When space and weight requirements are tight, the L...

[ [\$129.99] ]

[![LIDAR-Lite v3HP](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/6/1/14599-LIDAR-Lite_v3HP-01.jpg)](https://www.sparkfun.com/lidar-lite-v3hp.html)

### [LIDAR-Lite v3HP](https://www.sparkfun.com/lidar-lite-v3hp.html) 

[ SEN-14599 ]

LIDAR has never looked so good! The LIDAR-Lite v3HP is \*the\* ideal optical ranging solution for drone, robot, or unmanned veh...

[ [\$149.99] ]

LIDAR is a combination of the words \"light\" and \"RADAR.\" Or, if you\'d like, a backronym for \"LIght Detection and Ranging\" or \"Laser Imaging, Detection, and Ranging.\" At it\'s core, LIDAR works by shooting a laser at an object and then measuring the time it takes for that light to return to the sensor. With this, the distance to the object can be measured with fairly good accuracy.

By sweeping or spinning a LIDAR unit, systems can create detailed distance maps. Survey equipment, satellites, and aircraft can be equipped with complex LIDAR systems to create topographic maps of terrain and buildings. Luckily, Garmin™ has created a user-friendly LIDAR unit for your robotics and DIY needs!

Note that these use a [Class 1 Laser](https://en.wikipedia.org/wiki/Laser_safety#Class_1), if you are concerned about your safety (in short: A Class 1 laser is safe under all conditions of normal use).

**CLASS 1 LASER PRODUCT CLASSIFIED EN/IEC 60825-1 2014.** This product is in conformity with performance standards for laser products under 21 CFR 1040, except with respect to those characteristics authorized by Variance Number FDA-2016-V-2943 effective September 27, 2016.

### Suggested Viewing

What is the difference between the LIDAR-Lite v3 and the LIDAR-Lite v3HP? Let\'s ask Shawn Hymel!

### Required Materials

To follow along with this project tutorial, you will need the following materials:

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

### Differences Between v3 and v3HP

Functionally, the LIDAR-Lite v3 and LIDAR-Lite v3HP are quite similar. The primary differences are listed here:

  ----------------------------------- --------------- -------------------
  Specs                               LIDAR-Lite v3   LIDAR-Lite v3HP
  Update Rate                         500 Hz          \> 1kHz
  Current Consumption (idle)          105 mA          65 mA
  Current Consumption (acquisition)   130 mA          85 mA
  Casing                              None            IPX7 rated casing
  ----------------------------------- --------------- -------------------

**Note:** An IPX7 rating means that the body of this device can withstand incidental exposure to water of up to 1meter for up to 30 minutes. The bare wire portion of the wiring harness is not water resistant. All bare wire connections must either be made in a water tight location or properly sealed.

### Case

The LIDAR-Lite has two tubes on the front that contain a transmitter (laser) and receiver. You\'ll want to face these toward your target.

[![Front of LIDAR-Lite v3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-02.jpg)

**This step is only necessary for the LIDAR-Lite v3:**\
\
On the side, you\'ll find an electrical port that connects to the included 6-wire cable. Plug in the wire harness to the port to break out the pins.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-01.jpg)

On the back, you\'ll find 4 mounting holes that are designed to accept [#6](https://www.sparkfun.com/products/12423) or M3.5 screws or bolts.

[![Back of LIDAR-Lite v3](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/Lidar_Hookup_Guide-04.jpg)

### Wires

The LIDAR-Lite has 6 wires that can be used to communicate with the sensor.

[![LIDAR-Lite v3 pinout](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/LIDAR-Lite_back.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/LIDAR-Lite_back.png)

***NOTE:*** *This is looking at the back of the unit*

  Color    Pin      Description
  -------- -------- --------------------------------
  Red      5V       Power (5V)
  Orange   PWR EN   Power enable (internal pullup)
  Yellow   MODE     Mode control (for PWM mode)
  Green    SCL      I^2^C clock
  Blue     SDA      I^2^C data
  Black    GND      Ground

**Note:** V3\'s pinout, default address I^2^C (**0x62**), and overall functionality is the same as other versions. However, the [connector and cable](https://www.sparkfun.com/products/14043) for the V3 are different compared to V3HP and V2.\
\

[![LIDAR-Lite Accessory Cable](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/7/0/14043-01.jpg)](https://www.sparkfun.com/products/14043)

### [LIDAR-Lite Accessory Cable](https://www.sparkfun.com/products/14043) 

[ CAB-14043 ]

The LIDAR-Lite Accessory Cable is terminated with a simple 6-pin JST at one end and a bare wire pigtail at the other. The sam...

**Retired**

### Power

Both the LIDAR-Lite v3 as well as the LIDAR-Lite v3HP units require between **4.5V to 5.5V** of DC power to operate (**nominally, 5V**). The LIDAR-LITE v3 can draw up to 135 mA of current during continuous operation (105 mA at idle). Contrarily, the v3HP unit draws up to 85 mA of current during continuous operation (65 mA at idle). To maintain a level voltage, Garmin recommends putting a **680 μF capacitor** between power (5V) and ground (GND) as close to the LIDAR unit as possible.

⚡ **Note the difference in current draw!** Be aware that while the input voltage for the LIDAR-Lite v3 and v3HP is the same, the current draw is different

## Hardware Assembly

Follow the diagram below to connect the LIDAR unit to a RedBoard or other Arduino-compatible board. The LIDAR-Lite can communicate over I^2^C as well as use a pulse-width modulated (PWM) signal to denote measured distances. For this guide, we will show how to use I^2^C to communicate with the LIDAR unit.

[![LIDAR-Lite v3 to Arduino hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/7/1/Fritzing_LIDAR-Lite_Pull-Up_Resistors_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/Fritzing_LIDAR-Lite_Pull-Up_Resistors_bb.jpg)

*Click on the image to enlarge it*

**Note:** Garmin recommends a 680 μF capacitor, but anything near that value will work. I used a [1000 μF capacitor](https://www.sparkfun.com/products/8982) in this example. Make sure to add the electrolytic capacitor correctly to the circuit since it has a [polarity](https://learn.sparkfun.com/tutorials/polarity#electrolytic-capacitors).\
\
You also may need [I^2^C pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) for the SCL and SDA lines. It depends on the length between the Arduino and I^2^C device but usually a 4.7kΩ resistor is a good start. For long runs or systems with lots of devices, it is recommended to use smaller resistors. You can also use a I^2^C bus extender for distances beyond the maximum bus length as well.\
\

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun Capacitor Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/7/0/13698-02.jpg)](https://www.sparkfun.com/sparkfun-capacitor-kit.html)

### [SparkFun Capacitor Kit](https://www.sparkfun.com/sparkfun-capacitor-kit.html) 

[ KIT-13698 ]

Right after resistors, the capacitor is one of the most essential and common passive components in electronics. Not having th...

[ [\$11.50] ]

[![Electrolytic Decoupling Capacitors - 1000uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/0/8/08982-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html)

### [Electrolytic Decoupling Capacitors - 1000uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html) 

[ COM-08982 ]

Electrolytic decoupling capacitors 1000uF/25V. These capacitors are great transient/surge suppressors and work well in high-v...

[ [\$0.50] ]

[![SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/4/5/14589-SparkFun_Differential_I2C_Breakout_-_PCA9615__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14589)

### [SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://www.sparkfun.com/products/14589) 

[ BOB-14589 ]

The SparkFun Differential I2C Breakout is the fastest and easiest way to extend the range of your I2C communication bus.

**Retired**

## Software

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Garmin maintains an Arduino library to make working with the LIDAR-Lite very easy. Visit the [GitHub repository](https://github.com/garmin/LIDARLite_v3_Arduino_Library), or click the button below to download the library.

[Download the Garmin LIDAR-Lite v3 Arduino library](https://github.com/garmin/LIDARLite_v3_Arduino_Library/archive/master.zip)

Open a new Arduino sketch, and copy in the following code:

    language:c
    /**
     * LIDARLite I2C Example
     * Author: Garmin
     * Modified by: Shawn Hymel (SparkFun Electronics)
     * Date: June 29, 2017
     * 
     * Read distance from LIDAR-Lite v3 over I2C
     * 
     * See the Operation Manual for wiring diagrams and more information:
     * http://static.garmin.com/pumac/LIDAR_Lite_v3_Operation_Manual_and_Technical_Specifications.pdf
     */

    #include <Wire.h>
    #include <LIDARLite.h>

    // Globals
    LIDARLite lidarLite;
    int cal_cnt = 0;

    void setup()
    

    void loop()
     else 

      // Increment reading counter
      cal_cnt++;
      cal_cnt = cal_cnt % 100;

      // Display distance
      Serial.print(dist);
      Serial.println(" cm");

      delay(10);
    }

Upload the program, and open a [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). You should see distance measurements (in cm) being printed.

[![Measuring distance with LIDAR](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/Serial_Output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/1/Serial_Output.png)

## Troubleshooting

### Arduino Output Error [Poor Connection]

Are you seeing this output from the [LIDAR-Lite V3 I^2^C example code](https://github.com/garmin/LIDARLite_Arduino_Library/blob/master/examples/v3/GetDistanceI2c/GetDistanceI2c.ino) with the decoupling capacitors connected to the Arduino?

    > nack
    > nack
    > nack

You probably do not have a secure connection between the Lidar and the Arduino. I^2^C is sensitive to its connection. The cable wires are thin and can disconnect when in the Arduino\'s female header from a bump. A breadboard seems to work fine if there is not a lot of mechanical vibrations. However, a small bump can mess up the timing for the I^2^C even on the breadboard.

+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| [](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/3/ThinWiresLidarBreadboard.jpg)                                    | [](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/3/ThinWiresLidarRedBoardBreadboard.jpg)                                               |
|                                                                                                                           |                                                                                                                                              |
| :::                                                                                                       | :::                                                                                                                          |
| ![](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/3/ThinWiresLidarBreadboard.jpg "Lidar Connected with Breadboard") | ![](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/3/ThinWiresLidarRedBoardBreadboard.jpg "Lidar Connected to RedBoard and Breadboard") |
| :::                                                                                                                       | :::                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

For a secure connection, it is recommended soldering header pins with some [heat shrink](https://www.sparkfun.com/products/9353) or make sort of adapter when connecting it to an Arduino. Once disconnected, the Arduino might stop outputting sensor data. You can reset the Arduino for testing but to prevent the wires from disconnecting, it would be better to solder the wires to [header pins](https://www.sparkfun.com/products/116). This is a common \"issue\" with any I^2^C sensor and if they do not secure the wires, the Arduino will have problems talking with the Lidar Lite V3.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Heat Shrink Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/2/3/09353-01.jpg)](https://www.sparkfun.com/heat-shrink-kit.html)

### [Heat Shrink Kit](https://www.sparkfun.com/heat-shrink-kit.html) 

[ PRT-09353 ]

We love heat shrink! We use it for all sorts of handy projects. Use it to reinforce connections, protect devices, and electri...

[ [\$10.95] ]

### Arduino Output Error [I^2^C Pull-Up Resistors]

Another reason for the `nack` error may be that you need [I^2^C pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) for the SCL and SDA lines. It depends on the length between the Arduino and I^2^C device but usually a 4.7kΩ resistor is a good start. For long runs or systems with lots of devices, it is recommended to use smaller resistors. You can also use a I^2^C bus extender for distances beyond the maximum bus length as well.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/4/5/14589-SparkFun_Differential_I2C_Breakout_-_PCA9615__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14589)

### [SparkFun Differential I2C Breakout - PCA9615 (Qwiic)](https://www.sparkfun.com/products/14589) 

[ BOB-14589 ]

The SparkFun Differential I2C Breakout is the fastest and easiest way to extend the range of your I2C communication bus.

**Retired**

### Decoupling Capacitor

Looking for a 680µF capacitor? Unfortunately, the SparkFun catalog does not include a 680µF capacitor. There are [1000µF capacitors](https://www.sparkfun.com/products/8982), which can work as a substitute with the Lidar Lite.

[![SparkFun Capacitor Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/1/7/0/13698-02.jpg)](https://www.sparkfun.com/sparkfun-capacitor-kit.html)

### [SparkFun Capacitor Kit](https://www.sparkfun.com/sparkfun-capacitor-kit.html) 

[ KIT-13698 ]

Right after resistors, the capacitor is one of the most essential and common passive components in electronics. Not having th...

[ [\$11.50] ]

[![Electrolytic Decoupling Capacitors - 1000uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/0/8/08982-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html)

### [Electrolytic Decoupling Capacitors - 1000uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html) 

[ COM-08982 ]

Electrolytic decoupling capacitors 1000uF/25V. These capacitors are great transient/surge suppressors and work well in high-v...

[ [\$0.50] ]

Or, you can also wire capacitors in series and parallel to get an [equivalent capacitance](https://learn.sparkfun.com/tutorials/capacitors#capacitors-in-seriesparallel).

+----------------------------------------------------------------------------------------------------------------------+
| [](https://learn.sparkfun.com/tutorials/capacitors#capacitors-in-seriesparallel)                                     |
|                                                                                                                      |
| :::                                                                                                  |
| ![](https://cdn.sparkfun.com/r/600-600/assets/f/1/d/0/5/51951385ce395f451f000000.png "Capacitors in Parallel")       |
| :::                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+
| *[Capacitors: Capacitors in Parallel](https://learn.sparkfun.com/tutorials/capacitors#capacitors-in-seriesparallel)* |
+----------------------------------------------------------------------------------------------------------------------+

### Dimensions

For more details on the dimensions, check out the links below.

- [V3 Top and Side Dimension](https://github.com/SparkfunTechSupport/Dimensional-diagrams/blob/master/SEN-14032/SEN-14032%20dimensions.jpg)
- [V3HP Top Dimension](https://cdn.sparkfun.com//assets/parts/1/2/7/6/1/14599-LIDAR-Lite_v3HP-02.jpg)

### Product Showcase Example for LIDAR-Lite V3 Wand

Looking for the example code used in the product video for the LIDAR-LIte V3? Nick Poole basically used the same parts and [example code](https://github.com/NPoole/LIDAR-Lite-Glasses/blob/master/Firmware/LIDAR-Lite-Glasses.ino) that was used with the Lidar Lite V2 Glasses. For the Lidar Lite V3 Wand, he used the following components:

- LEDs
- [micro-B USB breakout](https://www.sparkfun.com/products/12035)
- micro-B USB Cable
- a backup portable cell phone charger
- [1kΩ resistor](https://www.sparkfun.com/products/14492)
- [5V/16 MHz Pro Micro](https://www.sparkfun.com/products/12640)

He happened to have a 5V/16 MHz Pro Micro around when building the project for the Lidar Lite V2 Glasses. The parts were reused for the Lidar Lite V3 Wand. Try looking at the [old wishlist for the Lidar Lite V2 Glasses](https://www.sparkfun.com/wish_lists/106741) for more information. Make sure to also add a [1kΩ resistor](https://www.sparkfun.com/products/14492) when using the PWM wiring as stated [on page 3 of the user manual](http://static.garmin.com/pumac/LIDAR_Lite_v3_Operation_Manual_and_Technical_Specifications.pdf).

### Additional Troubleshooting

Looking for additional troubleshooting tips and application notes related to the LIDAR Lite? Check out Garmin\'s support on the LIDAR Lite:

[Garmin Support: Lidar Lite V3 and V3HP](https://support.garmin.com/en-US/?productSearch=lidar%2520lite)

#### Application Notes on Reflective Surfaces

For more application notes on using the LIDAR-Lite v3/v3HP, check out the link below.

[Garmin Support: How the LIDAR-Lite v3/v3HP Works with Reflective Surfaces](https://support.garmin.com/en-US/?faq=IVeHYIKwChAY0qCVhQiJ67)

This can also be found in the operation & technical manual on page 11.

------------------------------------------------------------------------