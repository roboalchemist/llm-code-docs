# Source: https://learn.sparkfun.com/tutorials/lilypad-simple-power-hookup-guide

## Introduction

The [LilyPad Simple Power](https://www.sparkfun.com/products/11893) is a basic power board that enables you to power your wearable circuit with a lipo battery. It also allows battery charging in the circuit via [micro-B cable](https://www.sparkfun.com/products/10215), and it provides a nice on/off switch for your project.

[![LilyPad Simple Power](https://cdn.sparkfun.com/r/600-600/assets/parts/8/3/2/4/11893-01a.jpg)](https://www.sparkfun.com/lilypad-simple-power.html)

### [LilyPad Simple Power](https://www.sparkfun.com/lilypad-simple-power.html) 

[ DEV-11893 ]

The LilyPad Simple Power is a simple e-textile board with a 500mA charge rate that lets you connect and charge a lipo battery...

[ [\$12.50] ]

Being part of the [LilyPad line of boards](https://www.sparkfun.com/search/results?term=lilypad), you can wash this PCB even after it\'s been sewn to a garment. Just remember to **remove the battery** first before doing any washing!

With this quick tutorial, you\'ll learn how to get started with the Simple Power.

### Suggested Reading

Please check out the following tutorials, if you aren\'t familiar with any of the topics.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-powering-your-project)

### LilyPad Basics: Powering Your Project 

Learn the options for powering your LilyPad projects, LiPo battery safety and care, and how to calculate and consider power constraints on your projects.

## Hardware Overview

True to its name, the LilyPad Simple power is really simple! There\'s only a few features you need to be aware of.

[![LilyPad Simple Board LiPo Charger Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/2/Labeled_LilyPad_Simple_Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/2/Labeled_LilyPad_Simple_Front.jpg)

### Battery JST Connector

The Simple Power is designed to work with 3.7V lipo batteries. In order to connect the battery to the board, there should be a female [JST connector](https://www.sparkfun.com/products/8671) on the battery.

⚡ **Warning!** The charge rate for the MCP73831\'s is set at **500mA**. Make sure to have a battery that is higher than 500mAh to safely charge the LiPo battery.\
\

[![Lithium Ion Battery - 850mAh](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/1/13854-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-850mah.html)

### [Lithium Ion Battery - 850mAh](https://www.sparkfun.com/lithium-ion-battery-850mah.html) 

[ PRT-13854 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 850...

[ [\$13.61] ]

[![Lithium Ion Battery - 2Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/2/13855-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-2ah.html)

### [Lithium Ion Battery - 2Ah](https://www.sparkfun.com/lithium-ion-battery-2ah.html) 

[ PRT-13855 ]

These are very slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 200...

[ [\$19.41] ]

[![Lithium Ion Battery - 6Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/6/3/13856-01.jpg)](https://www.sparkfun.com/lithium-ion-battery-6ah.html)

### [Lithium Ion Battery - 6Ah](https://www.sparkfun.com/lithium-ion-battery-6ah.html) 

[ PRT-13856 ]

If you need some juice, this 6Ah Lithium Ion Battery is for you. These are very compact batteries based on Lithium Ion chemis...

[ [\$48.44] ]

[![Lithium Ion Battery - 1Ah](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/0/1/13813-01.jpg)](https://www.sparkfun.com/products/13813)

### [Lithium Ion Battery - 1Ah](https://www.sparkfun.com/products/13813) 

[ PRT-13813 ]

Slim, extremely light weight batteries based on Lithium Ion chemistry. Each cell outputs a nominal 3.7V at 1000 mAh!

**Retired**

### micro-B Connector

This allows you to charge your battery via a computer USB port, using a micro-B USB cable.

### Positive/Negative Terminals

These sew taps are the connection points from where the power to your circuit will flow. The positive terminal outputs 3.7V, and the negative terminal is the ground (GND) connection.

### On/Off Switch

This switch enables and disables power to flow out of the LilyPad Simple board. When it is in the \'on\' position, you can measure the battery voltage across the positive (+) and negative (-) terminals. When it is in the \'off\' position, there is no measurable voltage output from the board.

### Mounting Holes

These four holes spaced across the board are designed as additional anchoring sew taps. They are not conductive, and have no electrical functionality.

## Hardware Hookup

In our example, we are going to assume you are powering a basic [LilyPad LED](https://www.sparkfun.com/products/10045). However, you can use the Simple Power to power a [LilyPad Main board](https://www.sparkfun.com/products/9266), or various other products.

One thing to note about the Simple Power- it is designed for e-textile applications, but you [*can* solder to the board](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). Just keep in mind it\'s going to take more solder and more heat to attach wires to the sew taps.

[![Basic Simple Power Circuit](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/2/LilyPadSimple_Power_LiPo_Battery_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/2/LilyPadSimple_Power_LiPo_Battery_Fritzing_bb.jpg)

*Our example circuit using the Simple Power and a LilyPad LED.*

Find the \'+\' terminal on the Simple Power and run a stitch/wire to the \'+\' sew tap on the LED (or whatever board you are powering). Then run a wire or stitch from the \'-\' terminal on the Simple Power to the \'-\' sew tap on the LED. If you are using conductive thread, make sure you **don\'t let the two lines touch!** This will short out your battery, possibly short out your Simple Power, and you\'ll have a bad time.

Once your boards are connected, plug in your battery, and flip the Simple Power switch to the \'on\' position. Bask in that happy LED glow!

### Charging the Battery

If your battery runs down, have no fear! Simply plug in a microUSB cable into your computer and also into the LilyPad Simple board, and have some patience. There\'s a yellow LED that indicates when the board is charging the battery. The board may also get warm while charging, but this is totally normal. Charging times will vary depending on the capacity of the battery connected to the Simple Power.