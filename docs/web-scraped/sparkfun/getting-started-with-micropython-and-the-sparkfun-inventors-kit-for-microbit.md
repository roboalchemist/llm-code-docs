# Source: https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Getting Started with MicroPython and the SparkFun Inventor\'s Kit for micro:bit

# Getting Started with MicroPython and the SparkFun Inventor\'s Kit for micro:bit

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f6f741d8fcd8b4705b2aff1b118b6243?d=retro&s=20&r=pg) LightningHawk]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft683&name=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft683 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft683&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft683&t=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft683&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F8%2F3%2Flogo.jpg&description=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Pin It")

## Introduction to the SparkFun Inventor\'s Kit for micro:bit for MicroPython

**Note:** This tutorial applies to [KIT-14542](https://www.sparkfun.com/products/retired/14542), [KIT-15228](https://www.sparkfun.com/products/15228), [KIT-17362](https://www.sparkfun.com/products/17362), and lab packs. For more information, check out the note in the Included Materials.

[MicroPython](https://micropython.org/) is an open source interpreter for the [Python](https://www.python.org/) programming language developed specifically for microcontrollers. In this experiment guide, we will show you how to get started using MicroPython with the popular [micro:bit](https://www.sparkfun.com/products/17287) board and our [SparkFun Inventor\'s Kit for micro:bit](https://www.sparkfun.com/products/17362).

[![SparkFun Inventor\'s Kit for micro:bit v2](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/3/8/9/15228-SparkFun_Inventor_s_Kit_for_micro-bit-01.jpg)](https://www.sparkfun.com/sparkfun-inventor-s-kit-for-micro-bit-v2.html)

### [SparkFun Inventor\'s Kit for micro:bit v2](https://www.sparkfun.com/sparkfun-inventor-s-kit-for-micro-bit-v2.html) 

[ KIT-17362 ]

The SparkFun Inventor's Kit (SIK) for micro:bit v2 is a great way to get creative, connected and coding with the micro:bit ...

[ [\$53.50] ]

[![SparkFun Inventor\'s Kit for micro:bit v2 Lab Pack](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/3/9/0/15229-SparkFun_Inventor_s_Kit_for_micro-bit_Lab_Pack-06a.jpg)](https://www.sparkfun.com/sparkfun-inventor-s-kit-for-micro-bit-v2-lab-pack.html)

### [SparkFun Inventor\'s Kit for micro:bit v2 Lab Pack](https://www.sparkfun.com/sparkfun-inventor-s-kit-for-micro-bit-v2-lab-pack.html) 

[ LAB-17363 ]

The SIK for micro:bit v2 Lab Pack includes 10 complete m:b v2 Inventor\'s Kits, an SIK Refill Pack and 25 AAA-sized batteries ...

[ [\$460.00] ]

**Note:** This experiment guide assumes you have experience with programming. If you have never used a programming language before, we recommend checking out the [MakeCode version of this guide](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-microbit-experiment-guide%0A). MakeCode is a drag-and-drop editor that is great for beginners of all ages learning to program.

When you\'re done with this guide, you\'ll have the know-how to start creating your own projects and experiments with MicroPython for micro:bit!

### Included Materials

The SparkFun Inventor\'s Kit (SIK) for micro:bit includes the following:

- **micro:bit** \-\-- The brains of the outfit with a bunch of onboard components. The version will vary depending on the kit or lab pack that you ordered.
- **micro:bit Breakout (with Headers)** \-\-- Allows you to connect the micro:bit to the breadboard. The version will vary depending on the kit or lab pack that you ordered.
- **Breadboard** \-\-- Excellent for making circuits and connections off the micro:bit. We included a full-sized breadboard to give you plenty of room.
- **Small Servo** \-\-- Here is a simple, low-cost, high-quality servo for all your mechatronic needs.
- **Piezo Buzzer** \-\-- BUZZZZ! Used to make different frequencies of sound.
- **USB micro-B Cable** \-\-- This 6-foot cable provides you with a USB-A connector at the host end and standard B connector at the device end.
- **Male-to-Male Jumper Wires** \-\-- These are high-quality wires that allow you to make connections with components on the breadboard.
- **TMP36 Temperature Sensor** - A sensor for detecting temperature changes.
- **Photocell** \-\-- A sensor to detect ambient light. Perfect for detecting when a drawer is opened or when nighttime approaches.
- **Tri-Color LED** \-\-- Because everyone loves a blinky.
- **Red, Blue, Yellow, and Green LEDs** \-\-- Light-Emitting Diodes make great general indicators.
- **Momentary Pushbutton Switch** \-\-- Go crazy with buttons.
- **10kΩ Trimpot** \-\-- Also known as a variable resistor, this is a device commonly used to control volume and contrast, and makes a great general user control input.
- **100Ω Resistors** \-\-- Great current-limiting resistors for LEDs, and strong pull-up resistors.
- **10kΩ Resistors** \-\-- These make excellent pull-ups, pull-downs and current limiters.
- **2x AAA Battery Pack** \-\-- AAA battery pack with the JST connector that fits the micro:bit
- **Alligator Clip with Pigtail** \-\-- A great way to connect individual components on a breadboard to the micro:bit ring connectors.

**Note:** This tutorial applies to [KIT-14542](https://www.sparkfun.com/products/retired/14542), [KIT-15228](https://www.sparkfun.com/products/retired/15228), [KIT-17362](https://www.sparkfun.com/products/17362), and lab packs. For those interested in what the differences are between each revision, check below!\
\

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SparkFun Inventor\'s Kit\                                                                                                    Revision History
  micro:bit SKU                                                                                                                
  ---------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------
  [KIT-17362](https://www.sparkfun.com/products/17362), [LAB-17363](https://www.sparkfun.com/products/17363)                   \- Switch to micro:bit V2.\
                                                                                                                               - Switch to [Qwiic micro:bit breakout board (with headers)](https://www.sparkfun.com/products/16446).

  [KIT-15228](https://www.sparkfun.com/products/retired/15228), [LAB-15229](https://www.sparkfun.com/products/retired/15229)   Switch to [2xAAA battery holder with a built-in switch](https://www.sparkfun.com/products/15101).

  [KIT-14542](https://www.sparkfun.com/products/retired/14542), [LAB-14301](https://www.sparkfun.com/products/retired/14301)   Initial release.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** The kit does not include [AAA batteries](https://www.sparkfun.com/products/09274) in the individual SparkFun Inventor\'s Kit for micro:bit V2 and they will need to be purchased separately. For older versions of the kit, you will need to purchase [AA batteries](https://www.sparkfun.com/products/15201) for the AA battery pack.\
\
\

[![750 mAh Alkaline Battery - AAA](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/7/4/09274-1.jpg)](https://www.sparkfun.com/products/9274)

### [750 mAh Alkaline Battery - AAA](https://www.sparkfun.com/products/9274) 

[ PRT-09274 ]

These are your standard 1.5V AAA alkaline batteries from Rayovac. Don\'t even think about trying to recharge these. Roughly 75...

**Retired**

What\'s that? You\'ve already got a micro:bit but still want to follow along? We have options!

- Get the handy dandy [SparkFun Inventor\'s Kit Bridge Pack for micro:bit](https://www.sparkfun.com/products/14719), which contains all of the items in the SIK kit except for the micro:bit. You can get all the parts in one fell swoop and a nice red box to boot!

[![SparkFun Inventor\'s Kit Bridge Pack for micro:bit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/9/4/2/14719-SparkFun_Inventor_s_Kit_Bridge_Pack_for_micro-bit-02.jpg)](https://www.sparkfun.com/sparkfun-inventor-s-kit-bridge-pack-for-micro-bit.html)

### [SparkFun Inventor\'s Kit Bridge Pack for micro:bit](https://www.sparkfun.com/sparkfun-inventor-s-kit-bridge-pack-for-micro-bit.html) 

[ KIT-14719 ]

The SparkFun Inventor\'s Kit Bridge Pack for micro:bit was designed to provide you with an easy way to transform your m:b into...

[ [\$43.95] ]

- Alternatively, you can pick and choose parts for individual experiments. This is a great option for folks who may already have some of the items in this tutorial just hanging around. Throughout this guide, we will provide links to the parts used for each circuit. Below is a wishlist for the parts used in the kit. Depending on what you have, you may not need everything on this list. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you have never worked with electronics before, we recommend you be somewhat familiar with the concepts in the following tutorials:

- [Getting Started with the micro:bit](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit#hardware-overview) \-\-- Basic guide to getting started with the micro:bi such as programming with MakeCode to the hardware overview.
- [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) \-\-- The most basic concepts in electronics and electrical engineering. Get very familiar with these concepts, as they will be used throughout your electronics adventure.
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit#short-and-open-circuits) \-\-- In this guide, we will be building a variety of circuits. Understanding what that means is vital to understanding the Inventor\'s Kit.
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) \-\-- First time working with a breadboard? Please check out this tutorial! It will help you understand why the breadboard is great for prototyping and how to use one.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

September 2, 2021

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

February 6, 2013

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

February 6, 2013

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

May 14, 2013

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

### Open Source!

All of our experiments and guides are licensed under the Creative Commons Attribution Share-Alike 4.0 Unported License. Feel free to remix and reuse our work. But please, share the love and give us attribution for our hard work!

To view a copy of this license visit [this link](http://creativecommons.org/licenses/by-sa/4.0/), or write: Creative Commons, 171 Second Street, Suite 300, San Francisco, CA 94105, USA.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft683&name=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft683 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft683&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft683&t=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft683&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F8%2F3%2Flogo.jpg&description=Getting+Started+with+MicroPython+and+the+SparkFun+Inventor%27s+Kit+for+micro%3Abit "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/all) [Next Page →\
[Introduction to MicroPython]](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/introduction-to-micropython)

← Previous Page

[**Pages**] [Introduction to the SparkFun Inventor\'s Kit for micro:bit for MicroPython](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/introduction-to-the-sparkfun-inventors-kit-for-microbit-for-micropython) [Introduction to MicroPython](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/introduction-to-micropython) [Experiment 0: Hello, micro:bit!](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-0-hello-microbit) [Experiment 1: Blinking an LED](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-1-blinking-an-led) [Experiment 2: Reading a Potentiometer](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-2-) [Experiment 3: Reading a Photoresistor](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-3-reading-a-photoresistor) [Experiment 4: Driving an RGB LED](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-4-driving-an-rgb-led) [Experiment 5: Reading an SPDT Switch](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-5-reading-an-spdt-switch) [Experiment 6: Reading a Button Press](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-6-reading-a-button-press) [Experiment 7: Reading the Temperature Sensor](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-7-reading-the-temperature-sensor) [Experiment 8: Using a Servo Motor](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-8-using-a-servo-motor) [Experiment 9: Using a Buzzer](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-9-using-a-buzzer) [Experiment 10: Using the Accelerometer](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-10-using-the-accelerometer-) [Experiment 11: Using the Compass (Magnetometer)](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/experiment-11-using-the-compass-magnetometer) [Resources and Going Further](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/resources-and-going-further)

[Comments [3]](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/discuss) [Single Page](https://learn.sparkfun.com/tutorials/getting-started-with-micropython-and-the-sparkfun-inventors-kit-for-microbit/all) [Print]

- **Tags**
- - [Audio](https://learn.sparkfun.com/tutorials/tags/audio)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [micropython](https://learn.sparkfun.com/tutorials/tags/micropython)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]