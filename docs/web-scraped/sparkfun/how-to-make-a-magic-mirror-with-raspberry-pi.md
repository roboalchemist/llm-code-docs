# Source: https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- How to Make a Magic Mirror with Raspberry Pi

# How to Make a Magic Mirror with Raspberry Pi

[≡ Pages](#)

Contributors: [ Ell C]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1182&name=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1182 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi&url=http%3A%2F%2Fsfe.io%2Ft1182&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1182&t=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1182&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F2%2FMagic_Mirror-02-cropped.jpg&description=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Pin It")

## Introduction

If you follow the [SparkFun Blog](https://www.sparkfun.com/news/3288), you may have seen my post about my attempts to keep up with my family\'s ever changing schedule. With schooling and summer camps going online and both myself and my partner working from home\... there\'s just too many virtual meetings to keep up with. An offhand comment about needing a \"battle station\" led to the Magic Mirror project.

[![Magic Mirror](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/8/2/Magic_Mirror-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/8/2/Magic_Mirror-02.jpg)

This tutorial presumes you have some basic familiarity with Unix systems and commands. It\'s not required, but is certainly helpful. Let\'s dive in and see how to set this up, shall we?

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### You May Also Need

If you prefer a larger, wall mounted Magic Mirror (like the one in this tutorial), you will need to find the following:

- Computer screen with HDMI input
- [Shadow Box Frame](https://www.michaels.com/walnut-shadow-box-by-studio-decor/10546446.html)
- [Outdoor Reflective Film](https://www.amazon.com/dp/B00CWGIHBE/ref=cm_sw_em_r_mt_dp_U_8Os2EbZARWCJG)
- Shadow Box Mounting Supplies (heavy duty picture frame hangers)

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup)

### Headless Raspberry Pi Setup 

Configure a Raspberry Pi without a keyboard, mouse, or monitor.

[](https://learn.sparkfun.com/tutorials/setting-up-a-raspberry-pi-3-as-an-access-point)

### Setting up a Raspberry Pi 3 as an Access Point 

This guide will show you how to configure a Raspberry Pi as an access point and connect it to your local Ethernet network to share Internet to other WiFi devices.

[](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup)

### How to Run a Raspberry Pi Program on Startup 

In this tutorial, we look at various methods for running a script or program automatically whenever your Raspberry Pi (or other Linux computer) boots up.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1182&name=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1182 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi&url=http%3A%2F%2Fsfe.io%2Ft1182&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1182&t=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1182&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F8%2F2%2FMagic_Mirror-02-cropped.jpg&description=How+to+Make+a+Magic+Mirror+with+Raspberry+Pi "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/all) [Next Page →\
[Hardware Hookup]](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/hardware-hookup)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/introduction) [Hardware Hookup](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/hardware-hookup) [Installing Magic Mirror](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/installing-magic-mirror) [config.js](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/configjs) [Customizing The Modules - Compliments](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/customizing-the-modules---compliments) [Customizing The Modules - Using Your Google Calendar](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/customizing-the-modules---using-your-google-calendar) [Customizing The Modules - Adding New Modules](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/customizing-the-modules---adding-new-modules) [Finishing Touches](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/finishing-touches) [Troubleshooting](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/resources-and-going-further)

[Comments [4]](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/discuss) [Single Page](https://learn.sparkfun.com/tutorials/how-to-make-a-magic-mirror-with-raspberry-pi/all) [Print]

- **Tags**
- - [Enclosure](https://learn.sparkfun.com/tutorials/tags/enclosure)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]