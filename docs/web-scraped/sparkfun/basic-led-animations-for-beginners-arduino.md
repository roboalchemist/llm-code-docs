# Source: https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Basic LED Animations for Beginners (Arduino)

# Basic LED Animations for Beginners (Arduino)

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1eb65dbfef2baccd546de184fb04e522?d=retro&s=20&r=pg) Brandon J. Williams]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft999&name=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft999 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Basic+LED+Animations+for+Beginners+%28Arduino%29&url=http%3A%2F%2Fsfe.io%2Ft999&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft999&t=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft999&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F9%2F9%2F9%2FLED_Tutorial.jpg&description=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Pin It")

## Introduction

The control of light has been a quest for humankind older than written history. The power of illumination stirs a biological feeling in us all. We\'ve evolved from chemical combustion of energy stored in wood to the greater volatility of gasoline vapor. The physical flame was then replaced by warm, glowing, delicate, metal coils. My favorite method of light is as simple as the humble electron shedding energy through the process of *Electroluminescence*. [Light Emitting Diodes](https://www.sparkfun.com/leds), [LEDs](https://www.sparkfun.com/leds), are vastly more energy efficient than past methods and provides near endless possibilities for combating the darkness.

[![LED Projects](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/9/9/9/LED_Tutorial.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/9/9/9/LED_Tutorial.jpg)

In this tutorial, we will revisit some concepts about using LEDs and make some fun effects using the RedBoard Qwiic to control the individual LEDs.

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Heads up!** You\'ll notice that in the pictures above and below, I\'m using a red version of the ultrasonic distance sensor. We\'ve updated our inventory with a more accurate model listed in this wish list. **Please** make sure you get the blue instead of the red version!

This list is just a trimmed down list from our new SparkFun Inventor\'s Kit featuring the RedBoard Qwiic. If you\'d rather purchase the full set for more electrical goodies, please feel free.

[![SparkFun Inventor\'s Kit - v4.1](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/3/7/15267-SparkFun_Inventor_s_Kit_-_v4.1-01a.jpg)](https://www.sparkfun.com/products/15267)

### [SparkFun Inventor\'s Kit - v4.1](https://www.sparkfun.com/products/15267) 

[ KIT-15267 ]

The fourth edition of our popular SIK, fully reworked from the ground up for a better learning experience! V4.1 now has the a...

**Retired**

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft999&name=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft999 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Basic+LED+Animations+for+Beginners+%28Arduino%29&url=http%3A%2F%2Fsfe.io%2Ft999&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft999&t=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft999&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F9%2F9%2F9%2FLED_Tutorial.jpg&description=Basic+LED+Animations+for+Beginners+%28Arduino%29 "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/all) [Next Page →\
[Revisit Basics]](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/revisit-basics)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/introduction) [Revisit Basics](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/revisit-basics) [Simple ON/OFF with GPIO](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/simple-onoff-with-gpio) [Lights, Camera, ACTION](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/lights-camera-action) [One for the Road](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/one-for-the-road) [Resources and Going Further](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/discuss) [Single Page](https://learn.sparkfun.com/tutorials/basic-led-animations-for-beginners-arduino/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Concepts](https://learn.sparkfun.com/tutorials/tags/concepts)
  - [Education](https://learn.sparkfun.com/tutorials/tags/education)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]