# Source: https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun Qwiic Quad Solid State Relay Kit Hookup Guide

# SparkFun Qwiic Quad Solid State Relay Kit Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1186&name=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1186 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1186&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1186&t=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1186&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F6%2FQuad_Solid_State_Relay_Kit_Hookup_Guide-05.jpg&description=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Pin It")

## Introduction

We love our [Solid State Relay - 40A](https://www.sparkfun.com/products/13015). We love it so much we\'ve designed the [SparkFun Qwiic Quad Solid State Relay Kit](https://www.sparkfun.com/products/16833). This kit allows you to assemble up to four of these solid state relays on a single PCB and control them all via I^2^C from your favorite microcontroller. The Quad Solid State Relay Kit comes with four solid state relays rated up to **40A** at voltages between **28-380 VAC** so you can switch some serious power with this board all from a single Qwiic connector attached to an Arduino or other low-powered microcontroller.

[![SparkFun Qwiic Quad Solid State Relay Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/5/4/16833-SparkFun_Qwiic_Quad_Solid_State_Relay_Kit-12.jpg)](https://www.sparkfun.com/sparkfun-qwiic-quad-solid-state-relay-kit.html)

### [SparkFun Qwiic Quad Solid State Relay Kit](https://www.sparkfun.com/sparkfun-qwiic-quad-solid-state-relay-kit.html) 

[ KIT-16833 ]

The SparkFun Qwiic Quad Solid State Relay Kit takes one of our favorite solid state relays and lets you place up to four of t...

**Retired**

In this tutorial we\'ll cover what is included with the Quad Solid State Relay Kit along with how to assemble and finally how to connect it to an Arduino and Raspberry Pi to use the examples included in our Arduino Library and Python package.

### Required Materials

You will need a microcontroller to control the Qwiic Quad Solid State Relay in order to follow along with this tutorial. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Qwiic Pro Micro - USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/4/0/4/15795-Pro_Micro_C-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html)

### [SparkFun Qwiic Pro Micro - USB-C](https://www.sparkfun.com/sparkfun-qwiic-pro-micro-usb-c-atmega32u4.html) 

[ DEV-15795 ]

The SparkFun Qwiic Pro Micro adds a reset button, Qwiic connector, USB-C, and castellated pads to the miniaturized Arduino bo...

[ [\$23.95] ]

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

We also have a Python package available for this and our other Qwiic Relay boards so you can use a Raspberry Pi as your controller as well.

[![Raspberry Pi 4 Model B (4 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/2/15447-Raspberry_Pi_4_Model_B__4_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html)

### [Raspberry Pi 4 Model B (4 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-4-gb.html) 

[ DEV-15447 ]

The 4 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$64.95] ]

[![Raspberry Pi 4 Model B (2 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/1/15446-Raspberry_Pi_4_Model_B__2_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html)

### [Raspberry Pi 4 Model B (2 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html) 

[ DEV-15446 ]

The 2 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$69.75] ]

[![Raspberry Pi 3 B+](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/2/8/14643-Raspberry_Pi_3_B_-02.jpg)](https://www.sparkfun.com/raspberry-pi-3-b.html)

### [Raspberry Pi 3 B+](https://www.sparkfun.com/raspberry-pi-3-b.html) 

[ DEV-14643 ]

The Raspberry Pi 3 B+ is here to provide you with the same Pi as before, but now with gigabit and PoE capable Ethernet!

[ [\$43.50] ]

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

If your chosen microcontroller is not already Qwiic-enabled, you can add that functionality with one or more of the following items:

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/5/8/8/15945-SparkFun_Qwiic_pHAT_V3.0_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html)

### [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html) 

[ DEV-15945 ]

The SparkFun Qwiic pHAT V2 for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and sti...

[ [\$7.95] ]

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

You will also need at least one Qwiic cable to connect your Quad Solid State Relay Kit to your microcontroller.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Required Tools

While there is no soldering required to assemble the Qwiic Quad Solid State Relay, there is some minor assembly involved. You will need a screwdriver as well as wire strippers to assemble your kit and prepare your wires.

[![SparkFun Mini Screwdriver](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/6/3/09146-SparkFun_Mini_Screwdriver-01.jpg)](https://www.sparkfun.com/sparkfun-mini-screwdriver.html)

### [SparkFun Mini Screwdriver](https://www.sparkfun.com/sparkfun-mini-screwdriver.html) 

[ TOL-09146 ]

This is just your basic reversible screwdriver - pocket sized! Both flat and phillips heads available. Comes with pin clip an...

[ [\$1.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Self-Adjusting Wire Strippers](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/4/8/14872-Self-Adjusting_Wire_Strippers-04.jpg)](https://www.sparkfun.com/products/14872)

### [Self-Adjusting Wire Strippers](https://www.sparkfun.com/products/14872) 

[ TOL-14872 ]

The Self-Adjusting Wire Stripper can take a wire, placed in the head of the tool, compress the handles, and you will have a p...

**Retired**

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/6/6/15220_-_Wire_Strippers_-_20-30AWG.jpg)](https://www.sparkfun.com/products/15220)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/15220) 

[ TOL-15220 ]

These are higher grade wire strippers from Jonard Industries with a comfortable, curved grip making them an affordable option...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading here for an overview:

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also suggest reading through the following tutorials if you are not familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1186&name=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1186 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1186&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1186&t=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1186&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F6%2FQuad_Solid_State_Relay_Kit_Hookup_Guide-05.jpg&description=SparkFun+Qwiic+Quad+Solid+State+Relay+Kit+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/hardware-assembly) [Qwiic Relay Arduino Library](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/qwiic-relay-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/arduino-examples) [Qwiic Relay Python Package](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/qwiic-relay-python-package) [Python Examples](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/python-examples) [Register Map](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/register-map) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-quad-solid-state-relay-kit-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ATtiny](https://learn.sparkfun.com/tutorials/tags/attiny)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]