# Source: https://learn.sparkfun.com/tutorials/pca9306-logic-level-translator-hookup-guide-v2

## Introduction

**Heads up!** This is for the PCA9306 breakout v2. If you are using the previous PCA9306, you\'ll want to [head over to the older tutorial](https://learn.sparkfun.com/tutorials/pca9306-level-translator-hookup-guide). The package used on the PCA9306 breakout v2 is different from the PCA9306 breakout v1.

The [PCA9306](https://www.sparkfun.com/products/15439) is a dual bi-directional voltage translator for the I^2^C-bus and SMBus. It works at a range of voltages between 1.2V and 5.0V and doesn\'t require a direction pin to function. This is a great board for shifting voltages between sensors and your microcontroller.

[![SparkFun Level Translator Breakout - PCA9306](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/1/0/15439-SparkFun_Level_Translator_Breakout_-_PCA9306-01a.jpg)](https://www.sparkfun.com/sparkfun-level-translator-breakout-pca9306.html)

### [SparkFun Level Translator Breakout - PCA9306](https://www.sparkfun.com/sparkfun-level-translator-breakout-pca9306.html) 

[ BOB-15439 ]

Different parts sometimes use different voltage levels to communicate. This PCA9306 Level Translator can be the key to making...

[ [\$5.25] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Cable A to B - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/7/00512-USB_Cable_A_to_B_-_6_Foot-01.jpg)](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html)

### [USB Cable A to B - 6 Foot](https://www.sparkfun.com/usb-cable-a-to-b-6-foot.html) 

[ CAB-00512 ]

This is a standard issue USB 2.0 cable. This is the most common A to B Male/Male type peripheral cable, the kind that\'s usual...

[ [\$5.50] ]

[![Jumper Wires Premium 4\" M/M - 26 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/4/2/14284-Jumper_Wires_Premium_4in._M_M_-_26_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-4-m-m-26-awg-30-pack.html)

### [Jumper Wires Premium 4\" M/M - 26 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-premium-4-m-m-26-awg-30-pack.html) 

[ PRT-14284 ]

These are 101mm long 26AWG jumpers with male connectors on both ends. Use these to jumper from any female header on any board...

[ [\$2.80] ]

[![Breadboard - Mini Modular (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/6/12043-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-white.html)

### [Breadboard - Mini Modular (White)](https://www.sparkfun.com/breadboard-mini-modular-white.html) 

[ PRT-12043 ]

This white Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to b...

[ [\$5.25] ]

[![SparkFun Triple Axis Accelerometer Breakout - MMA8452Q](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/5/12756-00.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-mma8452q.html)

### [SparkFun Triple Axis Accelerometer Breakout - MMA8452Q](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-mma8452q.html) 

[ SEN-12756 ]

This breakout board makes it easy to use the tiny MMA8452Q accelerometer in your project. The MMA8452Q is a smart low-power, ...

**Retired**

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Suggested Reading

These level converters are pretty easy to start using, but you may want to check out some of the additional reading material below if you are unfamiliar with logic level shifting or haven\'t worked with Arduino boards prior to this.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

### Power and I^2^C Sides

At a minimum, the breakout board has seven pins that need to be connected to function properly. VREF1, SCL1, and SDA1 all connect to your lower voltage side.

[![Low Side Pins](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_PCA9306-Low_Side.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_PCA9306-Low_Side.jpg)

VREF2, SCL2, and SDA2 connect to your higher voltage side. One of the GND pins on either side needs to be connected to ground in your system.

[![High Side Pins](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_PCA9306-High-Side.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_PCA9306-High-Side.jpg)

What\'s that extra through-hole on the board labeled as EN? Well, it can be connected to an I/O pin to toggle the PC9306 from the high side. You\'ll need to adjust the jumper in the back to be able to use this feature. Check below for more information.

#### Allowable Voltage Level Translation

For most of the products listed in the catalog, usually you will be translating voltages between **3.3V** and **5V**. However, the datasheet for the PCA9306 states that it can be used to translate lower voltages if you need. Below are the acceptable voltages on the low and high sides.

  VREF1 (i.e. Low Side)   VREF2 (i.e. High Side)
  ----------------------- ------------------------
  1.2V                    1.8, 2.5V, 3.3V, 5V
  1.8V                    2.5V, 3.3V, 5V
  2.5V                    3.3V, 5V
  3.3V                    5V

### Jumpers

There is a jumpers on the underside of this board to turn on and off the PCA9306. By [cutting the trace](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) and adding a solder jumper toward the pad labeled as \"Switch,\" you can toggle the logic level translator with your microcontroller.

[![Enable Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_-_PCA9306-Enable-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/15439-I2C_Logic_Level_Translator_Breakout_-_PCA9306-Enable-Jumper.jpg)

#### Enable Feature

It\'s possible to use the PCA9306 as an I²C *switch*. First, as mentioned above, you\'ll want to cut the `ON` trace and solder the `Switch` trace. To use the feature you\'ll attach the high side `VREF2` to you\'re high side voltage as you normally would, and then attach the `EN` (enable) pin, to a digital Pin. Now when you want to enable I²C communication, pull the line **HIGH**.

## Hardware Assembly

To connect the board, you will need to [solder headers](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) into the through-holes, and use jumper wires to connect between devices when prototyping. Make sure to place it on a breadboard before soldering to test. You will need to make sure that the headers on each side of the PCA9306 breakout board are soldered at an angle in order for it to sit securely on a breadboard. The board shown at the top of the image shows how the pins are offset and soldered at a small angle. The board shown at the bottom of the image shows pins flush with the board. You will want to make sure that you soldered the pins like the board shown at the top of the image.

[![Offset Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/4/PCA9306_Headers-Angled-Offset.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/PCA9306_Headers-Angled-Offset.jpg)

**Heads up!** If you have issues with the bread not sitting flush with the breadboard, try reworking the board adding a blob of solder on the pins and carefully pushing the header outward on a solder mat. After angling the pins, make sure to remove the solder blob on the board and clean the solder joints.

You could also just solder some hookup wire or add a [protoshield](https://learn.sparkfun.com/tutorials/sparkfun-arduino-protoshield-hookup-guide) to connect all of your boards together securely for a project.

## Hardware Hookup

For this example, we are going to use an [Arduino Uno](https://www.sparkfun.com/products/11113) to connect to an [MMA8452 accelerometer breakout board](https://www.sparkfun.com/products/10530), which runs at 3.3V and communicates over I^2^C.

  3.3V Device (i.e. MMA8452)   PCA9306 (Low Side)   PCA9306 (High Side)   5V Device (i.e. Arduino Uno w/ ATmega328P)
  ---------------------------- -------------------- --------------------- --------------------------------------------
  3.3V                         VREF1                                      3.3V
                                                    VREF2                 5V
  SCL                          SCL1                 SCL2                  A5
  SDA                          SDA1                 SDA2                  A4
  GND                          GND                  GND                   GND
                                                    EN                    Any I/O Pin If Jumper is Adjusted

Here is a Fritizing diagram showing the actual connections between the MMA8452, the PCA9306 breakout and the Arduino Uno.

[![Fritzing Diagram of hookups](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/1/4/I2C-PCA9306-Logic-Level-Translator-Arduino-Fritzing-Example.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/1/4/I2C-PCA9306-Logic-Level-Translator-Arduino-Fritzing-Example.jpg)

You\'ll need to connect power for the Arduino via the barrel jack, VIN, or USB connector. In this case, we\'ll simply use power from the USB cable to provide 5V to the high side. The diagram shows the MMA8452 running off the Arduino Uno\'s 3.3V rail. Keep in mind your power supplies could be different, but you will still need to have a power supply for the lower voltage side of the system and a separate supply for the higher voltage side.

Once you have the boards physically connected, you are good to go! You don\'t need to use any special code with the PCA9306 board, and you can simply use any example sketch available for your sensors. In this case, we are using the example [MMA8452 from the hookup guide](https://learn.sparkfun.com/tutorials/mma8452q-accelerometer-breakout-hookup-guide). Head over to the tutorial to finishing programing your Arduino to start using the accelerometer!

[](https://learn.sparkfun.com/tutorials/mma8452q-accelerometer-breakout-hookup-guide)

### MMA8452Q Accelerometer Breakout Hookup Guide 

June 11, 2014

How to get started using the MMA8452Q 3-axis accelerometer \-- a solid, digital, easy-to-use acceleration sensor.