# Source: https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Experiment Guide for the Johnny-Five Inventor\'s Kit

# Experiment Guide for the Johnny-Five Inventor\'s Kit

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/36c697d974542aadaee06a0f39cb1437?d=retro&s=20&r=pg) rwaldron], [![](https://cdn.sparkfun.com/avatar/4e96e258e9d3bd640f9917d0ebda2639?d=retro&s=20&r=pg) reconbot], [![](https://cdn.sparkfun.com/avatar/bb21dc7d7c75175fd6edb50cda25d83f?d=retro&s=20&r=pg) D\_\_\_Run\_\_\_], [![](https://cdn.sparkfun.com/avatar/1c08c5bb17f9099b228de7077b587bcf?d=retro&s=20&r=pg) lyzadanger], [![](https://cdn.sparkfun.com/avatar/4f445d9df43505cdae80a4d6f18cfe89?d=retro&s=20&r=pg) Shawn Hymel]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft523&name=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft523 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit&url=http%3A%2F%2Fsfe.io%2Ft523&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft523&t=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft523&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F5%2F2%2F3%2F13847-_BMP_200_Update.jpg&description=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Pin It")

## Introduction to the Johnny-Five Inventor\'s Kit

**Note:** This tutorial was originally written for [KIT-13847](https://www.sparkfun.com/products/13847). However, you should not notice any significant differences when using it with KIT-14604. We just updated the resistor lead thickness, buttons, and silkscreen of the TB6612FNG motor driver.

[![Johnny-Five Inventor\'s Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/6/9/14604-Johnny_Five_Inventor_s_Kit-01.jpg)](https://www.sparkfun.com/products/14604)

### [Johnny-Five Inventor\'s Kit](https://www.sparkfun.com/products/14604) 

[ KIT-14604 ]

The Johnny-Five Inventor\'s Kit (J5IK) is your go-to source for developing projects using the Tessel 2 and the Johnny-Five pro...

**Retired**

The [Johnny-Five Inventor\'s Kit](https://www.sparkfun.com/products/14604) you have in front of you is your toolkit, and this Experiment Guide is your map. We\'re going to dive into the world of embedded electronics, JavaScript, the internet, and the way they come together as the \"Internet of Things\" (IoT).

The [Johnny-Five](http://www.johnny-five.io) JavaScript framework provides a beginner-friendly way to start building things---quickly. This guide contains all the information you need to successfully build the circuits in all 14 experiments. At the center of this guide is one core philosophy: that *anyone* can (*and should*) play around with basic electronics and code.

When you\'re done with this guide, you\'ll have the know-how to start creating your *own* projects and experiments. You can build robots, automate your home, or log data about the world around you. The world, in fact, will be your hardware-hacking oyster. Enough inspirational sentiment --- let\'s get building!

**Note:** To get started with this guide you will need to have an internet connection and administrative privileges on the computer that you are using.

### Included Materials

Here are all of the parts in the Johnny-Five Inventor\'s Kit for the Tessel 2 (J5IK):

- **Tessel 2** --- The Tessel 2 Single-Board Computer (SBC)
- **USB-A to USB micro B** --- for connecting your computer to the Tessel 2
- **Wall Charger (5V, 1A)** --- Gotta power the Tessel 2 somehow! This charger makes it easy to power your projects!
- **Breadboard** --- This perforated grid is the ticket to easy experimentation with circuits.
- **Carrying Case** --- Take your kit anywhere with ease!
- **Jumper wires** --- These multi-colored wires with pins on each end making connecting things together a breeze.
- **Rainbow Pack of LEDs** --- LEDs are indispensable. Here\'s a whole rainbow of \'em.
- **100 Ohm Resistors** --- These are just about right for using with LEDs at 3.3V (the voltage we\'ll be using for the circuits in this guide)
- **10K Ohm Resistors** --- These make excellent pull-ups, pull-downs and current limiters (don\'t worry if you haven\'t seen these terms before)
- **Photocell** --- A sensor that detects ambient light. Also called a *photoresistor*. Perfect for detecting when a drawer is opened or when nighttime approaches.
- **10KΩ Trimpots** --- Also known as a variable resistor or a *potentiometer*, this is a device commonly used to control volume and contrast (it usually has a dial or a slider), and makes a great general user control input.
- **Red, Blue, Yellow and Green Tactile Buttons** --- These fun-to-press buttons give you several colors to choose from.
- **RGB LED** --- Why use an LED that can only be one color when you can have *any* color?
- **SPDT (Single-Pole, Dual Throw) Switch** --- It\'s a switch! You slide it back and forth, and it fits into a breadboard just great.
- **Magnetic Door Switch** --- A mountable magnetic switch used in home automation and security. Great for detecting when a door or drawer is opened!
- **BME280 Atmospheric Sensor Breakout** --- A sensor for detecting temperature, pressure and humidity. It communicates using the I2C serial communication protocol. The header pins are soldered on for you, which makes connecting this to your project nice and easy.
- **Soil Moisture Sensor** --- The name describes it pretty well!
- **SparkFun Motor Driver** --- This nifty little board is perfect for controlling the speed and direction of up to two separate motors.
- **Hobby Gearmotor Set** --- A set of hobby level motors (two of \'em) with gearboxes set to 120 RPM.
- **7 Segment Display** --- It\'s an LED that lets you display numerals via the combination of lit-up segments, just like an alarm clock from the 1980s!
- **3.3V 16x2 White on Black LCD** --- This LCD can display 16 characters on two lines with a snazzy white-on-black background appearance. It operates at 3.3 volts (this is the voltage that the Tessel 2 is most comfortable with).
- **74HC595 Shift Register** --- An integrated circuit (IC) that allows you to increase the number of inputs and outputs you can control from a microcontroller.

### Suggested Reading

While you can get through this guide without doing any outside reading, the following tutorials cover the essential core of electronics and circuits and are super useful:

[](https://learn.sparkfun.com/tutorials/what-is-a-circuit)

### What is a Circuit? 

Every electrical project starts with a circuit. Don\'t know what a circuit is? We\'re here to help.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

### Open Source!

At SparkFun, our engineers and educators are constantly improving kits such as these and coming up with new experiments. We would like to give attribution to Rick Waldron and [Bocoup](https://bocoup.com), as he originally started the development of Johnny-Five many years ago. The contents of this guide are licensed under the [Creative Commons Attribution Share-Alike 4.0 Unported License](http://creativecommons.org/licenses/by-sa/4.0/).

To view a copy of this license visit [this link](http://creativecommons.org/licenses/by-sa/4.0/), or write: Creative Commons, 171 Second Street, Suite 300, San Francisco, CA 94105, USA.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft523&name=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft523 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit&url=http%3A%2F%2Fsfe.io%2Ft523&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft523&t=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft523&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F5%2F2%2F3%2F13847-_BMP_200_Update.jpg&description=Experiment+Guide+for+the+Johnny-Five+Inventor%27s+Kit "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/all) [Next Page →\
[About the Tessel 2]](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/about-the-tessel-2)

← Previous Page

[**Pages**] [Introduction to the Johnny-Five Inventor\'s Kit](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/introduction-to-the-johnny-five-inventors-kit) [About the Tessel 2](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/about-the-tessel-2) [Ports and Pins on the Tessel 2](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/ports-and-pins-on-the-tessel-2) [Software Installation and Setup](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/software-installation-and-setup) [Hardware Installation and Setup](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/hardware-installation-and-setup) [Experiment 1: Blink an LED](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-1-blink-an-led) [Experiment 2: Multiple LEDs](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-2-multiple-leds-) [Experiment 3: Reading a Potentiometer](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-3-reading-a-potentiometer) [Experiment 4: Reading a Push Button](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-4-reading-a-push-button) [Experiment 5: Reading an SPDT Switch](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-5-reading-an-spdt-switch) [Experiment 6: Reading a Light Sensor](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-6-reading-a-light-sensor) [Experiment 7: Animating LEDs](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-7-animating-leds) [Experiment 8: Driving an RGB LED](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-8-driving-an-rgb-led) [Experiment 9: Using an H-Bridge Motor Controller](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-9-using-an-h-bridge-motor-controller-) [Experiment 10: Using the BME280](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-10-using-the-bme280) [Experiment 11: Soil Moisture Sensor](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-11-soil-moisture-sensor) [Experiment 12: Using an LCD Screen](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-12-using-an-lcd-screen) [Experiment 13: Controlling LEDs with a Shift Register](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-13-controlling-leds-with-a-shift-register) [Experiment 14: Driving a Seven-Segment Display](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-14-driving-a-seven-segment-display) [Troubleshooting](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/troubleshooting) [Resources for Going Further](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/resources-for-going-further)

[Comments [8]](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/discuss) [Single Page](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/all) [Print]

- **Tags**
- - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Internet of Things](https://learn.sparkfun.com/tutorials/tags/internet-of-things)
  - [Javascript](https://learn.sparkfun.com/tutorials/tags/javascript)
  - [Johnny-Five](https://learn.sparkfun.com/tutorials/tags/johnny-five)
  - [LEDs](https://learn.sparkfun.com/tutorials/tags/leds)
  - [Light](https://learn.sparkfun.com/tutorials/tags/light)
  - [Motors](https://learn.sparkfun.com/tutorials/tags/motors)
  - [Node.js](https://learn.sparkfun.com/tutorials/tags/node-js)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)
  - [Weather](https://learn.sparkfun.com/tutorials/tags/weather)
  - [WiFi](https://learn.sparkfun.com/tutorials/tags/wifi)
  - [Wireless](https://learn.sparkfun.com/tutorials/tags/wireless)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]