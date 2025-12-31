# Source: https://learn.sparkfun.com/tutorials/using-the-sparkfun-picoboard-and-scratch

## Introduction

**Heads up!** As of the writing of this tutorial, Scratch 3.0 and 2.0 does not fully support the PicoBoard. We suggest using [Scratch 1.4](http://scratch.mit.edu/scratch_1.4/) until the full PicoBoard extensions are implemented, tested, and rolled out with Scratch 2.0+.

[Scratch](https://scratch.mit.edu/) is an amazing tool to teach kids how to program. Often, we focus on creating fun animations, games, presentations, and music videos in Scratch. But, imagine how how cool it would be if you could add physical interactivity into your Scratch animation. For example, what if your Scratch character started to dance when you turned off the lights in your room or stopped as soon as the lights turned back on! With the PicoBoard, we can do all of this and more.

[![PicoBoard](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/SparkFun_PicoBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/SparkFun_PicoBoard.jpg)

### What is the PicoBoard?

The [PicoBoard](https://www.sparkfun.com/products/11888) is a piece of hardware called a sensor board that can be combined with MIT\'s Scratch programming environment to allow your Scratch programs to react (and even respond) to events happening outside of the computer. (If you\'re unfamiliar with Scratch and would like to learn more about it, read the Science Buddies [Introduction to Scratch](http://www.sciencebuddies.org/science-fair-projects/project_ideas/scratch-intro.shtml) page.) A sensor is a device that detects (senses) and measures the presence or absence of something. The PicoBoard is actually made up of several different types of sensors so it can detect many different \"somethings,\" including sound and light.

The PicoBoard has several sensors that can be used directly with the Scratch programming environment:

**Slider:** Changes values from 0 to 100 based on the position of the slider.

**Light Sensor:** Changes values from 0 to 100 based on the amount of light on this sensor.

**Button:** The position or state of the button controls the button pressed value (true or false).

**Sound Sensor:** Changes values from 0 to 100 based on the amount of sound it detects.

**Auxiliary Connections (A,B,C,& D):** Alligator Clips: These are generic connections to any resistive sensor. As the resistance changes, so does the input value. This sensor can also be setup as a digital detector to detect whether the alligator clips are connected.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/picoBoardSensors2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/picoBoardSensors2.png)

### Download Scratch 1.4

Note: Currently, the PicoBoard is only compatible with Scratch 1.4.

To get started, you will need to install Scratch 1.4 for your computer. Visit [scratch.mit.edu/scratch_1.4/](http://scratch.mit.edu/scratch_1.4/) to download version 1.4 of Scratch.

At this moment, the interface between Scratch 2.0 and the PicoBoard is currently under development. We are still working out the kinks of this. We recommend using the older and stable (v1.4) version of Scratch for interfacing to the PicoBoard.

### Installing Drivers

In addition to installing Scratch, you will need to install the [FTDI drivers](http://www.ftdichip.com/Drivers/VCP.htm) for your computer. The FTDI driver will allow the PicoBoard hardware to communicate with your computer. Follow our guide [here](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) on how to install and setup the drivers for your machine.

### Connecting the PicoBoard

Using the USB cable, connect the PicoBoard to your computer, and open up Scratch. To test the functionality, let's play with the Scratch sprite's size feature using this block. Find these blocks and string them together. Move the (slider sensor value) block into the set size block to replace the size by the sensor value.

Find the \"Green Flag\" Hat block and forever block under the **Control palette**, the set size block under the **Looks palette**, and the sensor value block under the **Sensing palette**.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/drawing1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/drawing1.png)

Assemble the blocks together so that it looks like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/drawing2-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/drawing2-1.png)

Click the green flag or the "hat" block to start your program. In a few seconds, you should see the red / green lights on your PicoBoard start flashing. Move the slider back and forth and watch what happens!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/PicoBoard_txrx.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/PicoBoard_txrx.png)

-\>The red / green lights indicate data is being received (RX) and transmitted (TX) between the PicoBoard and your computer.\<-

The Sensor value reporter block can be used in place of any value field (blank / number) in Scratch. Experiment with any of the other Scratch blocks such as *move ( ) steps* or *go to x: ( ) y: ( )*. Any of these values can be replaced by the sensor value from the PicoBoard.

Find your favorite Scratch program and re-mix it using the Sensor blocks!

## Using Additional Sensors (PicoBoard Add-on / LabPack) 

The [PicoBoard LabPack](https://www.sparkfun.com/products/11683) comes with several add-ons to attach the the auxiliary ports.

### How to Add Sensors to the PicoBoard

The four additional ports (A-D) allow the PicoBoard to be connected to a number of other additional sensors. The PicoBoard measures the resistance across the two alligator clips. When plugging in the PicoBoard connectors, make sure that you push the connector all the way in.

- Plug an alligator clip into one of the PicoBoard end connectors. There are four end connectors. They are A, B, C, or D.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/plug_connect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/plug_connect.png)

The PicoBoard measures the resistance between the two alligator clips of the auxiliary ports. You can use any resistive sensor with these clips. We\'ve created an add-on kit of parts that you might find useful to play with. In the add-on kit, we have:

### Button / Switches (Digital Sensors)

The most basic \"sensor\" is a simple switch. Switches allow us to electrically connect or disconnect a path for electricity between two metal connections. The PicoBoard senses whether or not the two alligator clips are connected.

In the Add-on kit, we include two arcade switches.

[![alt text](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/3/2/9/button_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/button_1.jpg)

These switches are pretty neat. They use a momentary limit switch that has three connections to it. Connect one of the alligator clips to the inner-most tab. Connect the second alligator clip to the outer-most connection tab.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/9/ArcadeButtons.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ArcadeButtons.png)

The switches can be triggered in Scratch using the boolean sensor block:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/sensorConnected.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/sensorConnected.gif)

These blocks can be used with control blocks such as:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/booleanControl.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/booleanControl.gif)

### Analog Sensors

All other resistive sensors are considered \"analog\" sensors. The PicoBoard will measure the resistance of the sensor and report a value that ranges from 0 to 100 in Scratch. These values can be accessed using any of these blocks for the auxiliary sensors on A, B, C, or D.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/sensorvalue.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/sensorvalue.gif)

#### Turn / Rotary Potentiometer

A rotary potentiometer is basically the same as the slider \-- however, instead of moving the slider back and forth, you simply turn the knob on the potentiometer. Connect one of the alligator clips to the center tab and the second alligator clip to either one of the outside tabs. Note: The limits of this sensor will only vary from 0 to 50 (instead of 0 to 100).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/9/TurnPot.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/TurnPot.png)

#### Motor

Traditionally, a motor is an output device, but when connected to the PicoBoard, you can use the motor as a generator. Spin the motor and see what happens to your input values. Simply connect the two wires of the motor to the two alligator clips.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/Motor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/Motor.png)

#### [][Force Sensitive Resistor](#fsr)

This square sensor senses pressure applied to the surface. As you press down on the square, the resistance changes.

[![alt text](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/3/2/9/ForceResistor.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ForceResistor.png)

Attach the alligator clip extensions (regular alligator clip wires) onto the two metal prongs on the end of the Force Sensitive Resistor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/9/ForceResistor_clips.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ForceResistor_clips.png)

When clipping, make sure that the metal clips are fully seated and touching the metal part of the sensor. Also, make certain that the alligator clips do not touch each other.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ForceResistor_clips2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ForceResistor_clips2.png)

#### Thermistor

A thermistor is a special type of resistor whose resistance varies significantly with temperature. As the temperature increases, the resistance of a thermistor decreases. Technically, the thermistor requires the use of the [Steinhart-hart](http://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation) equation to convert from the PicoBoard sensor values to a real temperature but, you can simply connect the thermistor up using the alligator clips.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/thermistor2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/thermistor2.jpg)

If you\'re interested in a guide to calibrating a thermistor in Scratch, check out our [blog post](https://learn.sparkfun.com/blog/1663) on using a standard turkey thermometer in Scratch.

[](https://news.sparkfun.com/1663 "November 30, 2014: Happy Thanksgiving everyone! Check out this quick little hack using a standard temperature probe from my oven thermometer, our PicoBoard, and a little creative coding in Scratch!")

### Turkey Scratch \-- Thanksgiving, Programming, and a \'lil Data 

[November 30, 2014]

Read Post

## Quick Reference Guide

Now that you have the PicoBoard set up correctly, you\'re ready to start playing with it. The sensor table describes each sensor, how you can use it, and the Scratch blocks that you could use to capture and use the sensor information (Click the image for a larger view).

[![Drag and drop PicoBoard Reference Blocks](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/2/9/ScratchPicoTable.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/9/ScratchPicoTable.png)