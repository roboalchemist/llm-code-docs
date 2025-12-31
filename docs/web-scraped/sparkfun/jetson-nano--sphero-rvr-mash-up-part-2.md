# Source: https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Jetson Nano + Sphero RVR Mash-up (PART 2)

# Jetson Nano + Sphero RVR Mash-up (PART 2)

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/bb21dc7d7c75175fd6edb50cda25d83f?d=retro&s=20&r=pg) D\_\_\_Run\_\_\_]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1201&name=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1201 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29&url=http%3A%2F%2Fsfe.io%2Ft1201&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1201&t=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1201&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F1%2F20200421_130758.jpg&description=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Pin It")

## Introduction

Welcome to the second part of our two part tutorial around mashing up two robotics kits; our [SparkFun JetBot AI Kit v2.1 Powered by Jetson Nano](https://www.sparkfun.com/products/16417) and our [SparkFun Advanced Autonomous Kit for Sphero RVR](https://www.sparkfun.com/products/15303) into a single robot project.

[![Assembled Sphero JetBot Mash-up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/0/1/20200421_130758.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/0/1/20200421_130758.jpg)

In the first tutorial we assembled the robot from parts and pieces from the two kits on top of a Sphero RVR, using it as our driving base and offloading the computation and control to the NVIDIA Jetson Nano. As a recap here are the steps we took to get this far:

- Mounted the Jetson Nano on the standard topper plate for the RVR.
- Combined and assembled the Qwiic pHAT and Qwiic OLED on the Jetson Nano.
- Mounted and hooked up the camera.
- Add the microSD card with the JetBot image and Edimax WiFi Adapter to the Nano.
- Added a battery and powered up the NVIDIA Jetson Nano.

If you have not yet built up your own, or are curious about any of these steps please refer back to the hardware assembly tutorial for this project.

[](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1)

### Jetson Nano + Sphero RVR Mash-up (PART 1) 

April 23, 2020

We took two of our biggest robotics partnerships from the previous year and shazamed them together into one robot to rule them all!

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1201&name=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1201 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29&url=http%3A%2F%2Fsfe.io%2Ft1201&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1201&t=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1201&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F0%2F1%2F20200421_130758.jpg&description=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+2%29 "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/hardware-overview) [JetBot Image Introduction](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/jetbot-image-introduction) [Getting Starting with the JetBot Image](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/getting-starting-with-the-jetbot-image) [Introduction to Using Jupyter Notebooks](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/introduction-to-using-jupyter-notebooks) [Updating Firmware on the Sphero RVR](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/updating-firmware-on-the-sphero-rvr) [The \[HACKED\] Sphero RVR SDK](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/the-hacked-sphero-rvr-sdk) [Hardware Test](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/hardware-test) [Download Example Jupyter Notebook](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/download-example-jupyter-notebook) [Example 1: JetBot Camera Test](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/example-1-jetbot-camera-test) [Example 2: Teleoperation](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/example-2-teleoperation) [Example 3: Machine Learning and Collision Avoidance](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/example-3-machine-learning-and-collision-avoidance) [Resources and Going Further](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/discuss) [Single Page](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-2/all) [Print]

- **Tags**
- - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Machine Learning](https://learn.sparkfun.com/tutorials/tags/machine-learning)
  - [Nvidia](https://learn.sparkfun.com/tutorials/tags/nvidia)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Sphero](https://learn.sparkfun.com/tutorials/tags/sphero)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]