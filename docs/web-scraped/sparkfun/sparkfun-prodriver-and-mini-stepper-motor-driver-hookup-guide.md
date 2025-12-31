# Source: https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun ProDriver and Mini Stepper Motor Driver Hookup Guide

# SparkFun ProDriver and Mini Stepper Motor Driver Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1200&name=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1200 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1200&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1200&t=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1200&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F0%2Fexample8_demo.gif&description=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Pin It")

## Introduction

The SparkFun [ProDriver](https://www.sparkfun.com/products/16836) and [Mini Stepper Motor Driver](https://www.sparkfun.com/products/25167) utilize the latest [TC78H670FTG stepper motor driver from Toshiba](https://toshiba.semicon-storage.com/us/semiconductor/product/motor-driver-ics/stepping-motor-driver-ics/detail.TC78H670FTG.html). With a full to 1/128 stepping resolution and two different methods for control (serial communication or clock-in stepping) this is a great option for your next project that requires precise motor control.

[![SparkFun ProDriver - Stepper Motor Driver (TC78H670FTG)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/5/7/16836-SparkFun_ProDriver_-_Stepper_Motor_Driver__TC78H670FTG_-01a.jpg)](https://www.sparkfun.com/sparkfun-prodriver-stepper-motor-driver-tc78h670ftg.html)

### [SparkFun ProDriver - Stepper Motor Driver (TC78H670FTG)](https://www.sparkfun.com/sparkfun-prodriver-stepper-motor-driver-tc78h670ftg.html) 

[ ROB-16836 ]

The ProDriver makes it easy to start developing with the Toshiba TC78H670FTG bipolar stepper motor driver IC.

[ [\$22.95] ]

The advantage of the ProDriver is that it\'s solderless, out of the box. With the DC barrel jack and latch pins, the board can be easily powered and connected without any soldering. This is great for projects, where users want to easily swap out components in the event of a failure.

The primary disadvantage of this product is it\'s size. Users may face difficulties trying to squeeze this into smaller projects.

[![SparkFun Mini Stepper Motor Driver - TC78H670FTG](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/6/5/6/ROB-25167-Stepper-Motor-Carrier-Feature.jpg)](https://www.sparkfun.com/sparkfun-mini-stepper-motor-driver-tc78h670ftg.html)

### [SparkFun Mini Stepper Motor Driver - TC78H670FTG](https://www.sparkfun.com/sparkfun-mini-stepper-motor-driver-tc78h670ftg.html) 

[ ROB-25167 ]

The SparkFun Mini Stepper Motor Driver makes it easy to start developing with the TC78H670FTG bipolar stepper motor driver fr...

[ [\$12.70] ]

The advantage of the Mini Stepper Motor Driver is in its size. The small footprint of the board, allows users to squeeze it into smaller projects and the pin layout is breadboard compatible to simplify prototyping.

Its primary disadvantage, is that users may need to connect an electrolytic capacitor *(**\>50µF** is recommended)*, externally to its `VM` and `GND` pins.

Although both communication methods are included in the Arduino library, the serial command has some unique features. The serial communication allows users to precisely control the phase, torque, mixed decay ratio of each coil, and current limit while the motor is in motion. (*In contrast, most stepper motor drivers need an external trimpot that is physically adjusted to control the current output limit.*)

### Required Materials

The SparkFun [ProDriver](https://www.sparkfun.com/products/16836) and [Mini Stepper Motor Driver](https://www.sparkfun.com/products/25167) require a few additional items for you to get started. At minimum, users will want an Arduino compatible microcontroller with a USB cable, a power supply, some hookup wire or jumper wires, and a stepper motor (*\*we recommend a 4-wire, bipolar stepper motor to begin with*). You may already have a few of these items, including the USB cable, so feel free to modify your cart based on your needs. Additionally, there are also [alternative part options] that are available as well (*click button below to toggle options*).

[**Alternative Parts (Toggle)**]

**Recommended Parts**

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Stepper Motor - 68 oz.in (400 steps/rev, 300mm Wire)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/3/9/7/10846-04.jpg)](https://www.sparkfun.com/stepper-motor-68-oz-in-400-steps-rev.html)

### [Stepper Motor - 68 oz.in (400 steps/rev, 300mm Wire)](https://www.sparkfun.com/stepper-motor-68-oz-in-400-steps-rev.html) 

[ ROB-10846 ]

Standard stepper motors are great, but when your project demands smoother curves, finer positioning, or reduced vibration, yo...

[ [\$29.50] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/5/TOL-15312-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html)

### [Wall Adapter Power Supply - 5VDC, 2A (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-barrel-jack.html) 

[ TOL-15312 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA Barrel Jack wall power supply manufactured specifically for S...

[ [\$9.50] ]

**ProDriver**

[![Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/9/2/11709-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html)

### [Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html) 

[ PRT-11709 ]

Jumper wires are awesome. Just a little bit of stranded core wire with a nice solid pin connector on either end. They have th...

[ [\$7.75] ]

[![SparkFun ProDriver - Stepper Motor Driver (TC78H670FTG)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/5/7/16836-SparkFun_ProDriver_-_Stepper_Motor_Driver__TC78H670FTG_-01a.jpg)](https://www.sparkfun.com/sparkfun-prodriver-stepper-motor-driver-tc78h670ftg.html)

### [SparkFun ProDriver - Stepper Motor Driver (TC78H670FTG)](https://www.sparkfun.com/sparkfun-prodriver-stepper-motor-driver-tc78h670ftg.html) 

[ ROB-16836 ]

The ProDriver makes it easy to start developing with the Toshiba TC78H670FTG bipolar stepper motor driver IC.

[ [\$22.95] ]

**Mini Stepper Motor Driver**

**Note:** For prototyping with the Mini Stepper Motor Driver on a breadboard, we have included some header options; however, it is up to the user to determine the most suitable connection for their project. It is also recommended that users connect an electrolytic capacitor *(**\>50µF** is recommended)*, externally to its `VM` and `GND` pins.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Stackable Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/8/0/09279-1.jpg)](https://www.sparkfun.com/arduino-stackable-header-8-pin.html)

### [Stackable Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/arduino-stackable-header-8-pin.html) 

[ PRT-09279 ]

This is a 8-pin female header, with extra long legs \-- great for stacking Arduino shields. Pins are spaced by 0.1\".

[ [\$0.95] ]

[![SparkFun Mini Stepper Motor Driver - TC78H670FTG](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/5/6/ROB-25167-Stepper-Motor-Carrier-Feature.jpg)](https://www.sparkfun.com/sparkfun-mini-stepper-motor-driver-tc78h670ftg.html)

### [SparkFun Mini Stepper Motor Driver - TC78H670FTG](https://www.sparkfun.com/sparkfun-mini-stepper-motor-driver-tc78h670ftg.html) 

[ ROB-25167 ]

The SparkFun Mini Stepper Motor Driver makes it easy to start developing with the TC78H670FTG bipolar stepper motor driver fr...

[ [\$12.70] ]

[![Jumper Wires Premium 6\" Mixed Pack of 100](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/3/4/JumperWire-Female-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-mixed-pack-of-100.html)

### [Jumper Wires Premium 6\" Mixed Pack of 100](https://www.sparkfun.com/jumper-wires-premium-6-mixed-pack-of-100.html) 

[ PRT-09194 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires. Multiple jumpers can be installed next to one anothe...

[ [\$33.50] ]

[![Breadboard - Mini Modular (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/6/12043-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-white.html)

### [Breadboard - Mini Modular (White)](https://www.sparkfun.com/breadboard-mini-modular-white.html) 

[ PRT-12043 ]

This white Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to b...

[ [\$5.25] ]

[![Electrolytic Decoupling Capacitors - 100uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/00096-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html)

### [Electrolytic Decoupling Capacitors - 100uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html) 

[ COM-00096 ]

Electrolytic decoupling capacitors 100uF/25V. These capacitors are great transient/surge suppressors. Attach one between the ...

[ [\$0.50] ]

**Microcontrollers**

Here are a few other Arduino compatible microcontrollers. For a full list of options from our catalog, please visit the [Arduino microcontroller product category](https://www.sparkfun.com/categories/242).

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/7/4/15484-SparkFun_Artemis_Module_-_Low_Power_Machine_Learning_BLE_Cortex-M4F-01b.jpg)](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html)

### [SparkFun Artemis Module - Low Power Machine Learning BLE Cortex-M4F](https://www.sparkfun.com/sparkfun-artemis-module-low-power-machine-learning-ble-cortex-m4f.html) 

[ WRL-15484 ]

The Artemis Module from SparkFun is the first FCC certified, open-source, Cortex-M4F with BLE 5.0 running up to 96MHz and wit...

[ [\$9.95] ]

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

[![Pro Micro - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/2/6/12640-01a.jpg)](https://www.sparkfun.com/pro-micro-5v-16mhz.html)

### [Pro Micro - 5V/16MHz](https://www.sparkfun.com/pro-micro-5v-16mhz.html) 

[ DEV-12640 ]

Here at SparkFun, we refuse to leave \'good enough\' alone. That\'s why we\'re adding to our line-up of Arduino-compatible microc...

[ [\$22.50] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

**Wiring**

Here are a few other wiring options. For a full list of options from our catalog, please visit the [wire product category](https://www.sparkfun.com/categories/141).

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Jumper Wires - Connected 6\" (M/M, 20 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/6/1/3/12795-00.jpg)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html)

### [Jumper Wires - Connected 6\" (M/M, 20 pack)](https://www.sparkfun.com/jumper-wires-connected-6-m-m-20-pack.html) 

[ PRT-12795 ]

These are 6\" long jumper wires with male connectors on both ends. Use these to jumper from any female header on any board, to...

[ [\$2.95] ]

[![Jumper Wires Premium 6\" M/M Pack of 100](https://cdn.sparkfun.com/r/140-140/assets/parts/5/9/8/2/10897-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html)

### [Jumper Wires Premium 6\" M/M Pack of 100](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html) 

[ PRT-10897 ]

These are 26 AWG jumper wires terminated as male to male. Use these to jumper from any female header on any board, to any oth...

[ [\$27.50] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/8/9/2/11709-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html)

### [Jumper Wires Premium 6\" M/M - 20 AWG (10 Pack)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-20-awg-10-pack.html) 

[ PRT-11709 ]

Jumper wires are awesome. Just a little bit of stranded core wire with a nice solid pin connector on either end. They have th...

[ [\$7.75] ]

[![Hook-up Wire - Black (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/2/08022-01.jpg)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html)

### [Hook-up Wire - Black (22 AWG)](https://www.sparkfun.com/hook-up-wire-black-22-awg.html) 

[ PRT-08022 ]

Standard 22 AWG solid Black hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$3.25] ]

[![Hook-up Wire - Red (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/3/08023-01.jpg)](https://www.sparkfun.com/hook-up-wire-red-22-awg.html)

### [Hook-up Wire - Red (22 AWG)](https://www.sparkfun.com/hook-up-wire-red-22-awg.html) 

[ PRT-08023 ]

Standard 22 AWG solid Red hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes in...

[ [\$3.25] ]

[![Hook-up Wire - Yellow (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/4/08024-01a.jpg)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html)

### [Hook-up Wire - Yellow (22 AWG)](https://www.sparkfun.com/hook-up-wire-yellow-22-awg.html) 

[ PRT-08024 ]

Standard 22 AWG solid Yellow hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes...

[ [\$3.25] ]

**Headers**

While most users may only need headers for the Mini Stepper Motor Driver, they can also be used with the ProDriver.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Stackable Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/8/0/09279-1.jpg)](https://www.sparkfun.com/arduino-stackable-header-8-pin.html)

### [Stackable Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/arduino-stackable-header-8-pin.html) 

[ PRT-09279 ]

This is a 8-pin female header, with extra long legs \-- great for stacking Arduino shields. Pins are spaced by 0.1\".

[ [\$0.95] ]

[![Stackable Header - Female (PTH, 0.1in., 10-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/2/11376-01a.jpg)](https://www.sparkfun.com/arduino-stackable-header-10-pin.html)

### [Stackable Header - Female (PTH, 0.1in., 10-Pin)](https://www.sparkfun.com/arduino-stackable-header-10-pin.html) 

[ PRT-11376 ]

This is a 10-pin female header, with extra long legs \-- great for stacking R3-compatible Arduino shields! Pins are spaced...

[ [\$0.95] ]

[![Straight Header - Female (PTH, 0.1in., 10-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/1/8/11896-01.jpg)](https://www.sparkfun.com/header-10-pin-female-pth-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 10-Pin)](https://www.sparkfun.com/header-10-pin-female-pth-0-1.html) 

[ PRT-11896 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted. This header connects perfectly with most 10-pin ...

[ [\$0.80] ]

[![Straight Header - Female (PTH, 0.1in., 8-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/8/11895-01.jpg)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html)

### [Straight Header - Female (PTH, 0.1in., 8-Pin)](https://www.sparkfun.com/header-8-pin-female-pth-0-1.html) 

[ PRT-11895 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted. This header connects perfectly with most 8-pin m...

[ [\$0.80] ]

[![Straight Header - Female (PTH, 0.1in., 2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/3/1/22892-_01.jpg)](https://www.sparkfun.com/header-2-pin-female-pth-0-1in.html)

### [Straight Header - Female (PTH, 0.1in., 2-Pin)](https://www.sparkfun.com/header-2-pin-female-pth-0-1in.html) 

[ PRT-22893 ]

These are standard 0.1\" spaced header pins that can be through-hole mounted.

[ [\$0.50] ]

**Stepper Motors**

Here are a few other stepper motor options. For a full list of options from our catalog, please visit the [stepper motor product category](https://www.sparkfun.com/categories/246).

[![Stepper Motor - 32 oz.in (200 steps/rev, 1200mm Wire)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/1/5/09238-01.jpg)](https://www.sparkfun.com/stepper-motor-with-cable.html)

### [Stepper Motor - 32 oz.in (200 steps/rev, 1200mm Wire)](https://www.sparkfun.com/stepper-motor-with-cable.html) 

[ ROB-09238 ]

If you are building a 3D printer, a CNC machine, or a precision camera slider, you need a motor that fits the standard. This ...

[ [\$26.95] ]

[![Three Phase Brushless Gimbal Stabilizer Motor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/2/6/0/ROB-20441_4_Gimbal_Motor.jpg)](https://www.sparkfun.com/three-phase-brushless-gimbal-stabilizer-motor.html)

### [Three Phase Brushless Gimbal Stabilizer Motor](https://www.sparkfun.com/three-phase-brushless-gimbal-stabilizer-motor.html) 

[ ROB-20441 ]

A 3-phase DC brushless DC motor has the unique capability of being both a high efficiency, high torque, very smooth motor, a...

[ [\$45.95] ]

[![Small Stepper Motor - 100 g.cm (48 steps/rev, 100mm Wire)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/1/6/3/10551-01.jpg)](https://www.sparkfun.com/small-stepper-motor.html)

### [Small Stepper Motor - 100 g.cm (48 steps/rev, 100mm Wire)](https://www.sparkfun.com/small-stepper-motor.html) 

[ ROB-10551 ]

When you need exact positioning and repeatability rather than just raw speed, a DC motor won\'t cut it---you need a stepper. T...

[ [\$13.95] ]

[![Gimbal Motor with Encoder - 12V, 467RPM](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/6/0/5/27478-Gimbal-Motor-with-Encoder-Feature.jpg)](https://www.sparkfun.com/gimbal-motor-with-encoder-12v-587rpm.html)

### [Gimbal Motor with Encoder - 12V, 467RPM](https://www.sparkfun.com/gimbal-motor-with-encoder-12v-587rpm.html) 

[ ROB-27478 ]

This high-performance 12V Gimbal Servo Motor is engineered for precision control in demanding applications. Its compact 40x20...

[ [\$49.95] ]

**Power Supply**

Here are a few other power supply options. For a full list of options from our catalog, please visit the [power supply](https://www.sparkfun.com/categories/307) and [wall adapter](https://www.sparkfun.com/categories/308) product categories.

[![Adjustable Voltage Wall Adapter Power Supply - 5V-15V](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/6/1/9/19898-_01.jpg)](https://www.sparkfun.com/adjustable-voltage-wall-adapter-power-supply-5v-15v.html)

### [Adjustable Voltage Wall Adapter Power Supply - 5V-15V](https://www.sparkfun.com/adjustable-voltage-wall-adapter-power-supply-5v-15v.html) 

[ TOL-19898 ]

This adjustable wall adapter features a rotary switch on the enclosure that allows you to select the voltage.

[ [\$24.95] ]

[![Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/7/TOL-15314-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html)

### [Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html) 

[ TOL-15314 ]

This is a high quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for SparkFun Elect...

[ [\$9.25] ]

[![Battery Holder - 4xAA to Barrel Jack Connector](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/9/9/09835-01a.jpg)](https://www.sparkfun.com/battery-holder-4xaa-to-barrel-jack-connector.html)

### [Battery Holder - 4xAA to Barrel Jack Connector](https://www.sparkfun.com/battery-holder-4xaa-to-barrel-jack-connector.html) 

[ PRT-09835 ]

This is a simple 4 cell AA battery holder. The 5 inch cable is terminated with a standard 5.5x2.1mm, center positive barrel j...

[ [\$2.80] ]

[![Power Supply - 5V, 4A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/8/2/15352-Power_Supply_-_5V__4A-01.jpg)](https://www.sparkfun.com/power-supply-5v-4a.html)

### [Power Supply - 5V, 4A](https://www.sparkfun.com/power-supply-5v-4a.html) 

[ TOL-15352 ]

This is a high quality power supply manufactured specifically for SparkFun Electronics packs a lot of power; 20W at 5V and 40...

[ [\$19.50] ]

[![Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/6/TOL-15313-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html)

### [Wall Adapter Power Supply - 12VDC, 600mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-12vdc-600ma-barrel-jack.html) 

[ TOL-15313 ]

This is a high quality AC to DC \'wall wart\' which produces a regulated output of 12VDC at up to 600mA.

[ [\$9.25] ]

**Power Accessories**

Users may find these accessories useful for the Mini Stepper Motor Driver.

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Electrolytic Decoupling Capacitors - 100uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/8/9/00096-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html)

### [Electrolytic Decoupling Capacitors - 100uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-100uf-25v.html) 

[ COM-00096 ]

Electrolytic decoupling capacitors 100uF/25V. These capacitors are great transient/surge suppressors. Attach one between the ...

[ [\$0.50] ]

[![Electrolytic Decoupling Capacitors - 1000uF/25V](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/0/8/08982-03-L.jpg)](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html)

### [Electrolytic Decoupling Capacitors - 1000uF/25V](https://www.sparkfun.com/electrolytic-decoupling-capacitors-1000uf-25v.html) 

[ COM-08982 ]

Electrolytic decoupling capacitors 1000uF/25V. These capacitors are great transient/surge suppressors and work well in high-v...

[ [\$0.50] ]

#### Soldering Accessories

While the ProDriver is intended to be solderless, users will need [soldering equipment](https://www.sparkfun.com/categories/49) to attach wires and/or headers to the Mini Stepper Motor Driver. Additionally, to modify the jumpers on the Prodriver, users will need a [hobby knife](https://www.sparkfun.com/categories/379).

[![PINECIL Soldering Iron Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/3/8/5/KIT-24063-PINECIL-Soldering-Iron-Kit-Feature.jpg)](https://www.sparkfun.com/pinecil-soldering-iron-kit.html)

### [PINECIL Soldering Iron Kit](https://www.sparkfun.com/pinecil-soldering-iron-kit.html) 

[ KIT-24063 ]

The PINECIL Soldering Iron Kit provides a compact powerhouse and everything you need to ignite your DIY dream.

[ [\$119.95] ]

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Chip Quik No-Clean Flux Pen - 10mL](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/7/2/5/14579-Chip_Quik_No-Clean_Flux_Pen_-_10mL-01.jpg)](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html)

### [Chip Quik No-Clean Flux Pen - 10mL](https://www.sparkfun.com/chip-quik-no-clean-flux-pen-10ml.html) 

[ TOL-14579 ]

This 10mL no-clean flux pen from Chip Quik is great for all of your solder, de-solder, rework, and reflow purposes!

[ [\$8.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/2/0/2/TOL-22265-Beginner-Tool-Kit-Feature.jpg)](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/sparkfun-beginner-tool-kit-tol-22265.html) 

[ TOL-22265 ]

This assortment of tools is great for those who need a solid set of tools to start your workbench on the right foot!

**Retired**

### Suggested Reading

We will skip over the more fundamental tutorials like [**Ohm\'s Law**](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) and [**What is Electricity?**](https://learn.sparkfun.com/tutorials/what-is-electricity). However, below are a few fundamental tutorials that may help users familiarize themselves with various aspects of this board.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1200&name=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1200 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1200&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1200&t=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1200&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F0%2Fexample8_demo.gif&description=SparkFun+ProDriver+and+Mini+Stepper+Motor+Driver+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/all) [Next Page →\
[Hardware Overview - ProDriver]](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/hardware-overview---prodriver)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/introduction) [Hardware Overview - ProDriver](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/hardware-overview---prodriver) [Hardware Overview - Mini Stepper Motor Driver](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/hardware-overview---mini-stepper-motor-driver) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/hardware-assembly) [Arduino Library Overview](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/arduino-library-overview) [Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-prodriver-and-mini-stepper-motor-driver-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Components](https://learn.sparkfun.com/tutorials/tags/components)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Mechanical](https://learn.sparkfun.com/tutorials/tags/mechanical)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]