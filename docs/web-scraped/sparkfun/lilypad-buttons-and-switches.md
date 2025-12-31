# Source: https://learn.sparkfun.com/tutorials/lilypad-buttons-and-switches

## Introduction

[Buttons](https://www.sparkfun.com/products/8776), [slide switches](https://www.sparkfun.com/products/9350), and [reed switches](https://www.sparkfun.com/products/13343) are electronic components you can use to control a project, turn it on or off, or trigger behaviors in the code of a program. This guide will provide an overview of the options available in the LilyPad sewable electronics line and some examples of using them in a project.

[![LilyPad Button Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/08776-LilyPad_Button_Board-01.jpg)](https://www.sparkfun.com/lilypad-button-board.html)

### [LilyPad Button Board](https://www.sparkfun.com/lilypad-button-board.html) 

[ DEV-08776 ]

We designed this board to give the user a low profile button without any sharp edges. Button closes when you push it and open...

[ [\$2.10] ]

[![LilyPad Slide Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/1/9/09350-01.jpg)](https://www.sparkfun.com/lilypad-slide-switch.html)

### [LilyPad Slide Switch](https://www.sparkfun.com/lilypad-slide-switch.html) 

[ DEV-09350 ]

This is a simple slide switch for the LilyPad. Use it as a simple ON/OFF switch, or to control LEDs, buzzers, sensors, etc. T...

[ [\$2.05] ]

[![LilyPad Reed Switch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/5/2/13343-01.jpg)](https://www.sparkfun.com/lilypad-reed-switch.html)

### [LilyPad Reed Switch](https://www.sparkfun.com/lilypad-reed-switch.html) 

[ DEV-13343 ]

The LilyPad Reed Switch is a simple breakout for a reed switch that will make it easy to use in e-textiles circuits in exactl...

[ [\$6.75] ]

You can also explore buttons and switches in a pre-wired circuit using the [E-Sewing ProtoSnap](https://www.sparkfun.com/products/14546) or with Arduino in the [LilyPad ProtoSnap Plus](https://www.sparkfun.com/products/14346).

[![LilyPad E-Sewing ProtoSnap ](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/7/3/14546-01.jpg)](https://www.sparkfun.com/lilypad-e-sewing-protosnap.html)

### [LilyPad E-Sewing ProtoSnap ](https://www.sparkfun.com/lilypad-e-sewing-protosnap.html) 

[ DEV-14546 ]

The LilyPad E-Sewing ProtoSnap is a great way to explore how buttons and switches behave in simple e-sewing circuits before c...

[ [\$7.25] ]

[![LilyPad ProtoSnap Plus](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/2/4/14346-01.jpg)](https://www.sparkfun.com/lilypad-protosnap-plus.html)

### [LilyPad ProtoSnap Plus](https://www.sparkfun.com/lilypad-protosnap-plus.html) 

[ DEV-14346 ]

The LilyPad ProtoSnap Plus is a sewable electronics prototyping board that you can use to explore circuits and programming, t...

[ [\$47.50] ]

### Suggested Reading

Here are some additional resources to check out before you begin:

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/lilypad-basics-e-sewing)

### LilyPad Basics: E-Sewing 

Learn how to use conductive thread with LilyPad components.

[](https://learn.sparkfun.com/tutorials/getting-started-with-lilypad)

### Getting Started with LilyPad 

An introduction to the LilyPad ecosystem - a set of sewable electronic pieces designed to help you build soft, sewable, interactive e-textile projects.

## What are Buttons and Switches?

Buttons and switches are electronic components that control the flow of current in a circuit. They can act as a simple gateway to light up an LED or as inputs for a microcontroller. Buttons are considered a type of switch, often with a momentary push actuation. We\'ll refer to both as switches in this section.

### Switch States

To change a switch from one state to another requires a physical action, often a flip, slide, or push. This is called **actuating** the switch. Different types of switches have different actuation methods. In the LilyPad line you can activate switches by sliding, pushing, and even using a magnet to trigger.

### Maintained vs Momentary Switches

Switches that stay in one state until changed are called **maintained** switches. Examples of some common maintained switches are light switches, on/off switches on devices, and toggle switches. The LilyPad Slide Switch is an example of a maintained switch.

A **momentary** switch is only active when being actuated. Push buttons are a common example of a momentary switch. Other momentary switches you may find around you are the keys on your keyboard - a letter is only typed when the key is pressed. The LilyPad Button is an example of a momentary switch.

## LilyPad Slide Switch 

The LilyPad Slide Switch has a small switch labeled ON/OFF. When moved to the OFF position, parts inside the switch move away from each other and open the circuit (disconnecting it). No current will flow through the switch to the components connected to its sew tabs. When the toggle switch is moved to the ON position, the two sew tabs on the switch are connected, allowing current to flow through and close the circuit.

[![Detail of using LilyPad Switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/0/TurnOffSwitch.jpg)

*Using a LilyPad Slide Switch on the LilyPad ProtoSnap Plus*

### Examples

Slide switches can be used to control individual LEDs in an e-sewing project. Here\'s an example of using three slide switches connnected with conductive thread to control each color channel on a [LilyPad TriColor LED](https://www.sparkfun.com/products/8467).

[![Tri-Color LED stitched with conductive thread to three LilyPad Switches and a LilyPad Battery Holder](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/5/TriColorLED_SimpleStitched.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/5/TriColorLED_SimpleStitched.png)

*Simple color mixing circuit using LilyPad Switches connected to each color tab of the tri-color LED.*

A slide switch can also be used to turn off an element in a project, such as a buzzer or indicator while debugging or when you want a bit of peace and quiet. The example below shows a slide switch sewn in a [LilyPad Buzzer](https://www.sparkfun.com/products/8463). This allows the other features of the project to still function while disconnecting power to the buzzer.

[![Piezo buzzer sewn into a circuit with a slide switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/9/Buzzer_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/9/Buzzer_Switch.jpg)

You can also connect the slide switch to a LilyPad Arduino and read its state in your programs. Here\'s an example of using a LilyPad Button and LilyPad Switch in a project on the LilyPad ProtoSnap Plus to control LEDs.

This wearable dice project tutorial utilizes seven slide switches to select from a 4, 6, 8, 10, 12, 20, and 100 side virtual dice for gaming.

[](https://learn.sparkfun.com/tutorials/dungeons-and-dragons-dice-gauntlet)

### Dungeons and Dragons Dice Gauntlet 

August 13, 2013

A playful, geeky tutorial for a leather bracer that uses a LilyPad Arduino, LilyPad accelerometer, and seven segment display to roll virtual 4, 6, 8, 10, 12, 20, and 100 side dice for gaming.

## LilyPad Reed Switch 

The LilyPad Reed Switch is another kind of switch available in the LilyPad line. Unlike the other LilyPad switch offerings, the reed switch does not require you to touch the board to activate it. Inside the reed switch are two thin pieces of metal that are pulled in contact with each other when exposed to a magnetic field.

Read more about how to use it in the full hookup guide.

[](https://learn.sparkfun.com/tutorials/lilypad-reed-switch-hookup-guide)

### LilyPad Reed Switch Hookup Guide 

November 5, 2015

A guide to using the LilyPad Reed Switch breakout in your projects.

### Examples

In this episode of Electricute, Dia and Nick build an interactive Krampus stocking using the LilyPad Reed Switch and a magnet.

## LilyPad Button

The LilyPad Button Board is also a type of switch. When you press the button in the middle of the board, it connects the two sew tabs and allows current to flow through. When you let go of the button, the connection is opened again, and the button springs back into place. This button is an example of a momentary switch.

[![Pressing LilyPad button on E-Sewing ProtoSnap](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/0/EsewingButtonPress.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/0/EsewingButtonPress.jpg)

*Pressing the LilyPad Button on the E-Sewing ProtoSnap*

### Examples

This stuffed creature uses both a slide switch and button to control LEDs embedded in it.

[](https://learn.sparkfun.com/tutorials/light-up-plush)

### Light-Up Plush 

December 16, 2016

Craft a light-up plush with LilyPad LEDs controlled by pressing a button and sliding a switch in the creature\'s hands.

Here\'s an example of a button being used as an input connected to the LilyMini microcontroller to switch LED modes.