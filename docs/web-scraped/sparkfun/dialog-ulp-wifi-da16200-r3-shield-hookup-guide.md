# Source: https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Dialog ULP WiFi DA16200 R3 Shield Hookup Guide

# Dialog ULP WiFi DA16200 R3 Shield Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/088c8f0e731f2ba1712ed20b6b921c35?d=retro&s=20&r=pg) Alex the Giant], [ Ell C]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1991&name=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1991 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1991&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1991&t=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1991&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F9%2F1%2F18567-SparkFun_Qwiic_WiFi_Shield_-_DA16200-01.jpg&description=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Pin It")

## Introduction

Ultra. Low. Power. Arguably the best three words in the IoT world. SparkFun has teamed up with ARM and Dialog to provide you with the [ULP WiFi R3 Shield](https://www.sparkfun.com/products/18567) based around the DA16200 module. The DA16200 is a fully integrated WiFi module with a 40MHz crystal oscillator, 32.768KHz RTC clock, RF Lumped RF filter, 4MB flash memory, and an onboard chip antenna. With the addition of a Qwiic connector, multiple GPIO options, JTAG connectors for deep dive programming, and you\'ve got everything you need to get your R3 layout device ready to set up your next IoT project.

The SparkFun Qwiic WiFi Shield is ideal for door locks, thermostats, sensors, pet trackers, and other home IoT projects, thanks in part to the multiple sleep modes that allow you to take advantage of current draws as low as 0.2uA-3.5uA.

Additionally, the DA16200 module\'s certified WiFi alliance for IEEE802.11b/g/n, WiFi Direct, and WPS functionalities means that it has been approved for use by multiple countries and using the WiFi Alliance transfer policy, each WiFi Certification can be transferred without being tested again.

[![SparkFun Qwiic WiFi Shield - DA16200](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/0/2/6/18567-SparkFun_Qwiic_WiFi_Shield_-_DA16200-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-wifi-shield-da16200.html)

### [SparkFun Qwiic WiFi Shield - DA16200](https://www.sparkfun.com/sparkfun-qwiic-wifi-shield-da16200.html) 

[ WRL-18567 ]

SparkFun has teamed up with ARM and Dialog to provide you with this WiFi Shield based around the DA16200 module.

[ [\$19.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/connectivity-of-the-internet-of-things)

### Connectivity of the Internet of Things 

An overview of the different protocols that can be used for the development of Internet of Things (IoT)-based projects.

[](https://learn.sparkfun.com/tutorials/arduino-shields-v2)

### Arduino Shields v2 

An update to our classic Arduino Shields Tutorial! All things Arduino shields. What they are and how to assemble them.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1991&name=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1991 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1991&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1991&t=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1991&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F9%2F9%2F1%2F18567-SparkFun_Qwiic_WiFi_Shield_-_DA16200-01.jpg&description=Dialog+ULP+WiFi+DA16200+R3+Shield+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/hardware-overview) [Hardware Hookup](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/hardware-hookup) [Example 1: Baud Rate Shenanigans](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/example-1-baud-rate-shenanigans) [Example 2: GPIO and LEDs](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/example-2-gpio-and-leds) [Example 3: Connecting to WiFi](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/example-3-connecting-to-wifi-) [Troubleshooting](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/resources--going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/dialog-ulp-wifi-da16200-r3-shield-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Power](https://learn.sparkfun.com/tutorials/tags/power)
  - [Shields](https://learn.sparkfun.com/tutorials/tags/shields)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]