# Source: https://learn.sparkfun.com/tutorials/how-to-play-multiple-buzzers-at-once

## Polyphony in Action

Simple electronic sound devices, such as the [SparkFun Qwiic Buzzer](https://www.sparkfun.com/products/24474) can output one note at a time. For a simple beep here or a buzz there, this works just fine. However, if your project needs a little more pizzaz than a single note then you'll have to utilize multiple buzzers at once. This is what is called Polyphony. Polyphony is simply when two or more separate tones or melodies are sounded out simultaneously. As mentioned before, Qwiic Buzzers only make one sound at a time so in order to create a polyphonic melody you would need to utilize multiple Qwiic Buzzers. This involves setting each buzzer to a different I2C address and playing different notes simultaneously, creating more complex and rich soundscapes in your projects.

In this tutorial, we\'ll connect three Qwiic Buzzers to a [RedBoard](https://www.sparkfun.com/products/18158) microcontroller and play a melody, harmony, and bass part of one of the most recognizable tunes of all time; the Super Mario Bros theme!

## Hardware Needed

- Three [SparkFun Qwiic Buzzers](https://www.sparkfun.com/products/24474)
- We'll use the [SparkFun RedBoard Plus](https://www.sparkfun.com/products/18158) in this example but any Arduino compatible board should work.
- [Qwiic cables](https://www.sparkfun.com/products/15081)

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun RedBoard Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/4/8/7/18158-SparkFun_RedBoard_Plus-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-plus.html)

### [SparkFun RedBoard Plus](https://www.sparkfun.com/sparkfun-redboard-plus.html) 

[ DEV-18158 ]

The RedBoard Plus is an Arduino-compatible development board that has everything you need in an Arduino Uno with extra perks ...

[ [\$29.50] ]

[![SparkFun Qwiic Buzzer](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/8/3/2/BOB-24474-Qwiic-Buzzer-Feature.jpg)](https://www.sparkfun.com/sparkfun-qwiic-buzzer.html)

### [SparkFun Qwiic Buzzer](https://www.sparkfun.com/sparkfun-qwiic-buzzer.html) 

[ BOB-24474 ]

The SparkFun Qwiic Buzzer adds simple beeps and buzzes to your projects via I2C. Make some noises to alert you when something...

[ [\$10.50] ]

 

------------------------------------------------------------------------

 

## Connecting the Hardware

### Connections are breeze with Qwiic:

1.  Connect three SparkFun Qwiic Buzzers to your microcontroller via the Qwiic connectors.
2.  Ensuring each buzzer has a unique I2C address is key to playing the buzzers simultaneously:
    - Default addresses are **0x34**, **0x35**, and **0x36** for the melody, harmony, and bass buzzers, respectively.
3.  Setup Simple Circuit: Use Qwiic cables to daisy-chain the buzzers to the microcontroller.

 

[![Qwiic Buzzer Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/4/0/qwiic-buzzer-nintendo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/4/0/qwiic-buzzer-nintendo.jpg)

If you\'ve been to SparkFun HQ you\'ll recognize our giant Nintendo controller.

 

------------------------------------------------------------------------

 

## Software Setup

Before you begin you\'ll first need to [Install the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide/all) and SparkFun Qwiic Buzzer Arduino Library.

### Installing the Qwiic Buzzer Library

- Open the Arduino IDE.
- Go to Sketch \> Include Library \> Manage Libraries\...
- Search for \"SparkFun Qwiic Buzzer Arduino Library\" and install it or install from the link below.

[Qwiic Buzzer Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_Buzzer_Arduino_Library)

 

------------------------------------------------------------------------