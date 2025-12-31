# Source: https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Wireless Remote Control with micro:bit

# Wireless Remote Control with micro:bit

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft850&name=Wireless+Remote+Control+with+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft850 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+Remote+Control+with+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft850&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft850&t=Wireless+Remote+Control+with+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft850&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F8%2F5%2F0%2FWireless_Remote_micro-bot_MicroBit_Forward_Test.gif&description=Wireless+Remote+Control+with+micro%3Abit "Pin It")

## Introduction

In this tutorial, we will utilize MakeCode\'s radio blocks to have one [micro:bit](https://www.sparkfun.com/products/14208) transmit a signal to a receiving micro:bit on the same channel. Eventually, we will control a [micro:bot](https://www.sparkfun.com/products/14216) wirelessly using parts from the [micro:arcade](https://www.sparkfun.com/products/14218) kit!

[![Wireless Remote Control with micro:bit](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/0/Wireless_Remote_micro-bot_Battle_Bot_MicroBit.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/5/0/Wireless_Remote_micro-bot_Battle_Bot_MicroBit.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### You Will Also Need

The following materials are optional to make a battle bot.

- Scissors
- Electrical Tape or Glue
- Ping Pong Ball
- Skewers

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

[](https://learn.sparkfun.com/tutorials/microbot-kit-experiment-guide)

### micro:bot Kit Experiment Guide 

Get started with the moto:bit, a carrier board for the micro:bit that allows you to control motors, and create your own robot using this experiment guide for the micro:bot kit.

[](https://learn.sparkfun.com/tutorials/microarcade-kit-experiment-guide)

### micro:arcade Kit Experiment Guide 

We love games! We love writing games, building games and yes, even building game consoles. So we want to introduce to you the micro:arcade kit for the micro:bit!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft850&name=Wireless+Remote+Control+with+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft850 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+Remote+Control+with+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft850&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft850&t=Wireless+Remote+Control+with+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft850&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F8%2F5%2F0%2FWireless_Remote_micro-bot_MicroBit_Forward_Test.gif&description=Wireless+Remote+Control+with+micro%3Abit "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/all) [Next Page →\
[Installing the Extensions for Microsoft MakeCode]](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/installing-the-extensions-for-microsoft-makecode)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/introduction) [Installing the Extensions for Microsoft MakeCode](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/installing-the-extensions-for-microsoft-makecode) [Experiment 1: Sending and Receiving a Signal](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/experiment-1-sending-and-receiving-a-signal) [Experiment 2: Wirelessly Driving Forward](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/experiment-2-wirelessly-driving-forward) [Experiment 3: Wirelessly Controlling the micro:bot](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/experiment-3-wirelessly-controlling-the-microbot) [Coding Challenges](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/coding-challenges) [Troubleshooting](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/discuss) [Single Page](https://learn.sparkfun.com/tutorials/wireless-remote-control-with-microbit/all) [Print]

- **Tags**
- - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [pxt](https://learn.sparkfun.com/tutorials/tags/pxt)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]