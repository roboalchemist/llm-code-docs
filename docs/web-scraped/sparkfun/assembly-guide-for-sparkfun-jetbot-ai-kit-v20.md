# Source: https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Assembly Guide for SparkFun JetBot AI Kit V2.0

# Assembly Guide for SparkFun JetBot AI Kit V2.0

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/fcb400728a84349526800a9bfa58cc2f?d=retro&s=20&r=pg) Evan_Double_U]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1165&name=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1165 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0&url=http%3A%2F%2Fsfe.io%2Ft1165&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1165&t=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1165&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F6%2F5%2F16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01A.jpg&description=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Pin It")

## Introduction

SparkFun's multiple Jetbot offerings merge the industry leading machine learning capabilities of the NVIDIA Jetson Nano with the vast SparkFun ecosystem of sensors and accessories. Packaged as a ready-to-assemble robotics platform, the [SparkFun JetBot AI Kit v2.0](https://www.sparkfun.com/products/16390) requires no additional components or 3D printing to get started - just assemble the robot, boot up the Jetson Nano, connect to WiFi and start using the JetBot immediately. This combination of advanced technologies in a ready-to-assemble package makes the SparkFun JetBot Kit a standout, delivering one of the strongest robotics platforms on the market. This guide serves as hardware assembly instructions for the JetBot AI Kit v2.0. The SparkFun JetBot comes with a pre-flashed micro SD card image that includes the Nvidia JetBot base image with additional installations of the SparkFun Qwiic Python library, Edimax WiFi driver, AWS RoboMaker ready with AWS IoT Greengrass, and of course the JetBot ROS. Users only need to plug in the SD card and set up the WiFi connection to get started.

SparkFun has released several version of the Jetbot. Please make note of the comments under some photos to ensure it related to the Jetbot kit you have purchased. Completed Jetbot photos are shown below for comparison.

- [SparkFun JetBot AI Kit v2.0 - Purchase before Dec 2020](https://www.sparkfun.com/products/16390)
- [SparkFun JetBot AI Kit v2.1 - 4GB Jetson Nano Dev kit - Dec 2020 and later](https://www.sparkfun.com/products/16390)
- [SparkFun JetBot AI Kit Powered by Jetson Nano 2GB](https://www.sparkfun.com/products/17246)

[![Completed JetBot Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01A.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01A.jpg)

*JetBot V2.0 - Single camera mount & Jetson Dev Kit GPIO header oriented off the side of the Jetbot*

[![Completed JetBot 4GB Kit](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/4GB_Jetbot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/4GB_Jetbot.jpg)

*4GB JetBot V2.1 - Stereo camera mount with oriented camera ribbon connector & Jetson 4GB Dev Kit GPIO header oriented off the back of the Jetbot*

[![Completed JetBot 2GB Kit](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/2GB_Jetbot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/2GB_Jetbot.jpg)

*2GB JetBot V2.1 - Stereo camera mount with oriented camera ribbon connector & Jetson 2GB Dev Kit GPIO header oriented off the back of the Jetbot*

**Note:** We recommend that you read **all** of the directions first, before building your JetBot. However, we empathize if you are just here for the pictures & a general feel for the SparkFun JetBot. We are also those people who on occasion void warranties & recycle unopened instructions manuals but please note, SparkFun can only provide support for the instructions laid out in the following pages.

**Attention:** The SD card in this kit comes **pre-flashed** to work with our hardware and has the all the modules installed (including the sample machine learning models needed for the collision avoidance and object following examples). The only software procedures needed to get your JetBot running are [steps 2-4 from the Nvidia instructions](https://github.com/NVIDIA-AI-IOT/jetbot/wiki/Software-Setup) (i.e. setup the WiFi connection and then connect to the JetBot using a browser). Please **[DO NOT]** format or flash a new image on the SD card; otherwise, you will need to flash our image back onto the card.

If you accidentally make this mistake, don\'t worry. You can find instructions for re-flashing our image back onto the SD card in the [Software Setup](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit/5-software-setup-guide-from-nvidia) section of this guide

The Jetson Nano Developer Kit offers extensibility through an industry standard GPIO header and associated programming capabilities like the Jetson GPIO Python library. Building off this capability, the SparkFun kit includes the SparkFun Qwiic pHAT for Raspberry Pi, enabling immediate access to the extensive [SparkFun Qwiic ecosystem](https://www.sparkfun.com/qwiic) from within the Jetson Nano environment, which makes it easy to integrate more than 30 sensors (no soldering and daisy-chainable).

------------------------------------------------------------------------

*The SparkFun Qwiic Connect System is an ecosystem of I^2^C sensors, actuators, shields and cables that make prototyping faster and less prone to error. All Qwiic-enabled boards use a common 1mm pitch, 4-pin JST connector. This reduces the amount of required PCB space, and polarized connections mean you can't hook it up wrong.*

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

------------------------------------------------------------------------

### Materials

[![SparkFun Jetbot included parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01.jpg)

  Part                                                                          Qty
  ----------------------------------------------------------------------------- -----
  JetBot Chassis Kit                                                            1
  Hobby Gearmotor (pair) included as part of JetBot Chassis Kit                 1
  Camera mount included as part of JetBot Chassis Kit                           1
  Wheels & Tires - included as part of JetBot Chassis Kit                       2
  Lithium Ion Battery Pack - 10Ah (3A/1A USB Ports)                             1
  Edimax 2-in-1 WiFi and Bluetooth 4.0 Adapter \*not included in 2GB Jetbot\*   1
  Jetson Dev Kit \*Specific Jetson Dev Kit only included in specified Kits\*    1
  SparkFun JetBot image (Pre Flashed)                                           1
  Leopard Imaging 136 FOV Camera                                                1
  SparkFun Micro OLED Breakout (Qwiic)                                          1
  SparkFun Qwiic Motor Driver                                                   1
  SparkFun Qwiic pHAT v2.0 for Raspberry Pi                                     1
  Qwiic Cable - 100mm                                                           1
  Qwiic Cable - 200mm                                                           1
  Jumper Wires Premium 6\" M/M (2-pack black & red)                             1
  USB Micro-B Cable - 6\" \*Jetbot 2GB includes USB-C cable for power\*         1
  Dual Lock Velcro                                                              1

[![Included hardware with JetBot v2.1 Kit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-02.jpg)

  Part                                                               Qty
  ------------------------------------------------------------------ -----
  Standoff - Nylon (4-40; 3/8in.)                                    10
  1/4\" Phillips Screw with 4-40 Thread                              20
  Machine Screw Nut - 4-40                                           10
  M2 Nylon hex nut                                                   4
  M2 Nylon screw slotted drive                                       4
  JetBot Chassis Hardware \*included as part of JetBot Chassis Kit   1

### Recommended Tools

We did not include any tools in this kit because if you are like us you are looking for an excuse to use the tools you have more than needing new tools to work on your projects. That said, the following tools will be required to assemble your SparkFun JetBot.

- Small phillips & small flat head head screwdriver will be needed for chassis assembly & to tighten the screw terminal connections for each motor. We reccomend the Pocket Screwdriver Set; [TOL-12268](https://www.sparkfun.com/products/12891).
- Pair of scissors will be needed to cut the adhesive Dual Lock Velcro strap to desired size; recommended, but not essential..
- *Optional*- adjustable wrench or pliers to hold small components (nuts & standoffs) in place while tightening screws; your finger grip is usually enough to hold these in place while tightening screws & helps to ensure nothing is *over tightened*.

### A Note About Directions

When we talk about the \"Front,\" or \"Forward\" of the JetBot, we are referring to direction the camera is pointed when the JetBot is fully assembled. \"Left\" and \"Right\" will be from the perspective of the SparkFun JetBot (i.e. what the JetBot camera sees).

[![Jetbot Orientation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/5/Jetbot_orientation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/Jetbot_orientation.png)

*Orientation reference remain consistent between all kit offerings mentioned above*

[![Jetbot V2 Orientation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/5/JetBot_v2.2__Updates-28_with_labels.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/5/JetBot_v2.2__Updates-28_with_labels.jpg)

*Orientation reference remain consistent between all kit offerings mentioned above*

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1165&name=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1165 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0&url=http%3A%2F%2Fsfe.io%2Ft1165&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1165&t=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1165&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F6%2F5%2F16417-SparkFun_JetBot_AI_Kit_v2.1_Powered_by_Jetson_Nano-01A.jpg&description=Assembly+Guide+for+SparkFun+JetBot+AI+Kit+V2.0 "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/all) [Next Page →\
[1. Robotics Chassis Kit Initial Assembly]](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/1-robotics-chassis-kit-initial-assembly)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/introduction) [1. Robotics Chassis Kit Initial Assembly](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/1-robotics-chassis-kit-initial-assembly) [2. Camera Assembly & Installation](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/2-camera-assembly--installation) [3. Accessory Installation to Main Chassis](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/3-accessory-installation-to-main-chassis) [4. Software Setup Guide from NVIDIA](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/4-software-setup-guide-from-nvidia) [5. Examples](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/5-examples-) [Resources and Going Further](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/resources-and-going-further)

[Comments [16]](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/discuss) [Single Page](https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/all) [Print]

- **Tags**
- - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Nvidia](https://learn.sparkfun.com/tutorials/tags/nvidia)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]