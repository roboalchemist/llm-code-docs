# Source: https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Wireless RC Robot with Arduino and XBees

# Wireless RC Robot with Arduino and XBees

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft868&name=Wireless+RC+Robot+with+Arduino+and+XBees "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft868 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+RC+Robot+with+Arduino+and+XBees&url=http%3A%2F%2Fsfe.io%2Ft868&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft868&t=Wireless+RC+Robot+with+Arduino+and+XBees "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft868&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F8%2F6%2F8%2FWireless_RC_RedBot_Arduino_XBee_Joystick_Controller_Broadcast_Demo__3.gif&description=Wireless+RC+Robot+with+Arduino+and+XBees "Pin It")

## Introduction

In this tutorial, we will expand on the SIK for RedBot to control a robot wirelessly with XBee radios! We\'ll explore a different microcontroller and wirelessly control the RedBot at a distance. Beware, we\'ll need to solder the wireless controller together.

[![Wireless Joystick Controlling 3 Robots Simultaneously](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/8/Wireless_RC_RedBot_Arduino_XBee_Joystick_Controller_Broadcast_Demo__3.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/8/Wireless_RC_RedBot_Arduino_XBee_Joystick_Controller_Broadcast_Demo__3.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Heads up!** This tutorial uses the RedBot mainboard programmed with Arduino and shadow chassis. Depending on your setup, you can choose [different motor drivers](https://www.sparkfun.com/categories/178) for your motor and [chassis](https://www.sparkfun.com/categories/181).\
\

[![Wild Thumper 6WD Chassis - Black (34:1 gear ratio)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/2/7/11056-01.jpg)](https://www.sparkfun.com/products/11056)

### [Wild Thumper 6WD Chassis - Black (34:1 gear ratio)](https://www.sparkfun.com/products/11056) 

[ ROB-11056 ]

This is easily the most rugged and beefy robot chassis in its price range. The Wild Thumper 6-Wheel platform is the best of b...

**Retired**

[![Multi-Chassis - Tank Version](https://cdn.sparkfun.com/r/140-140/assets/parts/8/7/2/3/Chasis-Angle.jpg)](https://www.sparkfun.com/products/12091)

### [Multi-Chassis - Tank Version](https://www.sparkfun.com/products/12091) 

[ ROB-12091 ]

This is the Multi-Chassis Tank Kit, an easy to assemble and use robot chassis platform. The Multi-Chassis kit provides you wi...

**Retired**

[![Actobotics Kit - ActoBitty 2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/6/5/Actobotics_Kit-03.jpg)](https://www.sparkfun.com/products/13047)

### [Actobotics Kit - ActoBitty 2](https://www.sparkfun.com/products/13047) 

[ ROB-13047 ]

This is the ActoBitty 2 from \[Actobotics\](https://www.sparkfun.com/pages/Actobotics), an easy to assemble starter robotics ki...

**Retired**

[![Circular Robotics Chassis Kit (Three-Layer)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/1/5/14339-01a.jpg)](https://www.sparkfun.com/products/14339)

### [Circular Robotics Chassis Kit (Three-Layer)](https://www.sparkfun.com/products/14339) 

[ ROB-14339 ]

The three-layer Circular Robotics Chassis Kit is a sturdy, miniature robotics kit designed for beginners and experienced robo...

**Retired**

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49). If you have not soldered before, we suggest looking at the [tool kits](https://www.sparkfun.com/categories/375). You will also need a wire stripper and some wire depending on the XBees that you are using.

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Hook-up Wire - White (22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/4/6/08026-01.jpg)](https://www.sparkfun.com/hook-up-wire-white-22-awg.html)

### [Hook-up Wire - White (22 AWG)](https://www.sparkfun.com/hook-up-wire-white-22-awg.html) 

[ PRT-08026 ]

Standard 22 AWG solid White hook up wire. Use this with your bread board or any project in which you need sturdy wire. Comes ...

[ [\$2.95] ]

[![Wire Strippers - 20-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/1/14763-Wire_Strippers_-_758PL0066-03.jpg)](https://www.sparkfun.com/products/14763)

### [Wire Strippers - 20-30AWG](https://www.sparkfun.com/products/14763) 

[ TOL-14763 ]

These are high grade wire strippers from Techni-Tool with a curved grip making them an affordable option if you need to remov...

**Retired**

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis)

### Assembly Guide for RedBot with Shadow Chassis 

Assembly Guide for the RedBot Kit. This tutorial includes extra parts to follow to go along with the RedBot Inventor\'s Kit tutorial.

[](https://learn.sparkfun.com/tutorials/exploring-xbees-and-xctu)

### Exploring XBees and XCTU 

How to set up an XBee using your computer, the X-CTU software, and an XBee Explorer interface board.

[](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis)

### Experiment Guide for RedBot with Shadow Chassis 

This Experiment Guide offers nine experiments to get you started with the SparkFun RedBot. This guide is designed for those who are familiar with our SparkFun Inventor\'s Kit and want to take their robotics knowledge to the next level.

[](https://learn.sparkfun.com/tutorials/wireless-joystick-hookup-guide)

### Wireless Joystick Hookup Guide 

A hookup guide for the SparkFun Wireless Joystick Kit.

------------------------------------------------------------------------

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft868&name=Wireless+RC+Robot+with+Arduino+and+XBees "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft868 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+RC+Robot+with+Arduino+and+XBees&url=http%3A%2F%2Fsfe.io%2Ft868&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft868&t=Wireless+RC+Robot+with+Arduino+and+XBees "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft868&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F8%2F6%2F8%2FWireless_RC_RedBot_Arduino_XBee_Joystick_Controller_Broadcast_Demo__3.gif&description=Wireless+RC+Robot+with+Arduino+and+XBees "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/all) [Next Page →\
[Hardware Hookup]](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/hardware-hookup)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/introduction) [Hardware Hookup](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/hardware-hookup) [Configuring XBees](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/configuring-xbees) [Setting Up Drivers and Arduino](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/setting-up-drivers-and-arduino) [Experiment 1: Sending and Receiving a Signal](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-1-sending-and-receiving-a-signal) [Experiment 2: Wirelessly Driving Forward](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-2-wirelessly-driving-forward) [Experiment 3: Wirelessly Controlling a Robot](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-3-wirelessly-controlling-a-robot) [Experiment 4: Wirelessly Triggering Audio](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/experiment-4-wirelessly-triggering-audio) [Coding Challenges](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/coding-challenges) [Troubleshooting](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/resources-and-going-further)

[Comments [5]](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/discuss) [Single Page](https://learn.sparkfun.com/tutorials/wireless-rc-robot-with-arduino-and-xbees/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)
  - [XBee](https://learn.sparkfun.com/tutorials/tags/xbee)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]