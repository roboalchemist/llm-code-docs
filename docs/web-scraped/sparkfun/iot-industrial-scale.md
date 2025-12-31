# Source: https://learn.sparkfun.com/tutorials/iot-industrial-scale

## Introduction 

[![scale jump test](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/FinalScale-JumpTest1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/FinalScale-JumpTest1.jpg)

What does a baby elephant weigh?\* How much impact force does a jump have?? How can you tell if a rain barrel is full without looking inside??? Answer all these questions and more by building your very own Internet of Things (\"IoT\") industrial scale using the [SparkFun OpenScale board](https://www.sparkfun.com/products/13261)!

This project is intended for folks with a lil\' bit of background using Arduino or other microcontrollers. But, whether this is your first or 137th project, check out the links in the Suggested Reading section below (and throughout the tutorial) or leave a [comment](https://learn.sparkfun.com/tutorials/iot-industrial-scale/discuss) if you have any questions!

**Read time**: \~ 15 min.

**Build time**: Approx. 2 - 3 hours

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/Marley-Sitting1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/Marley-Sitting1.jpg)

\*\*To weigh a baby elephant, you might need to be a zookeeper or otherwise have an elephant friend.. but you could always weigh Fido and/or kitty!\*

For all you visual learners, check out a video of the project below:

### Required Materials

To follow along and build your own scale, all the parts used have been listed for your convenience.

#### Electronics

- [Open Scale](https://www.sparkfun.com/products/13261) (+ mini USB to USB cable)
- Four (4) [Load Cells](https://www.sparkfun.com/products/13332) (or strain gauges depending on needs and budget)
- [Particle Photon microcontroller](https://www.sparkfun.com/products/13345) or other [data logger](https://www.sparkfun.com/products/13712) (+ micro USB to USB cable)
- [Breadboard](https://www.sparkfun.com/products/12002) (or PCB board)
- [22 gauge stranded wire](https://www.sparkfun.com/products/11375) (breadboard wires also work)

**To make the system wireless:**

- [SparkFun Sunny buddy](https://www.sparkfun.com/products/12885) and/or [SparkFun Photon Battery Shield](https://www.sparkfun.com/products/13626)
- One 2000 mAh [Polymer Lithium Ion Battery](https://www.sparkfun.com/products/8483)

All these parts can be found in the wish list below.

#### Scale and Casing

- [Terminal blocks](https://www.sparkfun.com/search/results?term=terminal+block) (5)
- Three (3) M3 screws per load cell (total of 12)
- One (1) project case (to protect the electronics)
- One (1) base board, and one (1) top board (for the scale platform)
  - My base board was \~ 16\" x 16\" and my top board was \~ 12\" x 14\".
  - Both boards should be sturdy and not flex or dent.
- Wood slats to frame the sides of the top board to hold it in place.
- Four (4) feet for base

### Suggested Reading

Before getting started with this project, you may want to read up on some of the components and tools used throughout.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/openscale-applications-and-hookup-guide)

### OpenScale Applications and Hookup Guide 

OpenScale allows you to have a permanent scale for industrial and biological applications. Learn how to use the OpenScale board to read and configure load cells.

[](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells)

### Getting Started with Load Cells 

A tutorial defining what a load cell is and how to use one.

[](https://learn.sparkfun.com/tutorials/photon-development-guide)

### Photon Development Guide 

A guide to the online and offline Particle IDE\'s to help aid you in your Photon development.

As usual, don\'t forget to read the [Datasheet for the Load Cells](http://www.htc-sensor.com/products/151.html) and any other components you with to use in your project.

## Measuring Weight

### How Do We Measure Weight??

[![load sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/LoadCell-CloseUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/LoadCell-CloseUp.jpg)

[Strain gauges](https://en.wikipedia.org/wiki/Strain_gauge)! Also called load sensors, strain gauges measure electrical resistance changes in response (and proportional) to, well, strain! Strain is how much an object deforms under an applied force, or pressure (force per area). Check out [this super awesome tutorial](https://learn.sparkfun.com/tutorials/getting-started-with-load-cells#load-cell-basics) for more info on how strain gauges work.

Usually what you\'ll find in a bathroom scale is a **load cell**, which combines four strain gauges in a [wheatstone bridge](https://en.wikipedia.org/wiki/Wheatstone_bridge). This project uses four [disc compression load cells](https://www.sparkfun.com/products/13332) rated at 200 kg, like the one pictured above.

### OpenScale Overview

[![OpenScale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/OpenScale-CloseUp2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/OpenScale-CloseUp2.jpg)

The [OpenScale](https://www.sparkfun.com/products/13261) is a specialized board that allows a user to easily read and configure all types of load cells and strain gauges. It\'s designed for constant loads, includes an on-board temperature sensor, and is particularly helpful for places that are tricky to get to (e.g. [under a beehive](https://www.sparkfun.com/news/1951) or conveyor belt).

The OpenScale combines an [HX711 load cell amplifier](https://www.sparkfun.com/products/13879) with an ATmega328P, so you can program it just like an Arduino (Arduino Uno, specifically). The OpenScale uses [TTL serial communication at 9600bps 8-N-1](https://learn.sparkfun.com/tutorials/serial-communication) to transmit and receive data. It comes with software that allows it to be controlled in, and print data to, the [Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide?_ga=1.101219716.403001909.1472511467) serial monitor.

[Here\'s the GitHub page for the OpenScale](https://www.sparkfun.com/products/11931), which includes the Eagle schematic files.

## Build the Electronics

### Schematic:

[![Fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/IndustrialScale-SchematicV2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/IndustrialScale-SchematicV2.jpg)

### Part 1: Connect the Load Cells!

[![terminal block](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/TerminalBlocks-LoadCellsV2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/TerminalBlocks-LoadCellsV2.jpg)

Load cells have four signal wires:

- Red: Excitation+ (E+) or VCC
- Black: Excitation- (E-) or ground
- White: Output+ (O+), Signal+ (S+)+ or Amplifier+ (A+)
- Green (or blue): Output- (O-), Signal- (S-), or Amplifier (A-)

They also have bare (or yellow) grounding wires to block outside (electromagnetic) noise.

[![connect to scale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/TerminalBlocks-LoadCellsToOpenScale1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/TerminalBlocks-LoadCellsToOpenScale1.jpg)

Connect all five load cell wires **in parallel** to the OpenScale terminal blocks with the corresponding labels. *You might need to **switch the green and white load cell wires** \-- check this by adding weight to the load cells. If the weight is decreasing, switch the wire orientation.*

Since the OpenScale terminal blocks are somewhat cramped with four load cells, external connectors are recommended. I used the terminal blocks pictured above. If you have a case for the electronics, remember to put the connectors INSIDE the case before connecting them to the load cells (not speaking from experience or anything..).

### Part 2: Connect the OpenScale to a Data Logger!

In addition to printing, reading, and gathering data from the Arduino serial monitor (see [\"Reading Load Cells!\"](https://learn.sparkfun.com/tutorials/iot-industrial-scale#reading-the-load-cells)), we can add a Photon microcontroller to connect to WiFi and upload the measurements to the Internet!

[![close up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/OpenScale-ConnectionsCloseUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/OpenScale-ConnectionsCloseUp.jpg)

Connect the OpenScale \"Serial Out\" ground (\"GND\") port to the Photon GND, and the **OpenScale \"TX\" port to the Photon \"RX\" port**. If your data logger needs power, connect the OpenScale 5V port to the data logger Vin port. That\'s it!

## Build the Base and Case

[![LoadCellsMounting](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/BaseBoard-LoadCellsMounting2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/BaseBoard-LoadCellsMounting2.jpg)

1.  Plan out, measure, and mark location of load cells.

    Load cells should be at least 1\" in from the top platform board sides and installed equidistant and on the same plane (aka same height) with each other.

    [![PlasticStencilDrilling](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/LoadCells-PlasticStencilDrilling.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/LoadCells-PlasticStencilDrilling.jpg)

    Each load cell needs three M3 type screws, which requires fairly precise measurements. I opted for a quick & easy solution: make a plastic stencil that marks the load cell outline and the location of the screw holes. The plastic I used was cut from a discarded strawberry container (yay, free and upcycled!).

2.  Drill holes for load cell screws and attach load cells to base board.

    [![base feet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/Base-Feet.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/Base-Feet.jpg)

3.  Attach feet to base.

    [![BaseWall](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/FinalVersion-BaseWalls1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/FinalVersion-BaseWalls1.jpg)

4.  Secure the scale platform.

    Place platform on top of the load cells. Attach wood slats to sides of base with wood glue and/or screws to secure the platform in place laterally, but not vertically. AKA, be sure that there is no resistance to the board pushing downward.

    Add brackets on opposite sides for a more secure hold.

5.  Place electronics into project box container (or tupperware) and drill holes for cables.

    [![final](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/FinalVersion-Finished.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/FinalVersion-Finished.jpg)

6.  Admire your handiwork!

## Reading the Load Cells

### Connect the OpenScale

[![calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/Calibration-Computer1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/Calibration-Computer1.jpg)

One of the awesome features of the OpenScale program is that it outputs data to the Arduino IDE serial monitor (9600bps). That means all you need to do is plug in your OpenScale via USB, select the appropriate board (Arduino Uno) and port, and you can read the load cell data directly from the Arduino Serial Monitor or another preferred terminal program. [More info on how to do this here.](https://learn.sparkfun.com/tutorials/installing-arduino-ide?_ga=1.54541742.403001909.1472511467#windows)

Enter \'x\' to bring up the OpenScale settings menu. Entering \'x\' again leaves the menu and the OpenScale will start printing data!

[![serial monitor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/ArduinoSerialMonitor-FullMenu2_Labeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/ArduinoSerialMonitor-FullMenu2_Labeled.jpg)

*Note: If you are connected to another microcontroller, the OpenScale does not send data when in the menu mode.*

### Calibrate

Before we gather any data, we need to calibrate the OpenScale to get accurate measurements. It\'s also recommended to re-calibrate the system every few weeks (or days) to avoid creep (slow change in reading over time).

To calibrate the scale:

1.  Remove all weights (except the platform).
2.  Open the OpenScale menu and select \'2\' to open the calibration setting.
3.  Place a (known) weight on the scale and adjust the calibration factor using \'+\' and \'-\' until the scale reads out the calibration weight within a reasonable margin in error.\*

Also, the load cell output varies with temperature (\'cause [heat causes expansion](https://en.wikipedia.org/wiki/Thermal_expansion)), so we need to keep the system at a constant temperature. If you wanna get fancy, you can also use different calibration factors at different temperatures (or temperature ranges)..

\*\*My experimental uncertainty was about +/- 5 lbs.\*

### Tare

Each time you power up the OpenScale, you\'ll need to tare it. This is an easy process, but it means you need to connect the OpenScale directly to a laptop and open the settings menu.

To tare the scale, remove all weights. Input \'1\' in the OpenScale menu, wait for it to finish taring, then exit the menu and check that the output is close to zero (+/- 5 lbs). If the reading is still off, taring again should fix the problem \-- if not, check that the load cell grounding wires are properly connected to ground.

### Remove Trigger

We also need to remove the serial trigger from the OpenScale. Do this by going to the menu, inputting \'t\', and turning the serial trigger to OFF.

### Customizing the OpenScale

You can change various other settings on the OpenScale using the serial monitor, including units (lbs/kg), print rate, decimal places, etc. You can adjust, or peruse, the entire OpenScale program by [downloading it from GitHub](https://github.com/sparkfun/OpenScale/tree/master/firmware/OpenScale)!

## Program the Photon

[Write a program for the Photon](https://docs.particle.io/guide/getting-started/build/photon/) that will read in the serial output data from the OpenScale and push it to the IoT platform of your choice.

Or you can use/modify my code :) [Here\'s the GitHub repository for the IoT scale](https://github.com/jenfoxbot/IoTIndustrialScale/tree/master), or just copy and paste the code from here:

[IoT Industrial Scale Code](https://raw.githubusercontent.com/jenfoxbot/IoTIndustrialScale/master/IoTIndustrialScale)

\

This program reads data from the OpenScale and pushes it to ThingSpeak (also prints it to the [Photon serial monitor](https://docs.particle.io/reference/cli/#particle-serial-monitor)). ThingSpeak is super easy (and free!) to set up, the only downside is that it only allows data to be posted every 15s.

**What you need to do to make the program work for your setup:**

[![variables to change](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/ProgramCode-WhatToChange_Labeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/ProgramCode-WhatToChange_Labeled.jpg)

*Click for a closer look.*

1.  Include your WiFi SSID (network name) and your WiFi password in lines 53 & 54, and lines 69 & 70.

2.  Set up a [ThingSpeak channel!](https://thingspeak.com/).

    [![thingspeak channel setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/ThingSpeak-ChannelSetUp.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/ThingSpeak-ChannelSetUp.jpg)

    1.  Name the channel and write a brief description.
    2.  Include at least one field name. If you want to push more data, like temperature or a timestamp, include those corresponding fields.
    3.  Save the channel!

3.  Copy the \"Channel ID\" number and the \"Write API Key\" and input them into lines 84 & 85.

    [![API keys](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/ThingSpeak-APIKeys_labeled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/ThingSpeak-APIKeys_labeled.jpg)

Read through the comments in the program code for more information on how the program works.

## Test and Refine

[![test and refine](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/Marley-Laying1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/Marley-Laying1.jpg)

Prototype complete! Have your favorite human or animal stand (or awkwardly lay..) on the scale to check that it works as expected.

[![final](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/2/8/FinalScale1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/2/8/FinalScale1.jpg)

Check thoroughly to see if there is anything that needs to be fixed, secured, and/or improved. During my build process I noticed that a lot of the wood I was using to test would get dented by the load cells, resulting in inaccurate readings.