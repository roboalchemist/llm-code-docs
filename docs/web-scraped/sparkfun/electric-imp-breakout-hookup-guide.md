# Source: https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Electric Imp Breakout Hookup Guide

# Electric Imp Breakout Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom], [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft389&name=Electric+Imp+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft389 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Electric+Imp+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft389&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft389&t=Electric+Imp+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft389&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F8%2F9%2FElectric_Imp_002_Tutorial-07.jpg&description=Electric+Imp+Breakout+Hookup+Guide "Pin It")

## impRoduction

The Electric Imp is a deviously awesome development platform. Disguised as an every day SD card, the imp is actually a unique combination of microprocessor and WiFi module. The imp makes connecting any device to the Internet a breeze. Looking to catch on with this \"Internet of Things\" fad? The imp is an excellent place to start.

[![imp card and imp002](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/9/Electric_Imp_002_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/9/Electric_Imp_002_Tutorial-07.jpg)

*The Electric Imp card and imp002 Breakout Board*

In this tutorial, we\'ll be explaining how to use the [imp card](https://www.sparkfun.com/products/11395) with one of our [Breakout Boards](https://www.sparkfun.com/products/11400) as well as the [imp002 breakout board](https://www.sparkfun.com/products/12958). You will have the choice of which platform to use (the imp card or the imp002).

First, we\'ll cover how to hook up the hardware end of the imp and imp002. Following that we\'ll head over into the firmware domain, programming the imp to blink LEDs and read analog and digital inputs. The last code example shows off the coolest part of the imp: controlling hardware over the Internet!

### Required Materials

You have a choice to make! You can either use the imp card and Breakout Board, or you can use the imp002 Breakout Board.

If you want to use the imp card, you will need an [imp card](https://www.sparkfun.com/products/11395) and the [Electric Imp Breakout Board](https://www.sparkfun.com/products/12886).

[![Electric Imp](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/7/2/11395-03.jpg)](https://www.sparkfun.com/products/11395)

### [Electric Imp](https://www.sparkfun.com/products/11395) 

[ WRL-11395 ]

We know what you\'re thinking, \"What\'s the big deal? Looks like an SD card\...\" Well this is no SD card! The Electric Imp is a ...

**Retired**

[![SparkFun Electric Imp Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/7/6/12886-00.jpg)](https://www.sparkfun.com/products/12886)

### [SparkFun Electric Imp Breakout](https://www.sparkfun.com/products/12886) 

[ BOB-12886 ]

If you aren\'t familiar with the Electric Imp, it essentially provides an easy, integrated way to connect almost any hardware ...

**Retired**

If, on the other hand, you want to use the imp002, you will need the [Electric Imp imp002 Breakout Board](https://www.sparkfun.com/products/12958).

[![SparkFun Electric Imp imp002 Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/9/8/9/0/12958-01.jpg)](https://www.sparkfun.com/products/12958)

### [SparkFun Electric Imp imp002 Breakout](https://www.sparkfun.com/products/12958) 

[ BOB-12958 ]

If you aren\'t familiar with the Electric Imp, it essentially provides an easy, integrated way to connect almost any hardware ...

**Retired**

Aside from one of those platforms, we\'ll use a few common electronics parts you may already have. Here\'s a wishlist of everything else we\'ll be using.

**NOTE:** The 2-pin jumper is only required for the [Electric Imp Breakout Board](https://www.sparkfun.com/products/11395).

\

In addition to those items, you\'ll also need the following non-SparkFun materials:

- Wireless network with Internet access
- Electric Imp [planner account](https://plan.electricimp.com/) (sign up is free/easy)
- Electric Imp planner website pulled up in your web browser
- SmartPhone w/ the Electric Imp app ([Android](https://play.google.com/store/apps/details?id=com.electricimp.electricimp) or [iOS](http://itunes.apple.com/us/app/electric-imp/id547133856))

#### Tools

There will be some soldering involved. The Breakout Board does not come with header pins soldered on, which you\'ll need in order to interface with the imp\'s I/O pins. You\'ll need a [simple soldering iron](https://www.sparkfun.com/products/9507) and a bit of [solder](https://www.sparkfun.com/products/9163) (If you\'ve never soldered before, this is a great place to start! The solder points are easy, through-hole jobs).

### Before We Begin

This tutorial builds upon some basic electronics concepts. If you aren\'t familiar with any of the topics below, consider reading through that tutorial first:

- [How to Solder - Through-hole](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [How to Power a Project](https://learn.sparkfun.com/tutorials/how-to-power-a-project)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [Pulse Width Modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation)
- [Light-emitting Diodes](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

Aside from the imp\'s programming language, Squirrel, there will be a variety of coding languages used in later parts of this tutorial \-- primarily HTML and Javascript. Don\'t worry if you\'re not too familiar with those, as the examples aim to be short, sweet, and easy-to-modify.

------------------------------------------------------------------------

Let\'s start by overviewing the imp hardware itself. It\'s hard, at first, to wrap your head around the fact that this little, module is actually a powerful WiFi-enabled microcontroller platform.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft389&name=Electric+Imp+Breakout+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft389 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Electric+Imp+Breakout+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft389&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft389&t=Electric+Imp+Breakout+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft389&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F8%2F9%2FElectric_Imp_002_Tutorial-07.jpg&description=Electric+Imp+Breakout+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/all) [Next Page →\
[About the imp Card]](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/about-the-imp-card)

← Previous Page

[**Pages**] [impRoduction](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/improduction) [About the imp Card](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/about-the-imp-card) [About the Breakout](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/about-the-breakout) [About the imp002 Breakout](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/about-the-imp002-breakout) [Hardware Hookup](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/hardware-hookup) [BlinkUp](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/blinkup) [Example 0: Hello World](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/example-0-hello-world) [Example 1: I/O Control](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/example-1-io-control) [Example 2: Web Control (Request)](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/example-2-web-control-request) [Example 3: Web Response](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/example-3-web-response) [Resources and Going Further](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/resources--going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/electric-imp-breakout-hookup-guide/all) [Print]

- **Tags**
- - [Electric Imp](https://learn.sparkfun.com/tutorials/tags/electric-imp)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]