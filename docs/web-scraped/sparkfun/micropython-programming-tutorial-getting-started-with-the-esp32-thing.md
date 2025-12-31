# Source: https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MicroPython Programming Tutorial: Getting Started with the ESP32 Thing

# MicroPython Programming Tutorial: Getting Started with the ESP32 Thing

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft659&name=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft659 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing&url=http%3A%2F%2Fsfe.io%2Ft659&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft659&t=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft659&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F5%2F9%2FMicroPython_Tutorial-02.jpg&description=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Pin It")

## Introduction

In this guide, we will walk through the process of setting up MicroPython on the [ESP32 Thing](https://www.sparkfun.com/products/13907) and writing some example programs. Each \"experiment\" will show you how to wire up an example circuit and then control it using MicroPython.

[![Running MicroPython on the ESP32 Thing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/5/9/MicroPython_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/5/9/MicroPython_Tutorial-02.jpg)

### What is MicroPython?

MicroPython is a lean implementation of the Python 3 programming language that has been pared down to run efficiently on microcontrollers. [Python](https://www.sparkfun.com/python) is a relatively simple (but powerful) language that is easy for beginners to pick up and has been gaining popularity in schools as an introductory language. MicroPython has nearly all of the features of Python, which means that interacting with hardware is now easily accessible to beginners and seasoned Python programmers alike.

### Why the ESP32 Thing?

MicroPython is supported on many different microcontroller platforms, and [more are being added](https://github.com/micropython/micropython/wiki/Boards-Summary) all the time. The ESP32 is a great tool for learning MicroPython, as it has a powerful controller (240 MHz) with lots of RAM (520 kB). Additionally, the ESP32 has a built-in WiFi module, which makes networking and connecting to the Internet quite easy. All this is packaged up into a development board for you on [SparkFun\'s ESP32 Thing](https://www.sparkfun.com/products/13907).

**Note:** This guide uses MicroPython version: esp32-20180822-v1.9.4-479.

### Required Materials

To work through the activities in this tutorial, you will need a few pieces of hardware:

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide)

### ESP32 Thing Hookup Guide 

An introduction to the ESP32 Thing\'s hardware features, and a primer on using the WiFi system-on-chip in Arduino.

[] **Please note:** If you have trouble seeing any of the images throughout this tutorial, feel free to click on it to get a better look!

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft659&name=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft659 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing&url=http%3A%2F%2Fsfe.io%2Ft659&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft659&t=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft659&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F5%2F9%2FMicroPython_Tutorial-02.jpg&description=MicroPython+Programming+Tutorial%3A+Getting+Started+with+the+ESP32+Thing "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/hardware-overview) [Setup](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/setup) [REPL (Hello, World!)](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/repl-hello-world) [Experiment 1: Digital Input and Output](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/experiment-1-digital-input-and-output) [Experiment 2: Pulse Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/experiment-2-pulse-width-modulation-pwm) [Experiment 3: Analog Input](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/experiment-3-analog-input) [Experiment 4: I2C](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/experiment-4-i2c) [Experiment 5: WiFi](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/experiment-5-wifi) [Troubleshooting](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/discuss) [Single Page](https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/all) [Print]

- **Tags**
- - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [micropython](https://learn.sparkfun.com/tutorials/tags/micropython)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]