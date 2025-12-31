# Source: https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Internet of Things Experiment Guide

# Internet of Things Experiment Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft594&name=Internet+of+Things+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft594 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Internet+of+Things+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft594&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft594&t=Internet+of+Things+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft594&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F5%2F9%2F4%2FDemo_Update_02.jpg&description=Internet+of+Things+Experiment+Guide "Pin It")

## Introduction

The Internet of Things (IoT) is the network of connected physical objects, such as vehicles, buildings and people. These objects, or \"things,\" are often embedded with electronics to include sensors, actuators and microcontrollers that enable the devices to sense the environment around them, log data in real time, communicate with services or other devices, and be remotely controlled.

The [SparkFun ESP8266 Thing Dev Board](https://www.sparkfun.com/products/13711) is a microcontroller board with a built-in WiFi radio, which makes it a fantastic development platform for IoT and home automation projects.

[![SparkFun ESP8266 Thing Dev Board](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/4/13711-01.jpg)](https://www.sparkfun.com/products/13711)

Lucky for us, we can use the Arduino IDE to program the Thing Dev Board, which makes life easy for programming and configuring our IoT projects. This guide will show you how to set up your Thing Dev Board and construct a few simple (but useful!) connected projects involving logging sensor data and controlling home appliances.

**Note:** Please be aware that this tutorial uses 3^rd^ party web services. The web site layout, service names, and/or services provided by these vendors may change over time. Unfortunately, we are not responsible for any of those changes and you may need to do some research online to work around the changes.

### Required Materials

To follow along with this tutorial, you\'ll need the following parts:

**Note:** Previously, this tutorial used the [PowerSwitch Tail II](https://www.sparkfun.com/products/retired/10747). It has been updated to use the IoT Power Relay.

### Suggested Reading

We recommend checking out the following guides before diving in with the IoT experiments:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/esp8266-thing-development-board-hookup-guide)

### ESP8266 Thing Development Board Hookup Guide 

An overview of SparkFun\'s ESP8266 Thing Development Board - a development board for the Internet of Things.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft594&name=Internet+of+Things+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft594 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Internet+of+Things+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft594&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft594&t=Internet+of+Things+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft594&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F5%2F9%2F4%2FDemo_Update_02.jpg&description=Internet+of+Things+Experiment+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/all) [Next Page →\
[Soldering and Arduino Setup]](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/soldering-and-arduino-setup)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/introduction) [Soldering and Arduino Setup](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/soldering-and-arduino-setup) [Configure ThingSpeak](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/configure-thingspeak) [Experiment 1: Temperature and Humidity Logging](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-1-temperature-and-humidity-logging) [Experiment 2: IoT Buttons](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-2-iot-buttons) [Experiment 3: Appliance Controller](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-3-appliance-controller) [Resources and Going Further](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/resources-and-going-further)

[Comments [5]](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [ESP8266](https://learn.sparkfun.com/tutorials/tags/esp8266)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]