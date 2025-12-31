# Source: https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Stepoko: Powered by grbl Hookup Guide

# Stepoko: Powered by grbl Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/468388471d460cfeca6be21e3ab0defa?d=retro&s=20&r=pg) MTaylor]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft414&name=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft414 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Stepoko%3A+Powered+by+grbl+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft414&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft414&t=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft414&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F1%2F4%2FStepoko_Tutorial-11_smalllaser.jpg&description=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Pin It")

## Introduction

The [SparkFun Stepoko](https://www.sparkfun.com/products/13155) is an ATmega328p, Arduino compatible, 3-axis control solution. It\'s open source, uses open source firmware and works with an open source Java based cross platform G-Code sending application.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/4/topcrop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/topcrop.jpg)

*The SparkFun Stepoko, in all its glory.*

The simplest installation of it consists of *just plugging the stepper motors in*, but of course hard work pays off. Handy machine control buttons and locating features can be added at taste to give a mill whichever options are desired.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/4/Shapeoko_Tutorial-36.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/4/Shapeoko_Tutorial-36.jpg)

*The Stepoko implemented on a novelty-sized laser cutter, sitting atop a Shapeoko mill also driven by a Stepoko*

Features:

- 3 stepper connections
- Full, to 1/8 stepping
- Comes with heatsinks installed!
- Options for input and feedback include E-Stop (emergency stop, or general motor drive switch), Reset, Feed Hold, Cycle Start, Homing Location and Probing.
- Has option for spindle direction and PWM control.
- Can be powered from 12-30V.
- Independent axis current limiting adjustments

### Required Materials

- Flat-head Screwdriver
- Power supply
- Stepper motors
- USB type-B cable
- Software:
  - [Univeral Gcode Sender](https://github.com/winder/Universal-G-Code-Sender)
  - A gcode file [Github /Examples folder](https://github.com/sparkfun/SparkFun_Stepoko/tree/master/Examples)

### Suggested Reading

If you still need to assemble your Shapeoko Mill, please consult our Shapekoko Assembly Guide.

- [Motor tutorial](https://learn.sparkfun.com/tutorials/motors-and-selecting-the-right-one) \-- This tutorial covers all types of motors. If you\'re unfamiliar with stepper motors and how they work, check it out.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft414&name=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft414 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Stepoko%3A+Powered+by+grbl+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft414&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft414&t=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft414&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F1%2F4%2FStepoko_Tutorial-11_smalllaser.jpg&description=Stepoko%3A+Powered+by+grbl+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/all) [Next Page →\
[Hardware: Overview]](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/introduction) [Hardware: Overview](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-overview) [Hardware: The System and Power Supply](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-the-system-and-power-supply) [Hardware: The Stepper Drivers](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-the-stepper-drivers) [Hardware: Connecting the Motors](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-connecting-the-motors) [Hardware: Setting the Current](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-setting-the-current) [Hardware: Dealing with Heat](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/hardware-dealing-with-heat) [Software and Firmware Overview](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/software-and-firmware-overview) [Software: Machine control (Universal G-code Sender)](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/software-machine-control-universal-g-code-sender) [Firmware: grbl for the Stepoko](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/firmware-grbl-for-the-stepoko) [Firmware: Configuring grbl and Calibrating](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/firmware-configuring-grbl-and-calibrating) [Cutting a Square](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/cutting-a-square) [Cutting and Engraving a SparkFun Coaster](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/cutting-and-engraving-a-sparkfun-coaster) [Resources and Going Further](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/resources-and-going-fu)

[Comments [1]](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/stepoko-powered-by-grbl-hookup-guide/all) [Print]

- **Tags**
- - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Mechanical](https://learn.sparkfun.com/tutorials/tags/mechanical)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Shapeoko](https://learn.sparkfun.com/tutorials/tags/shapeoko)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]