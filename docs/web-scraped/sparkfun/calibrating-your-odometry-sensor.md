# Source: https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Calibrating Your Odometry Sensor

# Calibrating Your Odometry Sensor

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/c79948e7cb0fb6cc0dbfaa77301914ce?d=retro&s=20&r=pg) Christo-boots with the-pher], [![](https://cdn.sparkfun.com/avatar/935d3ed2b6c2516f85bce325946e6356?d=retro&s=20&r=pg) SparkFro]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3639&name=Calibrating+Your+Odometry+Sensor "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3639 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Calibrating+Your+Odometry+Sensor&url=http%3A%2F%2Fsfe.io%2Ft3639&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3639&t=Calibrating+Your+Odometry+Sensor "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3639&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F3%2F6%2F3%2F9%2FSEN-24904-Action-GIF-1.gif&description=Calibrating+Your+Odometry+Sensor "Pin It")

## Introduction

The SparkFun Qwiic Optical Tracking Odometry Sensor empowers you to elevate your robot\'s navigation capabilities with exceptional precision and streamlined integration. This compact, all-in-one sensor leverages the power of the PAA5160E1 chip from PixArt Imaging Inc., delivering accurate dual-axis motion data across various hard floor surfaces. But that\'s not all! This sensor boasts a powerful built-in 6-axis Inertial Measurement Unit (IMU) and an onboard microcontroller that performs real-time sensor fusion and tracking algorithms.

[![SparkFun Optical Tracking Odometry Sensor - PAA5160E1 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/5/2/0/9/SEN-24904-Optical-Tracking-Odometry-Sensor-Feature_1.jpg)](https://www.sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html)

### [SparkFun Optical Tracking Odometry Sensor - PAA5160E1 (Qwiic)](https://www.sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html) 

[ SEN-24904 ]

The SparkFun Qwiic Optical Tracking Odometry Sensor empowers you to elevate a robot\'s navigation capabilities with precision ...

[ [\$84.95] ]

In this tutorial, we will be going over how to calibrate your Qwiic Optical Tracking Odometry Sensor (or \"OTOS\") with Arduino and Python Examples. While we recommend using the OTOS with our XRP robotics platform (specifically for FTC teams), following this guide, you will be able to use the Odometry Sensor with any robot you feel comfortable with!

If you are looking for the [full Hookup Guide](https://docs.sparkfun.com/SparkFun_Optical_Tracking_Odometry_Sensor/) for the SparkFun Qwiic Optical Tracking Odometry Sensor, click the button bellow. This guide only covers sensor calibration to get you started, while the full Hookup Guide goes over every detail of the sensor.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_Optical_Tracking_Odometry_Sensor/)

**Warning:** The laser on this module is a Class 1, 850nm laser, classified IEC 60825-1 2014. Please use appropriate caution while operating.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3639&name=Calibrating+Your+Odometry+Sensor "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3639 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Calibrating+Your+Odometry+Sensor&url=http%3A%2F%2Fsfe.io%2Ft3639&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3639&t=Calibrating+Your+Odometry+Sensor "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3639&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fassets%2Flearn_tutorials%2F3%2F6%2F3%2F9%2FSEN-24904-Action-GIF-1.gif&description=Calibrating+Your+Odometry+Sensor "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/all) [Next Page →\
[Hardware Needed]](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/hardware-needed)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/introduction) [Hardware Needed](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/hardware-needed) [Software Setup](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/software-setup) [Arduino Examples & Calibration](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/arduino-examples--calibration) [Python Examples & Calibration](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/python-examples--calibration) [Going Further and Other Resources](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/going-further-and-other-resources)

[Comments [0]](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/discuss) [Single Page](https://learn.sparkfun.com/tutorials/calibrating-your-odometry-sensor/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Robotics](https://learn.sparkfun.com/tutorials/tags/robotics)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]