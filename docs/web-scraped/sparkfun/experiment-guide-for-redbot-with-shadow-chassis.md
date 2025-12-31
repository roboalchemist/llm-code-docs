# Source: https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Experiment Guide for RedBot with Shadow Chassis

# Experiment Guide for RedBot with Shadow Chassis

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/c6c1a1ae72fbf9f47bee08a43259f504?d=retro&s=20&r=pg) bri_huang], [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel], [![](https://cdn.sparkfun.com/avatar/f4e195a7becacb6d86238db8c87e90f0?d=retro&s=20&r=pg) SFUptownMaker]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft356&name=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft356 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Experiment+Guide+for+RedBot+with+Shadow+Chassis&url=http%3A%2F%2Fsfe.io%2Ft356&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft356&t=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft356&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F5%2F6%2FRedbot_Kit-94.jpg&description=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Pin It")

## Introduction

The SparkFun RedBot is a great way to get your feet wet in the world of robotics. However, once you have assembled your RedBot, you may be at a loss as to where to go from there. This guide will go through nine different experiments, ranging from learning how to drive your RedBot to using an accelerometer to trigger your RedBot to move. Once you\'ve mastered each experiment, you can take what you\'ve learned in this guide and apply it to creating your own robot platform.

### RedBot Basic Kit vs. SIK for RedBot

This tutorial will cover how to use everything in the [SparkFun RedBot Basic Kit](https://www.sparkfun.com/products/13166) and the [SparkFun Inventor\'s Kit for RedBot](https://www.sparkfun.com/products/12649) (SIK for RedBot).

[![SparkFun RedBot Basic Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/2/8/8/13166-07a.jpg)](https://www.sparkfun.com/products/13166)

### [SparkFun RedBot Basic Kit](https://www.sparkfun.com/products/13166) 

[ ROB-13166 ]

Welcome the RedBot Basic Kit, a robotic development platform capable of teaching two motor robotics and sensor integration! T...

**Retired**

[![SparkFun Inventor\'s Kit for RedBot](https://cdn.sparkfun.com/r/600-600/assets/parts/9/3/4/3/SIK_Shadow_Chasis.jpg)](https://www.sparkfun.com/products/12649)

### [SparkFun Inventor\'s Kit for RedBot](https://www.sparkfun.com/products/12649) 

[ ROB-12649 ]

The SparkFun Inventor's Kit for RedBot is a great way to get started with two motor robotics and sensor integration using t...

**Retired**

The SIK for RedBot contains a few extra parts in addition to the RedBot Kit that are covered in this tutorial. Sections pertaining to these extra parts will be marked with **(SIK)**.

#### RedBot Basic Kit

If you have the [RedBot Basic Kit](https://www.sparkfun.com/products/13166), you can **skip** the steps marked with **(SIK)**.

[![Completed RedBot Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/6/Redbot_Kit-93.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/6/Redbot_Kit-93.jpg)

Alternatively, you can pick up additional sensors to install on your RedBot. These parts include the [Wheel Encoder Kit](https://www.sparkfun.com/products/12629), [RedBot Buzzer](https://www.sparkfun.com/products/12567), and **two** [RedBot Mechanical Bumpers](https://www.sparkfun.com/products/11999). Follow the sections in this guide that cover any of the extra sensors you might have.

#### SIK for RedBot

If you have the [SIK for RedBot](https://www.sparkfun.com/products/13166), you can follow all the sections in this guide, including those marked with **(SIK)**.

[![Completed SIK for RedBot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/6/Redbot_Kit_Brian_Revisions-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/6/Redbot_Kit_Brian_Revisions-02.jpg)

### Experiment List:

Here is a breakdown of each experiment presented in this tutorial. Click on the link to jump to that section, or continue reading to learn more about the hardware and library before starting on Experiment 1.

1.  [Software Install and Basic Test](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-1-software-install-and-basic-test)
2.  [Drive Forward](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-2-drive-forward-)
3.  [Turning](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-3-turning)
4.  [Push to Start & Making Sounds](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-4-push-to-start--making-sounds-sik)
5.  [Bumpers](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-5-bumpers-sik)
6.  [Line Following with IR Sensors](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-6-line-following-with-ir-sensors)
7.  [Encoder](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-7-encoder-sik)
8.  [Accelerometer](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-8-accelerometer)
9.  [Remote Control](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-9-remote-control)

### Extra Supplies Needed

- [4x AA batteries](https://www.sparkfun.com/products/9100) (if not using the SIK for RedBot)
- [USB miniB cable](https://www.sparkfun.com/products/11301)
- Tape, paint, markers, pencils, etc for IR Sensors

### Suggested Reading

If you still need to assemble your RedBot, visit our [RedBot Assembly Guide](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis) for detailed instructions. Please note that are a couple of versions of the assembly guide. For an older version of the RedBot Kit, please see this [assembly guide](https://learn.sparkfun.com/tutorials/redbot-assembly-guide).

[](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis)

### Assembly Guide for RedBot with Shadow Chassis 

May 28, 2015

Assembly Guide for the RedBot Kit. This tutorial includes extra parts to follow to go along with the RedBot Inventor\'s Kit tutorial.

Already put together the RedBot? Great! It\'s a good idea to double-check the wiring. If you hooked up the RedBot differently, you can either change the example code to reflect your changes or rewire your bot as per the assembly guide.

Before you go any further, you should probably make certain that you\'re familiar with these other topics:

- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino) - Since the RedBot is based off the Arduino platform, it\'s a good idea to understand what that means.
- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino) - If you don\'t have the Arduino software installed, this guide will help you out.
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) - To get the most out of the RedBot, you\'ll want to install our RedBot library. This tutorial will show you how to install any library.
- [Accelerometer basics](https://learn.sparkfun.com/tutorials/accelerometer-basics) - One of the core sensors for the RedBot is an accelerometer. To find out more about accelerometers, check out this guide.
- [Analog to digital conversion](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) - Many useful sensors for the RedBot will be analog. This guide will help you interface with them and make the most of the data you get back.
- [Pulse width modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) - The RedBot includes two headers with PWM signals, and uses PWM to control the speed of the motors. It\'s probably a good idea to be familiar with the concept.
- [I^2^C](https://learn.sparkfun.com/tutorials/i2c) - The RedBot Accelerometer, which ships with the RedBot kit, uses I^2^C to communicate with the RedBot. While the accelerometer is accessible through the library with no knowledge of I^2^C required, if you want to get more out of it, you can check out this tutorial.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft356&name=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft356 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Experiment+Guide+for+RedBot+with+Shadow+Chassis&url=http%3A%2F%2Fsfe.io%2Ft356&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft356&t=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft356&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F5%2F6%2FRedbot_Kit-94.jpg&description=Experiment+Guide+for+RedBot+with+Shadow+Chassis "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/all) [Next Page →\
[Hardware]](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/hardware)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/introduction) [Hardware](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/hardware) [RedBot Library Quick Reference](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/redbot-library-quick-reference) [Experiment 1: Software Install and Basic Test](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-1-software-install-and-basic-test) [Experiment 2: Drive Forward](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-2-drive-forward-) [Experiment 3: Turning](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-3-turning) [Experiment 4: Push to Start & Making Sounds (SIK)](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-4-push-to-start--making-sounds-sik) [Experiment 5: Bumpers (SIK)](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-5-bumpers-sik) [Experiment 6: Line Following with IR Sensors](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-6-line-following-with-ir-sensors) [Experiment 7: Encoder (SIK)](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-7-encoder-sik) [Experiment 8: Accelerometer](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-8-accelerometer) [Experiment 9: Remote Control](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/experiment-9-remote-control) [Bonus Experiments!](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/bonus-experiments) [Resources and Going Further](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/resources-and-going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/discuss) [Single Page](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Audio](https://learn.sparkfun.com/tutorials/tags/audio)
  - [Computer Engineering](https://learn.sparkfun.com/tutorials/tags/computer-engineering-)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)
  - [XBee](https://learn.sparkfun.com/tutorials/tags/xbee)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]