# Source: https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun Inventor\'s Kit Experiment Guide - v4.0

# SparkFun Inventor\'s Kit Experiment Guide - v4.0

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1b00b259d107c598ffacb3664a190c26?d=retro&s=20&r=pg) Joel_E_B]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft728&name=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft728 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0&url=http%3A%2F%2Fsfe.io%2Ft728&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft728&t=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft728&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F2%2F8%2FSIK_Project5_Circuit5C_Action1.jpg&description=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Pin It")

## Introduction

Please note that this tutorial is for the SparkFun Inventor\'s Kit version 4.0 using the RedBoard with FTDI. If you are using version 4.1, please refer to the [tutorial using the RedBoard Qwiic and CH340](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41). The overall functionality of the circuits used in the kits are the same between v4.0 and v4.1.\
\
If you have SIK v3.3 or are using parts from the [add-on pack](https://www.sparkfun.com/products/14310), please refer to [this tutorial](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v33).

The SparkFun Inventor\'s Kit (SIK) is your map for navigating the waters of beginning embedded electronics. This guide contains all the information you will need to build five projects encompassing the 16 circuits of the SIK. At the center of this guide is one core philosophy: that anyone can (and should) play around with electronics. When you're done with this guide, you will have built five projects and acquired the know-how to create countless more. Now enough talk --- let's start something!

The print version of this guide is available as a PDF as well. Click the following link to download it. Keep in mind that the original file size used for the printed guidebook was reduced for the web. While the file size was reduced, it is still about a 26MB download.

[Download SIK V4.0a Printed Guide (PDF, 25.9MB)](https://github.com/sparkfun/SIK_Guide/raw/master/English/SIK%20v4a%20Book%20WEB%20Low%20Res.pdf)

**Notice:** This online guide is kept up to date with all the most recent improvements and corrections. For users following along with the printed version of this guide, please visit [sparkfun.com/SIKerrata](https://www.sparkfun.com/SIKerrata) for any and all changes that may affect your experience while using the printed guide.

### Choosing a Kit

You should have one of the two following versions of the SIK. If you need a overview of the parts included in your kit, please click on the product link below.

[![SparkFun Inventor\'s Kit - v4.0](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/2/2/0/SIK_V4-Kit_Shot.jpg)](https://www.sparkfun.com/products/14265)

### [SparkFun Inventor\'s Kit - v4.0](https://www.sparkfun.com/products/14265) 

[ KIT-14265 ]

The fourth edition of our popular SIK, fully reworked from the ground up for a better learning experience!

**Retired**

[![SparkFun Inventor\'s Kit for Arduino Uno - v4.0](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/4/4/14418-SparkFun_Inventor_s_Kit_for_Arduino_Uno_-_v4.0-01.jpg)](https://www.sparkfun.com/products/14418)

### [SparkFun Inventor\'s Kit for Arduino Uno - v4.0](https://www.sparkfun.com/products/14418) 

[ KIT-14418 ]

The 4th edition of our popular SIK for Arduino Uno, fully reworked from the ground up for a better learning experience! Perfe...

**Retired**

The primary difference between the two kits is the microcontroller included in the kit. The SparkFun Inventor\'s Kit includes a [SparkFun RedBoard](https://www.sparkfun.com/products/12757), while the SparkFun Inventor\'s Kit for Arduino Uno includes an [Arduino Uno R3](https://www.sparkfun.com/products/11021). At the heart of each is the ATmega328p microcontroller, giving both the same functionality underneath the hood. Both development boards are capable of taking inputs (such as the push of a button or a reading from a light sensor) and interpreting that information to control various outputs (like a blinking LED light or an electric motor). And much, much more!

**Note:** The Arduino Uno version of the kit **does not** include a [carrying case](https://www.sparkfun.com/products/14474) or printed copy of this manual to decrease weight and cost for international shipping.

**Note:** You can complete all 16 experiments in this guide with either kit.

If you need more information to determine which microcontroller is right for you, please check out the following tutorials.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

February 26, 2013

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/redboard-hookup-guide)

### RedBoard Hookup Guide 

January 7, 2014

How to get your RedBoard up-and-blinking!

### Open Source!

At SparkFun, our engineers and educators have been improving this kit and coming up with new experiments for a long time now. We would like to give attribution to [Oomlout](http://oomlout.com/), since we originally started working off their Arduino Kit material many years ago. The Oomlut version is licensed under the [Creative Commons Attribution Share-Alike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/).

The SparkFun Inventor\'s Kit V4.0 is licensed under the [Creative Commons Attribution Share-Alike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft728&name=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft728 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0&url=http%3A%2F%2Fsfe.io%2Ft728&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft728&t=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft728&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F2%2F8%2FSIK_Project5_Circuit5C_Action1.jpg&description=SparkFun+Inventor%27s+Kit+Experiment+Guide+-+v4.0 "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/all) [Next Page →\
[Baseplate Assembly]](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/baseplate-assembly)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/introduction) [Baseplate Assembly](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/baseplate-assembly) [The SparkFun RedBoard](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/the-sparkfun-redboard) [Understanding Breadboards](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/understanding-breadboards-) [Install the Arduino IDE and SIK Code](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/install-the-arduino-ide-and-sik-code) [Project 1: Light](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-1-light) [Circuit 1A: Blink an LED](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-1a-blink-an-led) [Circuit 1B: Potentiometer](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-1b-potentiometer) [Circuit 1C: Photoresistor](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-1c-photoresistor) [Circuit 1D: RGB Night-Light](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-1d-rgb-night-light) [Project 2: Sound](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-2-sound) [Circuit 2A: Buzzer](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-2a-buzzer) [Circuit 2B: Digital Trumpet](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-2b-digital-trumpet) [Circuit 2C: Simon Says Game](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-2c-simon-says-game-) [Project 3: Motion](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-3-motion) [Circuit 3A: Servo Motors](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-3a-servo-motors) [Circuit 3B: Distance Sensor](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-3b-distance-sensor) [Circuit 3C: Motion Alarm](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-3c-motion-alarm) [Project 4: Display](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-4-display) [Circuit 4A: LCD \"Hello, World!\"](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-4a-lcd-hello-world) [Circuit 4B: Temperature Sensor](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-4b-temperature-sensor) [Circuit 4C: DIY Who Am I? Game](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-4c-diy-who-am-i-game) [Project 5: Robot](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/project-5-robot) [Circuit 5A: Motor Basics](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-5a-motor-basics) [Circuit 5B: Remote-Controlled Robot](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-5b-remote-controlled-robot) [Circuit 5C: Autonomous Robot](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/circuit-5c-autonomous-robot) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/resources-and-going-further)

[Comments [3]](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v40/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Audio](https://learn.sparkfun.com/tutorials/tags/audio)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Game](https://learn.sparkfun.com/tutorials/tags/game)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Mechanical](https://learn.sparkfun.com/tutorials/tags/mechanical)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Start a Project](https://learn.sparkfun.com/tutorials/tags/start-a-project)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]