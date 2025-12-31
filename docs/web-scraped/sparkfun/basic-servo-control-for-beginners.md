# Source: https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Basic Servo Control for Beginners

# Basic Servo Control for Beginners

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1109&name=Basic+Servo+Control+for+Beginners "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1109 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Basic+Servo+Control+for+Beginners&url=http%3A%2F%2Fsfe.io%2Ft1109&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1109&t=Basic+Servo+Control+for+Beginners "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1109&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F9%2FBasic_Servo_Guide_Demo.gif&description=Basic+Servo+Control+for+Beginners "Pin It")

## Introduction

From simply sweeping an object back and forth to adding steering to your robot or R/C car, [hobby servos](https://www.sparkfun.com/servos) are a great way to add some motion to your next project. Servos allow you to easily control the speed, direction and position ^[\[1\]](#footnote1)^ of the output shaft with just three wires!

[![Short video Demo of Servo Control](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/9/Basic_Servo_Guide_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/9/Basic_Servo_Guide_Demo.gif)

This tutorial covers a few different ways to control servos along with a project demonstrating how to control a servo from an external input. We will cover some basics of controlling servos with one example that requires no programming at all. Then we will control the servos with code using the Arduino IDE and Python. Feel free to jump to the example you would like to work with depending on the parts and code environment you prefer.

### Recommended Reading

Before going through this tutorial, you may want to check out these related guides to get familiar with the concepts and parts used in the examples:

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one)

### Motors and Selecting the Right One 

Learn all about different kinds of motors and how they operate.

[](https://learn.sparkfun.com/tutorials/hobby-servo-tutorial)

### Hobby Servo Tutorial 

Servos are motors that allow you to accurately control the rotation of the output shaft, opening up all kinds of possibilities for robotics and other projects.

[][Note:](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners#footnote1) Output shaft positional feedback is only available on standard (closed-loop) servos. We cover that in more detail in the next section.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1109&name=Basic+Servo+Control+for+Beginners "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1109 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Basic+Servo+Control+for+Beginners&url=http%3A%2F%2Fsfe.io%2Ft1109&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1109&t=Basic+Servo+Control+for+Beginners "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1109&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F9%2FBasic_Servo_Guide_Demo.gif&description=Basic+Servo+Control+for+Beginners "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/all) [Next Page →\
[Servo Motor Basics]](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/servo-motor-basics)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/introduction) [Servo Motor Basics](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/servo-motor-basics) [Servo Control with the SparkFun Servo Trigger](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/servo-control-with-the-sparkfun-servo-trigger) [Controlling a Servo with Arduino and Servo Library](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/controlling-a-servo-with-arduino-and-servo-library) [Controlling a Servo with Python and Pi Servo pHAT](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/controlling-a-servo-with-python-and-pi-servo-phat) [Direct Servo Control with the Qwiic Joystick](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/direct-servo-control-with-the-qwiic-joystick) [Resources and Going Further](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/discuss) [Single Page](https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]