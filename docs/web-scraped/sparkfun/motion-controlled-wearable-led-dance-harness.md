# Source: https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Motion Controlled Wearable LED Dance Harness

# Motion Controlled Wearable LED Dance Harness

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft730&name=Motion+Controlled+Wearable+LED+Dance+Harness "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft730 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Motion+Controlled+Wearable+LED+Dance+Harness&url=http%3A%2F%2Fsfe.io%2Ft730&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft730&t=Motion+Controlled+Wearable+LED+Dance+Harness "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft730&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F3%2F0%2FBboy_Motion_Controlled_LED_Dance_Upside_Down_Headstand.gif&description=Motion+Controlled+Wearable+LED+Dance+Harness "Pin It")

## Introduction

[Continuing on from the last time](https://learn.sparkfun.com/tutorials/prototype-wearable-led-dance-harness), we are going to add an accelerometer to detect basic movements and control a 12V non-addressable LED strip for *Mark III*! Make your LEDs breathe by fading in and out when laying on the floor. Turn off the LEDs when moving to your side. Or make the LEDs blink in a headstand!

[![Motion Controlled Wearable LED Dance Harness in Action](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/0/Bboy_Motion_Controlled_LED_Dance_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/0/Bboy_Motion_Controlled_LED_Dance_Demo.gif)

*Mark III: Motion Controlled Wearable LED Dance Harness in Action*

### Required Materials

To follow along with this tutorial, you will need the following materials listed below to build **one** motion controller. This is assuming that you have [already soldered wires to LED strips and a harness from the first tutorial](https://learn.sparkfun.com/tutorials/prototype-wearable-led-dance-harness#introduction). You may not need everything, depending on what you have. Add it to your cart, read through the guides, and adjust the cart as necessary.

### Tools

You will need a soldering iron, solder, [general soldering accessories](https://www.sparkfun.com/categories/49), and tools to work with wire.

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Diagonal Cutters](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/3/4/08794-03-L.jpg)](https://www.sparkfun.com/diagonal-cutters.html)

### [Diagonal Cutters](https://www.sparkfun.com/diagonal-cutters.html) 

[ TOL-08794 ]

Mini Diagonal Cutters. These are great little cutters! A must have for clipping leads and extra solder tails. 4\" long.

[ [\$3.75] ]

[![Wire Strippers - 30AWG Hakko](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/1/2/12630-Hakko-Wire-Strippers-30AWG-Feature.jpg)](https://www.sparkfun.com/wire-strippers-30awg-hakko.html)

### [Wire Strippers - 30AWG Hakko](https://www.sparkfun.com/wire-strippers-30awg-hakko.html) 

[ TOL-12630 ]

It can be used as: Shears, Multi-diameter Wire stripper, pliers.

[ [\$13.95] ]

[![Weller WE1010 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/6/1/14734-Weller_WE1010_Soldering_Station_-01.jpg)](https://www.sparkfun.com/products/14734)

### [Weller WE1010 Soldering Station](https://www.sparkfun.com/products/14734) 

[ TOL-14734 ]

The WE1010 from Weller is a powerful 70 watt soldering station that is perfect for passionate hobbyists, DIYers, and anyone w...

**Retired**

You will also need:

- Scissors
- Electrical Tape
- Hot glue gun
- String

### Suggested Reading

If you do not have a harness or LED strips prepared, make sure you start with [this tutorial before continuing](https://learn.sparkfun.com/tutorials/prototype-wearable-led-dance-harness). This tutorial builds on the project that was used in the previous tutorial.

[](https://learn.sparkfun.com/tutorials/prototype-wearable-led-dance-harness)

### Prototype Wearable LED Dance Harness 

February 8, 2018

A project tutorial to add an extra effect for dancers performing a choreographed piece. The harness can be added quickly under a costume.

If you aren't familiar with the following concepts, we also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

[](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)

### Using the Arduino Pro Mini 3.3V 

This tutorial is your guide to all things Arduino Pro Mini. It explains what it is, what it\'s not, and how to get started using it.

[](https://learn.sparkfun.com/tutorials/transistors)

### Transistors 

A crash course in bi-polar junction transistors. Learn how transistors work and in which circuits we use them.

[](https://learn.sparkfun.com/tutorials/planning-a-wearable-electronics-project)

### Planning a Wearable Electronics Project 

Tips and tricks for brainstorming and creating a wearables project.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft730&name=Motion+Controlled+Wearable+LED+Dance+Harness "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft730 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Motion+Controlled+Wearable+LED+Dance+Harness&url=http%3A%2F%2Fsfe.io%2Ft730&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft730&t=Motion+Controlled+Wearable+LED+Dance+Harness "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft730&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F3%2F0%2FBboy_Motion_Controlled_LED_Dance_Upside_Down_Headstand.gif&description=Motion+Controlled+Wearable+LED+Dance+Harness "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/all) [Next Page →\
[Understanding Your Circuit]](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/understanding-your-circuit)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/introduction) [Understanding Your Circuit](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/understanding-your-circuit) [Hardware Hookup](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/hardware-hookup) [Securing the Controller](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/securing-the-controller) [Example Code](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/example-code) [Calibrating the Accelerometer](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/calibrating-the-accelerometer) [Solder, Rinse, Secure, Test, Code, Repeat\...](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/solder-rinse-secure-test-code-repeat-) [Stress Testing in the Field](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/stress-testing-in-the-field) [Making It Better](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/making-it-better) [Resources & Going Further](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/resources--going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/discuss) [Single Page](https://learn.sparkfun.com/tutorials/motion-controlled-wearable-led-dance-harness/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [E-Textiles](https://learn.sparkfun.com/tutorials/tags/e-textiles)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Soldering](https://learn.sparkfun.com/tutorials/tags/soldering)
  - [Wearables](https://learn.sparkfun.com/tutorials/tags/wearables)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]