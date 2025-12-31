# Source: https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Digital Sandbox Experiment Guide

# Digital Sandbox Experiment Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom], [![](https://cdn.sparkfun.com/avatar/c6c1a1ae72fbf9f47bee08a43259f504?d=retro&s=20&r=pg) bri_huang]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft175&name=Digital+Sandbox+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft175 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Sandbox+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft175&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft175&t=Digital+Sandbox+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft175&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F7%2F5%2Fsandbox-iso.jpg&description=Digital+Sandbox+Experiment+Guide "Pin It")

## Welcome to the Digital Sandbox!

The [Digital Sandbox](https://www.sparkfun.com/products/12651) is a learning platform that engages both the software and hardware worlds. It's powered by a microcontroller that can interact with real-world inputs -- like light or temperature sensors -- while at the same time controlling LEDs, motors, and other outputs. The Digital Sandbox is equipped with everything, on board, that you will need to complete 13 experiments including controlling an LED, measuring how loud things are, detecting the temperature is, and more. Think of this as a [SparkFun Inventor's Kit](https://www.sparkfun.com/products/12001) all in one board!

[![DS Cover Graphic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/7/5/DS_cover_graphic_red.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/7/5/DS_cover_graphic_red.png)

This tutorial walks you through a series of experiments that demonstrate how to program the Digital Sandbox using [ArduBlock](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/setting-up-arduino-and-ardublock), a graphical programming language for Arduino.

If you\'re interested in programming your Sandbox using the regular Arduino programming language, check out our parallel tutorial: the [Digital Sandbox Arduino Companion](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion).

### Experiment List (Table of Contents):

- [What is the Digital Sandbox?](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/what-is-the-digital-sandbox)
- [Setting up Arduino and ArduBlock](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/setting-up-arduino-and-ardublock)

0.  [Setup, Loop, and Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/0-setup-loop-and-blink)
1.  [Exploring Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/1-exploring-blink)
2.  [Multi-Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/2-multi-blink)
3.  [Dimming (the Hard Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/3-dimming-the-hard-way)
4.  [Dimming (the Easy Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/4-dimming-the-easy-way)
5.  [Color Mixing](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/5-color-mixing)
6.  [Number Storage with Variables](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/6-number-storage-with-variables)
7.  [If This Then That](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/7-if-this-then-that)
8.  [The Reaction Tester](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/8-the-reaction-tester)
9.  [Serial Calculator](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/9-serial-calculator)
10. [Do the Analog Slide](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/10-do-the-analog-slide)
11. [Automatic Night Light](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/11-automatic-night-light)
12. [Thermal Alert!](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/12-thermal-alert)
13. [Sound Detecting](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/13-sound-detecting)
14. [Opto-Theremin (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/14-opto-theremin-addon)
15. [Serial Motoring (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/15-serial-motoring-addon)
16. [Servo Sweeper (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/16-servo-sweeper-addon)

Please note that experiments 14, 15, and 16 require the [Digital Sandbox Add-On](https://www.sparkfun.com/products/12963), which can be purchased separately.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft175&name=Digital+Sandbox+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft175 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Sandbox+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft175&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft175&t=Digital+Sandbox+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft175&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F7%2F5%2Fsandbox-iso.jpg&description=Digital+Sandbox+Experiment+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/all) [Next Page →\
[What is the Digital Sandbox?]](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/what-is-the-digital-sandbox)

← Previous Page

[**Pages**] [Welcome to the Digital Sandbox!](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/welcome-to-the-digital-sandbox) [What is the Digital Sandbox?](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/what-is-the-digital-sandbox) [Setting up Arduino and ArduBlock](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/setting-up-arduino-and-ardublock) [0: Setup, Loop, and Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/0-setup-loop-and-blink) [1: Exploring Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/1-exploring-blink) [2: Multi-Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/2-multi-blink) [3: Dimming (the Hard Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/3-dimming-the-hard-way) [4: Dimming (the Easy Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/4-dimming-the-easy-way) [5: Color Mixing](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/5-color-mixing) [6: Number Storage with Variables](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/6-number-storage-with-variables) [7: If This Then That](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/7-if-this-then-that) [8: The Reaction Tester](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/8-the-reaction-tester) [9: Serial Calculator](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/9-serial-calculator) [10: Do the Analog Slide](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/10-do-the-analog-slide) [11: Automatic Night Light](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/11-automatic-night-light) [12: Thermal Alert!](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/12-thermal-alert) [13: Sound Detecting](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/13-sound-detecting) [14: Opto-Theremin (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/14-opto-theremin-addon) [15: Serial Motoring (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/15-serial-motoring-addon) [16: Servo Sweeper (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/16-servo-sweeper-addon) [Resources and Going Further](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/resources--going-further)

[Comments [6]](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Digital Sandbox](https://learn.sparkfun.com/tutorials/tags/digital-sandbox)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]