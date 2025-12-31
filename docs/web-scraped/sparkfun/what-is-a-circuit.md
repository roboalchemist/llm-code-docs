# Source: https://learn.sparkfun.com/tutorials/what-is-a-circuit

## Overview

Welcome to circuits 101! One of the first things you\'ll encounter when learning about electronics is the concept of a **circuit**. This tutorial will explain what a circuit is, as well as discuss **voltage** in further detail.

[![Picture of Circuit](//cdn.sparkfun.com/r/600-600/assets/2/f/9/d/a/513a1dfbce395fe524000001.JPG)](//cdn.sparkfun.com/assets/2/f/9/d/a/513a1dfbce395fe524000001.JPG)

*A simple circuit, involving a [button](https://learn.sparkfun.com/tutorials/switch-basics), an [LED](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds), and a [resistor](https://learn.sparkfun.com/tutorials/resistors), built two different ways.*

### Suggested Reading

There are a few concepts you should have a good understanding of to help you get the most out of this tutorial.

- [What is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity)
- [Electric Power](https://learn.sparkfun.com/tutorials/electric-power)
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
- [Alternating Current (AC) vs Direct Current (DC)](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)
- [Polarity](https://learn.sparkfun.com/tutorials/polarity)

## Circuit Basics

### Voltage and How it Works

You\'ve probably heard that a battery or a wall outlet has a certain number of **volts**. This is a measurement of the electrical **potential** produced by the battery, or the utility grid connected to the wall outlet.

All those volts are sitting there waiting for you to use them, but there\'s a catch: **in order for electricity to do any work, it needs to be able to move**. It\'s kind of like a blown-up balloon; if you pinch it off, there is air in there that *could* do something if it\'s released, but it won\'t actually do anything until you let it out.

Unlike air coming out of a balloon, electricity can only flow through materials that can conduct electricity, such as copper wire. If you connect a wire to a battery or wall outlet (**WARNING:** the voltage in a wall outlet is dangerous, don\'t do this!), you will be giving the electricity a path to follow. But if the wire isn\'t connected to anything else, the electricity won\'t have anywhere to go and still won\'t move.

[![alt text](//cdn.sparkfun.com/assets/b/6/f/8/b/51140a47ce395fae7e000004.png)](//cdn.sparkfun.com/assets/b/6/f/8/b/51140a47ce395fae7e000004.png)

What makes electricity move? **Electricity wants to flow from a higher voltage to a lower voltage.** This is exactly like the balloon: the pressurized air in the balloon wants to flow from inside the balloon (higher pressure) to outside the balloon (lower pressure). If you create a conductive path between a higher voltage and a lower voltage, electricity will flow along that path. And if you insert something useful into that path like an LED, the flowing electricity will do some work for you, like lighting up that LED. Huzzah!

[![alt text](//cdn.sparkfun.com/assets/c/7/a/6/8/51140a47ce395f5c7d000003.png)](//cdn.sparkfun.com/assets/c/7/a/6/8/51140a47ce395f5c7d000003.png)

So, where do you find a higher voltage and a lower voltage? Here\'s something really useful to know: **every source of electricity has two sides**. You can see this on batteries, which have metal caps on both ends, or your wall outlet that has two (or more) holes. In batteries and other [DC (Direct Current)](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc/direct-current-dc) voltage sources, these sides (often called **terminals**) are named **positive** (or \"+\"), and **negative** (or \"-\").

Why does every source of electricity have two sides? This goes back to the idea of "potential", and that you need a voltage difference in order to get electricity to flow. It sounds silly, but you can't have a difference without two things to be different. In any power supply, the positive side will have a higher voltage than the negative side, which is exactly what we want. In fact, when we measure voltage, we usually say that the negative side is 0 volts, and the positive side is however many volts the supply can provide.

Electrical sources are like pumps. Pumps always have two sides, an outlet that blows something out, and an inlet that sucks something in. Batteries and generators and solar panels work the same way. Something inside them is hard at work moving electricity towards the outlet (the positive side), but all that electricity leaving the device creates a void, which means that the negative side needs to pull electricity in to replace it.[\*](#franklin)

What have we learned so far?

- Voltage is potential, but electricity needs to flow to do anything useful.
- Electricity needs a path to flow through, which must be an electrical conductor such as copper wire.
- Electricity will flow from a higher voltage to a lower voltage.
- DC voltage sources always have two sides, called positive and negative, with the positive side a higher voltage than the negative side.

### The Simplest Circuit

We\'re finally ready to make electricity work for us! If we connect the positive side of a voltage source, through something that does some work such as a Light Emitting Diode (LED), and back to the negative side of the voltage source; electricity, or **current**, will flow. And we can put things in the path that do useful things when current flows through them, like LEDs that light up.

[![alt text](//cdn.sparkfun.com/assets/a/c/2/e/6/5113f6f5ce395fc77d000002.png)](//cdn.sparkfun.com/assets/a/c/2/e/6/5113f6f5ce395fc77d000002.png)

**This circular path, which is always required to get electricity to flow and do something useful, is called a circuit.** A circuit is a path that starts and stops at the same place, which is exactly what we\'re doing.

[Click this link](http://www.falstad.com/circuit/#%24+1+5.0E-6+10.20027730826997+50+5.0+50%0Av+224+288+224+160+0+0+40.0+5.0+0.0+0.0+0.5%0Aw+224+288+448+288+0%0A162+448+160+448+224+1+2.1024259+1.0+0.0+0.0%0Ar+448+224+448+288+0+330.0%0Aw+224+160+304+160+0%0As+304+160+368+160+0+0+false%0Aw+448+160+368+160+0%0Ax+266+186+397+190+0+18+switch+%28click+me%29%0Ax+475+198+510+202+0+18+LED%0Ax+485+263+544+267+0+18+resistor%0Ax+138+228+193+232+0+18+battery%0Ax+204+209+215+213+0+18+%2B%0Ax+207+247+213+251+0+18+-%0A) to see a simulation of current flowing through a simple circuit. This simulation requires Java to run.

------------------------------------------------------------------------

[] \*Benjamin Franklin originally wrote that electricity flows from the positive side of a voltage source to the negative side. However, Franklin had no way of knowing that [electrons actually flow in the opposite direction](http://www.allaboutcircuits.com/vol_1/chpt_1/7.html) - at the atomic level, they come out of the negative side and loop back to the positive side. Because engineers followed Franklin\'s lead for hundreds of years before the truth was discovered, we still use the \"wrong\" convention to this day. Practically speaking this detail doesn\'t matter, and as long as everyone uses the same convention, we can all build circuits that work just fine.

## Short and Open Circuits

### What is a "Load"?

The reason we want to build circuits is to make electricity do useful things for us. The way we do that is by putting things in the circuit that use the current flow to light up, make noise, run programs, etc.

These things are called **loads**, because they "load down" the power supply, just like you're "loaded down" when you're carrying something. The same way you could be loaded down with too much weight, it's possible to load down a power supply too much, which will slow down the current flow. But unlike you, it's also possible to load down a circuit too little - this may let too much current flow (imagine running too fast if you weren't carrying any weight), which can burn out your parts or even the power supply.

You'll learn all about voltage, current, and loads in the next tutorial: [Voltage, Current, Resistance, and Ohm\'s Law](http://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law). But for now, let's learn about two special cases of circuit: **short circuit**, and **open circuit**. Knowing about these will help tremendously when you\'re troubleshooting your own circuits.

### Short Circuit[]

DON\'T DO THIS, but if you connect a wire directly from the positive to the negative side of a power supply, you\'ll create what is called a **short circuit**. This is a very bad idea.

[![alt text](//cdn.sparkfun.com/assets/e/6/9/2/b/5113f781ce395f877e000005.png)](//cdn.sparkfun.com/assets/e/6/9/2/b/5113f781ce395f877e000005.png)

This seems like the best possible circuit, so why is it a bad idea? Remember that electrical current wants to flow from a higher voltage to a lower voltage, and if you put a load into the current, you can do something useful like light up an LED.

If you DO have a load in the current, the current flow through your circuit will be limited to that which your device consumes, which is usually a very small amount. However, if you DON\'T put anything in to restrict the current flow, there won\'t be anything to slow down the current, and it will try to be infinite!

Your power supply can\'t provide infinite current, but it will provide as much as it can, which may be a lot. This could cause your wire to burn up, damage the power supply, drain your battery, or other exciting things. Most of the time your power supply will have some sort of safety mechanism built into it to limit the maximum current in the event of a short circuit, but not always. This is the reason all homes and buildings have [circuit breakers](http://en.wikipedia.org/wiki/Circuit_breaker), to prevent fires from starting in the event of a short circuit somewhere in the wiring.

A closely related problem is accidentally letting too much current flow through part of your circuit, causing a part to burn up. This isn\'t quite a short circuit, but it\'s close. This most often happens when you use the incorrect **resistor** value, which lets too much current flow through another component such as an LED.

[![alt text](//cdn.sparkfun.com/assets/a/2/e/0/1/5114187dce395fdf01000002.png)](//cdn.sparkfun.com/assets/a/2/e/0/1/5114187dce395fdf01000002.png)

The bottom line: **if you notice that things are suddenly becoming hot or a part suddenly burns out, immediately turn off the power and look for possible short circuits.**[]

### Open Circuit

The opposite of a short circuit is an **open circuit**. This is a circuit where the loop isn\'t fully connected (and therefore this isn\'t really a circuit at all).

[![alt text](//cdn.sparkfun.com/assets/a/a/2/d/6/5113f6f5ce395fba7e000003.png)](//cdn.sparkfun.com/assets/a/a/2/d/6/5113f6f5ce395fba7e000003.png)

Unlike the short circuit above, nothing will get hurt by this \"circuit\", but your circuit won\'t work either. If you\'re new at circuits, it can often be hard to find where the break is, especially if you\'re using [breadboards](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) where all the conductors are hidden.

**If your circuit doesn\'t work, the most likely cause is an open circuit.** This is usually due to a broken connection or a loose wire. (Short circuits can steal all the power from the rest of your circuit, so be sure to look for those as well.)

**TIP:** if you can\'t easily find where your circuit is open, a **[multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)** can be very useful tool. If you set it to measure volts, you can use it to check the voltage at various points in your powered circuit, and eventually find the point where voltage isn\'t getting through.