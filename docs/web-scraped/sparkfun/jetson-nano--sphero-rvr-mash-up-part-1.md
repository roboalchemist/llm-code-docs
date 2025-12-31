# Source: https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Jetson Nano + Sphero RVR Mash-up (PART 1)

# Jetson Nano + Sphero RVR Mash-up (PART 1)

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/bb21dc7d7c75175fd6edb50cda25d83f?d=retro&s=20&r=pg) D\_\_\_Run\_\_\_]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1179&name=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1179 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29&url=http%3A%2F%2Fsfe.io%2Ft1179&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1179&t=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1179&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F9%2F20200421_130816.jpg&description=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Pin It")

## Introduction

We finally jumped on a project that we have been wanting to do for a while now: a mash-up of two robotics kits that we released over the past year! Those kits are the Advanced Autonomous kit for the Sphero RVR and our AI JetBot kit for the NVIDIA Jetson Nano. Both projects were fun to work on during launch and both products have astounding quality in their own perspective markets so we\'re very excited to combine them together!

[![SparkFun Advanced Autonomous Kit for Sphero RVR ](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/0/5/15303-SparkFun_Advanced_Autonomous_Kit_for_Sphero_RVR-01.jpg)](https://www.sparkfun.com/products/15303)

### [SparkFun Advanced Autonomous Kit for Sphero RVR ](https://www.sparkfun.com/products/15303) 

[ KIT-15303 ]

The SparkFun Advanced Autonomous Kit for Sphero RVR provides tools for building a smart robotics platform with distance sensi...

**Retired**

[![Sphero RVR - Programmable Robot](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/0/7/15304-Sphero_RVR-09.jpg)](https://www.sparkfun.com/products/15304)

### [Sphero RVR - Programmable Robot](https://www.sparkfun.com/products/15304) 

[ ROB-15304 ]

The Sphero RVR is the Go-Anywhere-Do-Anything Programmable Robot.

**Retired**

[![SparkFun JetBot AI Kit v2.1 Powered by Jetson Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/5/8/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-jetbot-ai-kit-v2-1-powered-by-jetson-nano.html)

### [SparkFun JetBot AI Kit v2.1 Powered by Jetson Nano](https://www.sparkfun.com/sparkfun-jetbot-ai-kit-v2-1-powered-by-jetson-nano.html) 

[ KIT-16417 ]

Utilize this kit to turn your Jetson Nano into a mobile machine with things like object following, collision avoidance via th...

**Retired**

We set about building this mash-up and this tutorial as a guide for you to follow along with us in building your own Jetson Nano powered Sphero RVR. We built the bot almost entirely from parts found in the two kits with and placed on top of a Sphero RVR.\

[![Fully assembled Jetson RVR Robot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/9/20200421_130758.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/9/20200421_130758.jpg)

\
With all of this being said and documented if you choose to build your Nano RVR mash-up feel free to riff on what we did. There is no real right way to do this, it was us in the shop for an afternoon being creative. Your sensors, board placement and hardware choices may vary. Use this tutorial more as... "guidelines".

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1179&name=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1179 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29&url=http%3A%2F%2Fsfe.io%2Ft1179&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1179&t=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1179&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F7%2F9%2F20200421_130816.jpg&description=Jetson+Nano+%2B+Sphero+RVR+Mash-up+%28PART+1%29 "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/hardware-overview) [Mounting the NVIDIA Jetson Nano](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/mounting-the-nvidia-jetson-nano) [Jetson Nano Peripherals](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/jetson-nano-peripherals) [SparkFun Hardware](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/sparkfun-hardware) [Camera and Camera Mount](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/camera-and-camera-mount) [Final Wiring](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/final-wiring) [In Closing and Next Steps](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/in-closing-and-next-steps)

[Comments [0]](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/discuss) [Single Page](https://learn.sparkfun.com/tutorials/jetson-nano--sphero-rvr-mash-up-part-1/all) [Print]

- **Tags**
- - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Machine Learning](https://learn.sparkfun.com/tutorials/tags/machine-learning)
  - [Nvidia](https://learn.sparkfun.com/tutorials/tags/nvidia)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Sphero](https://learn.sparkfun.com/tutorials/tags/sphero)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]