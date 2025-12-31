# Source: https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun Inventor\'s Kit for Edison Experiment Guide

# SparkFun Inventor\'s Kit for Edison Experiment Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft448&name=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft448 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft448&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft448&t=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft448&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F4%2F8%2F13742-Kit.jpg&description=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Pin It")

## Introduction

The [SparkFun Inventor\'s Kit for Intel® Edison](https://www.sparkfun.com/products/13742), otherwise known as the *Edison SIK*, introduces the Edison as a powerful Internet of Things (IoT) platform. The experiments contained within these pages will guide you through programming the Edison using [JavaScript](https://en.wikipedia.org/wiki/JavaScript) and controlling various electronics. Whether you are new to electronics and JavaScript or are looking to take your skills to the next level (to the \"cloud!\"), this kit is a great starting point.

**[] Set Aside Some Time** - Please allow yourself ample time to complete each experiment. You may not get through all the experiments in one sitting. Each experiment also contains suggestions on project ideas and taking the examples to the next level. We suggest that you challenge yourself and try some of them!

### Included Materials

Here is a complete list of all the parts included in the Edison SIK.

[![Inventor\'s Kit for Intel Edison components](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/8/EdisonKit13742-Kit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/8/EdisonKit13742-Kit.jpg)

The SparkFun Inventor\'s Kit for Intel® Edison includes the following:

- 1x [Intel® Edison](https://www.sparkfun.com/products/13024)
- 1x [SparkFun Block for Intel® Edison - Base](https://www.sparkfun.com/products/13045)
- 1x [SparkFun Block for Intel® Edison - GPIO](https://www.sparkfun.com/products/13038)
- 1x [SparkFun Block for Intel® Edison - ADC](https://www.sparkfun.com/products/13327)
- 1x [Basic 16x2 Character LCD - White on Black 3.3V](https://www.sparkfun.com/products/9052)
- 1x [Mini Photocell](https://www.sparkfun.com/products/9088)
- 1x [Temperature Sensor - TMP36](https://www.sparkfun.com/products/10988)
- 1x [LED - RGB Diffused Common Cathode](https://www.sparkfun.com/products/9264)
- 20x 100Ω Resistors
- 20x 10kΩ Resistors
- 3x [2N3904 NPN Transistors](https://www.sparkfun.com/products/521)
- 1x [Piezo Speaker](https://www.sparkfun.com/products/7950)
- 1x [10k Trimpot](https://www.sparkfun.com/products/9806)
- 1x [USB OTG Cable](https://www.sparkfun.com/products/11604)
- 1x [USB microB Cable](https://www.sparkfun.com/products/10215)
- 1x [Breadboard](https://www.sparkfun.com/products/12002)
- 1x [Intel® Edison Hardware Pack](https://www.sparkfun.com/products/13187)
- 30x [Jumper Wires](https://www.sparkfun.com/products/11026)
- 4x [Push Buttons](https://www.sparkfun.com/products/10302)
- 1x [Screwdriver](https://www.sparkfun.com/products/9146)

If, at any time, you are unsure which part a particular experiment is asking for, reference this section.

### Suggested Reading

The following links may help guide you in your journey through the Edison SIK.

- [Edison Getting Started Guide](https://learn.sparkfun.com/tutorials/edison-getting-started-guide) - A quick way to program the Edison using the Arduino IDE.
- [General Guide to SparkFun Blocks for Intel® Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison) - Describes how the Blocks work with the Edison and provides a brief overview of all the available Blocks.
- [Intel\'s Getting Started Guide](https://software.intel.com/en-us/iot/library/edison-getting-started) - Tutorial on how to get the Edison running with either the [Arduino Breakout Board](https://www.sparkfun.com/products/13097) or the [Mini Breakout Board](https://www.sparkfun.com/products/13025).

Each experiment will also have a Suggested Reading section to aid you in understanding the components and concepts used in that particular experiment.

**NOTE:** If you would like to see all of the example code in one place, it can be found on GitHub! Just click the button below to be taken to the GitHub repository and click the link to **Download ZIP.**

[Edison SIK Example Code](https://github.com/sparkfun/Inventors_Kit_For_Edison_Experiments)

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft448&name=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft448 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide&url=http%3A%2F%2Fsfe.io%2Ft448&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft448&t=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft448&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F4%2F4%2F8%2F13742-Kit.jpg&description=SparkFun+Inventor%27s+Kit+for+Edison+Experiment+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/all) [Next Page →\
[Using the Kit]](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/using-the-kit)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/introduction) [Using the Kit](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/using-the-kit) [Building the Block Stack](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/building-the-block-stack) [Installing the Intel® XDK IoT Edition](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/installing-the-intel-xdk-iot-edition) [Updating the Edison Firmware](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/updating-the-edison-firmware) [Using the XDK](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/using-the-xdk) [Connecting to WiFi](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/connecting-to-wifi) [Experiment 1: Hello, World!](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-1-hello-world) [Experiment 2: Pushing Some Buttons](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-2-pushing-some-buttons) [Experiment 3: Blinky](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-3-blinky) [Experiment 4: Email Notifier](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-4-email-notifier) [Experiment 5: Web Page](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-5-web-page) [Experiment 6: RGB LED Phone App](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-6-rgb-led-phone-app) [Experiment 7: Speaker](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-7-speaker) [Experiment 8: Temperature and Light Logger](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-8-temperature-and-light-logger) [Experiment 9: Weather on an LCD](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-9-weather-on-an-lcd) [Experiment 10: Keyboard](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-10-keyboard) [Experiment 11: Phone Accelerometer](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-11-phone-accelerometer) [Experiment 12: Bluetooth Game Controller](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/experiment-12-bluetooth-game-controller) [Finale: Next Steps](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/finale-next-steps) [Appendix A: Troubleshooting](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-a-troubleshooting) [Appendix B: Programming Without the XDK](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-b-programming-without-the-xdk) [Appendix C: Using a USB Network](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-c-using-a-usb-network) [Appendix D: Manually Updating the Firmware](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-d-manually-updating-the-firmware) [Appendix E: MRAA Pin Table](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/appendix-e-mraa-pin-table)

[Comments [1]](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-edison-experiment-guide/all) [Print]

- **Tags**
- - [BLE](https://learn.sparkfun.com/tutorials/tags/ble)
  - [Bluetooth](https://learn.sparkfun.com/tutorials/tags/bluetooth)
  - [Bluetooth Low Energy](https://learn.sparkfun.com/tutorials/tags/bluetooth-low-energy)
  - [Edison](https://learn.sparkfun.com/tutorials/tags/edison)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]