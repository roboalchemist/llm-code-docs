# Source: https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun gator:RTC Hookup Guide

# SparkFun gator:RTC Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft923&name=SparkFun+gator%3ARTC+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft923 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3ARTC+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft923&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft923&t=SparkFun+gator%3ARTC+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft923&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F2%2F3%2Fgatorrtc.gif&description=SparkFun+gator%3ARTC+Hookup+Guide "Pin It")

## Introduction

Most of you probably have done a science experiment that required data of some sort to be recorded. In which case, the data often had a temporal component that also needed to be recorded\...

[![SparkFun gator:RTC - micro:bit Accessory Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/0/7/6/15486-SparkFun_gator-RTC_-_micro-bit_Accessory_Board-01.jpg)](https://www.sparkfun.com/sparkfun-gator-rtc-micro-bit-accessory-board.html)

### [SparkFun gator:RTC - micro:bit Accessory Board](https://www.sparkfun.com/sparkfun-gator-rtc-micro-bit-accessory-board.html) 

[ COM-15486 ]

The gator:RTC is a supplemental data logging tool with a RV-3028 real time clock (RTC) module from Micro Crystal, using a con...

**Retired**

The [gator:RTC](https://www.sparkfun.com/products/15486) is a [real-time clock](https://en.wikipedia.org/wiki/Real-time_clock). This means that the gator:RTC can be used as a supplemental data logging tool, in conjunction with the [gator:log](https://www.sparkfun.com/products/15270) to add precise timing to your data collection. Therefore, student(s) can put down that stopwatch and start focusing more attention on what is happening in their experiments. Other applications for the gator:RTC include time lapse photography, timers and alarms, clocks, and etc.

This tutorial will show you how to get started using this gator:RTC with the [gator:bit (v2)](https://www.sparkfun.com/products/15162) in the micro:bit development environment.

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

To easily use the gator board ecosystem, a gator:bit (v2) will help breakout the necessary pins and you will also need alligator and/or banana cables to connect the gator:bit to the gator:RTC.

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

The gator:RTC sensor is pretty straight forward to use in application. However, you may find the following concepts useful along the way.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-real-time-clock-module-rv-1805-hookup-guide)

### Qwiic Real Time Clock Module (RV-1805) Hookup Guide 

Find out what time it is, even after the power\'s been out on your project for a while with the Qwiic Real Time Clock (RTC) module.

[](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide)

### SparkFun gator:log Hookup Guide 

The gator:log is a serial communication based data logger. This tutorial will get you started using the gator:log with the micro:bit platform.

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

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft923&name=SparkFun+gator%3ARTC+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft923 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3ARTC+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft923&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft923&t=SparkFun+gator%3ARTC+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft923&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F2%2F3%2Fgatorrtc.gif&description=SparkFun+gator%3ARTC+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/hardware-assembly) [Adding the MakeCode Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/adding-the-makecode-extension) [MakeCode Examples](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/makecode-examples) [Troubleshooting the Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/troubleshooting-the-extension) [Other Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/other-troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide/all) [Print]

- **Tags**
- - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [pxt](https://learn.sparkfun.com/tutorials/tags/pxt)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]