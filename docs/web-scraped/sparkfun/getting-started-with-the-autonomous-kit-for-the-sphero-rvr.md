# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Getting Started with the Autonomous Kit for the Sphero RVR

# Getting Started with the Autonomous Kit for the Sphero RVR

[≡ Pages](#)

Contributors: [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1100&name=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1100 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR&url=http%3A%2F%2Fsfe.io%2Ft1100&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1100&t=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1100&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F0%2Frvr-gif.gif&description=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Pin It")

## STEP 1: Connect the Sphero RVR to the App!

Although the Sphero RVR (*pronounced: rover or ˈrōvər*) is [**[NOT]**] included with these kits, in our collaboration with Sphero, they made it abundantly clear that it was imperative for users to perform this action before connecting a Raspberry Pi to the RVR. So, before you proceed any further, please be sure to connect your Sphero RVR to the [Sphero EDU App](https://edu.sphero.com/d) to update the firmware.

[**Important: Update Your Firmware to Unlock Your RVR**]

First things first, you must connect your RVR to the EDU App before connecting it to a development board (i.e. Raspberry Pi, Arduino, or micro:bit), in order to ensure that it has the most up-to-date firmware.

You can always check back on the Sphero SDK [[firmware update page](https://sdk.sphero.com/docs/getting_started/before_you_start/firmware_update/)] for firmware version updates or, if you want Sphero to do all the legwork, add yourself to Sphero\'s [[updates email list](https://sdk.sphero.com/sign-up)] to get notifications about all of the stuffs. Sphero will always try to keep things backwards compatible, but there are instances where it will be imperative that they repair something that simply won\'t align with previous versions of the firmware, since Sphero doesn\'t want that getting in the way of your fun.

\

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Sphero EDU App Icon](https://2xkovp-p045k91rjvr9.cloudmaestro.com/7Gqp0Otqt/about/wp-content/uploads/2019/01/xdownload-app__icon-edu.png.pagespeed.ic.r75VneGOZm.png)](https://edu.sphero.com/d) | [](https://edu.sphero.com/d)                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           | # **Sphero Edu**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           | ##### Program all Sphero Robots                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                           | [![Supported Platforms](https://bk0hgy-p045k91rjvr9.cloudmaestro.com/7Gqp0Otqt/about/wp-content/uploads/2019/01/xapp-download-edu-all-icons.png.pagespeed.ic.qZyZI5p9NP.png)](https://edu.sphero.com/d) |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**(*\*For more details, check out Sphero\'s [[SDK webpage](https://sdk.sphero.com/)]; they also have a [[support page](https://support.sphero.com/)] if you get stuck.*)**

**Note:** Users will need to log-in/register an account on the app (*if you are a teacher or an administrator we recommend at minimum performing this step before class/distributing out your Sphero RVRs*). Also, don\'t forget to power on the Sphero RVR and enable the Bluetooth functionality on your computer or mobile device.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1100&name=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1100 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR&url=http%3A%2F%2Fsfe.io%2Ft1100&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1100&t=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1100&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F0%2Frvr-gif.gif&description=Getting+Started+with+the+Autonomous+Kit+for+the+Sphero+RVR "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/all) [Next Page →\
[Introduction]](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/introduction)

← Previous Page

[**Pages**] [STEP 1: Connect the Sphero RVR to the App!](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/step-1-connect-the-sphero-rvr-to-the-app) [Introduction](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/hardware-overview) [Software Overview: Part 1 - Raspbian OS](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/software-overview-part-1---raspbian-os) [Configure the Raspberry Pi](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/configure-the-raspberry-pi) [Remote Access with SSH](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/remote-access-with-ssh) [Software Overview: Part 2 - Python](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/software-overview-part-2---python) [Initial Hardware Tests](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/initial-hardware-tests) [Hardware Assembly](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/hardware-assembly) [Software Overview: Part 3 - Sphero SDK](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/software-overview-part-3---sphero-sdk) [Examples](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/examples) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/troubleshooting-tips) [Resources and Going Further](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/resources-and-going-further)

[Comments [14]](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/discuss) [Single Page](https://learn.sparkfun.com/tutorials/getting-started-with-the-autonomous-kit-for-the-sphero-rvr/all) [Print]

- **Tags**
- - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Navigation](https://learn.sparkfun.com/tutorials/tags/navigation)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Science](https://learn.sparkfun.com/tutorials/tags/science)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Sphero](https://learn.sparkfun.com/tutorials/tags/sphero)
  - [Start a Project](https://learn.sparkfun.com/tutorials/tags/start-a-project)
  - [Technology](https://learn.sparkfun.com/tutorials/tags/technology)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]