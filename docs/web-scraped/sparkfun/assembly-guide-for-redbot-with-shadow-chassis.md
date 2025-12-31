# Source: https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Assembly Guide for RedBot with Shadow Chassis

# Assembly Guide for RedBot with Shadow Chassis

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/c221e70aedb663ceb99faf8afd2734d3?d=retro&s=20&r=pg) HelloTechie], [![](https://cdn.sparkfun.com/avatar/f4e195a7becacb6d86238db8c87e90f0?d=retro&s=20&r=pg) SFUptownMaker], [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft337&name=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft337 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Assembly+Guide+for+RedBot+with+Shadow+Chassis&url=http%3A%2F%2Fsfe.io%2Ft337&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft337&t=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft337&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F3%2F7%2FRedbot_Kit_Brian_Revisions-02.jpg&description=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Pin It")

## Introduction

The SparkFun RedBot is a platform for teaching basic robotics and sensor integration! It is based on the SparkFun RedBoard and fully programmable using [Arduino](https://www.arduino.cc). This guide describes the assembly of the new [Shadow Chassis](https://www.sparkfun.com/products/13301) for the RedBot. If you want to learn how to program your robot, see the [Experiment Guide for RedBot](https://learn.sparkfun.com/tutorials/experiment-guide-for-redbot-with-shadow-chassis).

[![Completed RedBot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_Kit_Brian_Revisions-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_Kit_Brian_Revisions-03.jpg)

**NOTE:** We recommend that you read **all** of the directions first, before building your RedBot.

### RedBot Basic Kit vs. SIK for RedBot

This tutorial will cover how to install all the parts in the [SparkFun RedBot Basic Kit](https://www.sparkfun.com/products/13166) and the [SparkFun Inventor\'s Kit for RedBot](https://www.sparkfun.com/products/12649) (SIK for RedBot).

The SIK for RedBot contains additional parts to the RedBot Basic Kit. If you have the RedBot Basic Kit, please ignore sections pertaining to these extra parts. These sections are marked with the label **(SIK)**.

#### SparkFun RedBot Basic Kit

We have two flavors of the RedBot available - the Basic kit and the SparkFun Inventor\'s Kit for RedBot. If you have the [SparkFun RedBot Basic Kit](https://www.sparkfun.com/products/13166), you can **skip** the sections marked with **(SIK)**.

[![SparkFun RedBot Basic Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_Kit-93.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_Kit-93.jpg)

Alternatively, you can pick up additional sensors to install on your RedBot. These parts include the [Wheel Encoder Kit](https://www.sparkfun.com/products/12629), [RedBot Buzzer](https://www.sparkfun.com/products/12567), and **two** [RedBot Mechanical Bumpers](https://www.sparkfun.com/products/11999). Follow the sections in this guide that covers any of the extra sensors you might have.

#### SIK for RedBot

The SIK for RedBot has a few extra parts that you won\'t see in the Basic Kit. These include the mechanical bump sensors (whiskers), the buzzer, and wheel encoders. If you have the [SIK for RedBot](https://www.sparkfun.com/products/12649), you can follow all the sections in this guide, including those marked with **(SIK)**.

[![Completed RedBot SIK](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_Kit_Brian_Revisions-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_Kit_Brian_Revisions-02.jpg)

### Materials

The SparkFun RedBot Basic Kit contains the following pieces. SIK-only parts are noted with an asterisk (\*). Note that several of the parts need to be snapped out of the main chassis boards.

[![RedBot Kit parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_Kit-00_annotated_updated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_Kit-00_annotated_updated.jpg)

+-------------------+-------------------------------------------------------------------------------+-------------------+
|                   | Part                                                                          | Qty               |
+===================+===============================================================================+===================+
| A                 | Bottom Chassis Plate                                                          | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| B                 | Top Chassis Plate                                                             | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| C                 | Front Motor Mount                                                             | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| D                 | Rear Motor Mount                                                              | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| E                 | Side Strut                                                                    | 4                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| F                 | Encoder Mount                                                                 | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| G                 | Mainboard Mount                                                               | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| H                 | Battery Pack Clip                                                             | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| I                 | Line Follower Mount                                                           | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| J                 | Line Follower Mount Plate                                                     | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| K                 | [Motor](https://www.sparkfun.com/products/13302)                              | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| L                 | [Wheel](https://www.sparkfun.com/products/13259)                              | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| M                 | Nub Caster                                                                    | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| N\*               | [Encoder Magnet Plate (SIK)](https://www.sparkfun.com/products/12629)         | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| O\*               | [Encoder Hall Effect Sensor (SIK)](https://www.sparkfun.com/products/12629)   | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| P                 | [RedBot Mainboard](https://www.sparkfun.com/products/12097)                   | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| Q                 | [Line Follower Board](https://www.sparkfun.com/products/11769)                | 3                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| R                 | [Accelerometer Board](https://www.sparkfun.com/products/12589)                | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| S\*               | [Buzzer Board (SIK)](https://www.sparkfun.com/products/12567)                 | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| T\*               | [Bumper Board (SIK)](https://www.sparkfun.com/products/11999)                 | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| U\*               | [Bumper Whisker (SIK)](https://www.sparkfun.com/products/11999)               | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| V\*               | [#4-40 x 3/8\" Screw (SIK)](https://www.sparkfun.com/products/11999)          | 6                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| W\*               | [#4-40 Nylon Standoff (SIK)](https://www.sparkfun.com/products/11999)         | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| X\*               | [#4-40 Hex Nut (SIK)](https://www.sparkfun.com/products/11999)                | 2                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| Y                 | [3-Wire Jumper Cable (SIK)](https://www.sparkfun.com/products/13164)          | 3 (5\*)           |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| Z                 | Battery Holder                                                                | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| AA\*              | [AA Batteries (SIK)](https://www.sparkfun.com/products/9100)                  | 4                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| AB\*              | [Screwdriver (SIK)](https://www.sparkfun.com/products/9146) (Not Shown)       | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| AC\*              | [USB Mini-B Cable (SIK)](https://www.sparkfun.com/products/11301) (Not Shown) | 1                 |
+-------------------+-------------------------------------------------------------------------------+-------------------+
| \* Indicates parts included in the SIK for RedBot                                                                     |
+-----------------------------------------------------------------------------------------------------------------------+

**IMPORTANT:** If you have the RedBot Basic Kit, you will need 4x AA batteries.

### Recommended Tools

None! The RedBot Basic Kit does not require any additional tools. The SIK for RedBot comes with a screwdriver, which you will need to mount the Bumper Boards. If you bought the Bumper Boards separately, you will need a [Phillips screwdriver](https://www.sparkfun.com/products/9146).

**WARNING:** Do **not** attempt to remove chassis parts by squeezing them with pliers. You will break them, and the robot will be sad.

[![You\'re going to have a bad time](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_Kit-31_do_not.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_Kit-31_do_not.jpg)

### A Note About Directions

When we talk about the \"front,\" \"left,\" \"right,\" and \"back\" of the RedBot, we are referring to specific sides of the robot when viewed from above.

[![Directions on the RedBot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/7/Redbot_re-wired_shots-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/7/Redbot_re-wired_shots-01.jpg)

Notice that we consider the Mainboard to be on the \"back\" of the RedBot and the Bumper Whiskers and Line Follower Boards to be in the \"front.\"

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft337&name=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft337 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Assembly+Guide+for+RedBot+with+Shadow+Chassis&url=http%3A%2F%2Fsfe.io%2Ft337&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft337&t=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft337&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F3%2F7%2FRedbot_Kit_Brian_Revisions-02.jpg&description=Assembly+Guide+for+RedBot+with+Shadow+Chassis "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/all) [Next Page →\
[1. Wheel Encoders (SIK)]](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/1-wheel-encoders-sik)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/introduction) [1. Wheel Encoders (SIK)](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/1-wheel-encoders-sik) [2. Motors and Wheels](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/2-motors-and-wheels) [3. Line Follower](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/3-line-follower) [4. Mechanical Bumpers (SIK)](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/4-mechanical-bumpers-sik) [5. Chassis](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/5-chassis) [6. Mainboard](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/6-mainboard) [7. Accelerometer](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/7-accelerometer) [8. Buzzer (SIK)](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/8-buzzer-sik) [9. Batteries](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/9-batteries) [10. Run It!](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/10-run-it) [Resources and Going Further](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/discuss) [Single Page](https://learn.sparkfun.com/tutorials/assembly-guide-for-redbot-with-shadow-chassis/all) [Print]

- **Tags**
- - [Actobotics](https://learn.sparkfun.com/tutorials/tags/actobotics)
  - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]