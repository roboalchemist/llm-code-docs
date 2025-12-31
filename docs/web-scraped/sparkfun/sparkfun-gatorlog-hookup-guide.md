# Source: https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun gator:log Hookup Guide

# SparkFun gator:log Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft924&name=SparkFun+gator%3Alog+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft924 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Alog+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft924&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft924&t=SparkFun+gator%3Alog+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft924&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F2%2F4%2FSD_Card.gif&description=SparkFun+gator%3Alog+Hookup+Guide "Pin It")

## Introduction

**Note:** The gator:log will **[NOT]** function properly when used with the original [gator:bit](https://www.sparkfun.com/products/14484). Users should use the updated [gator:bit (v2)](https://www.sparkfun.com/products/15162) with the gator:log for it to operate properly.

Most of you probably have done a science experiment that required data of some sort to be recorded\...

[![SparkFun gator:log - micro:bit Accessory Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/4/1/15270-SparkFun_gator-log_-_micro-bit_Accessory_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-gator-log-micro-bit-accessory-board.html)

### [SparkFun gator:log - micro:bit Accessory Board](https://www.sparkfun.com/sparkfun-gator-log-micro-bit-accessory-board.html) 

[ DEV-15270 ]

The gator:log is the perfect data logging tool for your next experiment.

[\$13.95] [ [\$7.25] ]

The [gator:log](https://www.sparkfun.com/products/15270) is the perfect [data logging](https://en.wikipedia.org/wiki/Data_logger) tool for your next experiment. With the automation of the data collection process, gone are the days of rushing around with a pen and composition notebook to simultaneously record data and your observations. Now, you only need to sit back and observe your experiment (*or just wait for it to complete, if no observations are necessary*).

The gator:log allows a student(s) to focus more on the experiment than watching a thermometer or sensor readout. Additionally, the micro:bit can still be used to provide a graphical display for observing changes in data, when a sensor readout is required. If tied in conjunction with the [gator:RTC](https://www.sparkfun.com/products/15486), stop watches on time based experiments can become a thing of the past too (with the added benefit of more accurate timing results)!

This tutorial will show you how to get started using this gator:log with the [gator:bit (v2)](https://www.sparkfun.com/products/15162) in the micro:bit development environment.

### Required Materials

**Note:** The gator:log will **[NOT]** function properly when used with the original [gator:bit](https://www.sparkfun.com/products/14484). Users should use the updated [gator:bit (v2)](https://www.sparkfun.com/products/15162) with the gator:log for it to operate properly.

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

To easily use the gator board ecosystem, a gator:bit (v2) will help breakout the necessary pins and you will also need alligator and/or banana cables to connect the gator:bit to the gator:log.

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

Additionally, users will also need a µSD card and a µSD USB reader:

[![microSD Card with Adapter - 32GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/1/0/2/14832-microSD_Card_with_Adapter_-_32GB__Class_10_-02.jpg)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html)

### [microSD Card with Adapter - 32GB (Class 10)](https://www.sparkfun.com/microsd-card-with-adapter-32gb-class-10.html) 

[ COM-14832 ]

This is a class 10 32GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

[\$26.95] [ [\$14.95] ]

[![microSD Card - 1GB (Class 4)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/7/0/15107-microSD_Card_-_1GB__Class_4_-01.jpg)](https://www.sparkfun.com/microsd-card-1gb-class-4.html)

### [microSD Card - 1GB (Class 4)](https://www.sparkfun.com/microsd-card-1gb-class-4.html) 

[ COM-15107 ]

For the times when all you need is a basic SD card this is the card for you. 1GB capacity is plenty to store MP3s or log envi...

[ [\$5.50] ]

[![microSD USB Reader](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/5/8/13004-01.jpg)](https://www.sparkfun.com/microsd-usb-reader.html)

### [microSD USB Reader](https://www.sparkfun.com/microsd-usb-reader.html) 

[ COM-13004 ]

This is an awesome little microSD USB reader. Just slide your microSD card into the inside of the USB connector, then stick t...

**Retired**

[![microSD Card with Adapter - 16GB (Class 10)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/3/0/13833-02.jpg)](https://www.sparkfun.com/products/13833)

### [microSD Card with Adapter - 16GB (Class 10)](https://www.sparkfun.com/products/13833) 

[ COM-13833 ]

This is a class 10 16GB microSD memory card, perfect for housing operating systems for single board computers and a multitude...

**Retired**

You may already have some of these materials, so feel free to modify your cart as necessary.

### Suggested Reading

The gator:log is pretty straight forward to use in application. However, you may find the following concepts useful along the way.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/openlog-hookup-guide)

### OpenLog Hookup Guide 

An introduction to working with the OpenLog data logger.

[](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide)

### SparkFun gator:RTC Hookup Guide 

The gator:RTC is an I2C based, real-time clock (RTC) for keeping time while your micro:bit isn\'t powered. This tutorial will get you started using the gator:RTC with the micro:bit platform.

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

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft924&name=SparkFun+gator%3Alog+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft924 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Alog+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft924&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft924&t=SparkFun+gator%3Alog+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft924&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F9%2F2%2F4%2FSD_Card.gif&description=SparkFun+gator%3Alog+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/hardware-assembly) [Adding the MakeCode Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/adding-the-makecode-extension) [MakeCode Examples](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/makecode-examples) [Troubleshooting the Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/troubleshooting-the-extension) [Other Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/other-troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-gatorlog-hookup-guide/all) [Print]

- **Tags**
- - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [pxt](https://learn.sparkfun.com/tutorials/tags/pxt)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Storage](https://learn.sparkfun.com/tutorials/tags/storage)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]