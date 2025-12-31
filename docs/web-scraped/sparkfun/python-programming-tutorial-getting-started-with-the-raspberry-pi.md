# Source: https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Python Programming Tutorial: Getting Started with the Raspberry Pi

# Python Programming Tutorial: Getting Started with the Raspberry Pi

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft783&name=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft783 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi&url=http%3A%2F%2Fsfe.io%2Ft783&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft783&t=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft783&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F8%2F3%2FPython_Tutorial-08.jpg&description=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Pin It")

## Introduction

The [Raspberry Pi](https://www.sparkfun.com/raspberry_pi) is an amazing *single board computer* (SBC) capable of running Linux and a whole host of applications. [Python](https://www.sparkfun.com/python) is a beginner-friendly programming language that is used in schools, web development, scientific research, and in many other industries. This guide will walk you through writing your own programs with Python to blink lights, respond to button pushes, read sensors, and log data on the Raspberry Pi.

[![Speaker, button, and LED connected to a Raspberry Pi](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/3/Python_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/Python_Tutorial-08.jpg)

**Notice:** This tutorial was written with Raspbian version \"April 2018\" and Python version 3.5.3. Other versions may affect how some of the steps in this guide are performed.

### Required Materials

To work through the activities in this tutorial, you will need a few pieces of hardware:

**Note:** As an alternative for the I^2^C example, you could also use the the Qwiic cables and the Qwiic TMP102 to easily connect without needing to solder or connect to the four pins.\
\

[![SparkFun Digital Temperature Sensor - TMP102 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/0/7/16304-SparkFun_Digital_Temperature_Sensor_-_TMP102__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-tmp102-qwiic.html)

### [SparkFun Digital Temperature Sensor - TMP102 (Qwiic)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-tmp102-qwiic.html) 

[ SEN-16304 ]

The SparkFun TMP102 Qwiic is an easy-to-use digital temperature sensor equipped with a couple of Qwiic connectors for easy I2...

[ [\$8.23] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Optional Materials

You have several options when it comes to working with the Raspberry Pi. Most commonly, the Pi is used as a standalone computer, which requires a monitor, keyboard, and mouse (listed below). To save on costs, the Pi can also be used as a *headless* computer (without a monitor, keyboard, and mouse). This setup has a slightly more difficult learning curve, as you will need to use the *command-line interface* (CLI) from another computer.

[![Raspberry Pi LCD - 7\" Touchscreen](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/4/13733-01.jpg)](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html)

### [Raspberry Pi LCD - 7\" Touchscreen](https://www.sparkfun.com/raspberry-pi-lcd-7-touchscreen.html) 

[ LCD-13733 ]

This 7\" Raspberry Pi Touchscreen LCD provides you with the ability to create a standalone device that can be utilized as a cu...

[ [\$88.30] ]

[![Multimedia Wireless Keyboard](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/2/6/14271-02.jpg)](https://www.sparkfun.com/multimedia-wireless-keyboard.html)

### [Multimedia Wireless Keyboard](https://www.sparkfun.com/multimedia-wireless-keyboard.html) 

[ WIG-14271 ]

With Single-Board Computers (SBCs) on the rise, it is a good idea to have an easy way to interface with them. Operating on a ...

[\$29.95] [ [\$19.95] ]

[![SmartiPi Touch](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/9/14059-06.jpg)](https://www.sparkfun.com/products/14059)

### [SmartiPi Touch](https://www.sparkfun.com/products/14059) 

[ PRT-14059 ]

The SmartiPi Touch is a case and stand for the official \[Raspberry Pi 7\" Touchscreen LCD\](https://www.sparkfun.com/products/1...

**Retired**

[] **Please note:** If you have trouble seeing any of the images throughout this tutorial, feel free to click on it to get a better look!

### Open Source!

This guide is licensed under the [Creative Commons Attribution Share-Alike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft783&name=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft783 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi&url=http%3A%2F%2Fsfe.io%2Ft783&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft783&t=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft783&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F7%2F8%2F3%2FPython_Tutorial-08.jpg&description=Python+Programming+Tutorial%3A+Getting+Started+with+the+Raspberry+Pi "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all) [Next Page →\
[Install the OS]](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/install-the-os)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/introduction) [Install the OS](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/install-the-os) [Configure Your Pi](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/configure-your-pi) [Hello, World!](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/hello-world) [Programming in Python](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/programming-in-python) [Experiment 1: Digital Input and Output](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-1-digital-input-and-output) [Experiment 2: Play Sounds](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-2-play-sounds) [Experiment 3: SPI and Analog Input](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input) [Experiment 4: I2C Temperature Sensor](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-4-i2c-temperature-sensor) [Experiment 5: File Reading and Writing](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-5-file-reading-and-writing) [Resources and Going Further](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/discuss) [Single Page](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all) [Print]

- **Tags**
- - [Concepts](https://learn.sparkfun.com/tutorials/tags/concepts)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]