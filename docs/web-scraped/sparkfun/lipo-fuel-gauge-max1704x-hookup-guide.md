# Source: https://learn.sparkfun.com/tutorials/lipo-fuel-gauge-max1704x-hookup-guide

## Introduction

The [SparkFun LiPo Fuel Gauge - MAX17043](https://www.sparkfun.com/products/20680) connects your LiPo battery to your project and uses a sophisticated algorithm to detect the relative state of charge and direct A/D measurement of battery voltage. In other words, it tells your microcontroller how much \'fuel\' is left in the tank. The LiPo Fuel Gauge Breakout communicates with your project over I^2^C and an alert pin also tells you when the charge has dropped below a certain percentage.

[![SparkFun LiPo Fuel Gauge](https://cdn.sparkfun.com/r/600-600/assets/parts/2/0/5/1/7/20680-_TOL_SparkFun_LiPo_Fuel_Gauge-_01.jpg)](https://www.sparkfun.com/sparkfun-lipo-fuel-gauge.html)

### [SparkFun LiPo Fuel Gauge](https://www.sparkfun.com/sparkfun-lipo-fuel-gauge.html) 

[ TOL-20680 ]

The LiPo Fuel Gauge communicates with your project over I2C and an alert pin also tells you when the charge has dropped below...

[ [\$13.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. Below is a wishlist of the parts that you need to get started.

### Microcontroller

You will need a microcontroller with an I^2^C port when connecting to the LiPo Fuel Gauge. For the scope of this tutorial, we will be focusing on the Arduino Library for the LiPo Fuel Gauge.

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

[![SparkFun RedBoard Artemis Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/8/15443-SparkFun_RedBoard_Artemis_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html)

### [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/sparkfun-redboard-artemis-nano.html) 

[ DEV-15443 ]

The RedBoard Artemis Nano is a miniature extremely versatile implementation of the Artemis module.

[ [\$19.95] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun Qwiic Micro - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/0/15423-SparkFun_Qwiic_Micro_-_SAMD21-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html)

### [SparkFun Qwiic Micro - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html) 

[ DEV-15423 ]

The SparkFun Qwiic Micro is molded to fit our standard 1\" x 1\" Qwiic board size which makes it our smallest SAMD21 micro-cont...

[ [\$22.95] ]

[![Arduino Pro 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/0/4/3/10914-01.jpg)](https://www.sparkfun.com/arduino-pro-328-3-3v-8mhz.html)

### [Arduino Pro 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-328-3-3v-8mhz.html) 

[ DEV-10914 ]

It\'s blue! It\'s skinny! It\'s the Arduino Pro! SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running t...

[ [\$18.50] ]

**Note:** Depending on the microcontroller that you receive, there may already be a built-in LiPo Fuel Gauge! The following are a few boards that include the MAX1704X. Note that some boards like the ESP32 Thing Plus, IoT RedBoard ESP32, and QDuino Mini use the MAX17048. The MAX17048 is similar to the MAX17043 but it can provide a few more readings from your LiPo battery (i.e. charge rate, disharge rate, 1% change in SOC, undervoltage, overvoltage, etc.). The Arduino Library that we are using is also compatible with MAX17048!\
\

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun IoT RedBoard - ESP32 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/8/0/0/ESP32_03.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html)

### [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-development-board.html) 

[ WRL-19177 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board that has everything you need in an Arduino Uno with extra perks...

[ [\$41.87] ]

[![SparkFun Wireless Joystick Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/0/14051-02.jpg)](https://www.sparkfun.com/sparkfun-wireless-joystick-kit.html)

### [SparkFun Wireless Joystick Kit](https://www.sparkfun.com/sparkfun-wireless-joystick-kit.html) 

[ KIT-14051 ]

The SparkFun Wireless Joystick Kit provides an easy way to control your next XBee project.

[ [\$44.95] ]

[![Qduino Mini - Arduino Dev Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/9/8/7/13614-01b.jpg)](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html)

### [Qduino Mini - Arduino Dev Board](https://www.sparkfun.com/qduino-mini-arduino-dev-board.html) 

[ DEV-13614 ]

The Qduino Mini is a tiny, Arduino-compatible board with a battery connector and charger built-in as well as a fuel gauge tha...

[ [\$35.95] ]

### Display

The example code can be used to print the voltage and state of charge of a single cell, LiPo battery using a serial monitor. For those that want to monitor a battery remotely, you can add a display to the setup. Below is the Qwiic Micro OLED breakout that can be used. [You can also use a different display](https://www.sparkfun.com/categories/76). However, you will need to adjust the code to display the readings properly.

[![SparkFun Micro OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/6/2/1/14532-SparkFun_Micro_OLED_Breakout__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14532)

### [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532) 

[ LCD-14532 ]

The SparkFun Qwiic Micro OLED Breakout is a Qwiic enabled version of our popular MicroView and micro OLED display!

**Retired**

### Single Cell LiPo Battery

Of course, you will also need a single cell LiPo battery. Below are a few LiPo batteries to choose from in the [SparkFun catalog](https://www.sparkfun.com/categories/54).

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 400mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/5/8/13857-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-400mah.html)

### [Lithium Ion Battery - 400mAh](https://www.sparkfun.com/lithium-ion-battery-400mah.html) 

[ PRT-13851 ]

This is a very small, extremely lightweight battery based on Lithium Ion chemistry, with the highest energy density currently...

[ [\$7.98] ]

[![Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/6/17748-Lithium_Ion_Battery_-_1250_mAh__IEC62133_certified_-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html)

### [Lithium Ion Battery - 1250mAh (IEC62133 Certified)](https://www.sparkfun.com/lithium-ion-battery-1250mah-iec62133-certified.html) 

[ PRT-18286 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1250 mAh and is IE...

**Retired**

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

### Tools

Building a circuit using this breakout requires some assembly and soldering. You may already have a few of these items but if not, the tools and hardware below help with that assembly.

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

#### Prototyping Accessories

Depending on your setup, you may want to use IC hooks for a temporary connection. However, you will want to solder header pins to connect devices to the plated through holes for a secure connection. Depending on your application, you could use straight headers or right angle headers. Of course, you could also solder wire as well.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![JST Jumper 2 Wire Assembly](https://cdn.sparkfun.com/r/140-140/assets/parts/4/0/2/0/09914-02b.jpg)](https://www.sparkfun.com/jst-jumper-2-wire-assembly.html)

### [JST Jumper 2 Wire Assembly](https://www.sparkfun.com/jst-jumper-2-wire-assembly.html) 

[ PRT-09914 ]

This is a simple two wire cable. Great for jumping from board to board or just about anything else. There is a 2-pin JST conn...

[ [\$1.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![IC Hook with Pigtail](https://cdn.sparkfun.com/r/140-140/assets/parts/3/6/9/6/09741-01.jpg)](https://www.sparkfun.com/ic-hook-with-pigtail.html)

### [IC Hook with Pigtail](https://www.sparkfun.com/ic-hook-with-pigtail.html) 

[ CAB-09741 ]

These are good quality IC test hooks with a male connection wire. Instead of a single hook, these have two hooks that are cap...

[ [\$5.75] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

[![Jumper Wire - JST Black Red](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/2/6/08670-03-L.jpg)](https://www.sparkfun.com/jumper-wire-jst-black-red.html)

### [Jumper Wire - JST Black Red](https://www.sparkfun.com/jumper-wire-jst-black-red.html) 

[ PRT-08670 ]

This is a simple two wire cable. Great for jumping from board to board. 2-pin JST connector on one end, bare cable on the opp...

[ [\$1.10] ]

For those that want to take advantage of the Qwiic enabled devices, you\'ll want to grab a Qwiic cable. Users can cut, strip, and solder half of a cable to easily connect the LiPo Fuel Gauge to a Qwiic-enabled microcontroller. For those that soldered male header pins to the board when prototyping, users can use a Qwiic cable with male pins or female sockets to connect without desoldering the header pins on the board. Note that this causes the board to have a higher height profile than soldering wires straight to the board.

[![Flexible Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/5/17258-Flexible_Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html)

### [Flexible Qwiic Cable - 200mm](https://www.sparkfun.com/flexible-qwiic-cable-200mm.html) 

[ PRT-17258 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Flexible Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/0/7/8/17912-Flexible_Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-breadboard-jumper-4-pin.html)

### [Flexible Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/flexible-qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-17912 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![Flexible Qwiic Cable - Female Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/8/17261-Flexible_Qwiic_Cable_-_Female_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin.html)

### [Flexible Qwiic Cable - Female Jumper (4-pin)](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin.html) 

[ CAB-17261 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

### Recommended Reading

If you aren't familiar with the following concepts, we also recommend checking out a few of these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/what-is-a-battery)

### What is a Battery? 

An overview of the inner workings of a battery and how it was invented.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project)

### LilyPad Basics: Powering Your Project 

Learn the options for powering your LilyPad projects, LiPo battery safety and care, and how to calculate and consider power constraints on your projects.

## Breakout Board (MAX17043) Hardware Overview

**Revision Change:** The LiPo Fuel Gauge - MAX17043 illustrated in this section highlights V1.2. The hardware is slightly different. In V1.2, the battery voltage is separate from VCC\'s pull-up resistors. When using V1.2, make sure to connect a regulated 3.3V from your microcontroller to provide voltage to the pull-up resistors.

In this section, we will highlight parts of the LiPo Fuel Gauge (MAX17043) breakout board. For users that have a built in fuel gauge (MAX17043/MAX17048) already on your Arduino microcontroller, you can skip this section. The row of 1x3 header pins are arranged in a way so that you can insert the board a standard breadboard.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View.jpg)   [![Bottom View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View.jpg)
  *Top View*                                                                                                                                                                                                                                    *Bottom View*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Battery and Power Input

The board includes a 2-pin JST connector to mate with single cell LiPo batteries. We have also broke out the pins to PTHs labeled as + and −. These can be used to solder the LiPo battery wires directly to the board and to your system\'s VBATT pin. The input voltage range is between **2.5V** to **4.5V**. Note that the nominal voltage of a single cell LiPo Battery is around 3.7V. Fully charged, the voltage is at around 4.2V. This input also powers the IC and should be connected to your system\'s power input as well.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Battery Input Highlighted - Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-Power_Input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-Power_Input.jpg)   [![Battery Input Highlighted - Bottom View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Power_Input.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Power_Input.jpg)

  *Battery Input\                                                                                                                                                                                                                                                                                   *Battery Input\
  Highlighted - Top View*                                                                                                                                                                                                                                                                           Highlighted - Bottom View*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Pull-Up Resistor\'s Voltage Input

VCC pin is connected to the I^2^C and alert pull-up resistors. This voltage input pin is different from the battery input pin. The maximum voltage that can be connected to this pin is 5.5V. This is typically **3.3V**. If you decide to daisy chain the LiPo Fuel Gauge to Qwiic-enabled devices, we recommend using 3.3V.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Power Input Highlighted - Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Power_Input_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Power_Input_2.jpg)   [![Power Input Highlighted - Bottom View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-Power_Input_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-Power_Input_2.jpg)

  *Power Input\                                                                                                                                                                                                                                                                                             *Power Input\
  Highlighted - Top View*                                                                                                                                                                                                                                                                                   Highlighted - Bottom View*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### I^2^C Pins

The I^2^C pins are broken out to PTHs. The 7-bit, unshifted address of the MAX17043 is **0x36**. The address becomes *0x6C* for write and *0x6D* for read. There are two 2.2kΩ pull-up resistors connected to the SDA and SCL lines. These lines are connected to the VCC pin.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![I2C Pins Highlighted - Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-I2C.jpg)   [![I2C Pins Highlighted - Bottom View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-I2C.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-I2C.jpg)

  *I^2^C Pins\                                                                                                                                                                                                                                                                 *I^2^C Pins\
  Highlighted - Top View*                                                                                                                                                                                                                                                      Highlighted - Bottom View*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Alert] Pin (ALT)

The ALT pin is the alert pin. The datasheet labels this as [ALRT] but we decided to label it as ALT due to the size of the board. This pin is active low indicating that there is a low state of charge. This pin can be connected to a microcontroller\'s interrupt pin. This pin can be left unconnected and the status can be viewed though I^2^C.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Alert Pin Highlighted - Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-ALT_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-ALT_.jpg)   [![Alert Pin Highlighted - Bottom View\<](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-ALT.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-ALT.jpg)

  *Alert Pin\                                                                                                                                                                                                                                                                     *Alert Pin\
  Highlighted - Top View*                                                                                                                                                                                                                                                         Highlighted - Bottom View*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** For users interested in using the alert pin to trigger an interrupt, we recommend checking out the [Processor Interrupts with Arduino](%20https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino/all) tutorial for more information.

### Quick-Start Input Pin (QST)

The QST pin is for quick-start input. The datasheet labels this pin as QSTRT but we decided to label it as QST due to the size of the board. This allows users to reset the device through hardware. By default, the pin is connected to ground through a built-in 2.2kΩ resistor as suggested by the datasheet. A rising edge on this pin will initiate a hardware reset. One possible application is connecting this pin to a microcontrollers reset pin should users decide to initiate a hardware reset. A reset can also be initiated through software as well.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Alert Pin Highlighted - Top View](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-QST_.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Top_View-QST_.jpg)   [![Alert Pin Highlighted - Bottom View\<](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-QST.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-QST.jpg)

  *Quick-Start Input Pin\                                                                                                                                                                                                                                                         *Quick-Start Input Pin\
  Highlighted - Top View*                                                                                                                                                                                                                                                         Highlighted - Bottom View*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Jumpers

By default, this 3-pad jumper is closed and located on the bottom of the board. The 2.2kΩ pull-up resistors are attached to the primary I^2^C bus; if multiple devices are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, [disable all but one pair of pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) if multiple devices are connected to the bus.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/20680-_SparkFun_LiPo_Fuel_Gauge-MAX17043_Bottom_View-Jumpers.jpg)

*Jumpers Highlighted - Bottom View*

### Board Dimensions

The board is 0.40\" x 0.95\". To make the board as small as possible, there are no mounting holes included on the board.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/e/b/d/c/4/20680-SparkFunLipoFuelGauge-BoardOutline.png)](https://cdn.sparkfun.com/assets/e/b/d/c/4/20680-SparkFunLipoFuelGauge-BoardOutline.png)

## Hardware Hookup

⚠ **Warning:** The LiPo Fuel Gauge - MAX17043 illustrated in the hardware hookup uses V1.2. The hardware is slightly different. In V1.2, the battery voltage is separate from VCC\'s pull-up resistors. This requires you to connect a voltage from your microcontroller. The previous version (V1.1) connected VCC to the LiPo battery input which can vary between 3.0V and 4.2V. As a result the pull-up resistors were also connected to the LiPo battery. This is fine for 5V tolerant microcontrollers. However, users should be careful when connecting any 3.3V devices that are not tolerant at those levels when using the previous version.

Now that we\'re familiar with the LiPo Fuel Gauge Breakout, let\'s connect it to a microcontroller and monitor a single cell LiPo battery!

### LiPo Fuel Gauge Breakout Connections

For a permanent connection, we recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) [wires](https://learn.sparkfun.com/tutorials/working-with-wire) (or headers) to the PTHs on the breakout. We chose to use a combination of header pins and wires when prototyping. Of course, you could also solder wires to the breakout board as well. For a temporary connection during prototyping, you can use IC hooks like [these](https://www.sparkfun.com/products/9741).

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

We recommend soldering the header pins and wires on one side. After soldering two rows of 1x3 header pins and a two wire cable, your setup should look like the following image below. We decided to solder the straight header pins and wire all on the top side of the board. Depending on your application, you could solder the straight header pins on the bottom side as well. This will allow you to easily view the silkscreen if you decide to solder on the bottom. Make sure to wire the red wire to the PTH labeled as \"+\" and the black wire to the PTH labeled as \"−\".

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Soldered_Header_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Soldered_Header_Cable.jpg)

For users that want to prototype on a breadboard, you could insert the breakout board in the middle of a breadboard. Thanks to the header pin\'s plastic spacers, the cable can fit between the PCB and the breadboard. The image below shows the breakout board inserted into a mini breadboard. The edge of the board is on the edge of the mini breadboard so that you can disconnect/connect a LiPo battery to the 2-pin JST connector.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Breadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Breadboard.jpg)

### Connecting the LiPo Fuel Gauge to a Microcontroller

Connect the I^2^C pins, GND, and Vcc from LiPo Fuel Gauge to your microcontroller. We recommend using 3.3V for Vcc. Insert the battery into the LiPo Fuel Gauge\'s 2-pin JST connector. Then connect the JST cable that was soldered to your microcontroller\'s voltage input. In this case, we connected Qwiic cable to the RedBoard Artemis Nano\'s Qwiic connector and the 2-wire JST cable to the 2-pin JST connector.

[![Fritzing Diagram connected to microcontroller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Fritzing_bb.jpg)

### Connecting a LiPo Charge Circuit

Users can include a LiPo charge circuit to safely charge the LiPo battery without needing to remove the LiPo battery from the LiPo Fuel Gauge. Below is one example that uses the LiPo Charger Plus to charge a single cell LiPo battery while it is also connected to an Arduino Pro Mini 3.3V/8MHz.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/Arduino_Pro_Mini_3V3_Fuel_Gauge_MAX17043_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/Arduino_Pro_Mini_3V3_Fuel_Gauge_MAX17043_Fritzing_bb.jpg)

As the note indicates in the image, make sure to choose one power source for your Arduino microcontroller to avoid conflicting voltages: either from the LiPo battery or a USB-to-serial converter.

The Fritzing diagram shows male header pins connected to all but the VCC pin on the serial header. When connecting the USB-to-serial converter, this allows users to upload code or view serial data through the Arduino Serial Monitor without needing to worry about conflicting voltages from the FTDI\'s 3.3V pin.

**Note:** Certain microcontrollers have built-in charge circuits already integrated in the design so you may not need to add a charge circuit. Make sure to check your microcontroller for more information.

### Connecting a Boost Circuit

Users can also include a boost circuit when users need a steady 5V input. Below is one example that uses the LiPo Charger/Booster 5V/1A to boost the voltage to 5V for the RedBoard Qwiic. Most microcontrollers usually run at 3.3V so you may not need to worry about boosting it for your Arduino. However, 5V could be used for addressable LEDs, servos, and motors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/RedBoard_Qwiic_5V_Fuel_Gauge_MAX17043_Charger_MCP73831_Boost_PAM2401_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/RedBoard_Qwiic_5V_Fuel_Gauge_MAX17043_Charger_MCP73831_Boost_PAM2401_Fritzing_bb.jpg)

As the note indicates in the image, make sure to choose one power source for your Arduino microcontroller to avoid conflicting voltages: either from the LiPo battery and charger/booster, or USB on the Arduino.

The Fritzing diagram does not show the wires disconnected from the LiPo charger/booster. However, this would be the better option to ensure that the battery is not connected to the RedBoard Qwiic\'s input power pins. Users could also disconnect the 5V pin from the RedBoard Qwiic\'s input power pin.

The other option would be to hack the USB cable and disconnect the 5V wire, which would be more of a hassle.

### Connecting a Display

For users that are interested in viewing how much charge a single cell LiPo battery has a available without a computer, users can attach a display to your microcontroller. Below is one example that addes a Qwiic Micro OLED to the first setup. Since you can control the display through I^2^C, it can be daisy chained using the Qwiic connectors. If you decide to use a different display, you will need to write code to output the values on the display.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials.\
\

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

\
If you\'ve never connected an CH340 device to your computer before, you may need to install drivers for the USB-to-serial converter. Check out our section on [\"How to Install CH340 Drivers\"](https://learn.sparkfun.com/tutorials/sparkfun-serial-basic-ch340c-hookup-guide#drivers-if-you-need-them) for help with the installation.

### SparkFun MAX1704x Fuel Gauge Arduino Library

The SparkFun MAX1704x Fuel Gauge Arduino Library can be downloaded with the Arduino library manager by searching \'**SparkFun MAX1704x Fuel Gauge**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library) to manually install.

[MAX1704x Fuel Gauge (ZIP)](https://github.com/sparkfun/SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library/archive/refs/heads/main.zip)

\

### SparkFun Qwiic OLED Arduino Library

For users using a Qwiic Micro OLED to display the readings, the SparkFun Qwiic OLED Arduino Library can be downloaded with the Arduino library manager by searching \'**SparkFun Qwiic OLED**\' or you can grab the zip here from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_OLED_Arduino_Library) to manually install.

[SparkFun Qwiic OLED Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_Qwiic_OLED_Arduino_Library/archive/refs/heads/main.zip)

\

**Note:** There are two different Arduino libraries that can be used for the Qwiic Micro OLED. In this tutorial we are going to use the latest Qwiic OLED Arduino Library. You can use the [older Micro OLED Breakout Arduino Library](https://github.com/sparkfun/SparkFun_Micro_OLED_Arduino_Library) as well. However, you will need to adjust the example code to work with the alternative library.

## Example 1: Simple Serial

In this example, we will be checking a single cell LiPo battery\'s voltage and the state of charge using the MAX17043. The output will be sent to the Serial Monitor.

### Hardware Hookup

For this example we will use the following parts from the [wishlist](https://www.sparkfun.com/wish_lists/170828).

- 1x [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/products/15425)
- 1x [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/products/15443)
- 1x [Break Away Headers - Straight](https://www.sparkfun.com/products/116)
- 1x [SparkFun LiPo Fuel Gauge - MAX17043](https://www.sparkfun.com/products/20680)
- 1x [Flexible Qwiic Cable - Female Jumper (4-pin)](https://www.sparkfun.com/products/17261)
- 1x [LiPo Battery](https://www.sparkfun.com/products/13854)
- 1x [JST Jumper 2 Wire Assembly](https://www.sparkfun.com/products/9914)

Solder and connect the circuit based on the following diagram as shown earlier. Instead of inserting the LiPo Fuel Gauge in a mini breadboard, you could connect the flexible Qwiic cable with female jumpers to the male break away headers that were soldered on the breakout board. For a more permanent connection, you could also cut the female jumpers, strip the Qwiic cable wires, and solder directly to the breakout board.

[![Fritzing Diagram connected to microcontroller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Fritzing_bb.jpg)

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library** \> **[Example1_Simple](https://github.com/sparkfun/SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library/blob/main/examples/Example1_Simple/Example1_Simple.ino)**. If you have not already, select your Board (in this case the **RedBoard Artemis Nano**), and associated COM port (in this case, **COM27**). Then hit the upload button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX1704X_Arduino_Simple.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX1704X_Arduino_Simple.JPG)

**Note:** This example can also be used with other LiPo Fuel Gaugs such as the MAX17044, MAX17048, and MAX17049. Simply comment out the line making an instance of the LiPo Fuel Gauge (i.e. `SFE_MAX1704X lipo;` by adding a single line comment (i.e. `//`. Then remove the single line comment line comment on the respective LiPo Fuel Gauge that you are using.

Open the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) and set it to **115200** baud to view the serial output. You should see the voltage, battery percent, and alert flag. In this case, the single cell LiPo battery that was connected to the IC was almost fully charged and at about 4.20V. Since the battery was higher than the threshold that was set, the alert flag was not triggered and remained low.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Battery_Percent_Fuel_Gauge_MAX1704X_Arduino_Simple_Serial_Output.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Battery_Percent_Fuel_Gauge_MAX1704X_Arduino_Simple_Serial_Output.JPG)

Depending on how your battery is connected to your system, the reading can be a bit misleading. When there is a dedicated LiPo battery charging circuit actively charging the single cell LiPo battery and the MAX1704X initially reads the battery, the values can be higher. Try disconnecting the LiPo battery from the microcontroller\'s VBATT pin and hitting the reset button on your microcontroller to restart the code. The image below shows both wires disconnected from the RedBoard Artemis Nano\'s JST connector since we would be using a 2-pin JST jumper wire.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_LiPo_Disconnected_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_LiPo_Disconnected_Fritzing_bb.jpg)

**Note:** For boards that have a built in LiPo charger and Fuel Gauge, try closing out the Arduino Serial Monitor, disconnecting the USB, and disconnecting the LiPo battery. Then reinsert the LiPo battery, connect the USB cable, and reopen the Arduino Serial Monitor. The IC will recalculate everything. While the voltage will be misleading as the LiPo battery is being actively charged by the charge circuit, the remaining charge will be closer to what is expected.

By reopening the Arduino Serial Monitor, you may see a different reading reflecting the current state of the single cell LiPo battery rather than the output voltage of the charge IC. The image below shows actual voltage and remaining charge. You may want to add a display and write additional code as an alternative to connecting to a computer\'s serial terminal.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX1704X_Arduino_Simple_Battery_Disconnected.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX1704X_Arduino_Simple_Battery_Disconnected.JPG)

## Example 4: MAX17048 KitchenSink

In this example, we will be checking a single cell LiPo battery\'s voltage and the state of charge using the MAX17048. The output will be sent to the Serial Monitor.

### Hardware Hookup

For this example we will use the following parts from the [wishlist](https://www.sparkfun.com/wish_lists/170829).

- 1x [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/products/15425)
- 1x [SparkFun IoT RedBoard - ESP32 Development Board](https://www.sparkfun.com/products/19177)
- 1x [LiPo Battery](https://www.sparkfun.com/products/13854)

In this case, we did not need to solder anything! The IoT RedBoard - ESP32 has a built in LiPo Fuel Gauge (MAX17048). By simply connecting a LiPo battery to the 2-pin JST connector and uploading code, we should be good to go!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/IoT_RedBoard_ESP32_LiPo_Fuel_Gauge_MAX17048_Battery_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/IoT_RedBoard_ESP32_LiPo_Fuel_Gauge_MAX17048_Battery_bb.jpg)

### Upload Code

From the menu, select the following: **File** \> **Examples** \> **SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library** \> **[Example4_MAX17048_KitchenSink](https://github.com/sparkfun/SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library/blob/main/examples/Example4_MAX17048_KitchenSink/Example4_MAX17048_KitchenSink.ino)**. If you have not already, select your Board (in this case the **SparkFun ESP32 IoT RedBoard**), and associated COM port (in this case **COM27**). Then hit the upload button.

[![LiPo connected to IoT RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048-Arduino_Kitchen_Sink.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048-Arduino_Kitchen_Sink.JPG)

Open the Arduino Serial Monitor and set it to **115200** baud to view the serial output. You should see the voltage, battery percent, alert flag, and several more readings. In this case, the single cell LiPo battery that was connected to the IC was fully charged and at about 4.10V.

[![Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048_Arduino_Kitchen_Sink.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048_Arduino_Kitchen_Sink.JPG)

*Click on image for closer view.*

But wait! Remember the previous example? If you looked closely at the circuit of the SparkFun IoT RedBoard - ESP32 Development Board, there is also\... you guessed it: a charge circuit built in. Try closing out the Arduino Serial Monitor, disconnecting the USB, and disconnecting the LiPo battery. Then reinsert the LiPo battery, connect the USB cable, and reopen the Arduino Serial Monitor. The IC will recalculate everything. In the image below, the voltage is a bit misleading since the charge IC is charging the LiPo battery and may not be the true representation of the LiPo battery\'s voltage. The remaining charge was closer to what was expected.

[![Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048_Arduino_Kitchen_Sink_Battery.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_LiPo_Fuel_Gauge_MAX17048_Arduino_Kitchen_Sink_Battery.JPG)

*Click on image for closer view.*

**Note:** For development boards that have a built in charge circuit and fuel gauge, you may want to consider using a display to view the LiPo battery\'s true voltage and remaining charge. Otherwise, you could use a multimeter to measure the LiPo battery\'s voltage when a USB cable is not plugged in. Below is an example that uses the Qwiic Micro OLED to display the LiPo battery\'s voltage and remaining charge since the IoT RedBoard ESP32 includes a built in charge circuit and fuel gauge (MAX17048). Just make sure to adjust the code for your fuel gauge and display. You can find some example code in the [Combined Example A](https://learn.sparkfun.com/tutorials/lipo-fuel-gauge-max1704x-hookup-guide#combined-example-a-simple-serial-and-qwiic-micro-oled) and [Combined Example B](https://learn.sparkfun.com/tutorials/lipo-fuel-gauge-max1704x-hookup-guide#combined-example-b-simple-serial-qwiic-micro-oled-battery-icon) later in this tutorial.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED_Simple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED_Simple.jpg)

## More Examples!!!

Looking for more examples? Try checking the other examples in the Arduino Library. Example 2 is basically the same as Example 1, however the code was written for Arduino microcontrollers that have a different non-standard Wire and Serial ports. Example 3 is also based on Example but are for users that are using the MAX17044 IC (MAX17044 is configured for a dual-cell 2S pack). You will see the same readings on the Arduino Serial Monitor for both examples.

[SparkFun MAX1704x Fuel Gauge Arduino Library \> Examples](https://github.com/sparkfun/SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library/tree/main/examples)

## Combined Example A: Simple Serial and Qwiic Micro OLED

In this example, we will be checking a single cell LiPo battery\'s voltage and the state of charge using the MAX17043. The output will be sent to the Serial Monitor and the Qwiic Micro OLED.

### Hardware Hookup

For this example we will use the following parts from the [wishlist](https://www.sparkfun.com/wish_lists/170830.js).

- 1x [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/products/15425)
- 1x [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/products/15443)
- 1x [Break Away Headers - Straight](https://www.sparkfun.com/products/116)
- 1x [SparkFun LiPo Fuel Gauge - MAX17043](https://www.sparkfun.com/products/20680)
- 1x [Flexible Qwiic Cable - Female Jumper (4-pin)](https://www.sparkfun.com/products/17261)
- 1x [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532)
- 1x [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260)
- 1x [LiPo Battery](https://www.sparkfun.com/products/13854)
- 1x [JST Jumper 2 Wire Assembly](https://www.sparkfun.com/products/9914)

Solder and connect the circuit based on the following diagram as shown earlier. Instead of inserting the LiPo Fuel Gauge in a mini breadboard, you could connect the flexible Qwiic cable with female jumpers to the male break away headers that were soldered on the breakout board. For a more permanent connection, you could also cut the female jumpers, strip the Qwiic cable wires, and solder directly to the breakout board. Insert the Qwiic Micro OLED between the LiPo Fuel Gauge and the RedBoard Artemis Nano.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)

After soldering and connecting the boards together, your setup should look similar to the following.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED.jpg)

Depending on the microcontroller that you have and setup, you may want to disconnect the LiPo battery when uploading code and monitoring the LiPo battery through the Arduino Serial Monitor. The values may be misleading due the built in charge circuit that is on the RedBoard Artemis Nano.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Power_Output_Disconnected_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Power_Output_Disconnected_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED.jpg)

### Upload Code

Copy and paste following code into your Arduino IDE. If you have not already, select your Board (in this case the **RedBoard Artemis Nano**), and associated COM port (in this case, **COM27**). Then hit the upload button.

    language:c
    /******************************************************************************
      Combined Simple Serial and Qwiic Micro OLED Example
      Modified By: Ho Yun "Bobby" Chan
      SparkFun Electronics
      Date: February 10, 2023
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This is a combined example of Paul Clark's MAX17043 Fuel Guage
      simple serial example and Kirk Benell's Qwiic OLED Hello
      example. The example reads a single cell LiPo battery's voltage
      and state-of-charge (SOC) using the MAX1704X. The voltage,
      percent remaining (i.e. the SOC), and alert flag are displayed
      as an output on the Qwiic Micro OLED.

      By opening the Arduino Serial Monitor (115200 baud), the example
      will also print the gauge's voltage, state-of-charge (SOC)
      readings, alert status to Serial.

      Feel like supporting open source hardware?
      Buy a board from SparkFun!

      LiPo Fuel Gauge - MAX17043: https://www.sparkfun.com/products/20680
      Qwiic Micro OLED: https://www.sparkfun.com/products/14532

      Distributed as-is; no warranty is given.
    ******************************************************************************/

    #include <Wire.h> // Needed for I2C

    //////////LIPO FUEL GAUGE//////////
    #include <SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library.h> // Click here to get the library: http://librarymanager/All#SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library

    SFE_MAX1704X lipo; // Defaults to the MAX17043

    //SFE_MAX1704X lipo(MAX1704X_MAX17043); // Create a MAX17043
    //SFE_MAX1704X lipo(MAX1704X_MAX17044); // Create a MAX17044
    //SFE_MAX1704X lipo(MAX1704X_MAX17048); // Create a MAX17048
    //SFE_MAX1704X lipo(MAX1704X_MAX17049); // Create a MAX17049

    double voltage = 0; // Variable to keep track of LiPo voltage
    double soc = 0; // Variable to keep track of LiPo state-of-charge (SOC)
    bool alert; // Variable to keep track of whether alert has been triggered

    //////////QWIIC MICRO OLED//////////
    #include <SparkFun_Qwiic_OLED.h> //http://librarymanager/All#SparkFun_Qwiic_Graphic_OLED

    // The Qwiic OLED Library supports three different types of SparkFun boards. The demo uses the following
    // defines to determine which device is being used. Uncomment the device being used for this demo.

    QwiicMicroOLED myOLED;
    // QwiicTransparentOLED myOLED;
    // QwiicNarrowOLED myOLED;

    // Fonts
    #include <res/qw_fnt_5x7.h>
    //#include <res/qw_fnt_8x16.h>, not used
    //#include <res/qw_fnt_31x48.h>, not used
    //#include <res/qw_fnt_7segment.h>, not used
    //#include <res/qw_fnt_largenum.h>, not used

    void setup() 

      // Initalize the OLED device and related graphics system
      if (myOLED.begin() == false)
      

      // Quick start restarts the MAX17043 in hopes of getting a more accurate
      // guess for the SOC.
      lipo.quickStart();

      // We can set an interrupt to alert when the battery SoC gets too low.
      // We can alert at anywhere between 1% - 32%:
      lipo.setThreshold(20); // Set alert threshold to 20%.
    }// end setup()

    void loop() 
      else 

      // There's nothing on the screen yet - Now send the graphics to the device
      myOLED.display();

      // Print the variables to Serial Terminal:
      Serial.print(F("Voltage: "));
      Serial.print(voltage);  // Print the battery voltage
      Serial.println(F(" V"));

      Serial.print(F("Percentage: "));
      Serial.print(soc); // Print the battery state of charge
      Serial.println(F(" %"));

      Serial.print(F("Alert: "));
      Serial.println(alert);
      Serial.println();

      delay(500);
    }//end loop()

Disconnect the USB cable from your RedBoard Artemis Nano. Hit the reset button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED_Powered_Simple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED_Powered_Simple.jpg)

Looking close at the display, you should see the voltage, remaining charge, the alert flag indicating if the battery is low, and a battery meter icon. These values may be different depending on how much charge the LiPo battery has available.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX1704X_Qwiic_Cable_Micro_OLED_Output_Display_Simple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX1704X_Qwiic_Cable_Micro_OLED_Output_Display_Simple.jpg)

**Note:** For development boards that have a built in charge circuit and fuel gauge, you may want to consider using a display to view the LiPo battery\'s true voltage and remaining charge. Otherwise, you could use a multimeter to measure the LiPo battery\'s voltage when a USB cable is not plugged in. Below is an example that uses the Qwiic Micro OLED to display the LiPo battery\'s voltage and remaining charge since the IoT RedBoard ESP32 includes charge circuit and fuel gauge (MAX17048). Just make sure to adjust the code for your fuel gauge and display.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED_Simple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED_Simple.jpg)

## Combined Example B: Simple Serial, Qwiic Micro OLED, Battery Icon

This example is pretty much the same as the previous combined example. However, we will add an additional battery meter icon.

### Hardware Hookup

For this example we will use the same parts as the previous combined example\'s [wishlist](https://www.sparkfun.com/wish_lists/170830).

- 1x [Reversible USB A to C Cable - 0.8m](https://www.sparkfun.com/products/15425)
- 1x [SparkFun RedBoard Artemis Nano](https://www.sparkfun.com/products/15443)
- 1x [Break Away Headers - Straight](https://www.sparkfun.com/products/116)
- 1x [SparkFun LiPo Fuel Gauge - MAX17043](https://www.sparkfun.com/products/20680)
- 1x [Flexible Qwiic Cable - Female Jumper (4-pin)](https://www.sparkfun.com/products/17261)
- 1x [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/products/14532)
- 1x [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/products/17260)
- 1x [LiPo Battery](https://www.sparkfun.com/products/13854)
- 1x [JST Jumper 2 Wire Assembly](https://www.sparkfun.com/products/9914)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/SparkFun_Artemis_Thing_Plus_Fuel_Gauge_MAX17043_Qwiic_Micro_OLED_Fritzing_bb.jpg)

### Upload Code

Copy and paste following code into your Arduino IDE.

    language:c
    /******************************************************************************
      Combined Simple Serial and Qwiic Micro OLED Example
      Modified By: Ho Yun "Bobby" Chan
      SparkFun Electronics
      Date: February 10, 2023
      License: MIT. See license file for more information but you can
      basically do whatever you want with this code.

      This is a combined example of Paul Clark's MAX17043 Fuel Guage
      simple serial example, Kirk Benell's Qwiic OLED Hello example,
      and Nathan Seidle's RTK Display Test Sketch. The example reads a
      single cell LiPo battery's voltage and state-of-charge (SOC) 
      using the MAX1704X. The voltage, percent remaining (i.e. the 
      SOC), and alert flag are displayed as an output on the Qwiic
      Micro OLED. A graphic of a LiPo battery's remaining charge is
      displayed on the Qwiic Micro OLED as well.

      By opening the Arduino Serial Monitor (115200 baud), the example
      will also print the gauge's voltage, state-of-charge (SOC)
      readings, alert status to Serial.

      Feel like supporting open source hardware?
      Buy a board from SparkFun!

      LiPo Fuel Gauge - MAX17043 : https://www.sparkfun.com/products/20680
      Qwiic Micro OLED: https://www.sparkfun.com/products/14532

      Distributed as-is; no warranty is given.
    ******************************************************************************/

    #include <Wire.h> // Needed for I2C

    //////////LIPO FUEL GAUGE//////////
    #include <SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library.h> // Click here to get the library: http://librarymanager/All#SparkFun_MAX1704x_Fuel_Gauge_Arduino_Library

    SFE_MAX1704X lipo; // Defaults to the MAX17043

    //SFE_MAX1704X lipo(MAX1704X_MAX17043); // Create a MAX17043
    //SFE_MAX1704X lipo(MAX1704X_MAX17044); // Create a MAX17044
    //SFE_MAX1704X lipo(MAX1704X_MAX17048); // Create a MAX17048
    //SFE_MAX1704X lipo(MAX1704X_MAX17049); // Create a MAX17049

    double voltage = 0; // Variable to keep track of LiPo voltage
    double soc = 0; // Variable to keep track of LiPo state-of-charge (SOC)
    bool alert; // Variable to keep track of whether alert has been triggered

    //////////QWIIC MICRO OLED//////////
    #include <SparkFun_Qwiic_OLED.h> //http://librarymanager/All#SparkFun_Qwiic_Graphic_OLED
    #include "icons.h"

    // The Qwiic OLED Library supports three different types of SparkFun boards. The demo uses the following
    // defines to determine which device is being used. Uncomment the device being used for this demo.
    QwiicMicroOLED myOLED;
    // QwiicTransparentOLED myOLED;
    // QwiicNarrowOLED myOLED;

    // Fonts
    #include <res/qw_fnt_5x7.h>
    //#include <res/qw_fnt_8x16.h>, not used
    //#include <res/qw_fnt_31x48.h>, not used
    //#include <res/qw_fnt_7segment.h>, not used
    //#include <res/qw_fnt_largenum.h>, not used

    void setup() 

      // Initalize the OLED device and related graphics system
      if (myOLED.begin() == false)
      

      // Quick start restarts the MAX17043 in hopes of getting a more accurate
      // guess for the SOC.
      lipo.quickStart();

      // We can set an interrupt to alert when the battery SoC gets too low.
      // We can alert at anywhere between 1% - 32%:
      lipo.setThreshold(20); // Set alert threshold to 20%.
    }

    void loop() 
      else 

      if (soc >= 50.00) 
      else if (20.00 <= soc < 50.00) 
      else if (10.00 <= soc < 20.00) 
      else 

      // There's nothing on the screen yet - Now send the graphics to the device
      myOLED.display();

      // Print the variables to Serial Terminal:
      Serial.print(F("Voltage: "));
      Serial.print(voltage);  // Print the battery voltage
      Serial.println(" V");

      Serial.print(F("Percentage: "));
      Serial.print(soc); // Print the battery state of charge
      Serial.println(" %");

      Serial.print(F("Alert: "));
      Serial.println(alert);
      Serial.println();

      delay(500);
    }

    //Wrapper to avoid needing to pass width/height data twice
    void displayBitmap(uint8_t x, uint8_t y, uint8_t imageWidth, uint8_t imageHeight, uint8_t *imageData) 

To keep track of the icons that we create, we are going to create a header file with the **\*.ino**. This is useful when writing code for big projects that involve a lot of components (e.g. RTK Express, RTK Express Plus, RTK Facet, RTK Facet L-Band, etc.). Click on the icon to create a new tab. We will name this **icons.h**.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/Creating_New_Tab_Arduino.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/Creating_New_Tab_Arduino.JPG)

Copy and paste the following code into tab.

    language:c
    uint8_t Battery_3 [] = ;
    int Battery_3_Height = 12;
    int Battery_3_Width = 19;

    uint8_t Battery_2 [] = ;
    int Battery_2_Height = 12;
    int Battery_2_Width = 19;

    uint8_t Battery_1 [] = ;
    int Battery_1_Height = 12;
    int Battery_1_Width = 19;

    uint8_t Battery_0 [] = ;
    int Battery_0_Height = 12;
    int Battery_0_Width = 19;

If you have not already, select your Board (in this case the **RedBoard Artemis Nano**), and associated COM port (in this case, **COM27**). Then hit the upload button. Disconnect the USB cable from your RedBoard Artemis Nano. Hit the reset button.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED_Powered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17043_Qwiic_Cable_Artemis_RedBoard_Nano_Micro_OLED_Powered.jpg)

Looking close at the display, you should see the voltage, remaining charge, the alert flag indicating if the battery is low, and a battery meter icon. These values may be different depending on how much charge the LiPo battery has available!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX1704X_Qwiic_Cable_Micro_OLED_Output_Display.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX1704X_Qwiic_Cable_Micro_OLED_Output_Display.jpg)

**Note:** Similar to the previous example, you could use this code for boards that have a built in charge circuit and fuel gauge. Just make sure to adjust the code for your fuel gauge and display.\
\

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/4/6/LiPo_Fuel_Gauge_MAX17048_Qwiic_Cable_IoT_RedBoard-ESP32_Nano_Micro_OLED.jpg)

## Troubleshooting

[] **Not working as expected and need help?**\
\
If you need technical assistance and more information on a product that is not working as you expected, we recommend heading on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\

[SparkFun Forums](https://forum.sparkfun.com/)