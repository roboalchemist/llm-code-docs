# Source: https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Graph Sensor Data with Python and Matplotlib

# Graph Sensor Data with Python and Matplotlib

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft798&name=Graph+Sensor+Data+with+Python+and+Matplotlib "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft798 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Graph+Sensor+Data+with+Python+and+Matplotlib&url=http%3A%2F%2Fsfe.io%2Ft798&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft798&t=Graph+Sensor+Data+with+Python+and+Matplotlib "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft798&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F9%2F8%2Ftemplivefast1.gif&description=Graph+Sensor+Data+with+Python+and+Matplotlib "Pin It")

## Introduction

[Python](https://www.sparkfun.com/python) is a wonderful high-level programming language that lets us quickly capture data, perform calculations, and even make simple drawings, such as graphs. Several graphical libraries are available for us to use, but we will be focusing on [matplotlib](https://matplotlib.org/) in this guide. Matplotlib was created as a plotting tool to rival those found in other software packages, such as [MATLAB](https://www.mathworks.com/products/matlab.html). Creating 2D graphs to demonstrate mathematical concepts, visualize statistics, or monitor sensor data can be accomplished in just a few lines of code with matplotlib.

[![Graphing temperature data with Python and matplotlib](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/9/8/Matplotlib_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/9/8/Matplotlib_Tutorial-02.jpg)

The [Raspberry Pi](https://www.sparkfun.com/raspberry_pi) is a great platform for connecting sensors (thanks to the exposed GPIO pins), collecting data via Python, and displaying live plots on a monitor.

**Notice:** This tutorial was written with Raspbian version \"June 2018\" and Python version 3.5.3. Other versions may affect how some of the steps in this guide are performed.

### Required Materials

To work through the activities in this tutorial, you will need a few pieces of hardware:

**Note:** As an alternative, you could also use the the Qwiic cables and the Qwiic TMP102 to easily connect without needing to solder or connect to the four pins.\
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

You have several options when it comes to working with the Raspberry Pi. Most commonly, the Pi is used as a standalone computer, which requires a monitor, keyboard, and mouse (listed below). To save on costs, the Pi can also be used as a *headless* computer (without a monitor, keyboard, and mouse).

Note that for this tutorial, you will need access to the Raspbian (or other Linux) graphical interface (known as the *desktop*). As a result, the two recommended ways to interact with your Pi is through a monitor, keyboard, and mouse or by using [Virtual Network Computing (VNC)](https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc).

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

At the bare minimum, you need a breadboard and some jumper wires to connect the Pi to the TMP102 sensor. However, the Pi Wedge and some M/M jumper wires may make prototyping easier.

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![SparkFun Pi Wedge](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/1/3/13717-Pi_Wedge.jpg)](https://www.sparkfun.com/sparkfun-pi-wedge.html)

### [SparkFun Pi Wedge](https://www.sparkfun.com/sparkfun-pi-wedge.html) 

[ BOB-13717 ]

This is the SparkFun Pi Wedge, a small board that connects to the 40-pin GPIO connector on the Raspberry Pi and breaks the pi...

[ [\$13.50] ]

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[] **Please note:** If you have trouble seeing any of the images throughout this tutorial, feel free to click on it to get a better look!

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft798&name=Graph+Sensor+Data+with+Python+and+Matplotlib "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft798 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Graph+Sensor+Data+with+Python+and+Matplotlib&url=http%3A%2F%2Fsfe.io%2Ft798&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft798&t=Graph+Sensor+Data+with+Python+and+Matplotlib "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft798&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F7%2F9%2F8%2Ftemplivefast1.gif&description=Graph+Sensor+Data+with+Python+and+Matplotlib "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/all) [Next Page →\
[Prepare Your Pi]](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/prepare-your-pi)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/introduction) [Prepare Your Pi](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/prepare-your-pi) [Hardware Assembly](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/hardware-assembly) [Introduction to Matplotlib](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/introduction-to-matplotlib) [Plot Sensor Data](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/plot-sensor-data) [Update a Graph in Real Time](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time) [Speeding Up the Plot Animation](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/speeding-up-the-plot-animation) [Resources and Going Further](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/discuss) [Single Page](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/all) [Print]

- **Tags**
- - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]