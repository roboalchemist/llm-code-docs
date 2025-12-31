# Source: https://learn.sparkfun.com/tutorials/terminal-basics

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Serial Terminal Basics

# Serial Terminal Basics

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1b00b259d107c598ffacb3664a190c26?d=retro&s=20&r=pg) Joel_E_B], [![](https://cdn.sparkfun.com/avatar/3d3509851c3a5223dbe27da5fddd33df?d=retro&s=20&r=pg) jimblom], [ maettu_this]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft112&name=Serial+Terminal+Basics "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft112 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Serial+Terminal+Basics&url=http%3A%2F%2Fsfe.io%2Ft112&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft112&t=Serial+Terminal+Basics "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft112&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F2%2FterminalThumb.jpg&description=Serial+Terminal+Basics "Pin It")

## Serial Terminal Overview

COM ports. Baud rate. Flow control. Tx. Rx. These are all words that get thrown around a lot when working with electronics, especially microcontrollers. For someone who isn\'t familiar with these terms and the context in which they are used, they can be confusing at times. This tutorial is here to help you understand what these terms mean and how they form the larger picture that is serial communication over a terminal.

In short, serial terminal programs make working with microcontrollers that much simpler. They allow you to see data sent to and from your microcontroller, and that data can be used for a number of reasons including troubleshooting/debugging, communication testing, calibrating sensors, configuring modules, and data monitoring. Once you have learned the ins and outs of a terminal application, it can be a very powerful tool in your electronics and programming arsenal.

### Covered in this Tutorial

There are lots of different terminal programs out there, and they all have their pros and cons. In this tutorial we will discuss what a terminal is, which terminal programs are best suited for certain situations and operating systems, and how to configure and use each program.

### Suggested Reading

You should be familiar with these topics before diving into this tutorial. If you need a refresher, feel free to pop on over to these links. We\'ll be right here waiting.

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)
- [Binary](https://learn.sparkfun.com/tutorials/binary)
- [Hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal)
- [ASCII](https://learn.sparkfun.com/tutorials/ascii)
- [Installing FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)
- [RS-232 vs TTL Serial Communication](https://www.sparkfun.com/tutorials/215)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics) particularly the [USB section](https://learn.sparkfun.com/tutorials/connector-basics/usb-connectors)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft112&name=Serial+Terminal+Basics "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft112 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Serial+Terminal+Basics&url=http%3A%2F%2Fsfe.io%2Ft112&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft112&t=Serial+Terminal+Basics "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft112&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F2%2FterminalThumb.jpg&description=Serial+Terminal+Basics "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/terminal-basics/all) [Next Page →\
[What is a Terminal?]](https://learn.sparkfun.com/tutorials/terminal-basics/what-is-a-terminal)

← Previous Page

[**Pages**] [Serial Terminal Overview](https://learn.sparkfun.com/tutorials/terminal-basics/serial-terminal-overview) [What is a Terminal?](https://learn.sparkfun.com/tutorials/terminal-basics/what-is-a-terminal) [Basic Terminology](https://learn.sparkfun.com/tutorials/terminal-basics/basic-terminology-) [Connecting to Your Device](https://learn.sparkfun.com/tutorials/terminal-basics/connecting-to-your-device) [Arduino Serial Monitor (Windows, Mac, Linux)](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) [Hyperterminal (Windows)](https://learn.sparkfun.com/tutorials/terminal-basics/hyperterminal-windows) [Tera Term (Windows)](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows) [Real-Term (Windows)](https://learn.sparkfun.com/tutorials/terminal-basics/real-term-windows) [YAT - Yet Another Terminal (Windows)](https://learn.sparkfun.com/tutorials/terminal-basics/yat---yet-another-terminal-windows) [CoolTerm (Windows, Mac, Linux)](https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux) [ZTerm (Mac)](https://learn.sparkfun.com/tutorials/terminal-basics/zterm-mac) [Command Line (Windows, Mac, Linux)](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux) [Tips and Tricks](https://learn.sparkfun.com/tutorials/terminal-basics/tips-and-tricks) [Resources and Going Further](https://learn.sparkfun.com/tutorials/terminal-basics/res)

[Comments [9]](https://learn.sparkfun.com/tutorials/terminal-basics/discuss) [Single Page](https://learn.sparkfun.com/tutorials/terminal-basics/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]