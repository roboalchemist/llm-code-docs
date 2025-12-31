# Source: https://learn.sparkfun.com/tutorials/blynk-board-project-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Blynk Board Project Guide

# Blynk Board Project Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft490&name=Blynk+Board+Project+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft490 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Blynk+Board+Project+Guide&url=http%3A%2F%2Fsfe.io%2Ft490&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft490&t=Blynk+Board+Project+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft490&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F9%2F0%2Fmaterials-01-iot-kit.jpg&description=Blynk+Board+Project+Guide "Pin It")

## Introduction

So you\'ve provisioned your [SparkFun Blynk Board](https://www.sparkfun.com/products/13794) \-- connected it to your Wi-Fi network and started using the zeRGBa to control the RGB LED \-- now what? Time to build some projects!

[![BotaniTweet project in action](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/9/0/12-01-project.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/9/0/12-01-project.jpg)

*[Project 12](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-12-botanitweeting) of this guide: creating a sentient, tweeting plant.*

This tutorial will walk you through fourteen Blynk projects, which range from blinking an LED with a smartphone to setting up a tweeting, moisture-sensing house plant.

This tutorial follows our \"Getting Started with the SparkFun Blynk Board\" tutorial, which demonstrates how to **provision your Blynk Board** and get it connected to a **Blynk project**.

Have you **just powered up your Blynk Board?** You need to get your board on Wi-Fi first! Head over to the [Getting Started tutorial](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board) to learn how.

\

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board)

### Getting Started with the SparkFun Blynk Board 

March 25, 2016

How to provision a Blynk Board - get it connected to Wi-Fi and Blynk, so you can start Blynking!

All of the projects in this guide are **pre-loaded into the Blynk Board**. That means you don\'t have to write any code \-- just drag and drop some Blynk widgets, configure some settings and play! This tutorial will help familiarize you with both the Blynk Board hardware and the Blynk app, so, once you\'re ready, you can jump into [customizing the Blynk Board code](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide) and creating a project of your own.

#### Suggested Reading

We\'ll be (over-)using electrical engineering terms like \"voltage\", \"digital\", \"analog\", and \"signal\" throughout this tutorial, but that doesn\'t mean you need to be an electrical engineer to know what they mean.

We pride ourselves on our comprehensive list of conceptual tutorials, which cover topics ranging from basics, like [What is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity) or [Voltage, Current, Resistance, and Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) to more advanced tutorials, like [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels) and [I^2^C](https://learn.sparkfun.com/tutorials/i2c).

\

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

The fundamental components of electricity, and the law that rules them all!

[ [[ [] [Favorited] ] [ [] [Favorite] ]](# "Add to favorites") [16] ]

[](https://learn.sparkfun.com/tutorials/what-is-electricity)

### What is Electricity? 

Not an easy question, but in this tutorial we will shed some light on what is electricity!

[ [[ [] [Favorited] ] [ [] [Favorite] ]](# "Add to favorites") [9] ]

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3 V and 5 V devices.

[ [[ [] [Favorited] ] [ [] [Favorite] ]](# "Add to favorites") [8] ]

[](https://learn.sparkfun.com/tutorials/i2c)

### I^2^C 

An introduction to I^2^C -- one of the main embedded communications protocols in use today.

[ [[ [] [Favorited] ] [ [] [Favorite] ]](# "Add to favorites") [16] ]

We\'ll link to tutorials as we introduce new concepts throughout this tutorial. If you ever feel like you\'re in too deep, take a detour through some of those first!

------------------------------------------------------------------------

Before we really dive into those projects, though, let\'s familiarize ourselves with the Blynk Board and all of the components it features. Click the \"Next Page\" button below to proceed to the [Blynk Board Overview section](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/blynk-board-overview) (or click \"View as Single Page\" to load the entire tutorial in all of its glory).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft490&name=Blynk+Board+Project+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft490 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Blynk+Board+Project+Guide&url=http%3A%2F%2Fsfe.io%2Ft490&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft490&t=Blynk+Board+Project+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft490&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F9%2F0%2Fmaterials-01-iot-kit.jpg&description=Blynk+Board+Project+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/all) [Next Page →\
[Blynk Board Overview]](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/blynk-board-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/introduction) [Blynk Board Overview](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/blynk-board-overview) [Recommended Materials](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/recommended-materials) [Project 1: Blynk Button, Physical LED](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-1-blynk-button-physical-led) [Project 2: Physical Button, Blynk LED](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-2-physical-button-blynk-led) [Project 3: Slide-Dimming LEDs](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-3-slide-dimming-leds) [Project 4: Temperature and Humidity Values](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-4-temperature-and-humidity-values) [Project 5: Gauging the Analog-to-Digital Converter](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-5-gauging-the-analog-to-digital-converter) [Project 6: Automating With the Timer](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-6-automating-with-the-timer) [Project 7: The LCD\'s Wealth of Information](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-7-the-lcds-wealth-of-information) [Project 8: Joystick Joyride](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-8-joystick-joyride) [Project 9: Graphing Voltage](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-9-graphing-voltage) [Project 10: Charting Lighting History](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-10-charting-lighting-history) [Project 11: Terminal Chat](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-11-terminal-chat) [Project 12: BotaniTweeting](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-12-botanitweeting) [Project 13: Push Door, Push Phone](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-13-push-door-push-phone) [Project 14: Status Emails](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/project-14-status-emails) [Resources and Going Further](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/resources--going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/blynk-board-project-guide/all) [Print]

- **Tags**
- - [Blynk](https://learn.sparkfun.com/tutorials/tags/blynk)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [ESP8266](https://learn.sparkfun.com/tutorials/tags/esp8266)
  - [Input Devices](https://learn.sparkfun.com/tutorials/tags/input-devices)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]