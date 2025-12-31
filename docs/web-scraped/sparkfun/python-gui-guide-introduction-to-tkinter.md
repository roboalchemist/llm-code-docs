# Source: https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Python GUI Guide: Introduction to Tkinter

# Python GUI Guide: Introduction to Tkinter

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft803&name=Python+GUI+Guide%3A+Introduction+to+Tkinter "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft803 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Python+GUI+Guide%3A+Introduction+to+Tkinter&url=http%3A%2F%2Fsfe.io%2Ft803&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft803&t=Python+GUI+Guide%3A+Introduction+to+Tkinter "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft803&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F0%2F3%2FTkinter_Tutorial-05.jpg&description=Python+GUI+Guide%3A+Introduction+to+Tkinter "Pin It")

## Introduction

[Python](https://www.sparkfun.com/python) is generally more popular as a sequential programming language that is called from the command line interface (CLI). However, several frameworks exist that offer the ability to create slick graphical user interfaces (GUI) with Python. Combined with a single board computer, like the Raspberry Pi, this ability to build GUIs opens up new possibilities to create your own dashboard for watching metrics, explore virtual instrumentation (like LabVIEW), or make pretty buttons to control your hardware.

[![Raspberry Pi with sensor dashboard and live plot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/3/Tkinter_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/3/Tkinter_Tutorial-05.jpg)

In this tutorial, we\'ll go through the basics of Tkinter (pronounced \"Tee-Kay-Inter\", as it\'s the \"TK Interface\" framework), which is the default GUI package that comes bundled with Python. Other frameworks exist, such as [wxPython](https://wxpython.org/), [PyQt](https://riverbankcomputing.com/software/pyqt/intro), and [Kivy](https://kivy.org/). While some of these might be more powerful, Tkinter is easy to learn, comes with Python, and shares the same open source license as Python.

Later in the tutorial, we\'ll show how to control various pieces of hardware from a Tkinter GUI and then how to pull a [Matplotlib](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib) graph into an interface. The first part of the tutorial (Tkinter basics) can be accomplished on any computer without special hardware. The parts that require controlling hardware or reading from a sensor will be shown on a [Raspberry Pi](https://www.sparkfun.com/products/14643).

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

### Prepare the Software

Before diving in to Tkinter and connecting hardware, you\'ll need to install and configure a few pieces of software. You can work through the first example with just Python, but you\'ll need a Raspberry Pi for the other sections that involve connecting hardware (we\'ll be using the RPi.GPIO and SMBus packages).

Tkinter comes with Python. If Python is installed, you will automatically have access to the the Tkinter package.

Follow the steps outlined in the [Prepare Your Pi section of the Graph Sensor Data with Python and Matplotlib tutorial](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/prepare-your-pi) to install Raspbian and configure Python 3. You will only need to perform the last \"Install Dependencies\" step if you plan to replicate the final example in this guide (integrating Matplotlib with Tkinter).

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/raspberry-gpio)

### Raspberry gPIo 

How to use either Python or C++ to drive the I/O lines on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/preassembled-40-pin-pi-wedge-hookup-guide)

### Preassembled 40-pin Pi Wedge Hookup Guide 

Using the Preassembled Pi Wedge to prototype with the Raspberry Pi B+.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-raspberry-pi-zero-wireless)

### Getting Started with the Raspberry Pi Zero Wireless 

Learn how to setup, configure and use the smallest Raspberry Pi yet, the Raspberry Pi Zero - Wireless.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[](https://learn.sparkfun.com/tutorials/how-to-use-remote-desktop-on-the-raspberry-pi-with-vnc)

### How to Use Remote Desktop on the Raspberry Pi with VNC 

Use RealVNC to connect to your Raspberry Pi to control the graphical desktop remotely across the network.

[](https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib)

### Graph Sensor Data with Python and Matplotlib 

Use matplotlib to create a real-time plot of temperature data collected from a TMP102 sensor connected to a Raspberry Pi.

[] **Please note:** If you have trouble seeing any of the images throughout this tutorial, feel free to click on it to get a better look!

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft803&name=Python+GUI+Guide%3A+Introduction+to+Tkinter "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft803 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Python+GUI+Guide%3A+Introduction+to+Tkinter&url=http%3A%2F%2Fsfe.io%2Ft803&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft803&t=Python+GUI+Guide%3A+Introduction+to+Tkinter "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft803&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F0%2F3%2FTkinter_Tutorial-05.jpg&description=Python+GUI+Guide%3A+Introduction+to+Tkinter "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/all) [Next Page →\
[Hello, World!]](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/hello-world)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/introduction) [Hello, World!](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/hello-world) [Tkinter Overview](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/tkinter-overview) [Experiment 1: Temperature Converter](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/experiment-1-temperature-converter) [Experiment 2: Lights and Buttons](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/experiment-2-lights-and-buttons) [Experiment 3: Sensor Dashboard](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/experiment-3-sensor-dashboard) [Resources and Going Further](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/resources-and-going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/discuss) [Single Page](https://learn.sparkfun.com/tutorials/python-gui-guide-introduction-to-tkinter/all) [Print]

- **Tags**
- - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]