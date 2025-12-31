# Source: https://learn.sparkfun.com/tutorials/qwiic-multiport-hookup-guide

## Introduction

The [SparkFun Qwiic Multiport](https://www.sparkfun.com/products/18012) adds additional ports to boards that have only one Qwiic port on their I^2^C bus. Once added, you can use it as a hub to add as many I^2^C devices to the bus as you need ^[\[1\]](https://learn.sparkfun.com/tutorials/qwiic-multiport-hookup-guide#note1)^ ! You can also use the board as an alternative to a daisy chained configuration.

[![SparkFun Qwiic MultiPort](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/2/2/3/18012-SparkFun_Qwiic_MultiPort-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-multiport.html)

### [SparkFun Qwiic MultiPort](https://www.sparkfun.com/sparkfun-qwiic-multiport.html) 

[ BOB-18012 ]

The Qwiic MultiPort adds additional ports to boards that have only one Qwiic port on the I2C bus.

[ [\$2.50] ]

[**Note:**](https://learn.sparkfun.com/tutorials/qwiic-multiport-hookup-guide#note1) Technically, there are limitations to how many boards that you can add to the bus. You may need to adjust [pull-up resistors](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) depending on what is connected. This is usually about 7x boards. You may also need to disconnect 3.3V to certain devices and inject power depending on the total power required. Keep in mind the Qwiic cable wires are [small and have a max current of about 226mA].

### Required Materials

To follow along with this tutorial, you will need a microcontroller or single board computer with a Qwiic connector. You will also need a Qwiic cable and a way to power the board. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

Besides having the Qwiic MultiPort in your cart, here are the parts if you decide to go with a microcontroller. You can easily [swap out the microcontroller depending on your project\'s needs with MicroMod](https://www.sparkfun.com/micromod#processor_boards). Make sure to include the Qwiic-enabled device in your cart as well!

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![USB 3.1 Cable A to C - 3 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/7/2/14743-USB_3.1_Cable_A_to_C_-_3_Foot-01.jpg)](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html)

### [USB 3.1 Cable A to C - 3 Foot](https://www.sparkfun.com/usb-3-1-cable-a-to-c-3-foot.html) 

[ CAB-14743 ]

USB C is fantastic. But until we have converted all our hubs, chargers, and ports over to USB C this is the cable you\'re goin...

[ [\$7.95] ]

[![SparkFun MicroMod ATP Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/8/1/2/16885-SparkFun_MicroMod_ATP_Carrier_Board-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html)

### [SparkFun MicroMod ATP Carrier Board](https://www.sparkfun.com/sparkfun-micromod-atp-carrier-board.html) 

[ DEV-16885 ]

If you need a \"lot\" of GPIO with a simple to program, ready to go to market module, the ATP is the fix you need.

[ [\$20.50] ]

[![SparkFun MicroMod SAMD51 Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/8/16791-SparkFun_MicroMod_SAMD51_Processor-01a.jpg)](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html)

### [SparkFun MicroMod SAMD51 Processor](https://www.sparkfun.com/sparkfun-micromod-samd51-processor.html) 

[ DEV-16791 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun MicroMod SAMD51 Processor Board is one powerful microcontroller packaged on a ...

[ [\$18.95] ]

Here are the parts if you decide to go with a single board computer. The Qwiic SHIM kit is a great starting point if you do not have a Qwiic-enabled device in mind.

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

[![SparkFun Qwiic SHIM Kit for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/9/2/5/16987-SparkFun_Qwiic_SHIM_Kit_for_Raspberry_Pi-01a.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-kit-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM Kit for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-kit-for-raspberry-pi.html) 

[ KIT-16987 ]

The SparkFun Qwiic SHIM Kit for Raspberry Pi comes with everything you need to turn your Raspberry Pi into a Qwiic enabled de...

**Retired**

### Suggested Reading

If you aren\'t familiar with the MicroMod ecosystem, we recommend reading [here for an overview](https://www.sparkfun.com/micromod). We recommend reading [here for an overview](https://www.sparkfun.com/qwiic) if you decide to take advantage of the Qwiic connector.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![MicroMod Logo](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/1/1/8/9/micromod-logo.jpg "Click to learn more about the MicroMod ecosystem!")](https://www.sparkfun.com/micromod)   [![Qwiic Connect System](https://cdn.sparkfun.com/r/457-457/assets/learn_tutorials/8/2/Qwiic-registered-black.png "Click to learn more about the Qwiic Connect System!")](https://www.sparkfun.com/qwiic)
  *[MicroMod Ecosystem](https://www.sparkfun.com/micromod)*                                                                                                                                        *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

[](https://learn.sparkfun.com/tutorials/getting-started-with-micromod)

### Getting Started with MicroMod 

Dive into the world of MicroMod - a compact interface to connect a microcontroller to various peripherals via the M.2 Connector!

## Hardware Overview

The board is a simple design that allows you to connect devices to the I^2^C bus easily with the [Qwiic Connect System](https://www.sparkfun.com/qwiic). Power and [logic levels](https://learn.sparkfun.com/tutorials/logic-levels/all) are set to 3.3V. Make sure to use a [logic level converter](https://learn.sparkfun.com/tutorials/i2c/all#i2c-at-the-hardware-level) if your board uses a voltage higher than 3.3V.

  Wire Color   Signal
  ------------ --------
  Black        GND
  Red          3.3V
  Blue         SDA
  Yellow       SCL

### Qwiic Connectors

There are 4x Qwiic connectors populated on the board.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Qwiic_Connectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Qwiic_Connectors.jpg)

### LED and Jumper

In addition to the connectors, there is an LED to indicate when power is available on the I^2^C bus. On the back, there is a jumper in case you would like to [disable the LED](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces/all).

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Power_LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Power_LED.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Jumper.jpg)
  *Front of Board*                                                                                                                                                                                                    *Back of Board*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Mounting Holes

There are 2x mounting holes included on the board.

[![Mounting Holes](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Mounting_Holes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/18012-SparkFun_Qwiic_MultiPort-Mounting_Holes.jpg)

### Board Dimensions

Below are the board dimensions. The overall size of the board is 1.00\" x 1.00\". Each connector extending from the center has a width of about 0.30\". As stated earlier, this board has 2x mounting holes located around the center.

[![Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Board_Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Board_Dimensions.png)

## Hardware Assembly

### Expanding on Boards with One Qwiic Connector

Depending on the design, there may only be enough room for one Qwiic connector. Below are a few of these [boards from the SparkFun catalog](https://www.sparkfun.com/categories/399)

[![SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/2/4/16398-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html)

### [SparkFun 20x4 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/sparkfun-20x4-serlcd-rgb-backlight-qwiic.html) 

[ LCD-16398 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 20x4 Black ...

[ [\$42.95] ]

[![SparkFun 16x2 SerLCD - RGB Text (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/2/3/16397-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-text-qwiic.html)

### [SparkFun 16x2 SerLCD - RGB Text (Qwiic)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-text-qwiic.html) 

[ LCD-16397 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 16x2 RGB on...

[ [\$32.50] ]

[![SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/2/2/16396-SparkFun_16x2_SerLCD_-_RGB_Backlight__Qwiic_-05.jpg)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-backlight-qwiic.html)

### [SparkFun 16x2 SerLCD - RGB Backlight (Qwiic)](https://www.sparkfun.com/sparkfun-16x2-serlcd-rgb-backlight-qwiic.html) 

[ LCD-16396 ]

The SparkFun Qwiic SerLCD is a serial enabled LCD that provides a simple and cost effective solution for adding a 16x2 Black ...

[ [\$32.50] ]

[![SparkFun GPS Breakout - ZOE-M8Q (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/1/4/15193-SparkFun_GPS_Breakout_-_U.FL__ZOE-M8__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gps-breakout-zoe-m8q-qwiic.html)

### [SparkFun GPS Breakout - ZOE-M8Q (Qwiic)](https://www.sparkfun.com/sparkfun-gps-breakout-zoe-m8q-qwiic.html) 

[ GPS-15193 ]

The SparkFun ZOE-M8Q GPS Breakout is a high accuracy, miniaturized, GPS board that is perfect for applications that don\'t pos...

[ [\$50.95] ]

[![SparkFun Power Delivery Board - USB-C (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/1/4/15801-SparkFun_Power_Delivery_Board_-_USB-C__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-power-delivery-board-usb-c-qwiic.html)

### [SparkFun Power Delivery Board - USB-C (Qwiic)](https://www.sparkfun.com/sparkfun-power-delivery-board-usb-c-qwiic.html) 

[ DEV-15801 ]

The SparkFun Power Delivery Board provides takes 5-20V input and produces up to 100W power, so you can use the same power ada...

[ [\$31.92] ]

[![SparkFun Qwiic Soil Moisture Sensor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/4/8/17731-SparkFun_Qwiic_Soil_Moisture_Sensor-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor.html)

### [SparkFun Qwiic Soil Moisture Sensor](https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor.html) 

[ SEN-17731 ]

A simple breakout for measuring the moisture in soil and similar materials. The exposed pads function together acting as a va...

**Retired**

If you are looking to connect more than one device with one Qwiic connector to your development board, you will just need a Qwiic MultiPort board and an additional Qwiic cable for each device.

[![Qwiic MultiPort Connecting Several I2C Devices with One Qwiic Connector on the Qwiic MicroMod Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_MicroMod_to_I2C_Devices.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_MicroMod_to_I2C_Devices.jpg)

### Alternative to a Daisy Chained Configuration

The Qwiic MultiPort can also be used as a hub so that you do not have to place the board with one Qwiic connector at the end of the daisy chain. Below is an example with the Qwiic SHIM Kit for Raspberry Pi. Instead of having the Qwiic 9DoF between the Pi and Qwiic SerLCD,

[![Raspberry Pi Connecting to the Qwiic SHIM Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Raspberry_Pi_to_I2C_Devices.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Raspberry_Pi_to_I2C_Devices.jpg)

### Mounting with Standoffs

The two boards can be [mounted with standoffs](https://www.sparkfun.com/categories/257) for a secure connection. Below is the Qwiic Micro (SAMD21), Qwiic MultiPort, Qwiic GPS (ZOE-M8Q), and a GPS antenna (W3062A) connected stacked on top of each other. They are all connected to the Qwiic SerLCD connect using Qwiic cables (with the exception of the antenna).

[![Qwiic MultiPort Mounted to the Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Hookup_Mounting_Standoffs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/5/9/Qwiic_MultiPort_Hookup_Mounting_Standoffs.jpg)