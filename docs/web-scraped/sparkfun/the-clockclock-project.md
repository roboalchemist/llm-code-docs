# Source: https://learn.sparkfun.com/tutorials/the-clockclock-project

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- The ClockClock Project

# The ClockClock Project

[≡ Pages](#)

Contributors: [ Alchitry], [ Ell C]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1299&name=The+ClockClock+Project "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1299 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=The+ClockClock+Project&url=http%3A%2F%2Fsfe.io%2Ft1299&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1299&t=The+ClockClock+Project "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1299&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F9%2F9%2FImage1.jpg&description=The+ClockClock+Project "Pin It")

## Introduction

What time is it?! It\'s time for an awesome Alchitry project, that\'s what! In this tutorial I'm going to walk you through how I built a ClockClock using the [Alchitry Au](https://www.sparkfun.com/products/16527) to control all the motors.

[![Image of the clock clock on the wall](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/9/Image1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/9/Image1.jpg)

What is a ClockClock? It is simply a clock made of clocks! The idea is to use many analog style clocks together to form the digits of the time. So meta.

First, let me start by saying this wasn't my original idea. I came across this concept a few years ago and always thought it would be a great demo FPGA project since it requires so many control signals. The original clock can be found [here](https://clockclock.com/).

There are a couple reasons this project makes such a great FPGA demo project. First, the clock requires 48 stepper motors. There are 24 "clocks" and each one has two independent hands. Using a standard step/direction stepper driver means you need two control signals per motor or 96 outputs. I wanted to be able to disable the drivers when the clock was stationary to save power. This added four more outputs (one for each "digit" of the clock). I also wanted to use an Arduino to generate the animations as it would be much easier to do this in code than hardware. To talk to the Arduino, I decided to use I^2^C over the Alchitry Au's Qwiic connector. This required two more IO pins for a total of 102. Conveniently, the Alchitry Au has exactly 102 IO pins.

Besides showing off the massive amount of IO FPGAs are capable of, this project uses the Qwiic connector on the FPGA in a semi-unconventional way. The FPGA in this project acts as a peripheral instead of as a controller. The Arduino is the controller and issues all the commands to the FPGA. I actually think this will be a useful paradigm for many projects.

Some tasks are very simple in software but incredibly complicated in hardware. The opposite is also true. By linking a microcontroller and FPGA together you get the best of both worlds. The Qwiic connector on both boards makes this easy.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

While there are quite a few ways to machine parts for this project, here are the tools we used:

- 3D Printer
- Shapeoko XXL

### You Will Also Need

- 48x [Valve Gear Stepper Motor](https://www.amazon.com/gp/product/B01J3KV3B2)
- 48x [StepStick Stepper Motor Diver Module with Heat Sink](https://www.amazon.com/gp/product/B01FFGAKK8)
- 1x [UBEC Adjustable BEC UBEC 2-6S for Quadcopter RC Drone](https://www.amazon.com/gp/product/B07PLSYX9G)
- 1x [Enclosed AC-DC Switching Power Supply](https://www.amazon.com/gp/product/B07Z55FCQQ)

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/programming-an-fpga)

### Programming an FPGA 

Come look at the basics of working with Field Programmable Gate Arrays.

[](https://learn.sparkfun.com/tutorials/how-does-an-fpga-work)

### How Does an FPGA Work? 

The What, How, Why, and When of Field Programmable Gate Arrays, aka FPGAs

[](https://learn.sparkfun.com/tutorials/first-fpga-project---getting-fancy-with-pwm)

### First FPGA Project - Getting Fancy with PWM 

An initial project using Alchitry\'s onboard FPGA to manipulate PWM

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1299&name=The+ClockClock+Project "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1299 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=The+ClockClock+Project&url=http%3A%2F%2Fsfe.io%2Ft1299&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1299&t=The+ClockClock+Project "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1299&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F9%2F9%2FImage1.jpg&description=The+ClockClock+Project "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/the-clockclock-project/all) [Next Page →\
[Physical Build]](https://learn.sparkfun.com/tutorials/the-clockclock-project/physical-build)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/the-clockclock-project/introduction) [Physical Build](https://learn.sparkfun.com/tutorials/the-clockclock-project/physical-build) [FPGA](https://learn.sparkfun.com/tutorials/the-clockclock-project/fpga) [Software Setup and Programming](https://learn.sparkfun.com/tutorials/the-clockclock-project/software-setup-and-programming) [Troubleshooting](https://learn.sparkfun.com/tutorials/the-clockclock-project/troubleshooting) [Conclusion](https://learn.sparkfun.com/tutorials/the-clockclock-project/conclusion) [Resources and Going Further](https://learn.sparkfun.com/tutorials/the-clockclock-project/resources-and-going-further)

[Comments [17]](https://learn.sparkfun.com/tutorials/the-clockclock-project/discuss) [Single Page](https://learn.sparkfun.com/tutorials/the-clockclock-project/all) [Print]

- **Tags**
- - [3D Printing](https://learn.sparkfun.com/tutorials/tags/3d-printing)
  - [Alchitry](https://learn.sparkfun.com/tutorials/tags/alchitry)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [FPGA](https://learn.sparkfun.com/tutorials/tags/fpga)
  - [Mechanical](https://learn.sparkfun.com/tutorials/tags/mechanical)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Shapeoko](https://learn.sparkfun.com/tutorials/tags/shapeoko)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]