# Source: https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun gator:particle Hookup Guide

# SparkFun gator:particle Hookup Guide

[≡ Pages](#)

Contributors: [ santaimpersonator], [![](https://cdn.sparkfun.com/avatar/fde91fc929973498fdcfcfc9ccb086ab?d=retro&s=20&r=pg) Englandsaurus]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft872&name=SparkFun+gator%3Aparticle+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft872 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Aparticle+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft872&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft872&t=SparkFun+gator%3Aparticle+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft872&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F2%2FAssembly_Particle.jpg&description=SparkFun+gator%3Aparticle+Hookup+Guide "Pin It")

## Introduction

Do you have an experiment involving biometrics or particle detection?

[![SparkFun gator:particle - micro:bit Accessory Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/4/3/15271-SparkFun_gator-particle_-_micro-bit_Accessory_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-gator-particle-micro-bit-accessory-board.html)

### [SparkFun gator:particle - micro:bit Accessory Board](https://www.sparkfun.com/sparkfun-gator-particle-micro-bit-accessory-board.html) 

[ SEN-15271 ]

The SparkFun gator:particle incorporates the powerful MAX30102 sensor, enabling sensing of pulse oximetry, heart rate, monito...

**Retired**

The [gator:particle](https://www.sparkfun.com/products/15271) is an amazing tool that uses a high-sensitivity pulse oximeter and heart-rate sensor, the MAX30102. Similar to the [SparkFun Particle Sensor](https://www.sparkfun.com/products/14045), with the MAX30105 high-sensitivity optical sensor, the gator:particle can also be used for particle detection. The primary difference between these boards is that the [SparkFun Particle Sensor](https://www.sparkfun.com/products/14045) also uses a green LED that requires more power than the micro:bit can provide. This tutorial will show you how to get started using the gator:particle sensor with the [gator:bit (v2)](https://www.sparkfun.com/products/15162) in the micro:bit development environment.

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

To easily use the gator board ecosystem, a gator:bit (v2) will help breakout the necessary pins and you will also need alligator and/or banana cables to connect the gator:bit to the gator:particle.

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

The gator:particle sensor is pretty straight forward to use in application. However, you may find the following concepts useful along the way.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide)

### MAX30105 Particle and Pulse Ox Sensor Hookup Guide 

The SparkFun MAX30105 Particle Sensor is a flexible and powerful sensor enabling sensing of distance, heart rate, particle detection, even the blinking of an eye. Get ready. Set. Shine!

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

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft872&name=SparkFun+gator%3Aparticle+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft872 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+gator%3Aparticle+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft872&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft872&t=SparkFun+gator%3Aparticle+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft872&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F2%2FAssembly_Particle.jpg&description=SparkFun+gator%3Aparticle+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/hardware-assembly) [Adding the MakeCode Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/adding-the-makecode-extension) [MakeCode Example](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/makecode-example) [Troubleshooting the Extension](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/troubleshooting-the-extension) [Other Troubleshooting Tips](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/other-troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-gatorparticle-hookup-guide/all) [Print]

- **Tags**
- - [Biometrics](https://learn.sparkfun.com/tutorials/tags/biometrics)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]