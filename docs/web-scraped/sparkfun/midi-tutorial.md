# Source: https://learn.sparkfun.com/tutorials/midi-tutorial

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- MIDI Tutorial

# MIDI Tutorial

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/d069e186dea25a3b82d74ef824716693?d=retro&s=20&r=pg) Byron J.]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft408&name=MIDI+Tutorial "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft408 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MIDI+Tutorial&url=http%3A%2F%2Fsfe.io%2Ft408&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft408&t=MIDI+Tutorial "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft408&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F0%2F8%2Fmidi-ports.jpg&description=MIDI+Tutorial "Pin It")

## Introduction

Perhaps you\'ve seen the plug on the back of something. In today\'s world of micro-USB and thunderbolt connections, it\'s a rather large circular connector, about 1/2\" in diameter, with five electrical connections. There are often two or three of these plugs in a row.

[![MIDI ports](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/0/8/midi-ports.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/0/8/midi-ports.jpg)

This is the **M**usical **I**nstrument **D**igital **I**nterface (**MIDI**) plug. Musical instruments use these ports to communicate performance data, but the protocol has also been extended to related devices, such as stage lighting and recording studio equipment.

MIDI itself is a relatively simple serial communication standard, but it can be daunting because there\'s a lot of terminology. In the following sections, we\'ll do our best to explain the terminology, while exploring the finer technical details.

## Background

MIDI is built atop some concepts we\'ve explored in more detail in other tutorials.

- MIDI transmits data using [serial ports](https://learn.sparkfun.com/tutorials/serial-communication).
- To make good use of the transmitted data, it\'s helpful to know how to convert to and from [hexadecimal](https://learn.sparkfun.com/tutorials/hexadecimal), and use [binary operators](https://learn.sparkfun.com/tutorials/binary).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft408&name=MIDI+Tutorial "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft408 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=MIDI+Tutorial&url=http%3A%2F%2Fsfe.io%2Ft408&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft408&t=MIDI+Tutorial "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft408&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F0%2F8%2Fmidi-ports.jpg&description=MIDI+Tutorial "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/midi-tutorial/all) [Next Page →\
[History]](https://learn.sparkfun.com/tutorials/midi-tutorial/history)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/midi-tutorial/introduction) [History](https://learn.sparkfun.com/tutorials/midi-tutorial/history) [MIDI Devices](https://learn.sparkfun.com/tutorials/midi-tutorial/midi-devices) [The MIDI Standard](https://learn.sparkfun.com/tutorials/midi-tutorial/the-midi-standard) [Hardware & Electronic Implementation](https://learn.sparkfun.com/tutorials/midi-tutorial/hardware--electronic-implementation) [Messages](https://learn.sparkfun.com/tutorials/midi-tutorial/messages) [Advanced Messages](https://learn.sparkfun.com/tutorials/midi-tutorial/advanced-messages) [Topologies](https://learn.sparkfun.com/tutorials/midi-tutorial/topologies) [Implementing MIDI](https://learn.sparkfun.com/tutorials/midi-tutorial/implementing-midi) [Other MIDI Technologies](https://learn.sparkfun.com/tutorials/midi-tutorial/other-midi-technologies) [Shortcomings](https://learn.sparkfun.com/tutorials/midi-tutorial/shortcomings) [Updates and Alternatives](https://learn.sparkfun.com/tutorials/midi-tutorial/updates-and-alternatives) [Resources and Going Further](https://learn.sparkfun.com/tutorials/midi-tutorial/resources-and-going-further)

[Comments [2]](https://learn.sparkfun.com/tutorials/midi-tutorial/discuss) [Single Page](https://learn.sparkfun.com/tutorials/midi-tutorial/all) [Print]

- **Tags**
- - [Audio](https://learn.sparkfun.com/tutorials/tags/audio)
  - [Communication](https://learn.sparkfun.com/tutorials/tags/communication)
  - [Concepts](https://learn.sparkfun.com/tutorials/tags/concepts)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]