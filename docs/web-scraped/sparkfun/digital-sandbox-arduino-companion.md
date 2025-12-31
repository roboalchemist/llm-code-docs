# Source: https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Digital Sandbox Arduino Companion

# Digital Sandbox Arduino Companion

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft267&name=Digital+Sandbox+Arduino+Companion "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft267 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Sandbox+Arduino+Companion&url=http%3A%2F%2Fsfe.io%2Ft267&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft267&t=Digital+Sandbox+Arduino+Companion "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft267&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F6%2F7%2FDS_cover_graphic_red.png&description=Digital+Sandbox+Arduino+Companion "Pin It")

## Introduction

The [Digital Sandbox](https://www.sparkfun.com/products/12651) is a learning platform that engages both the software and hardware worlds. It's powered by a microcontroller that can interact with real-world inputs -- like light or temperature sensors -- while at the same time controlling LEDs, motors, and other outputs. The Digital Sandbox is equipped with everything, on board, that you will need to complete 13 experiments including controlling an LED, measuring how loud things are, detecting the temperature is, and more. Think of this as a [SparkFun Inventor's Kit](https://www.sparkfun.com/products/12001) all in one board!

[![DS graphic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/6/7/DS_cover_graphic_red.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/7/DS_cover_graphic_red.png)

In our original [Digital Sandbox Experiment Guide](https://learn.sparkfun.com/tutorials/digital-sandbox-experiment-guide), we show you how to program the Sandbox using a simple, graphical programming language called [ArduBlock](https://learn.sparkfun.com/tutorials/alternative-arduino-interfaces/ardublock). This time around, we\'ll show you how to ditch the graphical editor in favor of **actual Arduino code**.

If you\'re looking to get into Arduino coding, this is a great place to begin. Grab a Sandbox and get started!

### Experiment List (Table of Contents):

We\'ll explore the Sandbox through a series of progressive experiments. If you\'ve already completed the Sandbox Experiment Guide, this list will look familiar. We\'ve recreated the code from those experiments using Arduino code instead of ArduBlock.

After [setting up your Sandbox](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/setup), here\'s what\'s covered:

0.  [Setup and Loop](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/0-setup-and-loop)
1.  [Exploring Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/1-exploring-blink)
2.  [Multi-Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/2-multi-blink)
3.  [Dimming (the Hard Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/3-dimming-the-hard-way)
4.  [Dimming (the Easy Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/4-dimming-the-easy-way)
5.  [Color Mixing](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/5-color-mixing)
6.  [Number Storage with Variables](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/6-number-storage-with-variables)
7.  [If This Then That](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/7-if-this-then-that)
8.  [The Reaction Tester](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/8-the-reaction-tester)
9.  [Serial Calculator](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/9-serial-calculator)
10. [Do the Analog Slide](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/10-do-the-analog-slide)
11. [Automatic Night Light](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/11-automatic-night-light)
12. [Thermal Alert!](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/12-thermal-alert)
13. [Sound Detecting](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/13-sound-detecting)
14. [Opto-Theremin (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/14-opto-theremin-addon)
15. [Serial Motoring (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/15-serial-motoring-addon)
16. [Servo Sweeper (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/16-servo-sweeper-addon)

Click [here](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/7/00.DigSandboxExamples.zip) to download a complete set of example code.

Need a little quick reference guide to Arduino? Download our Digital Sandbox / Arduino [Quick Reference (Cheatsheet)](https://cdn.sparkfun.com/assets/learn_tutorials/2/6/7/Arduino_Cheatsheet_DigitalSandbox.pdf)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft267&name=Digital+Sandbox+Arduino+Companion "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft267 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Digital+Sandbox+Arduino+Companion&url=http%3A%2F%2Fsfe.io%2Ft267&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft267&t=Digital+Sandbox+Arduino+Companion "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft267&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F2%2F6%2F7%2FDS_cover_graphic_red.png&description=Digital+Sandbox+Arduino+Companion "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/all) [Next Page →\
[What is the Digital Sandbox?]](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/what-is-the-digital-sandbox)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/introduction) [What is the Digital Sandbox?](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/what-is-the-digital-sandbox) [Setup](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/setup) [0. Setup and Loop](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/0-setup-and-loop) [1. Exploring Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/1-exploring-blink) [2. Multi-Blink](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/2-multi-blink) [3. Dimming (the Hard Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/3-dimming-the-hard-way) [4. Dimming (the Easy Way)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/4-dimming-the-easy-way) [5. Color Mixing](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/5-color-mixing) [6. Number Storage with Variables](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/6-number-storage-with-variables) [7. If This Then That](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/7-if-this-then-that) [8. The Reaction Tester](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/8-the-reaction-tester) [9. Serial Calculator](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/9-serial-calculator) [10. Do the Analog Slide](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/10-do-the-analog-slide) [11. Automatic Night Light](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/11-automatic-night-light) [12. Thermal Alert!](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/12-thermal-alert) [13. Sound Detecting](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/13-sound-detecting) [14. Opto-Theremin (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/14-opto-theremin-addon) [15. Serial Motoring (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/15-serial-motoring-addon) [16. Servo Sweeper (Addon)](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/16-servo-sweeper-addon) [Resources and Going Further](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/resources--going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/discuss) [Single Page](https://learn.sparkfun.com/tutorials/digital-sandbox-arduino-companion/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Digital Sandbox](https://learn.sparkfun.com/tutorials/tags/digital-sandbox)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]