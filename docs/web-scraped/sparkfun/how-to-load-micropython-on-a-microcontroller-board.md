# Source: https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- How to Load MicroPython on a Microcontroller Board

# How to Load MicroPython on a Microcontroller Board

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft809&name=How+to+Load+MicroPython+on+a+Microcontroller+Board "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft809 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Load+MicroPython+on+a+Microcontroller+Board&url=http%3A%2F%2Fsfe.io%2Ft809&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft809&t=How+to+Load+MicroPython+on+a+Microcontroller+Board "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft809&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F0%2F9%2FPython_Images-02.jpg&description=How+to+Load+MicroPython+on+a+Microcontroller+Board "Pin It")

## Introduction

MicroPython is a subset of the Python 3 language that has been pared down to run efficiently on several microcontrollers. If you are familiar with Python or looking for a quick way to write code for a microcontroller (that isn\'t C/C++, Arduino, or assembly), MicroPython is a good option.

Some development boards, like the pyboard and micro:bit, are capable of running MicroPython out of the box. Others, like the Teensy or ESP32, will require that you load the MicroPython interpreter onto the board first before it will run your MicroPython code.

**The more you know!** If you are not familiar with an interpreter, it is a program that executes instructions from a programming language without requiring those instructions to be previously compiled into machine language. See [this article](https://en.wikipedia.org/wiki/Interpreter_(computing)) to learn more.

[![Boards that run MicroPython](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/9/Python_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/9/Python_Images-02.jpg)

To use this guide, find your development board under the table of contents, navigate to that page, and follow the instructions to get MicroPython working on it.

[] Click on any of the images in this tutorial for a closer look!

![Python Logo](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/3/python-logo-gray-bg.jpg)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft809&name=How+to+Load+MicroPython+on+a+Microcontroller+Board "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft809 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Load+MicroPython+on+a+Microcontroller+Board&url=http%3A%2F%2Fsfe.io%2Ft809&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft809&t=How+to+Load+MicroPython+on+a+Microcontroller+Board "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft809&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F0%2F9%2FPython_Images-02.jpg&description=How+to+Load+MicroPython+on+a+Microcontroller+Board "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/all) [Next Page →\
[pyboard]](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/pyboard)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/introduction) [pyboard](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/pyboard) [ESP32 Thing](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/esp32-thing) [Teensy 3.x](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/teensy-3x) [micro:bit](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/microbit) [Pycom LoPy4](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/pycom-lopy4) [OpenMV M7 Camera](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/openmv-m7-camera) [Resources and Going Further](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/discuss) [Single Page](https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/all) [Print]

- **Tags**
- - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [ESP32](https://learn.sparkfun.com/tutorials/tags/esp32)
  - [microbit](https://learn.sparkfun.com/tutorials/tags/microbit)
  - [micro:bit](https://learn.sparkfun.com/tutorials/tags/micro-bit)
  - [micropython](https://learn.sparkfun.com/tutorials/tags/micropython)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)
  - [Teensy](https://learn.sparkfun.com/tutorials/tags/teensy)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]