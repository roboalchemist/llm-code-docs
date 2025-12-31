# Source: https://learn.sparkfun.com/tutorials/gatorcolor-protosnap-hookup-guide

## Introduction

The [gator:color](https://www.sparkfun.com/products/14890) is one of a series of gator-clippable boards called gator:boards that SparkFun has created to interface with the [micro:bit](https://www.sparkfun.com/products/14208) and [gator:bit v2](https://www.sparkfun.com/products/15162) expansion for micro:bit. The gator:color has a smattering of a different color LEDs that can be used either in place or broken away from the main board. In this hookup guide we\'ll go over how to light up our LEDs, both by simply turning them on and also by dimming them using a process called [Pulse Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation).

[![SparkFun gator:color ProtoSnap](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/7/1/COM-14890-1.jpg)](https://www.sparkfun.com/sparkfun-gator-color-protosnap.html)

### [SparkFun gator:color ProtoSnap](https://www.sparkfun.com/sparkfun-gator-color-protosnap.html) 

[ COM-14890 ]

The gator:color ProtoSnap is perfect if you want to add a low-profile glowing component to your project.

**Retired**

### Required Materials

For this activity, you\'ll of course need a micro:bit. You\'ll also need some alligator clips to connect everything together, and a micro usb cable to program your micro:bit. All of these things are shown below, so grab them if you haven\'t already. You can go ahead and grab a gator:bit v2 as well to create some more robust projects, but you\'ll be able to get along fine with just a micro:bit.

[![Alligator Test Leads - Multicolored (10 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/1/9/12978-01.jpg)](https://www.sparkfun.com/alligator-test-leads-multicolored-10-pack.html)

### [Alligator Test Leads - Multicolored (10 Pack)](https://www.sparkfun.com/alligator-test-leads-multicolored-10-pack.html) 

[ PRT-12978 ]

Alligator clips (or Crocodile clips, if you prefer) are likely to be the most useful thing on your workbench besides the work...

[ [\$5.25] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

[![micro:bit Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/4/8/13988-01.jpg)](https://www.sparkfun.com/products/14208)

### [micro:bit Board](https://www.sparkfun.com/products/14208) 

[ DEV-14208 ]

The BBC micro:bit is a pocket-sized computer that lets you get creative with digital technology.

**Retired**

[![SparkFun gator:bit v2.0 - micro:bit Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/5/1/15162-SparkFun_Gator-bit-03a.jpg)](https://www.sparkfun.com/products/15162)

### [SparkFun gator:bit v2.0 - micro:bit Carrier Board](https://www.sparkfun.com/products/15162) 

[ DEV-15162 ]

The SparkFun gator:bit is an all-in-one "carrier" board for your micro:bit that provides you with a fully functional deve...

**Retired**

### Suggested Reading

If this is your first time using a gator:bit, check out the [SparkFun gator:bit v2 Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-gatorbit-v2-hookup-guide).

[](https://learn.sparkfun.com/tutorials/sparkfun-gatorbit-v2-hookup-guide)

### SparkFun gator:bit v2 Hookup Guide 

January 31, 2019

The gator:bit v2 is a breakout board for the BBC micro:bit. The gator:bit exposes almost every pin on the micro:bit to clippable pad with circuit protection. It also has as built-in addressable LEDs and a built-in buzzer.

Also, if you\'re starting out with electronics and aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

We can see electricity in action on our computers, lighting our houses, as lightning strikes in thunderstorms, but what is it? This is not an easy question, but this tutorial will shed some light on it!

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

## Hardware Overview

The gator:color is perfect if you want to add a low-profile glowing component to your project. The gator:color contains 6 monochrome LEDs, which means that each light only emits one color. On board there are two white LEDs, along with one each of red, green, blue, and yellow LEDs. The board has power tabs broken out on the edges so that the board doesn\'t have to be broken apart to light up the LEDs.

### Powering your LEDs

The LEDs can be powered through either of two ways. The first simply turns the LEDs on, and is done by clipping the `-` side of the LED to ground on the micro:bit and connecting the `+` to 3V on the micro:bit. The other way to control these LEDs would be to connect the gator:color\'s `Power` to pins `0`, `1` or `2` on the micro:bit (with `Ground` connecting to `Ground`). This method gives you more control over your LEDs, allowing you to turn the LEDs on and off with the micro:bit, as well as change the brightness level using [Pulse width modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation).

[![Power Tabs](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/2/1/gatorcolor1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gatorcolor1.png)

*Power Tabs*

If and when you choose to incorporate your gator:color LEDs into a project, there is also a breakout power strip at the top of the board that you can use.

[![Power Rail](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/8/2/1/gator_bit_powerRail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gator_bit_powerRail.jpg)

*Power Strip*

### Breaking Apart Your Board

Each of the LEDs can be broken away from the board to be lit individually. To do so, twist the LED board gently from side to side until it pops out. The connection points are highlighted in the image below.

[![break points for gator:color LED tabs](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gator_bit_breakPoint.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gator_bit_breakPoint.jpg)

*Break points for gator:color LED tabs*

The Power Strip breaks out in a similar manner as the LED boards. Break points are highlighted below.

[![break points for gator:color power strip](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gator_bit_breakPoint_PowerRail.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/gator_bit_breakPoint_PowerRail.jpg)

*Break points for gator:color power strip*

## Hardware Assembly

Let\'s start by simply turning the LEDs on. Using your alligator clips, connect the `-` side of the LED to ground on the micro:bit and connect the `+` to 3.3V on the micro:bit. You should see all of the gator:color\'s LEDs light up. This type of setup is shown in the photo below.

[![Normal Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/1/3R8A9385.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/3R8A9385.JPG)

*Click on the image for a closer look*

If you want to dim the LED or control it with the micro:bit, you can connect the `+` on the LED to any of pins `0`, `1` or `2`. LEDs are either on or off, with no brightness in between, so we control brightness by turning the light on and off very fast in a process known as [PWM](https://learn.sparkfun.com/tutorials/pulse-width-modulation). Connect your pins as you see in the image below and we\'ll go over the code necessary to dim your LEDs in the next section.

[![Dimming Connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/2/1/2018-10-18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/1/2018-10-18.jpg)

*Click on the image for a closer look*

⚡**Using with the gator:bit** If you are using the [gator:bit v1](https://www.sparkfun.com/products/14484) (with the power switches and JST connector), keep in mind that you\'ll have to use pins P15, P14 or P13 to drive your LEDs, as the protection circuitry on the rest of the gator:bit pins does not create a high enough voltage to drive some colors of LED.

## Using MakeCode

As you\'ve seen, it\'s pretty simple to get your LEDs to simply light up; just connect power to power and ground to ground. However, if you want to do some fancy dimming or flashing effects, you\'ll need to upload some code to your micro:bit.

If you\'ve never used MakeCode before, refer to the *Using MakeCode* section of our [Getting Started with the Micro:Bit](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit#using-makecode).

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

September 2, 2021

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

Dimming LEDs is done using [Pulse Width Modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation). To use PWM in MakeCode, go to `Advanced`-\>`Pins` and select the **analog write** block, shown below.

[![Analog Write Block](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/9/analogwrite.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/1/9/analogwrite.PNG)

*Analog Write Block*

The analog write block defaults to a value of 1023, or 100%. If you wanted to turn the light down to 50% brightness, you\'d plug a value of 511 into your analog write function. Of course, you also want to make sure that whichever pin is selected in the MakeCode block is the pin that is clipped to the `+` pin on the LEDs. This can be done with any of the LEDs to create patterns with different brightnesses or even flashing LEDs.

### Example: LED Pulse

The following example will gradually turn the LEDs up to full brightness, then gradually go back down. This will fade the LED\'s on and off. To do this, we write the value `LightValue` (Which we initialize to 0 in our `on start` function) to our analog pin **P0** (3.3V from the LED\'s should be connected to this pin). We then add `lightStep` (which we set to 5 in our `on start` function) to `LightValue`, which changes the brightness by a tiny amount. Once `LightValue` reaches its maximum (1023) we multiply `lightStep` by **-1**, changing the value of `lightStep` to **-5**. This means that when we add `lightStep` to `LightValue`, `LightValue` will decrease. We do the same thing (multiply by **-1**) when `LightValue` reaches 0 to flip the direction around again. Finally, we add a delay of our choosing from `Advanced`-\>`Control` in to slow our fade down a little bit. The whole program is shown below.

*Pulsing LED Code*