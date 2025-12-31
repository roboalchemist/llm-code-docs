# Source: https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun gator:environment Hookup Guide

# SparkFun gator:environment Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft873&name=SparkFun+gator%3Aenvironment+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft873 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Aenvironment+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft873&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft873&t=SparkFun+gator%3Aenvironment+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft873&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F3%2FCO2_Levels.PNG&description=SparkFun+gator%3Aenvironment+Hookup+Guide "Pin It")

## Introduction

Do you have an experiment involving environmental changes?

[![SparkFun gator:environment - micro:bit Accessory Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/3/9/15269-SparkFun_gator-environment_-_micro-bit_Accessory_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-gator-environment-micro-bit-accessory-board.html)

### [SparkFun gator:environment - micro:bit Accessory Board](https://www.sparkfun.com/sparkfun-gator-environment-micro-bit-accessory-board.html) 

[ SEN-15269 ]

The SparkFun gator:environment utilizes the CCS811 and BME280 ICs to take care of all of your environmental readings of atmos...

**Retired**

The [gator:environment](https://www.sparkfun.com/products/15269) is the solution for any environmental experimentation. It utilizes both the CCS811 and BME280 ICs for all of your climate and atmospheric quality readings. The CCS811 is an exceedingly popular sensor, providing readings for equivalent CO~2~ (or eCO~2~) in the parts per million (PPM) and equivalent total volatile organic compounds (or eTVOC) in the parts per billion (PPB). While, the BME280 provides a combined humidity, temperature, and barometric pressure readings. This tutorial will show you how to get started using this environmental sensor with the [gator:bit (v2)](https://www.sparkfun.com/products/15162) in the micro:bit development environment.

### Required Materials

To get started, you\'ll need a micro:bit to control everything. Each of the products below includes a micro:bit, but the kit and bundle also include some additional accessories that you may want as well.

[![micro:bit Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/4/8/13988-01.jpg)](https://www.sparkfun.com/products/14208)

### [micro:bit Board](https://www.sparkfun.com/products/14208) 

[ DEV-14208 ]

The BBC micro:bit is a pocket-sized computer that lets you get creative with digital technology.

**Retired**

[![micro:bit Go Bundle](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/1/2/14336-02.jpg)](https://www.sparkfun.com/products/14336)

### [micro:bit Go Bundle](https://www.sparkfun.com/products/14336) 

[ DEV-14336 ]

The micro:bit is a pocket-sized computer and the Go Bundle provides you with everything you need to get hooked up and powered...

**Retired**

[![SparkFun Inventor\'s Kit for micro:bit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/7/5/15228-SparkFun_Inventor_s_Kit_for_micro-bit-01.jpg)](https://www.sparkfun.com/products/15228)

### [SparkFun Inventor\'s Kit for micro:bit](https://www.sparkfun.com/products/15228) 

[ KIT-15228 ]

The SparkFun Inventor's Kit (SIK) for micro:bit is a great way to get creative, connected and coding with the micro:bit.

**Retired**

To easily use the gator board ecosystem, a gator:bit (v2) will help breakout the necessary pins and you will also need alligator and/or banana cables to connect the gator:bit to the gator:environment.

[![Alligator Test Leads - Multicolored (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/1/9/12978-01.jpg)](https://www.sparkfun.com/alligator-test-leads-multicolored-10-pack.html)

### [Alligator Test Leads - Multicolored (10 Pack)](https://www.sparkfun.com/alligator-test-leads-multicolored-10-pack.html) 

[ PRT-12978 ]

Alligator clips (or Crocodile clips, if you prefer) are likely to be the most useful thing on your workbench besides the work...

[ [\$5.25] ]

[![SparkFun gator:bit v2.0 - micro:bit Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/5/1/15162-SparkFun_Gator-bit-03a.jpg)](https://www.sparkfun.com/products/15162)

### [SparkFun gator:bit v2.0 - micro:bit Carrier Board](https://www.sparkfun.com/products/15162) 

[ DEV-15162 ]

The SparkFun gator:bit is an all-in-one "carrier" board for your micro:bit that provides you with a fully functional deve...

**Retired**

[![Banana to Banana Cable - Right Angle](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/1/3/15368-Banana_to_Banana_Cable_-_Right_Angle-01.jpg)](https://www.sparkfun.com/banana-to-banana-cable-right-angle.html)

### [Banana to Banana Cable - Right Angle](https://www.sparkfun.com/banana-to-banana-cable-right-angle.html) 

[ CAB-15368 ]

12\" long cables terminated with banana plugs, ideal for the micro:bit and gator:bit ecosystems.

**Retired**

(*\*These banana cables have a special diameter on the attachment points designed specifically for use with the micro:bit ecosystem. They may or may not be compatible with the banana cables used on your test equipment.*)

You may already have some of these materials, so feel free to modify your cart as necessary.

### Suggested Reading

The gator:environment uses two separate sensors a BME280 and CCS811. The operation of the BME280 is fairly straight forward, but the CCS811 is a slightly more complicated metal oxide sensor. You may find the following concepts and tutorials useful with the gator:environment:

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/microclimate-kit-experiment-guide)

### micro:climate Kit Experiment Guide 

A weather station kit that is built on top of the inexpensive, easy-to-use micro:bit and Microsoft MakeCode.

[](https://learn.sparkfun.com/tutorials/ccs811bme280-qwiic-environmental-combo-breakout-hookup-guide)

### CCS811/BME280 (Qwiic) Environmental Combo Breakout Hookup Guide 

Sense various environmental conditions such as temperature, humidity, barometric pressure, eCO2 and tVOCs with the CCS811 and BME280 combo breakout board.

If you aren\'t familiar with the micro:bit, we recommend reading [here for an overview](https://www.sparkfun.com/microbit).

*[micro:bit Ecosystem](https://www.sparkfun.com/microbit)*

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

[](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit)

### Getting Started with MicroPython and the SparkFun Inventor\'s Kit for micro:bit 

Learn MicroPython with the micro:bit.

[](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board)

### How to Load MicroPython on a Microcontroller Board 

This tutorial will show you how to load the MicroPython interpreter onto a variety of development boards.

[](https://learn.sparkfun.com/tutorials/sparkfun-gatorbit-v2-hookup-guide)

### SparkFun gator:bit v2 Hookup Guide 

The gator:bit v2 is a breakout board for the BBC micro:bit. The gator:bit exposes almost every pin on the micro:bit to clippable pad with circuit protection. It also has as built-in addressable LEDs and a built-in buzzer.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft873&name=SparkFun+gator%3Aenvironment+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft873 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Aenvironment+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft873&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft873&t=SparkFun+gator%3Aenvironment+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft873&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F3%2FCO2_Levels.PNG&description=SparkFun+gator%3Aenvironment+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/hardware-assembly) [Adding the MakeCode Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/adding-the-makecode-extension) [MakeCode Examples](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/makecode-examples) [Troubleshooting the Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/troubleshooting-the-extension) [Other Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/other-troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-gatorenvironment-hookup-guide/all) [Print]

- **Tags**
- - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [pxt](https://learn.sparkfun.com/tutorials/tags/pxt)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]