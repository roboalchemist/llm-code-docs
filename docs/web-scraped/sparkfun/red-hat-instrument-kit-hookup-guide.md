# Source: https://learn.sparkfun.com/tutorials/red-hat-instrument-kit-hookup-guide

## Introduction

How can open source help us find new ways to express ourselves? In the [Red Hat Instrument Kit](https://www.sparkfun.com/products/18432), you\'ll learn how conductivity works and use that understanding to create an interactive musical instrument. Conductive paint and ink will allow you to explore how physical design affects the way a tool is used. This experiment empowers participants to bring their own creative thinking to the world of sound and instruments. This activity is best suited for people between the ages of 10-13 and does not require any prior knowledge of circuits or skill in wiring or electronics. Given that some of the components are small and making connections requires a level of dexterity, younger students may need some adult assistance.

### Required Materials

To follow along with this tutorial, you will need the Red Hat Instrument Kit.

[![Red Hat Co.Lab Instrument Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/8/6/0/18432-Red_Hat_Co.Lab_Instrument_Kit-01.jpg)](https://www.sparkfun.com/red-hat-co-lab-instrument-kit.html)

### [Red Hat Co.Lab Instrument Kit](https://www.sparkfun.com/red-hat-co-lab-instrument-kit.html) 

[ CUST-18432 ]

In this kit, you\'ll gain an understanding of how conductivity works while creating an interactive musical instrument.

[ [\$24.95] ]

If you wish to purchase the individual parts for this as refill or expansion, here is a list:

### You Will Also Need

You will need materials that didn't come with your kit (paper and a pair of scissors).

### Suggested Reading

If you are not familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

## Hardware Overview

It's always helpful to know the parts you will be using before diving into the build. Go ahead and lay the parts out in front of you on a piece of paper. As you lay them out, pick them up and explore each one. How many pins does it have? What colors are on it? Is each leg of the component the same length? Can you guess what it does, based on how it looks or what it\'s called? You should write these observations down next to each part. That will help you organize the pieces as we begin to explore and build. This is what you should have:

[![Labelled overview of parts in the kit](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/HardwareOverview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/HardwareOverview.png)

*Having a hard time seeing everything? Click the image for a closer look.*

### Breadboard

Let's start by taking a look at the breadboard in your kit. First, notice there are two long columns of holes running down each side of the board, one with a red line beside it, and one with a black line. These are the power rails, and all the holes in a single power rail are connected to each other. If power is connected to one hole in the column, it is connected to all the other holes in the column.

Second, all the holes in a numbered row are connected to each other, but this connection is broken at the small trench or indent that runs down the center of the board. Each side COULD be its own separate circuit. Our project will jump over the trench using jumper wires and send power back and forth.

Basically, you can view a breadboard as a series of columns (labeled A-E and F-J) and rows (labeled 1-30.) And remember, the trench in the middle means A5 isn't connected to F5. When we get to actually creating the circuit, we'll use this row-and-column system to mark where connections should be made (A6, E3, H23, etc.).

[![Image of the breadboard](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/12002-Breadboard_-_Self-Adhesive__White_-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/12002-Breadboard_-_Self-Adhesive__White_-03.jpg)

For more information on how to Use a Breadboard, feel free to head on over to our tutorial [here](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard?_ga=2.129710725.823923826.1629316107-2121418670.1568942816), or click on the breadboard image below.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

May 14, 2013

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

### 555 timer

A 555 circuit's use is so open-ended that contests are held to see who can conceive of the most useful, complex, and/or artistic use of the thing. Every sound we hear from an instrument is made of a waveform. The pitch (how high or low a note sounds to our ears) changes with the number of times a wave occurs in a second. With the 555 at the heart of our circuit, (and a handful of choice resistors and capacitors) we can create waveforms that oscillate at frequencies from thousandths to hundreds of thousandths of a second. That's a lot of waves per second!

[![Product image for the 555 timer](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/16473-IC_555_Timer__PTH_-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/16473-IC_555_Timer__PTH_-01.jpg)

### Capacitor

A capacitor is a two-terminal, electrical component. Along with resistors and inductors, they are one of the most fundamental passive components we use. You would have to look very hard to find a circuit which did not have a capacitor in it. What makes capacitors special is their ability to store energy; they are like a fully charged electric battery. Caps, as we usually refer to them, have all sorts of critical applications in circuits. Common applications include local energy storage, voltage spike suppression, and complex signal filtering.

[![Product image for the Capacitor Ceramic](https://cdn.sparkfun.com/assets/parts/8/3/2/08375-03-L.jpg)](https://cdn.sparkfun.com/assets/parts/8/3/2/08375-03-L.jpg)

For more information on capacitors and their uses, feel free to head on over to our tutorial [here](https://sparkle.sparkfun.com/sparkle/learn_tutorials/79#tab-attributes), or click on the Capacitor image below.

[](https://learn.sparkfun.com/tutorials/capacitors)

### Capacitors 

June 19, 2013

Learn about all things capacitors. How they\'re made. How they work. How they look. Types of capacitors. Series/parallel capacitors. Capacitor applications.

### Speaker

This little guy is similar to what you\'d find in one of those singing greeting cards. Thin and flat, and able to make just enough noise for our project.

[![Image of the speaker](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/15350-Thin_Speaker_-_0.5W-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/15350-Thin_Speaker_-_0.5W-02.jpg)

### Resistors

Resistors are electronic components which have a specific, never-changing [electrical resistance](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law#resistance). The resistor\'s resistance **limits the flow of electrons** through a circuit.

[![Product image for the Resistor 1K Ohm](https://cdn.sparkfun.com/assets/parts/1/2/5/4/8/14492-03.jpg)](https://cdn.sparkfun.com/assets/parts/1/2/5/4/8/14492-03.jpg)

For a basic description, this is good enough, but if you would like to delve into the world of resistors and Ohm\'s law, consider checking out [this tutorial](https://learn.sparkfun.com/tutorials/resistors) or click on the image below:

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

April 1, 2013

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

### Jumper Wires

Jumper wires help a circuit \"jump\" from one location to another. Hence the name \"jumper wire\". Pretty nifty eh? The end ports can be male or female - in this tutorial you\'ll be using Male to Male jumpers, meaning both ends have plugs on them.

[![Product photo of jumper wires](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/12795-00.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/12795-00.jpg)

### Alligator Clip Jumper Wires

These guys are just like Jumper Wires, except that they are pre-terminated with an alligator clip on one end and a hookup pigtail on the other. Like so:

[![Product photo for Alligator Clips](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/13191-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/13191-01.jpg)

### Electric Paint

Bare Conductive\'s Electric Paint is just like any other water-based paint\... except that it\'s electrically conductive. This means that you can actually paint wires onto things like models, clothes, furniture, walls, almost anything you can think of. In this case, we will be using it to draw our instrument. Check out the video below for more information on our conductive paint\...

If that nifty little video didn\'t sate your need for information, see the [datasheet](http://cdn.sparkfun.com/datasheets/E-Textiles/Materials/TechnicalDataSheet_BareConductivePaint.pdf) for more in-depth info.

There are other parts in this kit, but this is the bulk of what you\'ll need to know for this tutorial. Let\'s get to building!

## Part 1: Drawing your Instrument

What is an instrument? This is kind of a weird question, right? Really, a musical instrument is anything you can use to produce sound. Guitars, gourds, seashells, pianos ― used the right way, they can all be instruments.

For the purposes of this kit, a musical instrument is a device that lets us make sounds and control their pitch ― how high or low they are. Using your conductive paint/ink, make a long line on your piece of paper. Be sure to draw at least one solid block of ink near the edge of the paper. You'll be able to redesign your instrument later and be really creative in how it takes shape, but for now just make a thin line.

[![Image of a thin line drawn with bare conductive electric paint](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/ConductivePaint.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/ConductivePaint.png)

*Image courtesy of Red Hat*

## Part 2: Breadboarding, 555 timer, and potentiometer

What is a circuit? A circuit is a closed loop that electricity can travel around. At its most basic, a circuit consists of three parts:

- A voltage source: The power for the circuit
- A load: The thing that is being powered, like a motor, buzzer, or light
- The circuit path: The continuous path that the current follows as it travels around the circuit

An example of a simple circuit would be a power source (like a battery), a load (like an LED), and the circuit path (the wires that connect them).

### The power/voltage source

Your kit comes with a 9V battery and 9V snap connector to be used as a power/voltage source. You\'ll notice that the snap connector has a plastic connector ― the small, white, rectangular box at the end of the red and black wires. This makes it easy to connect to many types of electronics; however, we won't be using it for our project today. We'll actually connect the power to the breadboard with jumper wires. The jumper wires in your kit have small metal pins on either side.

The colors of the jumper wires don't correspond to anything in your kit. Use any two colors that you prefer. That said, make sure you keep track of which jumper is positive and which jumper is negative. By convention, the red jumpers are positive, and the black jumpers are negative/ground.

There are two holes in the plastic molding at the end of the wires coming from the battery pack. Insert a jumper wire into each of these holes like so:

[![Battery and snap connector with jumper wires inserted into the ](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/Battery.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/Battery.jpg)

*Image courtesy of Red Hat*

Now insert the other ends into the (+) power rail and the (-) power rail - again making sure that your positive jumper goes to the (+) side of the power rail and the negative jumper goes to the (-) side of the power rail:

[![Battery and jumpers hooked into the breadboard](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/BatterywithBreadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/BatterywithBreadboard.jpg)

*Image courtesy of Red Hat*

### The load

For this circuit, we will use a 555 circuit attached to a speaker triggered by a potentiometer. Potentiometers can take multiple shapes. Sometimes, we might see them as knobs that we turn, like volume knobs on radios. Other times, they look like faders that slide up and down; think of some dimmable light switches. They can give us control over things like speed, voltage, or frequency in our circuit kits. As we make adjustments to our knob or fader, we are changing the amount of resistance that a circuit is passing.

For our circuit, we'll draw our potentiometer using conductive paint or ink. Since we know that circuits are continuous devices, we'll have to make sure that, whatever instrument we draw, all the lines connect somehow. The ink we used to draw our line above will serve as our potentiometer.

Our circuit culminates in the speaker. If you've used headphones or earbuds, or watched TV, you have a pretty good idea what speakers are capable of. For our purposes, the speaker converts the electrical audio signal (in the form of sound waves) from our 555 timer into sound. This is the same basic principle that a guitar amplifier or movie theater sound system uses.

[![Outline of breadboard hooked to the circuit including the speaker](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/Breadboard.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/Breadboard.png)

*Image courtesy of Red Hat*

### The circuit path

For a circuit to work, the path of the power can't be interrupted --- every piece must connect with another piece. Luckily, we have a breadboard, which is a helpful tool we can use to quickly plug in items and keep them connected. It also lets us create, fix small mistakes, and practice with our components.

[![Fritzing like image of the circuit](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/BreadboardFritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/BreadboardFritzing.png)

*Image courtesy of Red Hat*

We are going to replicate this circuit (the steps are below). We're using quite a few jumper wires, so be extra careful to place them into the appropriate coordinate points on your breadboard. We'll save the special alligator clip connections for last. We'll use both sides of our breadboard, so remember that each side has a positive (+) and negative (-) power rail, as well as its own unique set of column connections. The left hand columns are labeled A-E, and the right hand columns are F-J.

### Create your circuit:

- Place the 555 timer circuit so that one set of pins aligns with E9-E12 and the other set aligns with F9-F12. This will mean that the 555 timer bridges the center trench/gap. Gently press into place.
- Connect a jumper wire from positive power (+) rail 2 on the left side to positive power (+) rail 2 on the right side
- Connect a jumper wire from negative power (-) rail 2 on the left side to the negative power (-) rail 2 on the right side
- On the left side, connect a jumper wire from negative power (-) rail 9 to A9
- On the right side, connect a jumper wire from positive power rail (+) 9 to i9
- Connect a jumper wire from D10 to G11
- On the left side, connect a jumper wire from positive power rail (+) 11 to A12
- On the right side, place the resistor so that it bridges between H10 and positive power rail (+) 10
- On the left side, place a capacitor so that it bridges between C11 and B16
- On the right side, place a capacitor so that it bridges between i11 and the negative power rail (-) 13

### Connecting the Alligator Clip Jumper Wires

- On the left side, connect the pin end of an alligator clip jumper wire to A16 and clip the other end to the positive wire (+) of the speaker
- On the left side, connect the pin end of an alligator clip jumper wire to negative power rail (-) 15 and clip the other end to the negative wire (-) of the speaker
- On the right side, connect the pin end of an alligator clip jumper wire to H11 and clip the other end to the ink block on the edge of your drawing paper
- On the right side, connect the pin end of an alligator clip jumper wire to G10

### Testing

Once you complete the steps above and place the battery into the pack, you can play the ink like an instrument! To test your build, simply take the loose end of the final alligator clip jumper wire and tap it against any part of the conductive ink/paint line.

[![gif showing the alligator clip touching different parts of the conductive ink line](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/PaintGif.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/PaintGif.gif)

*Image courtesy of Red Hat*

### Redesign your instrument

Now that you see how the system works, take some time to redesign your instrument any way you want. Just remember that it's best to have a small block of conductive ink on the edge of your piece of paper to anchor the clip to. After you redesign your instrument, all you have to do is reclip the alligator wire that was previously on the edge of your paper with the straight line to the edge of the paper with the new instrument. Tap away!

[![image of whole system put together](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/KitFinal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/5/KitFinal.png)

*Image courtesy of Red Hat*

## Troubleshooting

Here are some things to look for if your project isn\'t working. Also, [ScienceBuddies.org](https://www.sciencebuddies.org/) has a great exploration of common mistakes people make with [breadboards](https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-breadboard#common-mistakes).

### Check your connections

- Be sure to double-check the coordinates in the instructions to make sure the pins are completely inserted into the matching holes on the breadboard
- Make sure components are fully seated in the breadboard. A component should go into the breadboard at least 4-5 mm (or a little less than the thickness of a pencil) when it\'s fully inserted.
- Check for short circuits. When components get connected accidentally, it can cause a short.
- Check the polarity of the capacitors and make sure they match the instructions

### Check your power

- Make sure your batteries are fully inserted
- Make sure your batteries work

### Replacement Parts

Sometimes, things break or get lost ― it\'s part of making and tinkering. If you need to replace a part, refer to the [wishlist](https://www.sparkfun.com/wish_lists/165238?_ga=2.201594520.823923826.1629316107-2121418670.1568942816) in the introduction of this guide to purchase any individual components that make up the Red Hat Co.Lab Instrument kit that you might need.