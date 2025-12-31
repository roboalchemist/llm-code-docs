# Source: https://learn.sparkfun.com/tutorials/using-eagle-schematic

## Introduction

PCB design in EAGLE is a two-step process. First you design your schematic, then you lay out a PCB based on that schematic. EAGLE\'s board and schematic editors work hand-in-hand. A well-designed schematic is critical to the overall PCB design process. It will help you catch errors before the board is fabricated, and it\'ll help you debug a board when something doesn\'t work.

This tutorial is the first of a two-part *Using EAGLE* series, and it\'s devoted entirely to the schematic-designing side of EAGLE. In part 2, [Using EAGLE: Board Layout](https://learn.sparkfun.com/tutorials/using-eagle-board-layout), we\'ll use the schematic designed in this tutorial as the basis for our example board layout.

[![Schematic and board layout from Using EAGLE tutorials](https://cdn.sparkfun.com/r/600-600/assets/7/7/8/e/b/52127573757b7f8a3e8b456c.png)](https://cdn.sparkfun.com/assets/7/7/8/e/b/52127573757b7f8a3e8b456c.png)

### Suggested Reading

If you\'d like to follow along with this tutorial, make sure you\'ve installed and setup the EAGLE software. Our [How to Install and Setup EAGLE](https://learn.sparkfun.com/tutorials/how-to-install-and-setup-eagle) tutorial goes over this process step-by-step, and it also covers the basics of what EAGLE is and what makes it great. It also covers how to download and install the **SparkFun EAGLE libraries** we\'ll be using in this tutorial. Definitely read through that tutorial before you continue on.

We\'d also recommend you read and understand the concepts behind these tutorials:

- [How to Read a Schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic)
- [PCB Basics](https://learn.sparkfun.com/tutorials/pcb-basics)

## Create a Project

We\'ll start by making a new **project folder** for our design. In the control panel, under the \"Projects\" tree, right click on the directory where you want the project to live (by default EAGLE creates an \"eagle\" directory in your home folder), and select **\"New Project\"**.

[![How to create a project folder](https://cdn.sparkfun.com/assets/8/0/3/2/4/51f82d95757b7f9a1c923eb3.png)](https://cdn.sparkfun.com/assets/8/0/3/2/4/51f82d95757b7f9a1c923eb3.png)

Give the newly created, red project folder a descriptive name. How about \"Bare Bones Arduino\".

[![Project folder created](https://cdn.sparkfun.com/assets/b/d/6/e/c/51f82f5b757b7fb61cad2df8.png)](https://cdn.sparkfun.com/assets/b/d/6/e/c/51f82f5b757b7fb61cad2df8.png)

Project folders are like any regular file system folder, except they contain a file named \"eagle.epf\". The EPF file links your schematic and board design together, and also stores any settings you may have set especially for the project.

### Create a Schematic

The project folder will house both our schematic and board design files (and eventually our gerber files too). To begin the design process, we need to lay out a schematic.

To add a schematic to a project folder, right-click the folder, hover over **\"New\"** and select **\"Schematic\"**.

[![Creating a new schematic](https://cdn.sparkfun.com/assets/0/3/7/6/9/51f833f8757b7f371c50b50e.png)](https://cdn.sparkfun.com/assets/0/3/7/6/9/51f833f8757b7f371c50b50e.png)

A new, blank window should immediately pop up. Welcome to the schematic editor!

## Adding Parts to a Schematic

Schematic design is a two step process. First you have to add all of the parts to the schematic sheet, then those parts need to be wired together. You can intermix the steps \-- add a few parts, wire a few parts, then add some more \-- but since we already have a [reference design](https://cdn.sparkfun.com/assets/6/e/4/f/4/52127868757b7f30438b4567.pdf) we\'ll just add everything in one swoop.

### Using the ADD Tool

The ADD tool \-- ![](https://cdn.sparkfun.com/assets/3/1/b/0/7/5203cfa5757b7fef1a36c04a.png) (on the left toolbar, or under the *Edit* menu) \-- is what you\'ll use to place every single component on the schematic. The ADD tool opens up a library navigator, where you can expand specific libraries and look at the parts it holds. With a part selected on the left side, the view on the right half should update to show both the schematic symbol of the part and its package.

[![An example of navigating the ADD tool](https://cdn.sparkfun.com/r/600-600/assets/b/2/1/b/f/5203d359757b7f8e1e389650.png)](https://cdn.sparkfun.com/assets/b/2/1/b/f/5203d359757b7f8e1e389650.png)

The ADD tool also has **search functionality** \-- very helpful when you have to navigate through dozens of libraries to find a part. The search is very literal, so don\'t misspell stuff! You can add **wildcards** to your search by placing an asterisk (\*) before and/or after your search term. For example if you search for *atmega328* you should find a single part/package combo in the SparkFun-DigitalIC library, but if you search *\*atmega328\** (note asterisks before and after), you\'ll discover two more versions of the IC (because they\'re actually named \"ATMEGA328*P*\"). You\'ll probably want to get accustomed to always adding an asterisk before and after your search term.

[![Searching the ADD tool. Wildcards!](https://cdn.sparkfun.com/assets/9/3/c/f/f/5203d4b5757b7f227ced6884.png)](https://cdn.sparkfun.com/assets/9/3/c/f/f/5203d4b5757b7f227ced6884.png)

To actually add a part from a library either select the part you want and click \"OK\", or double-click your part.

### Step 1: Add a Frame

The frame isn\'t a critical component for what will be the final PCB layout, but it keeps your schematic looking clean and organized. The frame we want should be in the SparkFun-Aesthetics library, and it\'s named **FRAME-LETTER**. Find that by either searching or navigating and add it to your schematic.

[![Adding the frame](https://cdn.sparkfun.com/r/600-600/assets/4/9/a/3/d/52127b1e757b7f763c8b4569.png)](https://cdn.sparkfun.com/assets/4/9/a/3/d/52127b1e757b7f763c8b4569.png)

After selecting the part you want to add, it\'ll \"glow\" and start hovering around following your mouse cursor. To place the part, left-click (once!). Let\'s place the frame so its bottom-left corner runs right over our origin (the small dotted cross, in a static spot on the schematic).

[![Frame added](https://cdn.sparkfun.com/r/600-600/assets/d/8/a/b/8/5203d92d757b7fcb7a88858c.png)](https://cdn.sparkfun.com/assets/d/8/a/b/8/5203d92d757b7fcb7a88858c.png)

After placing a part, the add tool will assume you want to add another \-- a new frame should start following your cursor. To get out of the add-mode either hit escape (ESC) twice or just select a different tool.

### Step 2: Save (And Save Often)

Right now your schematic is an untitled temporary file living in your computer\'s ether. To save either go to *File \> Save*, or just click the blue floppy disk icon \-- ![](https://cdn.sparkfun.com/assets/e/a/f/1/b/5203da49757b7fc731edc867.png). Name your schematic something descriptive. How about \"**BareBonesArduino.sch**\" (SCH is the file format for all EAGLE schematics).

As a bonus, after saving, your frame\'s title should update accordingly (you may have to move around the screen, or go to *View \> Redraw*).

### Step 3: Adding the Power Input

Next we\'ll add four different parts all devoted to our voltage supply input. Use the add tool for these parts:

  Part Description                                                    Library               Part Name       Quantity
  ------------------------------------------------------------------- --------------------- --------------- ----------
  [5.5mm Barrel Jack (PTH)](https://www.sparkfun.com/products/119)    SparkFun-Connectors   POWER_JACKPTH   1
  [0.1µF Ceramic Capacitor](https://www.sparkfun.com/products/8375)   SparkFun-Capacitors   CAPPTH          1
  Voltage Supply Symbol                                               SparkFun-Aesthetics   VCC             1
  Ground Symbol                                                       SparkFun-Aesthetics   GND             2

\

All of these parts will go in the top-left of the schematic frame. Arranged like this:

[![Power circuitry placed](https://cdn.sparkfun.com/assets/a/6/f/7/a/5203e92e757b7fc17b3d34d1.png)](https://cdn.sparkfun.com/assets/a/6/f/7/a/5203e92e757b7fc17b3d34d1.png)

If you need to move parts around, use the MOVE tool \-- ![](https://cdn.sparkfun.com/assets/2/9/0/d/e/5203de36757b7f6b28e50ad6.png) (left toolbar or under the *Edit* menu). Left-click once on a part to pick it up (your mouse should be hovering over the part\'s red \"+\" origin). Then left click again when it\'s where it needs to be.

### Step 4: Microprocessor and Supporting Circuitry

Next we\'ll add the main component of the design \-- the ATmega328 microprocessor \-- as well as some components to support it. Here are the parts we\'ll add:

  Part Description                                                    Library               Exact Part Name    Quantity
  ------------------------------------------------------------------- --------------------- ------------------ ----------
  [ATmega328P (PTH)](https://www.sparkfun.com/products/9061)          SparkFun-DigitalIC    ATMEGA328P_PDIP    1
  [¼W Resistors](https://www.sparkfun.com/products/10969)             SparkFun-Resistors    RESISTORPTH-1/4W   4
  [5mm LEDs](https://www.sparkfun.com/products/9881)                  SparkFun-LED          LED5MM             3
  [0.1µF Ceramic Capacitor](https://www.sparkfun.com/products/8375)   SparkFun-Capacitors   CAPPTH             1
  Voltage Supply Symbol                                               SparkFun-Aesthetics   VCC                2
  Ground Symbol                                                       SparkFun-Aesthetics   GND                4

\

To rotate parts as your placing them, either select one of the four options on the rotate toolbar \-- ![](https://cdn.sparkfun.com/assets/c/e/0/3/2/5203e83d757b7fbf2b2b734d.png) \-- or right click before placing the part. Place your microcontroller in the center of the frame, then add the other parts around it like so:

[![Microcontroller circuit added](https://cdn.sparkfun.com/r/600-600/assets/b/4/0/c/b/5203f0ce757b7fbf2278b59a.png)](https://cdn.sparkfun.com/assets/b/4/0/c/b/5203f0ce757b7fbf2278b59a.png)

### Step 5: Adding the Connectors

Three connectors will finish off our design. One 8-pin connector to break out the analog pins, a 6-pin serial programming header, and a 2x3-pin ICSP programming header. Here are the three parts to add for this step:

  Part Description                  Library               Exact Part Name             Quantity
  --------------------------------- --------------------- --------------------------- ----------
  8-Pin 0.1\" Header                SparkFun-Connectors   M081X08                     1
  2x3 AVR Programming Header        SparkFun-Connectors   AVR_SPI_PRG_6PTH            1
  6-Pin Serial Programming Header   SparkFun-Connectors   ARDUINO_SERIAL_PROGRAMPTH   1
  Voltage Supply Symbol             SparkFun-Aesthetics   VCC                         2
  Ground Symbol                     SparkFun-Aesthetics   GND                         2

\

Finally! Here\'s what your schematic should look like with every part added:

[![Schematic with all parts added](https://cdn.sparkfun.com/r/600-600/assets/4/9/2/a/1/5203f34c757b7f5e26864cd8.png)](https://cdn.sparkfun.com/assets/4/9/2/a/1/5203f34c757b7f5e26864cd8.png)

Next we\'ll ~~wire~~ net them all together.

## Wiring Up the Schematic

With all of the parts added to our schematic, it\'s time to wire them together. There\'s one major caveat here before we start: even though we\'re *wiring* parts on the schematic, we not going to use the WIRE tool \-- ![](https://cdn.sparkfun.com/assets/c/e/4/4/7/5203f995757b7f5d1eb06947.png) \-- to connect them together. Instead, we\'ll use the NET tool \-- ![](https://cdn.sparkfun.com/assets/b/e/e/9/4/5203f995757b7ff21d9d2ed7.png) (left toolbar, or under the *Draw* menu). The WIRE tool would be better-named as a line-drawing tool, NET does a better job of connecting components.

[![Use NET not WIRE](https://cdn.sparkfun.com/r/400-400/assets/8/4/9/b/d/5203f942757b7fcc2bcb6ef2.png)](https://cdn.sparkfun.com/assets/8/4/9/b/d/5203f942757b7fcc2bcb6ef2.png)

### Using the NET Tool

To use the NET tool, hover over the very end of a pin (as close as possible, zoom in if you have to), and left-click once to start a wire. Now a green line should be following your mouse cursor around. To terminate the net, left-click on either another pin or a net.

[![Routing GIF](https://cdn.sparkfun.com/assets/d/1/b/d/e/5203fd3f757b7fec1e7b81a7.gif)](https://cdn.sparkfun.com/assets/d/1/b/d/e/5203fd3f757b7fec1e7b81a7.gif)

The hard part, sometimes, is identifying which part on a circuit symbol is actually a pin. Usually they\'re recognizable by a thin, horizontal, red line off to the side of a part. Sometimes (not always) they\'re labeled with a pin number. Make sure you click on the very end of the pin when you start or finish a net route.

### Route the Power Input Circuit

Start back in the upper left, and route the power input circuit like so:

[![Power circuit wired up](https://cdn.sparkfun.com/r/400-400/assets/d/a/e/6/8/5204000a757b7f8e2d3b6d30.png)](https://cdn.sparkfun.com/assets/d/a/e/6/8/5204000a757b7f8e2d3b6d30.png)

Whenever a net splits in two directions a **junction node** is created. This signifies that all three intersecting nets *are* connected. If two nets cross, but there\'s not a junction, those nets *are not* connected.

### Route the ATmega328 Circuit

Next we\'ll route the ATmega328 to its supporting circuitry. There\'s LEDs, a connector, resistor, capacitor and VCC/GND symbols to route to:

[![Wiring the ATmega circuit](https://cdn.sparkfun.com/r/600-600/assets/5/1/5/5/4/52040152757b7f42164688d4.png)](https://cdn.sparkfun.com/assets/5/1/5/5/4/52040152757b7f42164688d4.png)

Don\'t forget to add nets between the LEDs, resistors, and GND symbols!

### Making Named, Labeled Net Stubs

The remaining nets we have to make are not going to be as easy to cleanly route. For example, we need to connect the TXO pin on JP2 to the ATmega\'s RXD pin, all the way on the other side. You could do it, it would work, but it\'d be really ugly. Instead, we\'ll make net \"stubs\" and give them unique names to connect them.

We\'ll start by adding short, one-sided nets to each of the six pins on the serial connector. Begin by starting a net at a pin, just as you\'ve been doing. Terminate the net by left-clicking a few grid-lengths over to the right of the pin. Then, instead of routing to another pin, just hit ESC to finish the route. When you\'re done, it should look like this:

[![Net stubs added to connector pins](https://cdn.sparkfun.com/assets/1/0/9/b/2/520403df757b7f52261a70c9.png)](https://cdn.sparkfun.com/assets/1/0/9/b/2/520403df757b7f52261a70c9.png)

Next, we\'ll use the NAME tool \-- ![](https://cdn.sparkfun.com/assets/7/a/8/f/7/5204043d757b7f2a22794ff2.png) (left toolbar, or under the *Edit* menu) \-- to name each of the six nets. With the NAME tool selected, clicking on a net should open a new dialog. Start by naming the net connected to the top, GND pin. Delete the auto-generated name (e.g. N\$14), and replace it with \"GND\" (sans the quotation marks). This should result in a warning dialog, asking you if you want to connect this net to all of the other nets named \"GND\" (that would be every net connected to a GND symbol). Thanks for looking out for us EAGLE, but in this case *Yes* we do want to connect GND to GND.

After naming a net, you should use the LABEL tool \-- ![](https://cdn.sparkfun.com/assets/7/6/7/e/a/52040571757b7f852a55619e.png) \-- to add a text label. With the LABEL tool selected, left-click on the net you just named. This should spawn a piece of text that says \"GND\", left-click again to place the label down right on top of your net.

Follow that same order of operations for the remaining five net stubs. In the end, they should look like this (note the net connected to the TXO pin is named \"RX\", and a \"TX\" net connects to RXI \-- that\'s on purpose):

[![Net stubs named and labeled](https://cdn.sparkfun.com/assets/0/f/a/7/b/52040644757b7fe37c0e7eb3.png)](https://cdn.sparkfun.com/assets/0/f/a/7/b/52040644757b7fe37c0e7eb3.png)

VCC should be the only other net that warns you that you\'ll be connecting to other nets named \"VCC\" (anything connected to a VCC voltage node). For the other named nets, we\'ll need to create this same stub somewhere else. Where exactly? Well, we need to add a \"RX\" and \"TX\" net on the ATmega328, and a \"DTR\" nearby as well:

[![Naming and labeling RX, TX, and DTR](https://cdn.sparkfun.com/r/600-600/assets/7/0/7/8/6/520407b6757b7fbc483a5576.png)](https://cdn.sparkfun.com/assets/7/0/7/8/6/520407b6757b7fbc483a5576.png)

Even though there\'s no green net connecting these pins, every net with the *same, exact* name is actually connected.

We need to do a lot of the same to connect the 2x3 programming header to the ATmega328. First, wire up the connector like so (naming/labeling MOSI, MISO, SCK, and RESET):

[![ICSP connecter wired](https://cdn.sparkfun.com/assets/4/f/a/3/1/5204086b757b7f191d9ae71b.png)](https://cdn.sparkfun.com/assets/4/f/a/3/1/5204086b757b7f191d9ae71b.png)

Then, back to the ATmega328, add the same four named/labeled nets:

[![ATmega328 SPI pins named/labeled](https://cdn.sparkfun.com/r/600-600/assets/5/8/a/c/6/520409f2757b7f4d23f5fd6f.png)](https://cdn.sparkfun.com/assets/5/8/a/c/6/520409f2757b7f4d23f5fd6f.png)

Phew \-- you\'re done. Get excited, it\'s about time to lay out a PCB! When your schematic is done, it should look a little something like this:

[![Final schematic](https://cdn.sparkfun.com/r/600-600/assets/a/c/0/a/c/52040a3b757b7f04237ab526.png)](https://cdn.sparkfun.com/assets/a/c/0/a/c/52040a3b757b7f04237ab526.png)

------------------------------------------------------------------------

The schematic layout is done, but there are a few tips and tricks we\'d like to share before moving over to the PCB layout portion of the tutorial.

## Tips and Tricks

### Names and Values

Every component on your schematic should have two editable text fields: a name and a value. The **name** is an identifier like *R1*, *R2*, *LED3*, etc. Every component on the schematic should have a unique name. You can use the NAME tool \-- ![](https://cdn.sparkfun.com/assets/7/a/8/f/7/5204043d757b7f2a22794ff2.png) on any component to change the name.

A part\'s **value** allows you to define unique characteristics of that part. For example, you can set a resistor\'s resistance, or a capacitor\'s capacitance. The importance of a part\'s value depends on what type of component it is. For parts like resistors, capacitors, inductors, etc. the value is a critical piece of information when you\'re generating a bill of materials or assembly sheet. To adjust a part\'s value parameter, use the VALUE tool \-- ![](https://cdn.sparkfun.com/assets/c/9/7/0/9/52128928757b7f403e8b456c.png).

### Verifying Connections

The SHOW tool \-- ![](https://cdn.sparkfun.com/assets/9/1/f/b/c/52040f2f757b7f127bc3e13a.png) \-- is very useful for verifying that pins across your schematic are connected correctly. If you use SHOW on a net, every pin it\'s connected to should light up. If you\'re dubious of the fact that two like-named nets are connected, give the SHOW tool a try. SHOW-ing a net connected to GND, for example, should result in a lot of GND nets lighting up.

[![SHOWing a GND trace](https://cdn.sparkfun.com/r/600-600/assets/6/c/e/6/2/52040ea7757b7f42162b3e74.png)](https://cdn.sparkfun.com/assets/6/c/e/6/2/52040ea7757b7f42162b3e74.png)

As an alternative to show, you can temporarily MOVE a part a part to make sure nets are connected to it. Use MOVE to pick a part up, and the nets connected to it should bend and adjust to remain so. Just make sure you hit ESC to *not* move the part (or UNDO if you accidentally move it).

[![Moving a part to verify a connection](https://cdn.sparkfun.com/r/600-600/assets/b/b/8/3/3/5204102b757b7f1d7b39aab5.png)](https://cdn.sparkfun.com/assets/b/b/8/3/3/5204102b757b7f1d7b39aab5.png)

*If all the nets connected to a part MOVE with it, all connections are good.*

If a net isn\'t moving along with the part, it\'s not connected to the pin correctly. Double check to make sure you routed to the very end of the pin, and not a bit further:

[![Poorly routed net](https://cdn.sparkfun.com/r/600-600/assets/0/1/9/8/2/5203fcf6757b7f1d4f77a9e9.png)](https://cdn.sparkfun.com/assets/0/1/9/8/2/5203fcf6757b7f1d4f77a9e9.png)

If you have any nets incorrectly connected like above, DELETE \-- ![](https://cdn.sparkfun.com/assets/5/4/d/c/d/520410b9757b7f237ca2a740.png) \-- it, and try re-netting.

### Group Moving/Deleting/Etc.

Any tool that you use on a single component, can also be used on a group of them. Grouping and performing an action on that group is a two-step process. First, use the group tool \-- ![](https://cdn.sparkfun.com/assets/3/6/4/7/6/52128bf4757b7fdb578b456c.png) \-- to select the parts you want to modify. You can either hold down the left-mouse button and drag a box around them, or click multiple times to draw a polygon around a group. Once the group is made, every object in that group should glow.

After grouping, select the tool you want to use. The status box in the far bottom-left will have some helpful information pertaining to using the tool on a group:

[![Group move status box](https://cdn.sparkfun.com/assets/c/5/0/9/d/5212817b757b7f35338b456a.png)](https://cdn.sparkfun.com/assets/c/5/0/9/d/5212817b757b7f35338b456a.png)

In order to perform any action on a group, you have to select the tool, then **hold down CTRL** and **right-click the group**. After you CTRL+right-click, the tool will operate on the group just as it does a single component.

### Copy/Paste

EAGLE\'s Copy \-- ![](https://cdn.sparkfun.com/assets/b/0/f/8/8/52128a2a757b7f5f7e8b4568.png)\-- and Paste \-- ![](https://cdn.sparkfun.com/assets/b/7/7/6/1/52128a2a757b7fd8418b456c.png) \-- tools don\'t work exactly like other copy/paste tools you may have encountered before. Copy actually performs both a copy and paste when it\'s used. As soon as you copy a part (or any object on the schematic \-- name, text, net, etc.) an exact copy will instantly spawn and follow your mouse awaiting placement. This is useful if you need to add multiples of the same part (like GND nodes or resistors).

Paste can only be used to paste a **group** that has previously been copied to your clipboard. To use paste you first have to create a group, then (with the copy tool selected) CTRL+right-click to copy it, but hit ESC instead of gluing it down. This\'ll store the copied group into your operating system\'s clipboard, and you can use paste to place it somewhere. This tool is especially useful if you need to copy parts of one schematic file into another.