# Source: https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Qwiic 12-Bit ADC Hookup Guide

# Qwiic 12-Bit ADC Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/f4f3cfa206713c4cee74e50b8ddf07cd?d=retro&s=20&r=pg) QCPete], [ santaimpersonator]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft899&name=Qwiic+12-Bit+ADC+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft899 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+12-Bit+ADC+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft899&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft899&t=Qwiic+12-Bit+ADC+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft899&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F9%2F9%2FInput_Screwdriver.jpg&description=Qwiic+12-Bit+ADC+Hookup+Guide "Pin It")

## Introduction

An [analog to digital converter (ADC)](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) is very useful tool for converting an analog voltage to a digital signal that can be read by a microcontroller. The ability to converting from analog to digital interfaces allows users to use electronics to interface to interact with the physical world.

[![SparkFun Qwiic 12 Bit ADC - 4 Channel (ADS1015)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/8/5/7/15334-SparkFun_Qwiic_12_Bit_ADC_-_4_Channel__ADS1015_-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-12-bit-adc-4-channel-ads1015.html)

### [SparkFun Qwiic 12 Bit ADC - 4 Channel (ADS1015)](https://www.sparkfun.com/sparkfun-qwiic-12-bit-adc-4-channel-ads1015.html) 

[ DEV-15334 ]

The SparkFun Qwiic 12 Bit ADC can provide four channels of I^2^C controlled ADC input to your Qwiic enabled project.

[ [\$9.95] ]

The [SparkFun Qwiic (12-bit) ADC](https://www.sparkfun.com/products/15334) provides four channels of I^2^C controlled ADC input to your Qwiic enabled project. These four channels can be used as single-ended inputs, or in pairs for differential inputs. The ADS1015 uses its own internal voltage reference for measurements, but the ground and 3.3V power are also available on the pin outs for users.

**Note:** The maximum resolution of the converter is **12-bits** in differential mode and **11-bits** for single-ended inputs. Step sizes range from 125μV per count to 3mV per count depending on the full-scale range (FSR) setting.

### Required Materials

The [SparkFun Qwiic ADC](https://www.sparkfun.com/products/15334) does need a few additional items for you to get started; a Qwiic enabled microcontroller, a Qwiic cable, and jewelry/precision screwdrivers (with **1.5mm** and **2.5mm flathead bits**). You may already have a few of these items, so feel free to modify your cart based on your needs.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun Thing Plus - SAMD51](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/2/7/14713-SparkFun_Thing_Plus_-_SAMD51-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html)

### [SparkFun Thing Plus - SAMD51](https://www.sparkfun.com/sparkfun-thing-plus-samd51.html) 

[ DEV-14713 ]

With a 32-bit ARM Cortex-M4F MCU, the SparkFun SAMD51 Thing Plus is one of our most powerful microcontroller boards yet!

[ [\$25.50] ]

[![SparkFun RedBoard Turbo - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/7/9/14812-SparkFun_RedBoard_Turbo_-_SAMD21_Development_Board-01b.jpg)](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html)

### [SparkFun RedBoard Turbo - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-redboard-turbo-samd21-development-board.html) 

[ DEV-14812 ]

If you're ready to step up your Arduino game from older 8-bit/16MHz microcontrollers, the SparkFun RedBoard Turbo is a form...

[ [\$22.50] ]

[![SparkFun Thing Plus - ESP32 WROOM](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/9/4/14689-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/products/14689)

### [SparkFun Thing Plus - ESP32 WROOM](https://www.sparkfun.com/products/14689) 

[ WRL-14689 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

**Retired**

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Magnetic Screwdriver Set (20 Piece)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/3/1/6/15003-Magnetic_Screwdriver_Set__24_Piece_-04.jpg)](https://www.sparkfun.com/products/15003)

### [Magnetic Screwdriver Set (20 Piece)](https://www.sparkfun.com/products/15003) 

[ TOL-15003 ]

This is a 20 piece screwdriver set that magnetically keeps each of the unused bits secured inside of a thin case that easily ...

**Retired**

### Suggested Reading:

If you\'re unfamiliar with analog to digital converters, jumper pads, or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

Additional Reading on Analog Circuits

**Note:** For a background on analog circuitry, check out these tutorials:\
\

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)

### Series and Parallel Circuits 

An introduction into series and parallel circuits.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic ADC utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the [**Logic Levels**](https://learn.sparkfun.com/tutorials/logic-levels) and [**I^2^C**](https://learn.sparkfun.com/tutorials/i2c) tutorials before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft899&name=Qwiic+12-Bit+ADC+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft899 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Qwiic+12-Bit+ADC+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft899&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft899&t=Qwiic+12-Bit+ADC+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft899&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F9%2F9%2FInput_Screwdriver.jpg&description=Qwiic+12-Bit+ADC+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/hardware-assembly) [Arduino Library](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/a) [Arduino Examples](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/arduino-examples) [Troubleshooting](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/troubleshooting) [Resources and Going Further](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/resources-and-going-further)

[Comments [1]](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/qwiic-12-bit-adc-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Components](https://learn.sparkfun.com/tutorials/tags/components)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Prototyping](https://learn.sparkfun.com/tutorials/tags/prototyping)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]