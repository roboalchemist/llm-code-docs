# Source: https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Wireless Remote Weather Station with micro:bit

# Wireless Remote Weather Station with micro:bit

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1173&name=Wireless+Remote+Weather+Station+with+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1173 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+Remote+Weather+Station+with+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft1173&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1173&t=Wireless+Remote+Weather+Station+with+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1173&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F3%2Fmicrobit_wireless_weather_station_thumb.gif&description=Wireless+Remote+Weather+Station+with+micro%3Abit "Pin It")

## Introduction

In this tutorial, we will utilize MakeCode\'s radio blocks to have one [micro:bit](https://www.sparkfun.com/products/14208) transmit a signal to a receiving micro:bit on the same channel! This is useful if your weather station is installed in a location that is difficult to retrieve data from the OpenLog. We will explore a few different ways to send and receive data.

[![Wireless Remote Weather Station with micro:bit Demo](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/3/Micro-Bit_Wireless_Weather_Station_Datalogging_RTC_Demo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/3/Micro-Bit_Wireless_Weather_Station_Datalogging_RTC_Demo.gif)

### Required Materials

To follow along with this tutorial, you will need the following materials at a minimum. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

This project tutorial builds on the experiments from the micro:climate kit. Make sure you check out the guide before proceeding.

[](https://learn.sparkfun.com/tutorials/microclimate-kit-experiment-guide)

### micro:climate Kit Experiment Guide 

July 21, 2017

A weather station kit that is built on top of the inexpensive, easy-to-use micro:bit and Microsoft MakeCode.

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit)

### Getting Started with the micro:bit 

The BBC micro:bit is a compact, powerful programming tool that requires no software installation. Read on to learn how to use it YOUR way!

[](https://learn.sparkfun.com/tutorials/microbit-breakout-board-hookup-guide)

### micro:bit Breakout Board Hookup Guide 

How to get started with the micro:bit breakout board.

[](https://learn.sparkfun.com/tutorials/sparkfun-gatorrtc-hookup-guide)

### SparkFun gator:RTC Hookup Guide 

The gator:RTC is an I2C based, real-time clock (RTC) for keeping time while your micro:bit isn\'t powered. This tutorial will get you started using the gator:RTC with the micro:bit platform.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1173&name=Wireless+Remote+Weather+Station+with+micro%3Abit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1173 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Wireless+Remote+Weather+Station+with+micro%3Abit&url=http%3A%2F%2Fsfe.io%2Ft1173&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1173&t=Wireless+Remote+Weather+Station+with+micro%3Abit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1173&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F3%2Fmicrobit_wireless_weather_station_thumb.gif&description=Wireless+Remote+Weather+Station+with+micro%3Abit "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/all) [Next Page →\
[Installing the Extensions for Microsoft MakeCode]](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/installing-the-extensions-for-microsoft-makecode)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/introduction) [Installing the Extensions for Microsoft MakeCode](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/installing-the-extensions-for-microsoft-makecode) [Experiment 1: Sending and Receiving a Signal](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/experiment-1-sending-and-receiving-a-signal) [Experiment 2: Wireless Remote Weather Data](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/experiment-2-wireless-remote-weather-data) [Experiment 3: Checking Sensor Data with Arrays](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/experiment-3-checking-sensor-data-with-arrays) [Experiment 4: Wireless Remote Weather Data (Revisited)](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/experiment-4-wireless-remote-weather-data-revisited) [Experiment 5: Real Time Wireless Data Logging](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/experiment-5-real-time-wireless-data-logging) [Coding Challenges](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/coding-challenges) [Troubleshooting](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/discuss) [Single Page](https://learn.sparkfun.com/tutorials/wireless-remote-weather-station-with-microbit/all) [Print]

- **Tags**
- - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [MakeCode](https://learn.sparkfun.com/tutorials/tags/makecode)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [pxt](https://learn.sparkfun.com/tutorials/tags/pxt)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]