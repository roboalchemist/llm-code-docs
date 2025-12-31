# Source: https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- How to Run a 5V Device On a 3.3V System With Qwiic

# How to Run a 5V Device On a 3.3V System With Qwiic

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/c79948e7cb0fb6cc0dbfaa77301914ce?d=retro&s=20&r=pg) Christo-boots with the-pher], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3738&name=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3738 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic&url=http%3A%2F%2Fsfe.io%2Ft3738&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3738&t=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3738&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F7%2F3%2F8%2Fdemo-sen55.jpg&description=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Pin It")

## Introduction

The SparkFun Qwiic AP3012K 5V Boost converts the logic-level and boost the voltage or power supply of the Qwiic connect system from 3.3V, to 5V on its [PTH](https://en.wikipedia.org/wiki/Through-hole_technology) pins. This is handy for connecting any I^2^C device that requires a higher supply voltage, such as super bright LEDs or mechanisms like a DC fan on our air quality sensors. On the board, we also provide `3V3`/`5V` jumpers, which can be used to configure the logic-levels of the I^2^C PTH pins. Therefore, this board can be utilized to connect an I^2^C device that requires any combination of 3.3V/5V for its power and/or signals.

[![SparkFun Qwiic 5V Boost - AP3012K](https://cdn.sparkfun.com/r/600-600/assets/parts/2/9/9/1/3/28203-Qwiic-Boost-Feature.jpg)](https://www.sparkfun.com/sparkfun-qwiic-5v-boost-ap3012k.html)

### [SparkFun Qwiic 5V Boost - AP3012K](https://www.sparkfun.com/sparkfun-qwiic-5v-boost-ap3012k.html) 

[ PRT-28203 ]

The SparkFun Qwiic 5V Boost simplifies interfacing 5V I2C devices with the 3.3V Qwiic ecosystem. It takes the 3.3V I2C signal...

[ [\$8.95] ]

The boost circuit on this board is rated to source up to a 100mA at 5V output, with 90% efficiency. However, users should note that this limitation is not only dependent on the load being connected, but also the amount of current that is being sourced to the [Qwiic connector system](https://www.sparkfun.com/qwiic).

**Attention:** Soldering is required for this board.

In this guide we\'ll cover the hardware and how to utilize the Qwiic 5V Boost with the [Sensirion SEN55 Sensor](https://www.sparkfun.com/sensirion-particle-voc-humidity-and-temperature-sensor-sen55.html) (but you can use the [SEN54](https://www.sparkfun.com/particle-voc-humidity-and-temperature-sensor-sen54.html) or [SPS30](https://www.sparkfun.com/particulate-matter-sensor-sps30.html), instead). To follow along with this tutorial, users will need the following items:

- [Thing Plus Development Board](https://www.sparkfun.com/thing-plus)
  - We recommend either the [ESP32 Thing Plus](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) or the [RP2350 Thing Plus](https://www.sparkfun.com/sparkfun-thing-plus-rp2350.html).
- [SparkFun Qwiic 5V Boost - AP3012K](https://www.sparkfun.com/sparkfun-qwiic-5v-boost-ap3012k.html)
- [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)
- [Sensirion SEN55 - Particle, VOC, NOx, Humidity, and Temperature Sensor](https://www.sparkfun.com/sensirion-particle-voc-humidity-and-temperature-sensor-sen55.html)
- Soldering tools
- Headers and jumper Wire
- USB cable

[![SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/9/6/8/20168Diagonal.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html)

### [SparkFun Thing Plus - ESP32 WROOM (USB-C)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-usb-c.html) 

[ WRL-20168 ]

The USB-C variant of ESP32 Thing Plus is a development board with WiFi, SPP, BLE, Qwiic connector, 21 I/O pins, RGB status LE...

[ [\$33.73] ]

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Sensirion Particle, VOC, Humidity, and Temperature Sensor - SEN55](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/0/4/0/23715-SEN55-Environmental-Node-Feature.jpg)](https://www.sparkfun.com/sensirion-particle-voc-humidity-and-temperature-sensor-sen55.html)

### [Sensirion Particle, VOC, Humidity, and Temperature Sensor - SEN55](https://www.sparkfun.com/sensirion-particle-voc-humidity-and-temperature-sensor-sen55.html) 

[ SEN-23715 ]

The SEN55 environmental node is a straightforward, all-in-one sensor solution platform for the accurate measurement of variou...

[ [\$36.95] ]

[![SparkFun Qwiic 5V Boost - AP3012K](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/9/1/3/28203-Qwiic-Boost-Feature.jpg)](https://www.sparkfun.com/sparkfun-qwiic-5v-boost-ap3012k.html)

### [SparkFun Qwiic 5V Boost - AP3012K](https://www.sparkfun.com/sparkfun-qwiic-5v-boost-ap3012k.html) 

[ PRT-28203 ]

The SparkFun Qwiic 5V Boost simplifies interfacing 5V I2C devices with the 3.3V Qwiic ecosystem. It takes the 3.3V I2C signal...

[ [\$8.95] ]

**Attention:** Again, soldering is *required* for this board.

**Tip:** The Sensirion SEN55 Sensor requires an extra GND connection to enable the I^2^C interface.

**Note:** The These other Sensirion particulate matter sensors, may also be used in place of the SEN55:

- [Sensirion SEN54 - Particle, VOC, Humidity, and Temperature Sensor](https://www.sparkfun.com/particle-voc-humidity-and-temperature-sensor-sen54.html)
- [Sensirion SPS30 - Particulate Matter Sensor](https://www.sparkfun.com/particulate-matter-sensor-sps30.html)

### Topics

This guide contains two main sections: Hardware Assembly and Quickstart Guide sub-sections.

- The **Hardware Assembly** section provides instructions to utilize this product with the Sensirion SEN55 Sensor.
- The **Project Setup** covers the basic hardware information and assembly instructions users would need to get started with this product.

If you are looking for the [full Hookup Guide](https://docs.sparkfun.com/SparkFun_Qwiic_5V_Boost_AP3012K/introduction/) for the SparkFun Qwiic 5V Boost - AP3012K, click the button bellow. This basic tutorial only covers utilizing this Qwiic AP3012K 5V Boost to attach a SEN55 sensor to our Qwiic connect system.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_Qwiic_5V_Boost_AP3012K/introduction/)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft3738&name=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft3738 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic&url=http%3A%2F%2Fsfe.io%2Ft3738&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft3738&t=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft3738&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F3%2F7%2F3%2F8%2Fdemo-sen55.jpg&description=How+to+Run+a+5V+Device+On+a+3.3V+System+With+Qwiic "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/all) [Next Page →\
[Hardware Assembly]](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/hardware-assembly)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/introduction) [Hardware Assembly](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/hardware-assembly) [Project Setup](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/project-setup) [Troubleshooting Tips](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/troubleshooting-tips)

[Comments [0]](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/discuss) [Single Page](https://learn.sparkfun.com/tutorials/how-to-run-a-5v-device-on-a-33v-system-with-qwiic/all) [Print]

- **Tags**
- - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]