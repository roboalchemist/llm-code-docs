# Source: https://learn.sparkfun.com/tutorials/reed-switch-hookup-guide

## Introduction

Reed switches are magnetically-actuated electrical switches (not magically-actuated, though it seems that way sometimes). When the body of the switch is exposed to a magnetic field \-- like a magnet or even a strong electrical current \-- two ferrous materials inside pull together, the connection closes, and current can flow. In absence of a magnetic field, the switch opens as does the circuit it\'s a part of.

[![Reed Switch](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/8/4/08642-02-L.jpg)](https://www.sparkfun.com/reed-switch.html)

### [Reed Switch](https://www.sparkfun.com/reed-switch.html) 

[ COM-08642 ]

This is a small device called a \[reed switch\](http://en.wikipedia.org/wiki/Reed_switch). When the device is exposed to a magn...

[ [\$2.25] ]

There are all sorts of creative applications for reed switches. They\'re perfect for any projects that require **non-contact** control. A [magnetic door switch](https://www.sparkfun.com/products/13247), for example, is just a dressed up reed switch and a mating magnet \-- by keeping both parts of the switch separate, the door can open and close freely (and maintain its regular duties as a door). The [anemometer in our weather meter](https://www.sparkfun.com/products/8942) combines a number of reed switches, which all open and close in order as the wind blows; count the time between switch closures to determine the wind speed.

### Suggested Materials

This tutorial serves as a quick primer on reed switches and demonstrates how to hook them up and use them. Beyond the switch itself, the following materials are recommended:

**[Magnet](https://www.sparkfun.com/products/8643)** \-- You\'ll need something to actuate the reed switch, and this small magnet should fit the bill.

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using a digital pin on the Arduino to read the state of the switch. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Breadboard](https://www.sparkfun.com/products/12002)** and **[Jumper Wires](https://www.sparkfun.com/products/11026)** \-- With it\'s legs properly bent, the reed switch is breadboard-compatible. We\'ll use the breadboard as an intermediary between reed switch and jumper wires, which will connect the switch to an Arduino.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Magnet Square - 0.25\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/8/5/08643-02-L.jpg)](https://www.sparkfun.com/magnet-square-0-25.html)

### [Magnet Square - 0.25\"](https://www.sparkfun.com/magnet-square-0-25.html) 

[ COM-08643 ]

These are small rare earth magnets - 0.25\" cubed. Composed of Neodymium/Iron/Boron (NdFeB), these magnets are curiously stron...

[ [\$1.75] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

### Suggested Reading

Read switches are a fun and easy-to-use component for beginners, but there are still a few basic electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

## Reed Switch Overview

Reed switches come in a variety of shapes and sizes. Through-hole, surface-mount, insulated, pre-formed \-- there are a lot of factors to consider.

[![Magnetic Door Switch Set](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/4/0/13247-01.jpg)](https://www.sparkfun.com/magnetic-door-switch-set.html)

### [Magnetic Door Switch Set](https://www.sparkfun.com/magnetic-door-switch-set.html) 

[ COM-13247 ]

This is the Magnetic Door Switch Set, a small reed switch assembly specifically designed to alert you when doors, drawers, or...

[ [\$4.50] ]

[![LilyPad Reed Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/5/2/13343-01.jpg)](https://www.sparkfun.com/lilypad-reed-switch.html)

### [LilyPad Reed Switch](https://www.sparkfun.com/lilypad-reed-switch.html) 

[ DEV-13343 ]

The LilyPad Reed Switch is a simple breakout for a reed switch that will make it easy to use in e-textiles circuits in exactl...

[ [\$6.75] ]

[![Reed Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/8/4/08642-02-L.jpg)](https://www.sparkfun.com/reed-switch.html)

### [Reed Switch](https://www.sparkfun.com/reed-switch.html) 

[ COM-08642 ]

This is a small device called a \[reed switch\](http://en.wikipedia.org/wiki/Reed_switch). When the device is exposed to a magn...

[ [\$2.25] ]

[![Reed Switch - Insulated](https://cdn.sparkfun.com/r/140-140/assets/parts/5/1/2/3/10601-01.jpg)](https://www.sparkfun.com/reed-switch-insulated.html)

### [Reed Switch - Insulated](https://www.sparkfun.com/reed-switch-insulated.html) 

[ COM-10601 ]

This is a small device called a \[reed switch\](http://en.wikipedia.org/wiki/Reed_switch). When the device is exposed to a magn...

[ [\$3.50] ]

The basic glass reed switches are relatively fragile. If you\'re project will feature large magnets repeatedly slamming against the body of the switch, consider upgrading to an [overmolded variant](https://www.sparkfun.com/products/10601).

You may also need to consider the **current and voltage** capabilities of your reed switch \-- they\'re usually not designed to carry a high amount of power. The glass switch we\'re using in this tutorial is rated for a **maximum of 1.2A and 10W**. Higher-power-capable switches are hard to find and can be expensive.

### Normally Open, Normally Closed?

One thing all of these switches have in common is the two-terminal interface. But whether those terminals are normally open or closed is another question. The reed switch we\'ll be using in this example is **normally-open**. That means \"normally\", when the switch is unaffected by a magnetic field, the switch is open and does not conduct electricity. When a magnet comes close enough for the switch to activate, the contacts close and current can flow.

Looking for a **normally-closed** switch? You can make one by adding a second magnet. [Check it out](https://standexelectronics.com/resources/magnet-interaction/form-b-reed-switch-actuation-parallel-position-perpendicular-movement/)!

### Magnetic Sensor Activation

Just as your magnet may have two poles, the reed switch\'s pair of ferrous contacts are also polarized. The position, distance, and orientation of your magnet all play a role in determining how the switch activates.

These example graphs, from the [Hamlin App Note AN104](http://www.hamlin.com/specSheets/AN104.pdf) do a great job of demonstrating how the position of the magnet affects the activation of the switch.

[![Reed switch activation graphs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/9/reed-activation-graph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/9/reed-activation-graph.png)

The graph on the left shows an expected activation area when the magnet is held parallel to the reed switch. This area, as expected, is a mostly parabolic field. The graph on the right demonstrates what you can expect when the magnet is perpendicular to the switch. In this orientation, there is usually a dead zone in the center of the switch. If it\'s in the middle of the body, it might not activate, even when the magnet is touching the reed switch.

The polarity and position of the magnet plays an important role in how your reed switch activates. If your switch doesn\'t seem as sensitive as you\'d like, **try placing the magnet to one side or the other**. Make sure you test the pair of components out before mounting either in place.

## Example Circuit

The circuit set up for this example is about as easy as can be. First **bend both legs** of the switch to point perpendicularly away from the body of the switch, so they form a \"U\" shape.

**Fragile!** The body of the glass-tubed reed switch is very delicate. While you\'re bending the legs, try not to place any stress on the body of the switch.

Insert the reed switch into the breadboard. Then use jumper wires to connect one end of the switch to ground and the other end to the Arduino\'s D2 pin. Here\'s an example circuit:

[![Reed switch circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/9/example_circuit_bb-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/9/example_circuit_bb-2.png)

That\'s all it takes! We\'ll use the Arduino\'s **internal pull-up resistor** on pin 2 to bias the switch high. When the switch closes, it will connect pin 2 directly to ground, and it should read low.

## Example Code

Here is a simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    Reed_Switch_Example.ino
    Example sketch for SparkFun's Reed Switch
      (https://www.sparkfun.com/products/8642)
    Jim Lindblom @ SparkFun Electronics
    May 3, 2016

    The reed switch is a two-terminal, magnetically-actuated, normally-open switch.
    Connect one end of the switch to ground, and the other to Arduino's D2 pin.

    The D2 pin's internal pull-up resistor is used to bias the pin high. When the
    switch closes, the pin should go low.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int REED_PIN = 2; // Pin connected to reed switch
    const int LED_PIN = 13; // LED pin - active-high

    void setup() 
    

    void loop() 
    
      else
      
    }

The sketch depends on an LED being attached to the Arduino\'s pin 13. That should be the case on 99% of the Arduino boards out there, but, if yours is different, you may need to check the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) for verification of the switch\'s operation.

With the sketch uploaded, grab your magnet, and draw it close to the switch. It should trigger when the magnet approaches, as close as 1cm away from the body of the reed switch. Try mapping out the entire activation region of the reed switch. See how far away you can get the magnet!