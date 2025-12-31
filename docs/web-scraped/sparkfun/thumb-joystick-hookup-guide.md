# Source: https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Thumb Joystick Hookup Guide

# Thumb Joystick Hookup Guide

[≡ Pages](#)

Contributors: [ followr], [![](https://cdn.sparkfun.com/avatar/415020da97cb779a33dc31e522712a57?d=retro&s=20&r=pg) MikeGrusin], [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft870&name=Thumb+Joystick+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft870 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Thumb+Joystick+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft870&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft870&t=Thumb+Joystick+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft870&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F0%2F09032-03-L_Thumb_Joystick.jpg&description=Thumb+Joystick+Hookup+Guide "Pin It")

## Introduction

**Heads up!** This tutorial is for the thumb joystick breakout board and shield. For those that want to quickly connect to the thumb joystick without needing to solder, check out the [Qwiic Joystick \[COM-15168\]](https://www.sparkfun.com/products/15168) to connect via I^2^C.

Whether you\'re blasting aliens, driving a robot, or write your awesome classic Arcade Game for your Arduino, you\'ll find the [analog thumb joystick](https://www.sparkfun.com/products/9032) a very useful addition to your projects. This tutorial will go over the analog [thumb joystick breakout board](https://www.sparkfun.com/products/9110) with some Arduino examples.

[![SparkFun Thumb Joystick Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/0/3/10467-LED_Tactile_Button_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-thumb-joystick-breakout.html)

### [SparkFun Thumb Joystick Breakout](https://www.sparkfun.com/sparkfun-thumb-joystick-breakout.html) 

[ BOB-09110 ]

If you are picking up a \[Thumb Joystick\](https://www.sparkfun.com/thumb-joystick.html), you are going to want this breakout b...

[ [\$2.75] ]

[![Thumb Joystick](https://cdn.sparkfun.com/r/600-600/assets/parts/2/4/2/7/09032-03-L.jpg)](https://www.sparkfun.com/thumb-joystick.html)

### [Thumb Joystick](https://www.sparkfun.com/thumb-joystick.html) 

[ COM-09032 ]

Add arcade-style control to your project with this analog thumb joystick. If you have ever used a PlayStation 2 controller, y...

[ [\$5.25] ]

Later, we\'ll also go over the [thumb joystick shield](https://www.sparkfun.com/products/9760) for Arduino and Processing examples. You can follow along with the examples using the breakout board if you have some additional hardware!

[![SparkFun Joystick Shield Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/3/7/3/1/09760-01.jpg)](https://www.sparkfun.com/products/9760)

### [SparkFun Joystick Shield Kit](https://www.sparkfun.com/products/9760) 

[ DEV-09760 ]

The SparkFun Joystick Shield Kit contains all the parts you need to enable your Arduino with a joystick! The shield sits on t...

**Retired**

### Suggested Viewing

For a simple demo of the thumb joystick, check out the video below!

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary. If you decide to use the breakout board, you\'ll need the parts from this wish list.

If you decide to use the shield, you\'ll need the parts from this wish list.

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Needle Nose Pliers](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/3/08793-03-L.jpg)](https://www.sparkfun.com/needle-nose-pliers.html)

### [Needle Nose Pliers](https://www.sparkfun.com/needle-nose-pliers.html) 

[ TOL-08793 ]

Mini Pliers. These are great little pliers! A must have for any hobbyist or electrical engineer. Crucial for inserting device...

[ [\$3.60] ]

[![Third Hand](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/5/8/09317-01.jpg)](https://www.sparkfun.com/third-hand.html)

### [Third Hand](https://www.sparkfun.com/third-hand.html) 

[ TOL-09317 ]

This is a solderer\'s best helper, the third hand. Comes with a heavy base, two alligator clips, a soldering iron holder, and ...

[ [\$15.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Panavise Jr. - Vacuum Base](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/8/1/10410-01.jpg)](https://www.sparkfun.com/products/10410)

### [Panavise Jr. - Vacuum Base](https://www.sparkfun.com/products/10410) 

[ TOL-10410 ]

The Panavise Jr. is a great vise with a vacuum base. Its jaws open up to about 3\" and have grooves for PCBs. It\'s perfect for...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing)

### Connecting Arduino to Processing 

Send serial data from Arduino to Processing and back - even at the same time!

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft870&name=Thumb+Joystick+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft870 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Thumb+Joystick+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft870&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft870&t=Thumb+Joystick+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft870&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F7%2F0%2F09032-03-L_Thumb_Joystick.jpg&description=Thumb+Joystick+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/all) [Next Page →\
[How Does an Analog Thumb Joystick Work?]](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/how-does-an-analog-thumb-joystick-work)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/introduction) [How Does an Analog Thumb Joystick Work?](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/how-does-an-analog-thumb-joystick-work) [Hardware Overview: Breakout](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/hardware-overview-breakout) [Hardware Assembly: Breakout](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/hardware-assembly-breakout) [Arduino Examples: Breakout](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/arduino-examples-breakout) [Hardware Overview: Shield](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/hardware-overview-shield) [Hardware Assembly: Shield](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/hardware-assembly-shield) [Arduino Examples: Shield](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/arduino-examples-shield) [Processing Library](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/processing-library-) [Processing Examples: Shield](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/processing-examples-shield) [Resources and Going Further](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Game](https://learn.sparkfun.com/tutorials/tags/game)
  - [Gaming](https://learn.sparkfun.com/tutorials/tags/gaming)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Input Devices](https://learn.sparkfun.com/tutorials/tags/input-devices)
  - [Javascript](https://learn.sparkfun.com/tutorials/tags/javascript)
  - [Johnny-Five](https://learn.sparkfun.com/tutorials/tags/johnny-five)
  - [Node.js](https://learn.sparkfun.com/tutorials/tags/node-js)
  - [Processing](https://learn.sparkfun.com/tutorials/tags/processing)
  - [Shields](https://learn.sparkfun.com/tutorials/tags/shields)
  - [Soldering](https://learn.sparkfun.com/tutorials/tags/soldering)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]