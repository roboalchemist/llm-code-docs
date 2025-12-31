# Source: https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Using SparkFun Edge Board with Ambiq Apollo3 SDK

# Using SparkFun Edge Board with Ambiq Apollo3 SDK

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/92955b303c984cbfe9a72102a670afc7?d=retro&s=20&r=pg) Liquid Soulder]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft866&name=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft866 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK&url=http%3A%2F%2Fsfe.io%2Ft866&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft866&t=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft866&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F6%2F15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg&description=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Pin It")

## Introduction

The [SparkFun Edge Development Board](https://www.sparkfun.com/products/15170) is designed to disconnect artificial intelligence capabilities \-- such as voice or image recognition \-- from the cloud. The idea of performing these computations in a decentralized location (or \"edge\") is how the board gets its name, but the Ambiq Apollo3 microcontroller is how the Edge gets its power. The Apollo3 is an ultra-low power microcontroller that features an Arm Cortex-M4 core running at 48 MHz but uses only 6 *microamps* per megahertz. Such a high computational to electrical power ratio can enable machine learning features even in battery powered IoT devices.

[![SparkFun Edge Development Board - Apollo3 Blue](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/6/7/15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg)](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html)

### [SparkFun Edge Development Board - Apollo3 Blue](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html) 

[ DEV-15170 ]

The SparkFun Edge Development Board powered by TensorFlow is perfect begin using voice recognition without relying on the ser...

**Retired**

While the Apollo3 has the convenience of support in Arduino, sometimes you want to dig a little deeper and have more control over how you program your board. With that in mind, our goal here is to set up a tool-chain that will give you that finer tuned control.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

#### Serial Terminal

For Windows, you will also want a serial terminal of your choice. A couple options exist such as:

- The Serial Monitor found in [Arduino IDE](https://www.arduino.cc/en/main/software)
- [CoolTerm (Mac and PC)](https://coolterm.en.lo4d.com/)
- [Putty](https://www.putty.org/)

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. Make sure to check out the Edge Hookup Guide for more information about the hardware and connecting it to your computer.

[](https://learn.sparkfun.com/tutorials/sparkfun-edge-hookup-guide)

### SparkFun Edge Hookup Guide 

September 26, 2019

Get to know your Edge board, including both the hardware features for you to utilize as well as how to get talking to it.

You will also need to have some knowledge about serial terminals. Depending on your computer, you may need to install drivers for the CH340.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft866&name=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft866 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK&url=http%3A%2F%2Fsfe.io%2Ft866&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft866&t=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft866&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F6%2F15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg&description=Using+SparkFun+Edge+Board+with+Ambiq+Apollo3+SDK "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/all) [Next Page →\
[Bash, Make, and Python \-- Oh My]](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/bash-make-and-python----oh-my)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/introduction) [Bash, Make, and Python \-- Oh My](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/bash-make-and-python----oh-my) [Toolchain Setup](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/toolchain-setup) [Installing the Compiler](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/new-page) [Installing the SDK and Board Support Files](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/installing-the-sdk-and-board-support-files) [Example Applications](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/example-applications) [Troubleshooting](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/resources-and-going-further)

[Comments [29]](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/discuss) [Single Page](https://learn.sparkfun.com/tutorials/using-sparkfun-edge-board-with-ambiq-apollo3-sdk/all) [Print]

- **Tags**
- - [BLE](https://learn.sparkfun.com/tutorials/tags/ble)
  - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Bluetooth 4.0](https://learn.sparkfun.com/tutorials/tags/bluetooth-4-0)
  - [Bluetooth Low Energy](https://learn.sparkfun.com/tutorials/tags/bluetooth-low-energy)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [SparkFun Edge](https://learn.sparkfun.com/tutorials/tags/sparkfun-edge)
  - [TensorFlow](https://learn.sparkfun.com/tutorials/tags/tensorflow)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]