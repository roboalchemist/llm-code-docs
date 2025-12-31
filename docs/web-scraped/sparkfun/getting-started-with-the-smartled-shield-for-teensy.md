# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-smartled-shield-for-teensy

## Introduction

The PixelMatix [SmartLED shield for Teensy](https://www.sparkfun.com/products/15046) makes it easy to connect to RGB LED matrix panels! The shield makes it easy to connect to the 16 pins required to drive the display, connects an external 5V supply to power the display and Teensy, and brings out the Teensy's free signals to a convenient header.

[![SmartLED Shield V4 for Teensy 3](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/3/8/0/15046-SmartLED_Shield-01.jpg)](https://www.sparkfun.com/products/15046)

### [SmartLED Shield V4 for Teensy 3](https://www.sparkfun.com/products/15046) 

[ DEV-15046 ]

The SmartLED Shield V4 is the next iteration of the SmartMatrix Shield and provides you with a bridge for your Teensy to your...

**Retired**

**Note:** This tutorial was originally written for the SmartLED Shield V4 for Teensy 3. If you are using a Teensy 4, we recommend using the [SmartLED Shield V5](https://www.sparkfun.com/products/17521) or an adapter. Make sure to check out the [compatibility notes](https://learn.sparkfun.com/tutorials/getting-started-with-the-smartled-shield-for-teensy#compatibility-with-teensy-4) for more information.\
\

[Compatibility with Teensy 4](https://learn.sparkfun.com/tutorials/getting-started-with-the-smartled-shield-for-teensy#compatibility-with-teensy-4)

In this tutorial, we will explore a some of the examples provided with the SmartLED shield using different RGB LED matrix panel sizes.

[![SmartLED Demos with Different Panels](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Different_RGB_LED_Matrix_Panel_Examples_with_the_SmartLED_Shield_for_Teensy_.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Different_RGB_LED_Matrix_Panel_Examples_with_the_SmartLED_Shield_for_Teensy_.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### RGB LED Matrix Panel

You will need a panel. The following has been tested to work with the examples provided.

[![RGB LED Matrix Panel - 32x32](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/3/2/12584-RGB_LED_Panel_-_32x32-01.jpg)](https://www.sparkfun.com/rgb-led-matrix-panel-32x32.html)

### [RGB LED Matrix Panel - 32x32](https://www.sparkfun.com/rgb-led-matrix-panel-32x32.html) 

[ COM-14646 ]

These 32x32 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

[ [\$48.50] ]

[![RGB LED Matrix Panel - 32x64](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/3/6/14718-RGB_LED_Matrix_Panel_-_32x64-01.jpg)](https://www.sparkfun.com/products/14718)

### [RGB LED Matrix Panel - 32x64](https://www.sparkfun.com/products/14718) 

[ COM-14718 ]

These 32x64 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

**Retired**

[![RGB LED Matrix Panel - 64x64](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/9/2/14824-RGB_LED_Matrix_Panel_-_64x64-01.jpg)](https://www.sparkfun.com/products/14824)

### [RGB LED Matrix Panel - 64x64](https://www.sparkfun.com/products/14824) 

[ COM-14824 ]

These 64x64 RGB LED panels are an awesome place to start to add color to a project! You can create animations, games, or usef...

**Retired**

**Heads Up!** The comments in the example code indicate that he known working *width* are: "*32, 64, 96, 128*". As for the *height*, the known working sizes are: *16, 32, 48, 64*. If you [dig into the library](https://github.com/pixelmatix/SmartMatrix/blob/master/src/SmartMatrix3.h#L132), the known working scan rates are:\
\

- 1:16 with 32 rows
- 1:8 with 16 rows
- 1:32 with 64 rows

\
For example, if you are trying to use a 32x32 panel with a 1:8 scan rate, it may not display as expected.

#### Teensy

To control the panel using the SmartLED shield, you will need a [Teensy](https://www.sparkfun.com/categories/267). You can use a Teensy 4.0 but you would need to make sure that you are using the appropriate SmartLED Shield version or adapter.

[![Teensy 3.2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/9/13736-01.jpg)](https://www.sparkfun.com/products/13736)

### [Teensy 3.2](https://www.sparkfun.com/products/13736) 

[ DEV-13736 ]

The Teensy 3.2 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

[![Teensy 3.5](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/5/14055-01.jpg)](https://www.sparkfun.com/products/14055)

### [Teensy 3.5](https://www.sparkfun.com/products/14055) 

[ DEV-14055 ]

The Teensy 3.5 is larger, faster and capable of more projects, especially with its onboard micro SD card port.

**Retired**

[![Teensy 3.5 (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/6/14056-01.jpg)](https://www.sparkfun.com/products/14056)

### [Teensy 3.5 (Headers)](https://www.sparkfun.com/products/14056) 

[ DEV-14056 ]

The Teensy 3.5 is larger, faster and capable of more projects, especially with its onboard micro SD card port and pre-soldere...

**Retired**

[![Teensy 3.6](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/7/14057-01.jpg)](https://www.sparkfun.com/products/14057)

### [Teensy 3.6](https://www.sparkfun.com/products/14057) 

[ DEV-14057 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port and upg...

**Retired**

[![Teensy 3.6 (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/8/14058-01.jpg)](https://www.sparkfun.com/products/14058)

### [Teensy 3.6 (Headers)](https://www.sparkfun.com/products/14058) 

[ DEV-14058 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port, ARM Co...

**Retired**

#### Power

You will also need a 5V power supply. A 5V wall adapter and barrel jack adapter is the easiest way to connect power to the panel and Teensy. However, there are [other methods depending on how you are powering the panel](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide#powering-the-panel).

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

Click for More Power Options

[![Terminal Block - 6 Position (15A, 600V)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/9/2/13061-01.jpg)](https://www.sparkfun.com/terminal-block-6-position-15a-600v.html)

### [Terminal Block - 6 Position (15A, 600V)](https://www.sparkfun.com/terminal-block-6-position-15a-600v.html) 

[ PRT-13061 ]

This 6 position screw terminal block provides a simple way to connect wires to a single connection point.

[ [\$3.10] ]

[![Adam Tech Wall Adapter Cable - Three Terminal (NA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/5/7/14092-01.jpg)](https://www.sparkfun.com/products/14092)

### [Adam Tech Wall Adapter Cable - Three Terminal (NA)](https://www.sparkfun.com/products/14092) 

[ CAB-14092 ]

These Adam Tech Wall Adapter Cables are terminated with a standard North American (NEMA 5\--15P) plug at one end and three ins...

**Retired**

[![Adam Tech Wall Adapter Cable - Three Terminal (EU)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/5/8/14093-01.jpg)](https://www.sparkfun.com/adam-tech-wall-adapter-cable-three-terminal-eu.html)

### [Adam Tech Wall Adapter Cable - Three Terminal (EU)](https://www.sparkfun.com/adam-tech-wall-adapter-cable-three-terminal-eu.html) 

[ CAB-14093 ]

These Adam Tech Wall Adapter Cables are terminated with a standard European (CEE 7/7) plug at one end and three insulated spa...

[\$4.95] [ [\$2.95] ]

[![Mean Well Switching Power Supply - 5VDC, 20A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/9/7/0/14098-01.jpg)](https://www.sparkfun.com/products/14098)

### [Mean Well Switching Power Supply - 5VDC, 20A](https://www.sparkfun.com/products/14098) 

[ TOL-14098 ]

This is a 100W single output switching power supply from Mean Well. This power supply is extremely reliable and able to outpu...

**Retired**

[![Mean Well LED Switching Power Supply - 5VDC, 5A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/6/3/14601-Mean_Well_LED_Switching_Power_Supply_5V_25W-01.jpg)](https://www.sparkfun.com/products/14601)

### [Mean Well LED Switching Power Supply - 5VDC, 5A](https://www.sparkfun.com/products/14601) 

[ TOL-14601 ]

This is a 40W single output switching power supply from Mean Well that has been specifically designed to be with LED applicat...

**Retired**

[![iPixel Wall Adapter Cable - Two Terminal (NA)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/6/5/14603-iPixel_Wall_Adapter_Cable_-_Two_Prong__NA_-01.jpg)](https://www.sparkfun.com/products/14603)

### [iPixel Wall Adapter Cable - Two Terminal (NA)](https://www.sparkfun.com/products/14603) 

[ CAB-14603 ]

These Wall Adapter Cables from iPixel are terminated with a standard NA plug at one end and two insulated spade terminal conn...

**Retired**

[Click Here for More 5V Power Supplies!](https://www.sparkfun.com/search/results?term=5v+power)

#### Additional Components

Depending on your setup and how you are controlling the panel, you may need these additional components.

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

[![SparkFun Real Time Clock Module](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/5/4/12708-01.jpg)](https://www.sparkfun.com/sparkfun-real-time-clock-module.html)

### [SparkFun Real Time Clock Module](https://www.sparkfun.com/sparkfun-real-time-clock-module.html) 

[ BOB-12708 ]

This is the SparkFun Real Time Clock (RTC) Module, a small breakout that utilizes the DS1307 to track the current year, month...

[ [\$8.50] ]

[![Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/8/00553-03-L.jpg)](https://www.sparkfun.com/break-away-male-headers-right-angle.html)

### [Right Angle Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-male-headers-right-angle.html) 

[ PRT-00553 ]

A row of right angle male headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custo...

[ [\$2.50] ]

[![microSD USB Reader](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

[![microSD Card - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/9/4/15051-microSD_Card_-_16GB__Class_10_-01.jpg)](https://www.sparkfun.com/microsd-card-16gb-class-10.html)

### [microSD Card - 16GB (Class 10)](https://www.sparkfun.com/microsd-card-16gb-class-10.html) 

[ COM-15051 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

### Tools

Depending on your setup, you may need pliers, a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide)

### RGB Panel Hookup Guide 

Make bright, colorful displays using the 32x16, 32x32, and 32x64 RGB LED matrix panels. This hookup guide shows how to hook up these panels and control them with an Arduino.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy)

### Getting Started with the Teensy 

Basic intro to the Teensy line of products, with soldering and programming suggestions.

## Hardware Overview

### Teensy Footprint

The SmartLED shield makes it easy to connect to RGB LED matrix panels. As opposed to wiring to 16 pins on the RGB LED matrix panel, you simply sandwich the shield between a Teensy and the IDC connector! The top of the board is where you would insert the Teensy populated with straight headers. The bottom of the shield includes female headers to make a secure connection.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Teensy Footprint (Top View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Teensy-Footprint.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Teensy-Footprint.jpg)   [![Teensy Footprint (Bottom View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield_Back-Teensy-Footprint.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield_Back-Teensy-Footprint.jpg)
  *Teensy Footprint (Top View)*                                                                                                                                                                                                          *Teensy Footprint (Bottom View)*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Adjacent to the Teensy footprint are additional pins that are broken out for easy access for prototyping or soldering wires directly to the shield.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Teensy Pins Broken Out (Top View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Teensy-Breakout-Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Teensy-Breakout-Pins.jpg)   [![Teensy Pins Broken Out (Bottom View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield_Back-Teensy-Breakout-Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield_Back-Teensy-Breakout-Pins.jpg)
  *Teensy Pins Broken Out (Top View)*                                                                                                                                                                                                                  *Teensy Pins Broken Out (Bottom View)*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information about the reserved pins on the SmartLED matrix shield, check out the image below for the pins that are used to drive the RGB LED matrix panel and APA102 LEDs.

[![Reserved Teensy Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/SmartLedV4TeensyPinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLedV4TeensyPinout.png)

*[Image Courtesy](http://docs.pixelmatix.com/SmartMatrix/shield-v4.html#smartled-shield-v4-for-teensy-specs) of PJRC and PixelMatix*

**📌 Tip:** If you are prototyping with the shield, try grabbing some square header pins, jumper wires, and a breadboard to connect. Make sure that the jumper wires are **square pins** for a secure connection with the female header populated on the bottom of the SmartLED shield.\
\

[![Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/4/2/7/12693-02.jpg)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html)

### [Long Centered Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-40-pin-male-long-centered-pth-0-1.html) 

[ PRT-12693 ]

This is a row of 40 break away headers spaced 0.1\" apart with long pins on both sides. This header is especially useful when ...

[ [\$1.50] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

[![Breadboard - Mini Modular (Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/7/12044-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-red.html)

### [Breadboard - Mini Modular (Red)](https://www.sparkfun.com/breadboard-mini-modular-red.html) 

[ PRT-12044 ]

This red Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to bui...

[ [\$4.50] ]

### IDC Connector

The shield breaks out the RGB LED matrix panel\'s IDC pins. Simply align the silkscreen with the panel\'s input and stack it on like a backpack. As an alternative, you can use an IDC cable and the included 2x8 long, centered header pins. Just make sure to align the cable\'s red wire with the silkscreen labeled **RED WIRE.**

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![IDC Connector (Top View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-RGB_LED_Matrix_Panel_IDC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-RGB_LED_Matrix_Panel_IDC.jpg)   [![IDC Connector (Bottom View)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Back-RGB-LED-Matrix-Panel-IDC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Back-RGB-LED-Matrix-Panel-IDC.jpg)
  *IDC Connector (Top View)*                                                                                                                                                                                                                          *IDC Connector (Bottom View)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### APA102 LED

The shield includes additional 4-pin JST SM connector pair to [connect a strip or matrix of APA102 LEDs](http://docs.pixelmatix.com/SmartMatrix/shield-v4.html#smartled-shield-v4-for-teensy-assembly-apa102-leds) from the SmartLED Shield.

[![APA102 JST SM Connected to the SmartLED Shield](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-APA102-Addressable_LED-Strip.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-APA102-Addressable_LED-Strip.jpg)

### Removable Mounting Holes

The shield includes mounting holes by each corner of the board. They can be used to to mount the shield when using the IDC cable. They are held to the rest of the board with mouse bites. Each of the mounting holes can be removed using [pliers](https://www.sparkfun.com/products/8793). The image below shows highlights the mounting holes with red lines along the mousebites.

[![Mousebites highlighted on the SmartLED Shield](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-04_snappable_mounting_holes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-04_snappable_mounting_holes.jpg)

📌 **Tip:** If you are using a Teensy 3.5/3.6 with headers populated beyond the 1x14 pins along the side of a Teensy, you will need to snap off the mounting hole below pin 13.\
\

[![snapping off a mounting holl with pliers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Mounting-Holes-Mousebites.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-Mounting-Holes-Mousebites.jpg)

### ADDX Pins and Logic Levels

Certain panels may require **5V logic levels**, which may not be enough with the [Teensy\'s output pins](https://www.pjrc.com/teensy/techspecs.html). While you can try to wire all 16 pins from the Teensy to the IDC cable, it is not the most reliable connection. The panel may flicker or fail to display properly. The SmartLED shield was designed to include level shifting buffers to safely and reliably control the RGB LED matrix panels.

[![Level Shifting Buffers Highlighted on the SmartLED Shield for Teensy](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-04_level_shifting_buffers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/15046-SmartLED_Shield-04_level_shifting_buffers.jpg)

## Compatibility with Teensy 4

The pinout of the Teensy 4 are different from the Teensy 3. Make sure that you are using the [SmartLED Shield V5 for Teensy 4](https://www.sparkfun.com/products/17521) or the [Teensy 4 adapter with the SmartLED Shield V4](https://community.pixelmatix.com/t/teensy-4-0-released/498/32).

[![SmartLED Shield - Teensy 4](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/5/9/5/17521-SmartLED_Shield_-_Teensy_4-01A.jpg)](https://www.sparkfun.com/smartled-shield-teensy-4.html)

### [SmartLED Shield - Teensy 4](https://www.sparkfun.com/smartled-shield-teensy-4.html) 

[ DEV-17521 ]

SmartLED Shield enables the Teensy 4 to drive high-quality graphics to HUB75 RGB LED panels, with 36-bit color and 240 Hz ref...

**Retired**

Below are reserved pins that are used on the SmartLED Shield V5 for Teensy 4.

[![Reserved Pins on the SmartLED Shield for Teensy 4](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLedT4V5TeensyPinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLedT4V5TeensyPinout.png)

*[Image Courtesy](http://docs.pixelmatix.com/SmartMatrix/shield-t4.html#smartled-shield-for-teensy-4-specs) of PJRC and PixelMatix*

Make sure to uncomment the following line by removing the single line comment \"`//`\" near the top of the example code.

    language:c
    //#include <MatrixHardware_Teensy4_ShieldV5.h> // SmartLED Shield for Teensy 4 (V5)

Depending on the hardware that you are using, you may need to adjust the connection and additional lines of code.

## Hardware Assembly

**Note:** This tutorial was originally written for the SmartLED Shield V4 for Teensy 3. If you are using the SmartLED Shield V5 and Teensy 4, the methods to install headers and stacking the shield is the same.

If you have not already, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the male header pins on your Teensy before connecting. We will be using the 1x14 header pins on each side of a Teensy but you can also solder additional pins or or wires depending on your setup.

[![Soldered Headers on the Teensy 3.2](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-56.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/4/Proto_Pedal_Tutorial_Images-56.jpg)

After soldering and removing the flux from a Teensy, stack the Teensy on the SmartLED shield. Make sure to face the USB connector in the same direction as the 4-pin JST SM connector.

[![Teensy 3.2 Stacked on SmartLED Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Stack_Teensy_on_Smart_LED_Shield.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Stack_Teensy_on_Smart_LED_Shield.jpg)

Align the IDC connector breakout on the SmartLED shield with the IDC connector on your RGB LED Matrix Panel. The location of the IDC connector depends on the manufacturer of the panel but usually it will be located on the left side relative to the arrows pointing up and toward the right.

[![SmartLED Shield Sandwiched between Teensy and RGB LED Matrix](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Add_SmartLED_shield_on_RGB_LED_Matrix_Panel_IDC_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Add_SmartLED_shield_on_RGB_LED_Matrix_Panel_IDC_Connector.jpg)

**Tip:** If you received a shield with the 2x8 header pins installed and decide to add the shield to the RGB LED matrix panel\'s IDC connector as a backpack, you can remove the headers from the shield. Otherwise, you can leave the 2x8 header pins inserted and connect using the IDC cable.\
\

[![Connecting via IDC Cable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Smart_LED_Shield_IDC_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_IDC_Cable.jpg)

Once connected, the back of your RGB LED matrix panel should look similar to the images below. On the left, a Teensy 3.2 was connected to a 64x64 panel with 3mm pitched LEDs. On the right, a Teensy 3.6 was used for a 32x32 with 6mm pitched LEDs.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Teensy 3.2, SmartLED Shield, and Panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.2_Stacked_RGB_LED_Matrix_Panel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.2_Stacked_RGB_LED_Matrix_Panel.jpg)   [![Teensy 3.6, SmartLED Shield, and Panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.6_Stacked__RGB_LED_Matrix_Panel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.6_Stacked__RGB_LED_Matrix_Panel.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have not already, attach a [5V power supply](https://www.sparkfun.com/products/12889) to your RGB LED matrix panel\'s power cable. If you are using a power supply with a barrel jack, you can use a [female barrel jack adapter](https://www.sparkfun.com/products/10288) and [screwdriver](https://www.sparkfun.com/products/9146) to get a quick and dirty connection between the spade and barrel jack.

[![Spade connected to barrel jack adapter](https://cdn.sparkfun.com/r/600-600/assets/d/3/1/8/7/52a9fe68757b7f74598b4567.jpg)](https://cdn.sparkfun.com/assets/d/3/1/8/7/52a9fe68757b7f74598b4567.jpg)

The connection should look similar to the image below. Depending on your 5V power supply, your [setup might be slightly different](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide#powering-the-panel).

[![Wall adapter connected via barrel jack adapter](https://cdn.sparkfun.com/r/600-600/assets/a/a/7/a/5/52a9fe67757b7f71118b4567.jpg)](https://cdn.sparkfun.com/assets/a/a/7/a/5/52a9fe67757b7f71118b4567.jpg)

Then slide the polarized power cable for the RGB matrix panel into its respective mating connector. The red wires should be connected to the **5V** pins while the black wires connected to the **GND** pins.

[![Power Cable Connected to Panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Connect_Power_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Connect_Power_Cable.jpg)

For the scope of this tutorial, we will connect **5V USB power** directly to the Teensy\'s USB connector. This is separate from the power supply that is powering the RGB LED matrix panel. Depending on your setup, you can use the same power supply that the RGB LED matrix panel is using by connecting to either the Teensy\'s V+ and GND pins or the APA102 JST SM connector. Just make sure that the voltage is regulated at 5V.

[![Powering the Teensy via the USB Connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Smart_LED_Shield_Teensy_USB_Cable.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_Teensy_USB_Cable.jpg)

**Heads up!** When powering the Teensy via the micro-B connector, make sure to hold the connector against the PCB with your thumb and index finger while inserting the cable to avoid pulling the USB connector off. If you plan on moving the panel frequently, you may want to consider connecting power the Teensy from either the SmartLED shield\'s V+ and GND pins, or the APA102 JST SM connector.

### Alternative Connections

There is an option to daisy chain the panels together if you are within the limits of the SmartLED library. Simply connect the output from the first panel to the input of the second panel. Make sure to provide power to each panel through the 4-pin polarized connector.

[![Daisy Chained Panels and Manually Connecting to Panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Teensy_Alternative_Connection_RGB_LED_Matrix_Panel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensy_Alternative_Connection_RGB_LED_Matrix_Panel.jpg)

As explained earlier, you can try to wire all 16 pins from the Teensy to the panel\'s IDC cable. It is not the most reliable connection. There is a higher probability of wiring incorrectly or a connection becoming loose. For more information on trying the connection, check out the table below. This connection is not possible when wiring to a 64x64 panel due to the extra 5th addressing pin.

  -------------------------------------------------------------------------------------------------------
  Panel Pin Label   Cable Connector Pin \#   Teensy 3          Notes
  ----------------- ------------------------ ----------------- ------------------------------------------
  R0                1                        2                 Red Data\
                                                               *(columns 1-16)*

  G0                2                        5                 Green Data\
                                                               *(columns 1-16)*

  B0                3                        6                 Blue Data\
                                                               *(columns 1-16)*

  GND               4                        GND               Ground

  R1                5                        21                Red Data\
                                                               *(columns 17-32)*

  G1                6                        8                 Green Data\
                                                               *(columns 17-32)*

  B1                7                        20                Blue Data\
                                                               *(columns 17-32)*

  GND               8                        GND               Ground

  A                 9                        15                Demux Input A0

  B                 10                       22                Demux Input A1

  C                 11                       23                Demux Input A2

  D                 12                       9                 Demux Input E1, E3 *(32x32 panels only)*

  CLK               13                       14                LED Drivers\' Clock

  STB               14                       3, 8              LED Drivers\' Latch

  OE                15                       4                 LED Drivers\' Output Enable

  GND               16                       GND               Ground
  -------------------------------------------------------------------------------------------------------

**Heads up!** When manually wiring the board to the panel, make sure that the latch pin is connected to both pins 3 and 8 on the Teensy! Doesn\'t the SmartLED shield sound good right about now?\
\

[![Schematic Reserved Pins for Manually Connecting Teensy and Panel](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/PixelMatix_SmartLEDShieldTeensyManualWiring.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/PixelMatix_SmartLEDShieldTeensyManualWiring.jpg)

\

*Image courtesy of [PixelMatix: Manually Connecting Teensy and Panel](http://docs.pixelmatix.com/SmartMatrix/shieldref.html#smartled-shield-formerly-smartmatrix-shield-overview-technical-details-manually-connecting-teensy-and-panel)*

## Software Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Teensyduino Add-On

If you haven\'t used Teensy before, you\'ll need to download and install the extension for the Arduino IDE called Teensyduino from PJRC. This will also install the drivers for the board. Follow the instructions on installing the add-on before continuing on.

[PJRC: Teensyduino Download Page](https://www.pjrc.com/teensy/td_download.html)

### Install Library

Louis Beaudoin has written an amazing library to control the RGB LED matrix panels. You can obtain these libraries through the Arduino Library Manager. Search for **SmartMatrix** and you should be able to install the latest version. If you prefer downloading the libraries manually you can also grab them from the [GitHub repository](https://github.com/pixelmatix/SmartMatrix):

[GitHub Pixelmatix - SmartMatrix (ZIP)](https://github.com/pixelmatix/SmartMatrix/archive/master.zip)

**Note:** The library was named **SmartMatrix3** in the past. It is now named **SmartMatrix** as of release **4.0.3**.

**Compatibility:** When trying to use other examples that were written for other platforms (such as the [Serial Paint Example](https://learn.sparkfun.com/tutorials/rgb-panel-hookup-guide#example-code) for Arduino Uno or Arduino Mega), they may not be compatible with the Teensy due to the different chipset.

#### Library Overview

For an overview of the functions, check out documentation in the *MIGRATION.md* file from the GitHub repository.

[GitHubPixelmatix Docs - SmartMatrix Library Overview](https://github.com/pixelmatix/SmartMatrix/blob/master/MIGRATION.md)

## Example: Feature Demo!

There are a few examples from the SmartMatrix library for the SmartLED Shield. For the scope of the tutorial, we will be highlighting three of the examples.

### Feature Demo!

Let\'s start with the feature demo. After installing the library, click **File** \> **Examples** \> **SmartMatrix** \> **FeatureDemo.ino** in the Arduino IDE. Once open, there are a minimum of 4 lines to modify to get the example working with your matrix panel:

- uncomment one line for your MatrixHardware configuration
  - e.g. \"`#include <MatrixHardware_Teensy3_ShieldV4.h>`\" if you are using the shield V4 or \"`#include <MatrixHardware_Teensy4_ShieldV5.h>`\" if you are using shield V5
- adjust `kMatrixWidth` to the width of your panel
- adjust `kMatrixHeight` to the height of your panel
- adjust `kPanelType` based on the scan rate of your panel as noted in the [MatrixCommonHub75.h header file](https://github.com/pixelmatix/SmartMatrix/blob/master/src/MatrixCommonHub75.h#L41)

**Heads Up!** The comments in the example code indicate that the known working *width* are: "*32, 64, 96, 128*". As for the *height*, the known working sizes are: *16, 32, 48, 64*. If you [dig into the library](https://github.com/pixelmatix/SmartMatrix/blob/master/src/MatrixCommonHub75.h#L41), the known working scan rates are:\
\

- 1:8 scan with 16 rows
- 1:16 scan with 32 rows
- 1:32 scan with 64 rows

\
For example, if you are trying to use a 32x32 panel with a 1:8 scan rate, it may not display as expected.

------------------------------------------------------------------------

### 64x64 Panel with 1:32 Scan Rate

Let\'s try modifying the example code to work with the 64x64 panel with a 1:32 scan rate. The SmartLED shield is required to address the extra 5th ADDX pin on the IDC connector.

#### Parts Needed

To follow this example, you would will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.\
\

#### Modifying Code

Adjust the code by simply:

- uncommenting the line for your hardware configuration
  - in this case, we chose \"`#include <MatrixHardware_Teensy3_ShieldV4.h>`\" for the Teensy 3 by removing the \"**`//`**\"
- adjusting **kMatrixWidth** to the width of your panel by replacing **`32`** with **`64`**
- adjusting **kMatrixHeight** to the height of your panel by replacing **`32`** with **`64`**
- adjusting **kPanelType** by replacing **`SMARTMATRIX_HUB75_32ROW_MOD16SCAN`** with **`SMARTMATRIX_HUB75_64ROW_MOD32SCAN`** as noted in the [MatrixCommonHub75.h header file](https://github.com/pixelmatix/SmartMatrix/blob/master/src/MatrixCommonHub75.h#L41)

#### Upload Code

When the changes are completed, select the Teensy board definition with the associated COM port and click upload. You should see the feature demo running. This includes scrolling text, animations, shapes being drawn, brightness changing, and refresh rate changing.

[![SmartLED Shield Feature Demo Displayed on a 64x64 Panel with 1:32 Scan Rate](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/PixelMatix_SmartLED_Shield_for_Teensy_Feature_Demo_Scrolling_Text_and_Animations_64x64_RGB_LED_Matrix_Panel.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/PixelMatix_SmartLED_Shield_for_Teensy_Feature_Demo_Scrolling_Text_and_Animations_64x64_RGB_LED_Matrix_Panel.gif)

**Note:** Notice that the GIF contains scan lines as the animation is displayed on the panel? This is due to the way the animation was recorded on video. You should see a smooth transition in real time as the panel displays the animation.

------------------------------------------------------------------------

### Daisy Chained 32x64 with 1:16 Scan Rate

Let\'s try modifying the example code to work with two 32x64 panels with a 1:16 scan rate. In this example, we manually wire the connection to a Teensy 3.2.

#### Parts Needed

To follow this example, you would will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.\
\

#### Modifying Code

Modify the original code by:

- leaving the line \"`#include <MatrixHardware_Teensy3_ShieldV4.h>`\" commented out by using the \"**`//`**\"
- adjusting **kMatrixWidth** to the width of your panel by replacing **`32`** with **`128`**
- keep **kMatrixHeight** based on the height of your panel by leaving **`32`** at **`32`**
- keep **kPanelType** by leaving **`SMARTMATRIX_HUB75_32ROW_MOD16SCAN`** at **`SMARTMATRIX_HUB75_32ROW_MOD16SCAN`** as noted in the [MatrixCommonHub75.h header file](https://github.com/pixelmatix/SmartMatrix/blob/master/src/MatrixCommonHub75.h#L41)

#### Upload Code

When the changes are completed, select the Teensy board definition with the associated COM port and click upload. You should see the same demo running but for a matrix size of 32x128!

[![SmartLED Shield Feature Demo Displayed on two 32x64 Panels with 1:32 Scan Rate](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Feature_Demo_32x128.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Feature_Demo_32x128.gif)

## Example: Matrix Clock w/ the DS1307 RTC Module

In this example, we will be using the DS1307 RTC module with the SmartLED Shield, Teensy 3.2, and 32x32 panel with 1:16 scan rate. We will use the included 2x8 header and IDC cable instead of mounting the shield on the back of the matrix.

#### Parts Needed

To follow this example, you would will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.\
\

### Setting Up the DS1307 RTC Module

If you have not already, solder [right angle headers](https://www.sparkfun.com/products/553) to the RTC module.

Make sure that you installed PJRC\'s [`DS1307RTC`](https://github.com/PaulStoffregen/DS1307RTC) and [`Time`](https://github.com/PaulStoffregen/Time) libraries with the Teensyduino add-on. You can check by viewing the Arduino program folder where the files were installed under. In this case, it was in the \"**\...Arduino\\hardware\\teensy\\avr\\libraries**\" path.

[![Teensy Libraries Used](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Teensy_DS1307_RTC_Time.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensy_DS1307_RTC_Time.jpg)

*Having a hard time seeing the image? Click the image for a closer look.*

If it is not installed, you can run the Teensyduino add-on installer again to add the associated files. Under **Libraries to Install**, make sure that the checkbox is checked off for DS1307RTC and Time libraries.

[![Teensyduino Installer - Libraries to Install](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensyduino_Add-On-Installer_DS1307_RTC_Time.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensyduino_Add-On-Installer_DS1307_RTC_Time.jpg)

#### Circuit Diagram 1

Make the following connection between the DS1307 breakout board and Teensy stacked on the SmartLED shield. If you used right angle headers on the DS1307 breakout board, you can use four [M/F jumper wires](https://www.sparkfun.com/products/9140) to connect.

[![Fritzing Diagram of DS1307 RTC Module and Teensy](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensy_DS1307_RTC_Arduino_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Teensy_DS1307_RTC_Arduino_Fritzing_bb.jpg)

#### Hookup Table 1

  DS1307   Teensy
  -------- --------
  SDA      18
  SCL      19
  SQW      N/C
  GND      GND
  5V       V+

### Upload Code

In the Arduino IDE, open **File** \> **Examples** \> **DS1307RTC** \> **SetTime.ino**. The sketch will automatically set the date and time for the RTC from the compiler once you upload. You will need to run this code if the battery was removed or the time does not match your time zone. Select the Teensy board definition with the associated COM port and click upload. To check if the clock matches your computer\'s time, simply open the [Arduino serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) set at **9600** baud. You should see an output similar to the one shown below.

    DS1307 configured Time=13:00:47, Date=Nov 12 2018

**Troubleshooting:** If you are receiving an output similar to the one below, check your connections or disconnect/connect the USB cable from the Teensy before opening the serial monitor again.\
\

    DS1307 Communication Error :-

**Note:** Depending on the library version that you download, you may need to also download the GIFDecoder Library as well. IF that is the case, you will need to download and unzip the files from this repository:\
\

[GitHub PixelMatrix: GIFDecoder](https://github.com/pixelmatix/GifDecoder)

Once the folder is unzipped, make sure that the *AnimatedGIFs.ino* file and all associated files are under the same folder name called \"**\.../AnimatedGIFs**\" as shown in the image below.

[![Animated GIFs Folder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/SmartLED_Shield_AnimatedGIFs_Example-Directory.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED_Shield_AnimatedGIFs_Example-Directory.jpg)

#### Modifying Code

Open the **AnimatedGIFs.ino** example. Since the defaults **kMatrixWidth**, **kMatrixHeight**, and **kPanelType** are already set for the 32x32 panel with 1:16 scan rate, we just need to:

- uncommenting the line for your hardware configuration
  - in this case, we chose \"`#include <MatrixHardware_Teensy3_ShieldV4.h>`\" for the Teensy 3 by removing the \"**`//`**\"
- uncomment line \"`//#define SD_CS BUILTIN_SDCARD`\" by removing the \"**`//`**\"
- comment next line \"`#define SD_CS 15`\" by adding the \"**`//`**\"

#### Upload Code

Once the code has been adjusted, select correct board and COM port to upload to the Teensy 3.6.

### Adding GIFs

The next step is to add the **\.../gifs** folder into the microSD card. Remove power from the Teensy 3.6 if a microSD card was inserted in the socket. Connect to the memory card using a card adapter or [microSD USB reader](https://www.sparkfun.com/products/13004). Copy and paste the **\.../gifs** folder into the root directory of the memory card.

[![GIFs folder in memory card](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/SmartLED_Shield-gifs-folder-microSD-Card.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED_Shield-gifs-folder-microSD-Card.jpg)

Safely remove the memory card from your computer by ejecting or unmounting the microSD card. After removing the memory card from the adapter or USB reader, insert it into the built-in microSD card socket on the Teensy.

**Note:** Unlike certain microSD card sockets, the microSD card will not click in when inserted into the Teensy.

Stack the board on the panel\'s IDC connector.

[![SmartLED Shield Sandwiched between a Teensy 3.6 and 32x32 RGB Matrix Panel](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.6_Stacked__RGB_LED_Matrix_Panel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_3.6_Stacked__RGB_LED_Matrix_Panel.jpg)

If you have not already, add power to the panel. Then add power to the Teensy. The Teensy will begin displaying the GIFs that were included in the folder. Pretty neat!

[![Example GIF from AnimatedGIFs Repo Displayed on the 32x32 Panel ](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED-Shield-WiFi.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED-Shield-WiFi.gif)

### Diffusing the LEDs

The animations may be hard to view as you can see on the image on the left. To help diffuse the light, a translucent material placed in the front of the panel to blend the pixels. The image on the right used a piece of white paper to blend the individual pixels. For long term installations, try using frosted acrylic as used in the [Aurora project](https://www.instructables.com/id/SmartMatrix-Dynamic-LED-Art-Display/).

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Without Diffusion](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Animated_GIF_32x32.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Animated_GIF_32x32.gif)   [![Diffused Panel](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Animated_GIF_32x32_Diffused.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/Smart_LED_Shield_for_Teensy_Animated_GIF_32x32_Diffused.gif)
  *Without Diffusion*                                                                                                                                                                                                                          *Diffused Panel*
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Adding MOAR GIFs

Looking for more GIFs? Try checking the GIFs provided in the [Aurora project](https://github.com/pixelmatix/aurora/tree/master/sd):

[GitHub Pixel Matix: Aurora / sd](https://github.com/pixelmatix/aurora/tree/master/sd)

Simply copy any file with the **\*.gif** extension and include it in the **\.../gifs** folder as explained earlier. The [10x weather GIFs](https://github.com/pixelmatix/aurora/tree/master/sd/weather) are neat animations if you want display the current weather on a panel for your next [cloud connected IoT project](https://learn.sparkfun.com/tutorials/led-cloud-connected-cloud/)!

[![Cloud GIF from the Aurora Repo](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED-IoT-Aurora-Project-Cloud.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/1/SmartLED-IoT-Aurora-Project-Cloud.gif)

You can also do a [custom search for 32x32 GIFs on Google](https://www.google.com/search?safe=active&tbs=isz:ex%2Ciszw:32%2Ciszh:32%2Citp:animated&tbm=isch&q=GIF).

[Google Image Search: 32x32 Animated \"GIFs\"](https://www.google.com/search?safe=active&tbs=isz:ex%2Ciszw:32%2Ciszh:32%2Citp:animated&tbm=isch&q=GIF)