# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-a111-pulsed-radar-sensor

## Introduction

**Heads up!** If you are looking for the hookup guide for the SparkX version of the A111, you can check out the retired tutorial: [Using the A111 Pulsed Radar Sensor with a Raspberry Pi](https://learn.sparkfun.com/tutorials/using-the-a111-pulsed-radar-sensor-with-a-raspberry-pi). However, the older tutorial is outdated due to the SDK version used in the previous guide.

Does your project require high-precision, cutting-edge distance, speed, motion, and/or gesture sensing? We\'re not talking ultrasonic, or even infrared here, but 60GHz radar! Say hello to our tiny, pulsed radar friend the [Acconeer A111](https://www.sparkfun.com/products/16826)!

[![SparkFun Pulsed Radar Breakout - A111](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/4/2/16826-SparkFun_Pulsed_Radar_Breakout_-_A111-02.jpg)](https://www.sparkfun.com/sparkfun-pulsed-radar-breakout-a111.html)

### [SparkFun Pulsed Radar Breakout - A111](https://www.sparkfun.com/sparkfun-pulsed-radar-breakout-a111.html) 

[ SEN-16826 ]

The SparkFun Pulsed Radar Breakout provide you with a high-precision distance measurement unit with reliable speed, motion, o...

[ [\$60.95] ]

[![SparkFun Pulsed Radar Breakout - A111](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/1/7/4/15577-SparkFun_Pulsed_Radar_Breakout_-_A111-01.jpg)](https://www.sparkfun.com/products/15577)

### [SparkFun Pulsed Radar Breakout - A111](https://www.sparkfun.com/products/15577) 

[ SEN-15577 ]

The SparkFun Pulsed Radar Breakout provide you with a high-precision distance measurement unit with reliable speed, motion, o...

**Retired**

The A111 is a single-chip solution for pulsed coherent radar (PCR) \-- it comes complete with antennae and an SPI interface capable of speeds of up to 50MHz. Applications for PCR include distance-sensing, gesture, motion, and speed detection. The sensor can monitor one-or-more objects at distances of up to two meters.

Our breakout board for the A111 includes a 1.8V regulator, voltage-level translation, and it breaks out all pins of the pulsed radar sensor to both 0.1-inch and Raspberry Pi-friendly headers.

### Required Materials

**Heads up!** The A111 was designed to work with an ARMv7 to work at a minimum. We were able to get the sensor working on the Raspberry Pi 3, 3B+, and 4.

To use the A111 you\'ll need either an ARMv7 or an ARM Cortex-M4 \-- the closed-source SDK currently only supports these architectures. This tutorial will explain how to use the radar sensor with a **Raspberry Pi** \-- a platform based on an architecture supported by the A111\'s SDK.

The A111 Breakout **includes a 20-pin, 2x10 female header**, which should mate to Raspberry Pi\'s of any generation. If you\'d rather manually wire the A111 to your Raspberry Pi and about 9x male-to-female wires should do the trick.

[![SparkFun Pulsed Radar Breakout - A111](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/4/2/16826-SparkFun_Pulsed_Radar_Breakout_-_A111-02.jpg)](https://www.sparkfun.com/sparkfun-pulsed-radar-breakout-a111.html)

### [SparkFun Pulsed Radar Breakout - A111](https://www.sparkfun.com/sparkfun-pulsed-radar-breakout-a111.html) 

[ SEN-16826 ]

The SparkFun Pulsed Radar Breakout provide you with a high-precision distance measurement unit with reliable speed, motion, o...

[ [\$60.95] ]

[![Jumper Wires Premium 12\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/8/7/09385-03.jpg)](https://www.sparkfun.com/jumper-wires-premium-12-m-f-pack-of-10.html)

### [Jumper Wires Premium 12\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-12-m-f-pack-of-10.html) 

[ PRT-09385 ]

This is a SparkFun exclusive! These are 12\" long, 26 AWG jumper wires terminated as male to female. Use these to jumper from ...

[ [\$4.95] ]

[![Raspberry Pi 3 B+ Starter Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/9/7/15361-Raspberry_Pi_3_B__Starter_Kit-01.jpg)](https://www.sparkfun.com/products/15361)

### [Raspberry Pi 3 B+ Starter Kit](https://www.sparkfun.com/products/15361) 

[ KIT-15361 ]

The Raspberry Pi 3 B+ Starter Kit is a great way to gain a solid introduction to the small, credit-card-sized computer.

**Retired**

#### Optional Materials

You have several options when it comes to working with the Raspberry Pi. Most commonly, the Pi is used as a standalone computer, which requires a monitor, keyboard, and mouse (listed below). To save on costs, the Pi can also be used as a [*headless* computer](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/all) (without a monitor, keyboard, and mouse). This setup has a slightly more difficult learning curve, as you will need to use the *command-line interface* (CLI) from another computer. However, you can also connect to a headless Pi using a [remote desktop connection with VNC](https://learn.sparkfun.com/tutorials/795) as well from another computer after configuring the settings.

[![Raspberry Pi LCD - 7\" Touchscreen](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/4/13733-01.jpg)](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html)

### [Raspberry Pi LCD - 7\" Touchscreen](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html) 

[ LCD-13733 ]

This 7\" Raspberry Pi Touchscreen LCD provides you with the ability to create a standalone device that can be utilized as a cu...

[ [\$88.30] ]

[![Logitech K400 Plus Wireless Touch Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/9/4/16300-Logitech_K400_Plus_Wireless_Touch_Keyboard-01.jpg)](https://www.sparkfun.com/logitech-k400-plus-wireless-touch-keyboard.html)

### [Logitech K400 Plus Wireless Touch Keyboard](https://www.sparkfun.com/logitech-k400-plus-wireless-touch-keyboard.html) 

[ WIG-16300 ]

The Logitech K400 Plus Wireless Touch Keyboard is a compact keyboard with an integrated touchpad that puts all your controls ...

[ [\$42.95] ]

### Suggested Reading

If you have not set up a Raspberry Pi before, we recommend looking at the following tutorials to get started. Overall, the setup is the same regardless of the version that you have.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

March 14, 2020

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

April 11, 2016

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. Using the Pi as a headless setup or with VNC can be useful when developing applications with the Pi.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

### Raspberry Pi SPI and I2C Tutorial 

Learn how to use serial I2C and SPI buses on your Raspberry Pi using the wiringPi I/O library for C/C++ and spidev/smbus for Python.

[](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup)

### Headless Raspberry Pi Setup 

Configure a Raspberry Pi without a keyboard, mouse, or monitor.

[](https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc)

### How to Use Remote Desktop on the Raspberry Pi with VNC 

Use RealVNC to connect to your Raspberry Pi to control the graphical desktop remotely across the network.

## Hardware Overview

**Revision Changes:** Overall, the functionality between v1.0 for v1.1 is the same. Minor changes in v1.1 include:\
\

- PTH for VCCIO
- Bypass jumper to set VCCIO to VIN
- Silkscreen name change for input voltage (5V =\> VIN)
- Improved logic level translation on the Raspberry Pi side

This section covers the hardware overview of both versions of the board. To see what version of the board that you have, you can check the back of the board near the CS pin. You\'ll also notice the additional bypass jumper on v1.1 that was not included on v1.0.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![v1.1 labeled on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1.jpg) | [![v1.0 labeled on the back of the board](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/15577-SparkFun_Pulsed_Radar_Breakout_-_A111-v1_0.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/15577-SparkFun_Pulsed_Radar_Breakout_-_A111-v1_0.jpg) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Version number on the back of the board for v1.1 and v1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Sensor and Crystal

The breakout board is populated with the A111 IC and an external 26MHz crystal oscillator. The IC comes with two antennae and uses mmWave radio to sense objects via radar pulses.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![A111 Populated on Top v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Sensor.jpg) | [![vA111 Populated on Top v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111.jpg) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *A111 Populated on Top v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

You\'ll find the external crystal oscillator populated on the back of the board. The location is the same on both versions of the board.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Crystal Oscillator Populated on Back v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Crystal_Oscillator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Crystal_Oscillator.jpg) | [![Crystal Oscillator Populated on Back v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Crystal_Oscillator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Crystal_Oscillator.jpg) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Crystal Oscillator Populated on Back v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### 2x13 Female Header

To keep the size of the board small, there is a 2x13 female header soldered on the board to easily mate with a [Raspberry Pi\'s standard header](https://learn.sparkfun.com/tutorials/raspberry-gpio#gpio-pinout).

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![HAT Standard Header with Female Connector v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Pi_HAT_Standard_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Pi_HAT_Standard_Header.jpg) | [![HAT Standard Header with Female Connector v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Pi_26-Pin_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Pi_26-Pin_Header.jpg) |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *HAT Standard Header with Female Connector v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

This should only cover the part of the 2x20 male headers on the Pi. Regardless of the version number, the HAT will be stacked near the display port\'s ribbon cable connector.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![A111 HAT Stacked on a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-v1_1_Pulsed-Radar-HAT-_Stacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-v1_1_Pulsed-Radar-HAT-_Stacked.jpg) | [![A111 HAT Stacked on a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-HAT-_Stacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-HAT-_Stacked.jpg) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *A111 HAT v1.1 and v1.0 Stacked on a Raspberry Pi*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Additional Pins and Jumper Broken Out

Just above the 26-Pin header, there are additional pins broken out for SPI, interrupt, enable, and power if you need access to the pins. Note that in v1.1, the input voltage is labeled as `VIN` while 1.0 labels the pin as `5V`. Both pins are connected to 5V of the Raspberry Pi\'s HAT standard pinout. For v1.1, the additional PTH for VCCIO is included between the enable and GND pin. For v1.1, additional pins are shifted and align with the 2x13 header.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![A111 Additional Header Pins Broken Out for SPI, Interrupt, Enable, Power, and VCCIO on v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_PTH.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_PTH.jpg) | [![A111 Additional Header Pins Broken Out for SPI, Interrupt, Enable, and Power on v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Additional_Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Additional_Pins.jpg) |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Pins broken out on v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For v1.1, you\'ll also notice a bypass jumper (labeled as `BYP`). [Adding a solder jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all#adding-a-solder-jumper) to the board will set `VCCIO` to `VIN`.

[![Bypass Jumper on v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Jumper.jpg)

**Note:** Adding a solder jumper to the v1.1\'s `BYP` pin will set VCCIO to VIN. If you are stacking the HAT on a Raspberry Pi, this will set the logic level on the Raspberry Pi\'s side to 5V.We recommend leaving this jumper alone when stacking the board on a Pi.

The A111 IC requires an input voltage of **1.8V**, so a voltage regulator is populated on the back.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Voltage Regulator on v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Voltage_Regulator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Voltage_Regulator.jpg) | [![Voltage Regulator v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Voltage_Regulator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111_Voltage_Regulator.jpg) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Voltage Regulator on v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Additionally, the [I/O logic level](https://learn.sparkfun.com/tutorials/logic-levels) on the A111 is **1.8V**, so a logic converter is included to translate the signals between the Raspberry Pi.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Logic Level Converter v1.1](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Logic_Level_Translator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/16826-SparkFun_Pulsed_Radar_Breakout_A111_v1_1_Logic_Level_Translator.jpg) | [![Logic Level Converter v1.0](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111-Logic_Level_Converter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Pulsed_Radar_Breakout_A111-Logic_Level_Converter.jpg) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Logic Level Converter on v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Board Dimensions

The overall board size is 1.30in x 1.55in. There are two additional mounting holes spaced 0.10 inches away from the edge of the board.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![v1.1 Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/3/7/2/1/b/SparkFun_A111_Pulsed_Radar_Breakout_Board_Dimensions_v1_1.png)](v1.1%20Board%20Dimensions) | [![v1.0 Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/SparkFun_A111_Pulsed_Radar_Sensor_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/SparkFun_A111_Pulsed_Radar_Sensor_Board_Dimensions.png) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Board Dimensions for v1.1 and v1.0*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Hardware Assembly

The A111 Pulsed Radar Breakout is designed to sit directly on top of a Raspberry Pi. Again, it doesn\'t span all 40 (2x20) pins of a Raspberry Pi B+ (or later), but the 26-pin --- 2x13 --- header should be compatible with any Pi.

Connect the shield to a Raspberry Pi ensuring that the \"**Pi Display**\" text on the breakout matches up with the display header on your Pi. The sensor should be facing up after plugging it in.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![A111 HAT Stacked on a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-v1_1_Pulsed-Radar-HAT-_Stacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-v1_1_Pulsed-Radar-HAT-_Stacked.jpg) | [![A111 HAT Stacked on a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-HAT-_Stacked.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-HAT-_Stacked.jpg) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *A111 HAT v1.1 and v1.0 Stacked on a Raspberry Pi*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Or, if you\'d like to manually wire the breakout up to a [Raspberry Pi\'s standard pinout](https://learn.sparkfun.com/tutorials/raspberry-gpio/all#gpio-pinout), here is the pin-out we\'ll use through the rest of this tutorial. As stated in the hardware overview for v1.1, the input voltage is labeled as `VIN` while 1.0 labels the pin as `5V`. Both pins are connected to 5V of the Raspberry Pi\'s HAT standard pinout. For v1.1, the additional PTH for VCCIO is included between the enable and GND pin.

  v1.1 Breakout Pin   v1.0 Breakout Pin   Raspberry Pi Pin Name   RasPi Hardware Pin Number
  ------------------- ------------------- ----------------------- ---------------------------
  CS                  CS                  SPI0 CS0                24
  SCLK                SCLK                SPI0 SCLK               23
  MISO                MISO                SPI0 MISO               21
  MOSI                MOSI                SPI0 MOSI               19
  INT                 INT                 GPIO25                  22
  EN                  EN                  GPIO27                  13
  VCCIO                                   **3.3V**                1, 17
  GND                 GND                 GND                     6, 14, 20, etc.
  VIN                 5V                  **5V**                  2, 4

⚡ **Input Voltage and Logic Levels:** \"5V\" should power the sensor, which can consume \~80mA.\
\
When connecting to the additional pins broken out next to the Raspberry Pi\'s I/O, make sure to not accidentally connect anything higher than 3.3V since it is only 3.3V tolerant.

## Configure Your Pi

**Raspbian and SPI**

This tutorial assumes you\'ve already set up a Raspberry Pi with Raspbian. For help installing the Debian-based OS on your Pi, check out the docs on [Raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/). Or \-- better yet! \-- check out our [Headless Raspberry Pi Setup tutorial](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup).

You\'ll also need to **enable SPI** on your Pi. For help with that, check out our [SPI on Pi tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#spi-on-pi).

We are going to assume you already have a Raspberry Pi up and running with Raspbian. We\'ll also assume that it is connected to the Internet. If not, check out our starter kits and tutorials on setting up a Raspberry Pi. We recommend looking at the following tutorials to get started. Overall, the setup is the same regardless of the version that you have.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

March 14, 2020

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

April 11, 2016

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

Make sure to update the image so that we have the latest distribution. Enter the following commands in the [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) individually to update your image.

    language:bash
    sudo apt-get update
    sudo apt-get dist-upgrade

**Note:** sudo stands for \"Super User Do\", it is a way to give you superuser powers from the command line. Be careful whenever using `sudo`.

### User Configuration Settings

Once you are set up, I highly recommend changing your default login and password: (**username**: pi, **password**: raspberry). The Raspberry Pi Configuration tool is a quick way to change your password as well as setup the network, language, keyboard, etc. There are two methods to adjust the settings. You can use the GUI by heading to the **Pi Start Menu** \> **Preferences** \> **Raspberry Pi Configuration** \> **Interfaces**. For the old school heads, you can also use the [**raspi-config** tool](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide/all#configuring-the-pi) by typing the following command using the [command line](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) and then go through the menus to update your information.

    language:bash
    sudo raspi-config

You\'ll want to enable the SPI pins using the tool to read sensor with SPI. If you are using hte GUI, simple select **Enable** and click on the OK button. If you are using the **raspi-config**, follow the prompts to finish setting up the SPI. For more information, check out our [tutorial to set up the SPI pins on a Pi](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#spi-on-pi).

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Enabling SPI via Desktop GUI](https://cdn.sparkfun.com/r/675-675/assets/learn_tutorials/4/4/9/Raspberry-Pi-Configuration-Enable-Interfaces.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/Raspberry-Pi-Configuration-Enable-Interfaces.png)   [![Enabling I2C on a Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/9/spi-menu2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/9/spi-menu2.png)
  *Enabling SPI via Desktop GUI*                                                                                                                                                                                                                                *raspi-config tool for SPI in the Terminal*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You\'ll need to restart your Pi for the changes to take effect.

## Get the SDK

**Heads up!** The following instructions are listed for SDK v2.1. Acconeer provides frequent software updates to the SDK packages to fix bugs and provide the latest features. The steps may not apply for higher SDK versions. You may need to adjust the path names depending on the changes. for higher versions.

The software development kit (SDK) for the A111 is, unfortunately, locked behind a closed source blob that currently only supports Cortex-M4 and ARMv7 platforms. However, the folks over at Acconeer have agreed to host the latest version of their SDK with our example code from their website. To download the latest SDK from Acconeer, visit [Acconeer\'s \"Developer\" page](https://developer.acconeer.com/) on your Raspberry Pi\'s browser.

[Visit Acconeer\'s \"Developer\" for the SDK](https://developer.acconeer.com/)

You\'ll need an account in order to have access to the files. Click on the link at the bottom of the page to create one or log in. Or click on the shortcuts below.

[Sign Up with Acconeer](https://developer.acconeer.com/register/) [Log In with Acconeer](https://developer.acconeer.com/log-in/)

Once you are logged in, the \"**Software Download**\" tab will include additional links to download the SDK. Scroll down the webpage to the section for the **SPARKFUN**. Acconeer is constantly updating and improving the software. We used **v2.1** of the software when writing this tutorial so the version may be different from the version that you download. Click on the **Download** button for the latest version. In this case, it was v2.1.

[![Download v2.1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Acconeer-A111-SDK_Downloads_Update.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Acconeer-A111-SDK_Downloads_Update.png)

*Download the SDK from Acconeer.*

Read through the license, agree, and click on the **Download acconeer_rpi_sparkfun** button for the software. Depending on your browser, you may need to refresh the page and repeat the directions before the button is active.

Once downloaded, head to directory where you downloaded the ZIP. You can use the GUI or you can use the [terminal](https://learn.sparkfun.com/tutorials/terminal-basics) to unzip the SDK using the following commands (included are commands to install unzip). Just make sure to update the file name with the version that you downloaded. Assuming that you are in the **Downloads** folder, you will be using the following command in the Terminal.

    language:bash
    unzip acconeer_rpi_sparkfun_v2_1_0.zip

**Note:** Make sure you replace the acconeer ZIP file name with that of your downloaded SDK version.

Then `cd` to the \"**rpi_sparkfun**\" directory to prepare to build the example software. Depending on the version that you downloaded, the path might be slightly different. Make sure to use the `ls` to verify the contents of the unzipped **a111** folder if you have issues navigating through the directory.

### SDK Overview

The A111 SDK includes source code, archived libraries, include files, and documentation for using the A111 pulsed radar sensor. Here\'s a quick overview of what\'s included with the SDK:

- **doc** --- Doxygen-generated documentation for the A111 API and source code.
- **include** --- Header and API files which describe how to interact with the pre-compiled A111 libraries.
- **lib** --- Pre-compiled A111 static archives. API for these files are provided in the \"include\" directory.
- **out** --- Compiled board and example object and executable files.
- **rule** --- Recursive Makefile rules for board and example files.
- **source** --- C source files for custom boards and example applications.
- **makefile** --- Top-level makefile. Recursively calls files in the \"rule\" directory to build example and board files.

## Build and Run the Test Sketch

In the terminal, executing the make file --- and it\'s recursive dependencies --- should build all of the examples you may use with the **A111**. To build all board and example files, navigate to the SDK\'s top-level directory (in this case, it should be similar to **\...Downloads/rpi_sparkfun**) where your **makefile** is located and type [make] or [make all] command in the terminal. You should see something similar to the output below.

[![Terminal Output Using Make Command](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_make_terminal-update.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_make_terminal-update.png)

#### Troubleshooting

If you have any trouble building the board and example files, ensure that you have gcc and make packages installed. (E.g. `apt-get install make gcc`)

### Running the Example Applications

Once compiled you can run the example applications. Navigate to the **\.../out** folder with the `cd` in the terminal window. You can run the example by clicking on the executable or typing the following command. We recommend typing the command in the terminal to view the data. A few of the applications will automatically close the window after taking sensor data if you choose to click on the executable.

    language:bash
    ./example_detector_distance_basic_rpi_sparkfun_a111_r2c

Once you type (or paste the command in the Terminal), hit [Enter] on your keyboard to execute the command.

[![Before Entering Command](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_Raspberry_Pi_Terminal_Distance_Basic_Sensor-update.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_Raspberry_Pi_Terminal_Distance_Basic_Sensor-update.png)

This will run our modified distance-detector example application. For simplicity, it will show the distance of an object that is in front of the antennae.

[![Distance Example Running](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_Raspberry_Pi_Distance_Sensing_Basic-update.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/A111_Raspberry_Pi_Distance_Sensing_Basic-update.png)

By placing an object in front of the sensor, the distance should vary based on what the A111 can detect. The application will continue running in the terminal window until the loop is finished. In this case, the example took 10 samples. Try adjusting the code to obtain more samples!

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Hand in Front of A111 Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111_v1_1-Pulsed-Radar-Sensing-Object-Distance.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111_v1_1-Pulsed-Radar-Sensing-Object-Distance.jpg) | [![Hand in Front of A111 Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-Sensing-Object-Distance.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/0/0/4/Raspberry-Pi-A111-Pulsed-Radar-Sensing-Object-Distance.jpg) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Hand placed in front the A111 v1.1 and v1.0 with the Pi remotely connected via VNC.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Running Other Examples

In addition to the distance detector basic, the SDK includes a few extra examples. To execute these files, run them from the **out** directory:

- **example_detector_presence_rpi_sparkfun_a111_r2c** --- If there is an object moving in front of the sensor, it will output a true. Otherwise, the output is false.
- **example_detector_obstacle_rpi_sparkfun_a111_r2c** --- Checks to see if there is an object in the way.
- **example_service_iq_rpi_sparkfun_a111_r2c** --- Advanced version of the envelope service, which includes phase information for very small variations in distance. The output will be in polar coordinates.
- **example_service_power_bins_rpi_sparkfun_a111_r2c** --- Demonstrates how to use A111 \"power bins,\" which are still, kind of, a mystery to us\...
- **example_detector_distance_peak_rpi_sparkfun_a111_r2c** --- This application will begin by calculating raw peak-distances, with a maximum of ten reflections. The example will briefly estimate minimum and maximum threshold.

Make sure to read through the comments in the code (located in the **source** folder), datasheet, user guide, and associated documents from Acconeer for more information before writing your own custom code for the A111.

## Troubleshooting 

For the best support, we recommend checking the FAQ or submitting a support ticket with Acconeer since they handle the software SDK packages.

[Acconeeer \> FAQ and SDK Support](https://developer.acconeer.com/)