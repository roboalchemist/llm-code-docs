# Source: https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview

## Introduction

The [MicroView](https://www.sparkfun.com/products/12923). Such a cool concept! An Arduino, with a built-in display, fully enclosed in a beautiful, ergonomic case. Use it to create small video games, wearable electronics, or to simply explore electronics and programming. But as cool as the MicroView is, if you can\'t reprogram it, it\'s not much more than an annoyingly repetitive demo.

[![MicroView Product Shot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/MV-product-ISO.jpg)](https://www.sparkfun.com/products/12923)

In August 2014, [we (unknowingly at the time) sent out nearly 2000 MicroViews without bootloaders](https://www.sparkfun.com/news/1575). Void of a bootloader, the MicroView is essentially un-programmable \-- that exciting Arduino platform becomes a glorified paperweight.

A **bootloader** is a small piece of firmware, living inside a microcontroller\'s memory, which can write to the remaining program memory of that microcontroller. Bootloaders usually allow for easier, less expensive means for updating the program memory on a processor. Instead of specialized tools to program the device, more generic, commonly available components can be used.

One of the reasons Arduinos, like the MicroView, are so popular is because they all have a **serial bootloader** built into them. Instead of using an external piece of specialized hardware -- in this case an **AVR ISP (in-system programmer)** -- to program the processor, a more commonly available serial port can be used. In the case of the MicroView, that\'s the [MicroView USB Programmer](https://www.sparkfun.com/products/12924), which converts the ubiquitously available USB to serial.

If you\'ve received a defective unit, first of all: we\'re so sorry! We\'re shipping replacements as fast as we can build them, you\'ll be getting one soon. In the mean time, this is a great opportunity to learn a new skill.

In this tutorial, we\'ll walk you through every step involved in loading a bootloader onto the MicroView: [disassembling the enclosure](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#carefully-opening-the-case), [wiring up an assortment of programmers](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#wiring-the-programmer) in a [variety of ways](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#wiring-the-microview), [programming the bootloader](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#burning-the-bootloader), and [testing it out](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#testing-and-closing).

## Gathering the Tools

Before you get going, there are a few tools you\'ll need to gather: something to pry open the MicroView, a method for connecting to the small vias, and an AVR programmer. There are many options for each of those tools, we\'ll list a few in the sections below.

For those short on one tool or another, we\'ve created the [MicroView Bootloading Kit](https://www.sparkfun.com/products/13088), which includes everything you\'ll need to follow along with this tutorial.

[![MicroView Bootloading Kit](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/microview_bootloading_kit.jpg)](https://www.sparkfun.com/products/13088)

The kit is an especially great deal if you need an AVR programmer \-- the price for the kit (which includes a knife, jumpers, and resistors) is the same as the programmer itself.

### An Opener

A thin, flat, rigid-ish tool is required to separate the MicroView\'s shell from the lens covering it. This can be a [spudger](http://en.wikipedia.org/wiki/Spudger), [hobby knife](https://www.sparkfun.com/products/9200), or a thin flathead screwdriver (the smallest bit in our [Pocket Screwdriver](https://www.sparkfun.com/products/12891) works).\

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

[![Hobby Knife](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/6/09200-Hobby_Knife-01.jpg)](https://www.sparkfun.com/hobby-knife.html)

### [Hobby Knife](https://www.sparkfun.com/hobby-knife.html) 

[ TOL-09200 ]

It\'s like an Xacto knife, only better. We use these extensively when working with PCBs. These small knives work well for cutt...

[ [\$3.75] ]

The knife has a lower potential for scratching your MicroView\'s shell, but the tip will also probably break on your first pry attempt. Use a more veteran, dulled blade if you can. Or, better yet, sacrifice a blade and break the sharp end of the tip off.

### []A Programmer

There are a multitude of tools that can perform the task of reprogramming a MicroView over ISP. There are boards built for the task, like the [Tiny AVR Programmer](https://www.sparkfun.com/products/11801), [STK500 USB Programmer](https://www.sparkfun.com/products/8702), or the [AVR Pocket Programmer](https://www.sparkfun.com/products/9825).\

[![Tiny AVR Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/8/1/1/1/11801-01.jpg)](https://www.sparkfun.com/tiny-avr-programmer.html)

### [Tiny AVR Programmer](https://www.sparkfun.com/tiny-avr-programmer.html) 

[ PGM-11801 ]

The ATtiny45 and 85 are a couple of really cool little MCUs but did you know you can program them in Arduino? That\'s right, n...

[ [\$18.95] ]

[![Pocket AVR Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/3/8/8/5/09825-01b.jpg)](https://www.sparkfun.com/pocket-avr-programmer.html)

### [Pocket AVR Programmer](https://www.sparkfun.com/pocket-avr-programmer.html) 

[ PGM-09825 ]

This new version uses an SMD 5x2 header. This is a simple to use USB AVR programmer. It is low cost, easy to use, works great...

[ [\$19.95] ]

[![STK500 Compatible USB Programmer](https://cdn.sparkfun.com/r/140-140/assets/parts/1/8/7/9/08702-03-L.jpg)](https://www.sparkfun.com/products/8702)

### [STK500 Compatible USB Programmer](https://www.sparkfun.com/products/8702) 

[ PGM-08702 ]

AVR-ISP500 is a fast and reliable USB AVR programmer, and works directly with AVR Studio. It is recognized as a STK500 progra...

**Retired**

Even if you don\'t have a dedicated AVR programmer, you might have a programmer and not even know it! Most [Arduino\'s](https://www.sparkfun.com/categories/tags/arduino) can be programmed to replicate an AVR Programmer. If you have an [Arduino Uno](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10915), or, really, any ATmega328P-based Arduino, you\'re already good-to-go.\

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Arduino Pro 328 - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/0/4/4/10915-01.jpg)](https://www.sparkfun.com/arduino-pro-328-5v-16mhz.html)

### [Arduino Pro 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-328-5v-16mhz.html) 

[ DEV-10915 ]

It\'s blue! It\'s skinny! It\'s the Arduino Pro! SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the...

**Retired**

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

By loading the [ArduinoISP sketch](http://arduino.cc/en/Tutorial/ArduinoISP) onto your Arduino, it\'ll transform into a USB AVR programmer. Arduinos programming Arduinos: madness!

### Jumper Wires

To connect between your Programmer and the MicroView, you\'ll need six, individual male-to-male jumper wires. Most M/M jumpers will do, including the [standard](https://www.sparkfun.com/products/11026) or [premium](https://www.sparkfun.com/products/8431) sets.\

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Jumper Wires Premium 6\" M/M Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/1/JumperWire-Male-01-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html)

### [Jumper Wires Premium 6\" M/M Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-10.html) 

[ PRT-08431 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumpers with male connectors on both ends. Use these to jumper fro...

[ [\$5.25] ]

You can even use [solid-core wire](https://www.sparkfun.com/products/11367) if you\'d like.

### The Arduino IDE

There are a handful of software tools that can be used to reprogram AVRs. The easiest program, and the one we recommend, is the good ol\' [Arduino IDE](http://arduino.cc/en/Main/Software). Arduino has a built-in tool, which allows you to **burn a bootloader** into any of its many boards, it makes programming a bootloader as easy as two clicks.

[![Burn bootlaoder in Arduino](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/burn_bootloader.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/burn_bootloader.png)

### (Optional, Recommended) Solder Tools or Thin-Gauge PTH Resistors

The hardest part of this whole process is connecting your programmer to three of the MicroView\'s tiny ISP pins. Due to space restrictions they\'re broken out to a trio of small, exposed vias.

[![MV exposed vias](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/2/9/2/07-display_lifted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/07-display_lifted.jpg)

*After lifting the cover off your MicroView, you\'ll need to connect to those vias labeled \"11\", \"12\", and \"13\".*

If you apply enough steady pressure, you can complete those three connections without soldering or connecting anything else. Be warned, though, that it\'ll take a few tries to get right; if you\'re low on patience, frustration might brew.

If you\'d like to avoid soldering to your MicroView, one trick is to plug through-hole, 0Ω (or, at least, very low resistance) resistors into the MicroView\'s three ISP vias. The trick is finding resistors with thin enough leads. The 0Ω resistors on our [Resistor Kit](https://www.sparkfun.com/products/10969) work perfectly for this task, but watch out, many other resistors \-- especially those rated for ¼W and above \-- have too-thick leads.

(There are all sorts of other, clever ways to connect into those vias. For example, you can [poke them with sewing needles](http://mythopoeic.org/microview-lazy-fix/). You just need something with a diameter under about 0.015\" that conducts electricity.)

Instead of jamming resistors into the vias, if you have soldering tools handy, you can make the programming process a lot smoother by temporarily [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a jumper wire to the test pin \-- creating a reliable electrical connection between MicroView and programmer. A [simple iron](https://www.sparkfun.com/products/9507), and some [solder](https://www.sparkfun.com/products/9163) is all you should need.

\

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Solder Wick #2 Yellow - No Clean](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/5/09327-Chipquik-Feature.jpg)](https://www.sparkfun.com/solder-wick-2-5ft-generic.html)

### [Solder Wick #2 Yellow - No Clean](https://www.sparkfun.com/solder-wick-2-5ft-generic.html) 

[ TOL-09327 ]

Solder wick, coffee, and paper towels keep SparkFun running. You can steal someone\'s diagonal cutters for a minute, but you\'d...

[ [\$2.95] ]

[![Soldering Iron - 30W (EU, 230VAC)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/7/3/0/09507-01.jpg)](https://www.sparkfun.com/products/11650)

### [Soldering Iron - 30W (EU, 230VAC)](https://www.sparkfun.com/products/11650) 

[ TOL-11650 ]

This is a very simple fixed temp, quick heating, 30W 230VAC soldering iron. We really enjoy using the more expensive irons, b...

**Retired**

[Solder wick](https://www.sparkfun.com/products/9327) might help when you get to disconnecting the wires and cleaning up.

## Identifying a Defective MV

Before we trip into the rabbit hole, we should at least make sure your MicroView is *actually* missing its bootloader. If you haven\'t already, follow along with the [MicroView Getting Started Guide](http://learn.microview.io/intro/getting-started.html). That will walk you through driver installation, and plugging in the MicroView.

### Testing With Arduino

Alternatively, you can try uploading a sketch in the Arduino IDE. Load up any of the examples included with the [MicroView Library](https://github.com/geekammo/MicroView-Arduino-Library). Double-check that your **Serial Port** is set correctly, and the **Board** is set to \"Arduino Uno\". Then click Upload.

During the upload, you should see the yellow \"RX\" LED on your MicroView USB Programmer blink. If all you see is three quick blinks, that\'s an early warning sign that the bootloader is missing. After waiting a few more seconds, an error should be produced in the Arduino IDE\'s console. If you get something like this:

[![Upload error console notification](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/error_console.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/error_console.png)

\...or any of these errors:

    avrdude: stk500_recv(): programmer is not responding

    avrdude: ser_recv(): programmer is not responding

    avrdude: stk500_getsync(): not in sync: resp=0x00

    avrdude: stk500_getsync() attempt 10 of 10: not in sync: resp=0x00

\...your MicroView probably doesn\'t have a bootloader. Time for surgery.

## (Carefully) Opening the Case

The AVR ISP programming interface requires six pins: VCC, GND, RST, MOSI, MISO, and SCK. VCC (power), GND (ground), and RST (reset) are all broken somewhere along the MicroView\'s readily available pair of 8-pin headers. Unfortunately, the three SPI signals are not broken out to the headers, they\'re tucked away, inside the enclosure, broken out to three unmasked vias. To expose these pins, you\'ll have to remove the Microview\'s covering lens and lift the display up.

Grab your spudger, [hobby knife](https://www.sparkfun.com/products/9200) or [small, flathead screwdriver](https://www.sparkfun.com/products/12891). And find a flat, steady surface to do the deed.

[![The opener and the MicroView](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/01-tools.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/01-tools.jpg)

If you\'re using a sharp-edged hobby knife, you may want to grab a pair of pliers and snap off a small chunk of the tip to get a more blunt, flat edge.

[![Knife edge snapped blunt](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/02-knife_edge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/02-knife_edge.jpg)

The lens cover is held in place by two securing notches on the left and right sides of the enclosure. Try to expose as much of a gap on one side as you can, by sliding the lens to either the left or right. You may be able to see one of the securing notches.

[![MV retaining notch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/03-MV_notch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/03-MV_notch.jpg)

Insert your opener somewhere between that notch and the bottom of the cover. You should be able to push it in about 2mm, before a beveled edge inside the enclosure gets in the way. Be gentle, but try to push in as far as you can to get more leverage.

[![Inserting the knife](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/04_knife-insert.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/04_knife-insert.jpg)

Then pry up the cover by tilting the opener towards the outside of the MicroView.

[![Prying the top off](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/05-knife_lever.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/05-knife_lever.jpg)

Once the edge of the screen has popped off, grab it with your fingers and pull it off.

[![Cover removed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/06-cover_removed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/06-cover_removed.jpg)

The exposed pins for MISO, MOSI, and SCK are just under the display. To access them, *very carefully* pry the OLED up. The OLED is connected to the PCB via a thin, black connector; it\'s fragile, take great care not to place any extra stress on it.

[![Display lifted off PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/07-display_lifted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/07-display_lifted.jpg)

Those three, small unmasked vias, labeled \"11\", \"12\", and \"13\", are what we\'re after!

## Wiring the Programmer

As evidenced by our list of devices in the [\"Programmer\"](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#programmer) part of the \"Gathering the Tools\" section, there is no shortage of boards that can program a bootloader. In this section we\'ll demonstrate how to hook up a few of the most common programming tools.

For each, we\'ll have to wire up six signals: VCC, GND, Reset, MOSI, MISO, and SCK. We\'ll use the following color coded wires for the six signals:

  Signal Name   MicroView Pin   Wire Color
  ------------- --------------- ------------
  VCC           5V              Red
  GND           GND             Black
  Reset         RST             Orange
  MOSI          11              Green
  MISO          12              Blue
  SCK           13              Yellow

\

We will repeat the hookup for each programmer, click below if you want to skip to a particular device:

- An [AVR Pocket Programmer](#2x3ISP) (or any dedicated AVR Programmer with a 2x3 ISP cable)
- A [Tiny AVR Programmer](#tinyISP)
- An [Arduino equipped with the ArduinoISP sketch](#arduinoISP).

### []Connecting to an AVR ISP 2x3 Cable

Before connecting the programmer to your MicroView, you may need to install drivers. If you\'re using the [AVR Pocket Programmer](https://www.sparkfun.com/products/9825), follow along with our [Pocket AVR Programmer Hookup Guide](https://learn.sparkfun.com/tutorials/pocket-avr-programmer-hookup-guide) for guidance.

Most AVR development boards, like the Arduino Uno, break out a 2x3 header specifically geared towards (re)programming via ISP. This header matches up to a standardized 2x3 ISP footprint (or a larger 2x5 variant) with the following pinout:

[![AVR ISP Pinouts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/isp-pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/isp-pinout.png)

Those pinouts are a top-view of the connector as it would be on the PCB. If you\'re plugging wires into the cable, you need to flip that image over the horizontal. Here\'s how those signals are routed on the cable connector:

[![How to wire the 2x3 connector](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/2x3-labeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/2x3-labeled.jpg)

Note that the notch in the cable indicates the pin-1 side of the footprint.

Unfortunately, the MicroView PCB wasn\'t big enough to fit the whole standardized ISP header, but, once you\'ve removed the cover, all of the pins you need are exposed in one way or another.

Plug your six jumper cables straight into the 2x3 connector. Use color-coded wires if you can. Here\'s where each ISP pin goes (note the notch, indicating the pin 1 side):

[![2x3 cable wired](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/09-2x3_wired.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/09-2x3_wired.jpg)

Then skip to the [Wiring to the MicroView](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#wiring-the-microview) section to complete the wiring.

### []Connecting to the Tiny AVR Programmer

The [Tiny AVR Programmer](https://www.sparkfun.com/products/11460) is a tool built for programming [ATtiny85\'s](https://www.sparkfun.com/products/9378), but it\'s more multi-purpose than that! It can program any AVR. If you\'re approaching this task with the Tiny AVR Programmer, make sure you\'ve read through our [Tiny AVR Programmer Hookup Guide](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide) \-- at least through the driver installation section.

The Tiny AVR Programmer doesn\'t mate to a standard 2x3 connector, the pins we\'ll need are all broken out to both the 8-pin DIP socket and the two 4-pin machine-pin connectors. Here\'s what\'s what:

[![Tiny programmer pins labeled](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/tiny-programmer.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/tiny-programmer.png)

Insert your wires. Color code them if you can.

[![ATtiny Wired](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/10-tiny_wired.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/10-tiny_wired.jpg)

Then proceed to the [Wiring to the MicroView section](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#wiring-the-microview).

### []Connecting to an ArduinoISP

Just about any, old Arduino can be turned into an AVR ISP. All you need is the right sketch: [ArduinoISP](http://arduino.cc/en/Tutorial/ArduinoISP), which is included by default with the Arduino IDE. Open the sketch by going to **File** \> **Examples** \> **ArduinoISP**. Then upload it to your Arduino, which fortunately already has a bootloader!

[![Open Arduino ISP](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/arduinoISP_example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/arduinoISP_example.png)

The ArduinoISP sketch uses Arduino pins 10, 11, 12, and 13 as RST, MOSI, MISO, and SCK, respectively. If you\'re using an [Arduino Uno](https://www.sparkfun.com/products/11021), you may also need to **connect a [10µF capacitor](https://www.sparkfun.com/products/523) between the reset pin and ground**. Here\'s how it\'ll be wired up to the MicroView:

[![ArduinoISP fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/microview_fix-ArduinoISP_bb-3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/microview_fix-ArduinoISP_bb-3.png)

Note that the ArduinoISP sketch does provide for some simple debugging by assigning LEDs to pins 7, 8, and 9. They\'re completely optional, but can make tracking down errors a bit easier. An LED on pin 9 will indicate a \"heartbeat\", 8 will blink if there\'s an error, and pin 7 will indicate that programming is in process.

Use some color-coded jumpers to wire it up, like this:

[![Arduino wired](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/11-arduinoISP_wired.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/11-arduinoISP_wired.jpg)

Then proceed to the next section, to wire it up to the MicroView.

## Wiring the MicroView

You\'ve wired up to the programmer, that\'s (the easier) half of the wiring. Now to wire up the MicroView. To begin, plug your MicroView into the USB Programmer, then plug the Programmer into a breadboard.

[![MV plugged into breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/12-MV_breadboarded.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/12-MV_breadboarded.jpg)

The breadboard will be useful as both a wire tie-in point and as a steadying tool.

### Power and Reset

The VCC, GND, and RST pins are, fortunately, all broken out on the Microview.

[![VCC, GND and RST locations](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/mv-pin-locations.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/mv-pin-locations.jpg)

Wiring those to your programmer is as simple as plugging some wires into a breadboard.

[![RST, VCC and GND wired](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/13-rst_pwr_wired.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/13-rst_pwr_wired.jpg)

This is a good time to think about how you\'re going to power the MicroView as it\'s being programmed. Some programmers \-- including the ArduinoISP, Tiny AVR Programmer, and AVR Pocket Programmer \-- can power the MicroView by themselves. Other programmers (like more official Atmel AVR ISPs) require the MicroView be powered externally. If you need to externally power the MicroView, plug the USB Programmer into your computer. But, **if you\'re going to power the MicroView from your AVR programmer, leave your MicroView\'s USB Programmer unplugged**.

### Connecting to MOSI, MISO, and SCK (11, 12, and 13)

Now the hard part. We need to connect the three SPI lines as follows:

  Programmer Pin   MicroView Pin
  ---------------- ---------------
  MOSI (D11)       11
  MISO (D12)       12
  SCK (D13)        13

\

Having gone through this process more than a few times, here are three possible methods we\'ve gotten to work. Click to skip to the respective section:

- [Soldering wires to vias](#connect-by-solder) \-- With soldering tools and a careful hand, you can solder jumper wires directly to the vias. This is the most reliable method, but also requires the most tools \-- not recommended for a beginning solderer.
- [Inserting 0Ω Resistors](#connect-by-resistor) \-- If you have 0Ω \"jumper\" resistors (like those in our [Resistor Kit](https://www.sparkfun.com/products/10969)), and their legs are skinny enough, you can plug them into the MicroView\'s vias. This is a relatively reliable, temporary solution.
- [Holding wires in place](#connect-by-push) \-- Short of any other option, you can try holding all three wires in place, as you burn the bootloader. This method works, but requires some patience and steady hands.

#### []Soldering the Wires

If you have a soldering iron handy, we recommend connecting the jumper wires to the vias with a small dab of solder. If you\'re taking a soldering iron to your MV, you may want to lift the entire board out of the enclosure to avoid burning the edges. Press down on the MicroView\'s enclosure, using the table to push the header pins up, it\'ll take a steady amount of force to unseat the PCB from its retaining clips.

Apply a dab of solder to the vias.

[![making solder dabs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/14-solder_dabs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/14-solder_dabs.jpg)

Then heat the solder dab back up and fuse an end of the jumper wire to it. Repeat that process for each of the three vias.

[![soldering the wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/15-wires_soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/15-wires_soldered.jpg)

After the wire is soldered, take care to not to let it pull on the MicroView too hard. You\'ll risk lifting the via and its copper of the board entirely (then you\'ll be left to soldering to the ATmega328P\'s pins).

Plug those wires into the correct port of your programmer:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/programming-arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/programming-arduino.jpg)

Then [skip to the next section](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#burning-the-bootloader).

#### [][Connecting via 0Ω Resistors (Or Thin Solid Wires)](#connect-by-resistor)

If you\'re lacking for soldering tools, or just want to avoid altering your MicroView, see if you can grab three 0Ω (or at the very least *very small*, \<50Ω) resistors. Those included in our [Resistor Kit](https://www.sparkfun.com/products/10969) work perfectly. You may have to dig around to find a resistor with thin enough terminations, they\'ll need to be less than about 0.015\" to fit in the MicroView\'s vias.

Plug each of the resistors into a different via on the MicroView, then plug the other end of the resistor into a unique row on the breadboard.

[![making connections with resistors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/16-resistors_plugged.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/16-resistors_plugged.jpg)

*See, 0Ω resistors aren\'t useless!*

Then route each of the programmer\'s SPI pins to the appropriate row in the breadboard. You may need to just slightly bend the resistor at the point that it hits the via \-- just enough for it to make an electrical contact.

[![AVR Pocket programmer and resistor-ed MicroView](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/programming-pocket.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/programming-pocket.jpg)

We\'re teetering on the edge of reliability here, but this option is still worlds better than the next\...

#### []\"Push-Connecting\" the Wires

If you don\'t have either soldering tools or low-impedance resistors, you better have dexterity, a steady hand, and patience. You can \"poke\" each of the three jumper wires into their respective vias, creating *just enough* of an electrical connection. We really recommend asking a buddy to help you out here, because while one hand is busy holding the wires in place, the other will have to be on your computer mouse, clicking through menus.

Before actually pushing the wires into place, click over to the next page and get fully prepared to program your bootloader. Once your mouse cursor is hovering over \"Burn Bootloder\" in the Arduino IDE, then you can start fussing with push-connecting your jumper wires.

There are no real tricks to this. Begin by pushing a wire into pin 13. Once that\'s steady continue on to pin 12, holding both jumpers between thumb and forefinger. Finally add pin 11.

[![Holding wires in place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/17-wires_held.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/17-wires_held.jpg)

Then quickly start programming! You\'ll have to hold them in place for about 30 seconds.

## Burning the Bootloader

This section will cover two readily available software tools that can be used to interact with your AVR ISP to burn a bootloader onto your MicroView. Pick one that best suits your comfort level:

1.  [Arduino IDE](#burn-arduino) \-- If you have the Arduino IDE installed, this is an easy GUI-based way to program your bootloader.
2.  [AVRDUDE (Command Line Utility](#burn-avrdude) \-- AVRDUDE is a command line utility which can be invoked to program AVR\'s. This method is recommended only for advanced users. Unknown factors, like file locations and environment variables, come into play here, so you may have to slightly alter our example commands to get them to work on your computer.

The Arduino method won\'t give you instant gratification after burning the bootloader. The MicroView Demo code isn\'t included with the bootloader, so you\'ll have to upload it separately, after burning the bootloader. With AVRDUDE you can pinpoint the HEX file you want to upload, so you can upload the combined bootloader/MicroView Demo file and instantly discover if your MicroView is back to 100%.

### [] Burning the Bootloader in the Arduino IDE

Open up Arduino, then go up to **Tools** \> **Programmer**. Select the programmer that matches what you\'re planning on using. For the programmers we\'ve discussed in this tutorial, that will either be USBTinyISP or Arduino as ISP.

[![Tools\>Programmer\>USBTinyISP or Arduino as ISP](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/programmer_select.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/programmer_select.png)

If you\'re using an Arduino as the ISP, make sure the **Serial Port** is set to that Arduino\'s port number. If you\'ve recently uploaded the ArduinoISP sketch to your Arduino, it\'s probably set correctly, but check!

Finally, make sure the board is correctly set. This will determine which bootloader gets programmed onto your MicroView. It should be set to **Arduino Uno**.

[![Tools\>Board\>Arduino Uno](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/board_select.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/board_select.png)

That\'s all for the settings. Now, make sure your programmer is correctly connected to your MicroView, and go to **Tools** \> **Burn Bootloader**, and enjoy the light show.

[![Tools\>Burn Bootloader](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/burn_bootloader.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/burn_bootloader.png)

The bootloader burn process usually takes around 30 seconds. If your holding the jumper wires in place, hold steady! After the bootloader has been programmed, you should see a surprisingly brief \"Done burning bootloader\" message above the console.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/bootloader_success.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/bootloader_success.png)

If you get an error, like `avrdude: initialization failed, rc=-1`, there\'s either an incorrect or missing connection. Double-check to make sure everything is connected correctly.

If you\'ve gotten good news, continue on to the [Testing and Closing section](https://learn.sparkfun.com/tutorials/installing-a-bootloader-on-the-microview#testing-and-closing). The MicroView screen will be blank; during bootloader upload, the program that was on the MicroView was erased, so, for now, the MicroView doesn\'t have any sketches on it.

### [] Programming via AVRDUDE and Command Line

Behind the scenes, Arduino uses [AVRDUDE](http://www.nongnu.org/avrdude/) to communicate with and command your programmer. Instead of using Arduino as a front end, you can invoke AVRDUDE from the command line. You\'ll need to have AVRDUDE installed or existing on your computer somewhere ([download AVRDUDE here](http://download.savannah.gnu.org/releases/avrdude/)).

You\'ll also need the (working) MicroView HEX file, [click here to download the MicroView bootloader hex file](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/MicroView_combined_8-19-14.hex), \"MicroView_combined_8-19-14.hex\". To make the example commands easier, we\'ll assume the hex file is in the same location as AVRDUDE.

If you have an **AVR Pocket Programmer** or **Tiny AVR Programmer**, a command like this will upload the bootloader to your Arduino.

    avrdude -c usbtiny -p atmega328p -U flash:w:MicroView_combined_8-19-14.hex -U lock:w:0x0F:m

If you\'re using an **Arduino as an ISP**, use a command like below. You\'ll need to put your Arduino\'s COM port \# in place of our placeholders (`COMN` for Windows or `/dev/tty.usbmodemNNNN` for Mac/Unix):

    Windows: avrdude -p atmega328p -c avrisp -P COMN -b 19200 -v -e -U flash:w:MicroView_combined_8-19-14.hex -U lock:w:0x0F:m

    Mac: avrdude -p atmega328p -c avrisp -P /dev/tty.usbmodemNNNN -b 19200 -v -e -U flash:w:MicroView_combined_8-19-14.hex -U lock:w:0x0F:m

After sending the command, your terminal will be swamped with writes, reads, and other messages until the entire bootloader has been programmed.

[![Example command line respons](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/avrdude_example_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/avrdude_example_2.png)

After AVRDUDE says it\'s done, the bootloader should be programmed. As an added bonus, this HEX file includes the MicroView demo \-- once it\'s been programmed the display should light up and start cycling through patterns.

## Testing and Closing

We\'re just about back to square one. Before closing the MicroView back up, it\'d be best to test it out and make sure it\'s bootloader-programmable.

Disconnect your AVR programmer from the MicroView, plug the MicroView into your the MicroView USB Programmer (if it wasn\'t already), and plug your programmer into the computer.

Then repeat the Arduino programming process from the \"Identifying\" section. In the Arduino IDE, load up an example from the [MicroView library](https://github.com/geekammo/MicroView-Arduino-Library), make sure the Serial Port and Board (\"Arduino Uno\") are set correctly in the Arduino IDE, and program away!

[![Done Uploading!](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/done_uploading.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/done_uploading.png)

If you\'re greeted with a \"Done uploading.\" message above the console, you\'ve succeeded in reprogramming your MicroView! The MicroView Demo you\'ve loaded should also start running. Program it again to make extra sure\...

### Closing the MicroView

If you soldered to any of the MicroView\'s vias, you\'ll first need to remove those jumpers from the board. Heat each joint up, and remove the wire one-by-one.

If you removed the MicroView PCB from the enclosure, put it back in. The MicroView PCB is keyed, so it should only go in one way, make sure the pairs of notches on the top and bottom of the board match up to the notches in the enclosure. **Don\'t press down on the screen**, lift it up and push the MicroView PCB into the enclosure. You should hear a snap as it clicks in, under two small clips on each side of the enclosure, which secure the PCB in place.

Next, fold the OLED back on top of the PCB. There are guides in the enclosure to hold the display in place. It should be seated just about flush with the enclosure notches on the sides and top of the display.

[![Replacing the OLED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/18-display_placed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/18-display_placed.jpg)

Before closing it up, gently **wipe off the OLED** to remove any fingerprints. You may also need to wipe off the bottom side of the enclosure lens as well.

Finally, close it up! The tabs of the enclosure are offset from the middle of the edge, they\'re closer to the inner-facing side of the lens. Slot in one tab of the enclosure lens, then press down on the opposite side to snap it in.

[![Closing the MicroView](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/19-closing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/19-closing.jpg)

No one will ever know the difference!

[![A disassembled MicroView put back together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/2/post-fix.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/2/post-fix.jpg)