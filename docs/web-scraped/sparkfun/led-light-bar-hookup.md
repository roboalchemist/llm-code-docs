# Source: https://learn.sparkfun.com/tutorials/led-light-bar-hookup

## Introduction

LED Light Bars are a super-easy way to add some extra-*bright* and colorful illumination to your project. Each Light Bar is essentially a set of three super-bright 5050-size LEDs. They\'re offered in a variety of colors including [white](https://www.sparkfun.com/products/12014), [red](https://www.sparkfun.com/products/12015), [blue](https://www.sparkfun.com/products/678), and [green](https://www.sparkfun.com/products/679) (note: the blue and green light bars are an older version, they look different but can still be connected the same way).

[![LED Light Bars lit up](https://cdn.sparkfun.com/r/600-600/assets/2/7/4/d/9/524476b7757b7fd53d8b4567.png)](https://cdn.sparkfun.com/assets/2/7/4/d/9/524476b7757b7fd53d8b4567.png)

While these bars are very simple devices, they do have a few quirks when it comes to using them. Like the fact that their nominal operating voltage is 12V. In this tutorial we\'ll go over some of the important specifications of these LED Light Bars. Then we\'ll dive into some example circuits that can help you get the most of these nifty little LED assemblies.

### Suggested Reading

Here are some concepts and tutorials you should be familiar with before diving into this tutorial:

- [Light Emitting Diodes (LEDs)](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds) \-- This tutorial will help familiarize you with the LED lexicon.
- [Polarity](https://learn.sparkfun.com/tutorials/polarity) \-- These LED Light Bars *are* polarized. Don\'t mix up the + and -!
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire) \-- It\'ll be good to know how to strip, tin, and splice wire.
- [Pulse Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) \-- PWM is a popular method to dim LEDs with a digital signal.
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) \-- One of our examples will an Arduino, a beginner-friendly programmable microcontroller, to help dim the Light Bars.

## Hardware Overview

A glance at the LED Bars will reveal that there\'s not a whole lot required to interface with them. There are two pairs of wire pigtails coming off the sides, labeled \'+\' and \'-\'. The darker-gray wire connects to the \'+\' pin, and the white wire connects to \'-\' on both sides.

[![LED Bar with quarter for size comparison](https://cdn.sparkfun.com/assets/5/9/4/1/1/52430b2d757b7f65438b4569.png)](https://cdn.sparkfun.com/assets/5/9/4/1/1/52430b2d757b7f65438b4569.png)

These wires supply power directly to the LEDs. A **nominal voltage of 12V** should be applied to these wires. A lower voltage will work (to a point) but result in dimmer LEDs. Either of the wire pairs can be used to supply power to the LED, and the unused pair can either be trimmed or connected to **another LED bar**.

The bars themselves measure about 3 inches across and half an inch wide. Each has three super bright SMD LEDs, which are spaced by about 1.07\".

For mounting purposes there are drill holes on either side of the board, and a peel-away sticky foam on the backside.

### LED Characteristics

The \"nominal\" voltage for these LED Bars is **12V**. \"Nominal\" as in that\'s what\'s recommended by the manufacturer. They will work at lower voltages, although that\'ll mean sacrificing some brightness.

The table below shows some of the characteristics for each of the LED bar colors. These are values we found while testing the bars out. The minimum voltage was the lowest voltage where the LEDs were at recognizably lit up, although very dim. We recommend that you at least give the LEDs around 7V. The higher the voltage, the brighter your LED will be.

  Color   Minimum voltage   Current @ 7V   Current @ 9V   Current @ 12V
  ------- ----------------- -------------- -------------- ---------------
  White   4.84 V            8.35 mA        25.8 mA        55.2 mA
  Red     2.8 V             13 mA          29.8 mA        54.0 mA

\

As far as current pull goes, both LED colors consume about the same when powered from between 9 and 12V, up to about 55mA when powered at the nominal voltage.

#### Reverse Engineering the Light Bar Circuit

Looking at the visible components on the bars, it\'s apparent that there\'s not a lot to them. Three six-pin, SMD LEDs, and an equal number of resistors. We can easily reverse-engineer this circuit to find out exactly how these things work.

Each SMD LED is actually a collection of three equal LEDs. The LED bar\'s PCB is set up to string those LEDs in series, with the resistor in-line to limit current. The values of the resistors depend on the color of the Bar. The red bar, for example uses 330Ω and the white bar uses 150Ω resistors.

[![LED bar schematic](https://cdn.sparkfun.com/assets/9/6/e/7/0/52430b2d757b7f0a438b456d.png)](https://cdn.sparkfun.com/assets/9/6/e/7/0/52430b2d757b7f0a438b456d.png)

Connect three of those circuits in parallel an you have your LED bar!

## Assembly Tips

In most cases, Light Bar assembly begins with [stripping some wire](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire). The wire pigtails on the bars are 20 AWG, and should be easy enough to strip with any, old [wire stripper](https://www.sparkfun.com/products/8696).

The wire lengths can be extended, if need be, with a little splice. Don\'t forget to cover your splice with [heatshrink](https://www.sparkfun.com/products/9353)!

Alternatively the stripped pigtails can be tinned, crimped, or plugged directly into a mating connector.

### Stringing Bars

The \'+\' and \'-\' wires of one bar can be connected to another to string them together. More and more bars can be stringed until you start to approach the current limit of the 20 AWG wires \-- about 1.5A. With some back of the napkin calculations \-- 55mA per bar, 1.5A max \-- that\'d be 25-ish bars.

[![Bars strung together](https://cdn.sparkfun.com/r/600-600/assets/0/b/6/b/2/524476f5757b7f0f3b8b456c.png)](https://cdn.sparkfun.com/assets/0/b/6/b/2/524476f5757b7f0f3b8b456c.png)

### Mounting the Bars

There are two possible methods for mounting the LED bars. There are mounting holes on either end of the bar with a 0.15\" drill diameter, allowing for the bars to be screwed down. Every bar also includes a peel-away sticky-foam backing which adheres about as well as you could expect.

With a little prying, the PCB assembly part of the LED bar can be removed from the plastic mounting backing. This might be useful if your boards might need a tighter fit.

[![Backing removed from bar](https://cdn.sparkfun.com/r/600-600/assets/f/a/5/3/c/52447722757b7f983e8b456a.png)](https://cdn.sparkfun.com/assets/f/a/5/3/c/52447722757b7f983e8b456a.png)

## Example Circuits

There are a variety of ways these LED bars can be controlled and illuminated. Let\'s look at a few example circuits:

### Direct Power

If you don\'t care about dimming the LEDs, the easiest way to power them up is to connect them directly to a 12V power supply. Stick them in your enclosure or project, plug the supply in, and forget about them. If you\'re looking for a supply that can source 12V, either a [wall wart](https://www.sparkfun.com/products/9442) or a more [general power supply](https://www.sparkfun.com/products/11296) should be able to do the job.

[![Bars directly powered](https://cdn.sparkfun.com/r/600-600/assets/c/6/b/5/9/52447759757b7f553d8b4567.png)](https://cdn.sparkfun.com/assets/c/6/b/5/9/52447759757b7f553d8b4567.png)

*The [DC Barrel Jack Screw Terminal Adapter](https://www.sparkfun.com/products/10288) makes connecting the 12V wall wart to the LED bar way easy.*

To gain a little control over the LEDs, you can add a [switch](https://learn.sparkfun.com/tutorials/button-and-switch-basics) in-line between the power source and either the \'+\' or \'-\' wire of the first LED bar. Just make sure you pick a switch that can handle the high amounts of current that may run through it.

### Dimming with MOSFETs

If you want to add some dimming control over your LED bar, [MOSFETs](https://www.sparkfun.com/products/10213) combined with [pulse width modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation) are the tools you\'ll need. There are a few approaches you can take to generating a PWM signal to control the MOSFET and LED bar. Here are a couple options:

#### Using an Arduino

If you\'ve got an [Arduino](https://www.sparkfun.com/products/11575) lying around (and what budding electrical engineer doesn\'t these days?), that may prove to be the easiest way to control the LED bars via PWM. Use a circuit like below, with an [n-channel MOSFET](https://www.sparkfun.com/products/10256) and the Arduino powered through the barrel jack connector by a [12V wall wart](https://www.sparkfun.com/products/9442):

[![Arduino MOSFET circuit](https://cdn.sparkfun.com/r/600-600/assets/a/f/5/0/9/52433cdc757b7f6c7a8b456a.png)](https://cdn.sparkfun.com/assets/a/f/5/0/9/52433cdc757b7f6c7a8b456a.png)

Make sure the positive LED wire (the gray one) is connected to \'VIN\' of the Arduino, which should be 12V (but could be 9V too). Our [MOSFET Power Control Kit](https://www.sparkfun.com/products/10256) works perfectly for a circuit like this:

[![Arduino control image](https://cdn.sparkfun.com/r/600-600/assets/1/7/e/2/3/524477d3757b7f182a8b4567.png)](https://cdn.sparkfun.com/assets/1/7/e/2/3/524477d3757b7f182a8b4567.png)

Where the pin connected to the MOSFET gate could be any PWM-capable Arduino pin (3, 5, 6, 9, 10, or 11 on most \'duinos). Then just write a simple sketch which `analogWrite()`\'s that pin to the desired level. For example, you could slowly dim the LED bars with a sketch like this:

    language:c
    /* MOSFET LED Bar Dimmer
        Example Arduino Sketch
    */

    // Define the pin connected to our MOSFET gate:
    int ledControlPin = 3; // Must be a PWM pin -- 3, 5, 6, 9, 10, 11

    void setup()
    

    void loop()
    
      delay(1000); // Hold at full brightness
      for (int i=255; i>=0; i-=5) // Sweep LED off
      
      delay(1000); // Hold at off
    }

Or come up with other nifty sketches. How about attaching a potentiometer, and controlling the LED\'s intensity with that?

#### Using a 555 Timer

If you don\'t have an Arduion around, or are looking for a more analog/elegant/cheap solution, you could use a [555 timer](https://www.sparkfun.com/products/9273) and a handful of common components to generate the PWM signal. Here\'s an example circuit:

[![555 Dimmer circuit](https://cdn.sparkfun.com/r/600-600/assets/7/d/0/2/4/52433239757b7fb7798b4567.png)](https://cdn.sparkfun.com/assets/7/d/0/2/4/52433239757b7fb7798b4567.png)

Most 555 timers can work at up to 16V, so you can run it directly off the 12V supply. Then twist the potentiometer to adjust the brightness. Woo 555 timers!

[![555 Timer circuit image](https://cdn.sparkfun.com/r/600-600/assets/1/4/5/3/5/524477d3757b7fbb068b4569.png)](https://cdn.sparkfun.com/assets/1/4/5/3/5/524477d3757b7fbb068b4569.png)