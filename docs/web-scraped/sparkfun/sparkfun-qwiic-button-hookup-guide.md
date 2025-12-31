# Source: https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- SparkFun Qwiic Button Hookup Guide

# SparkFun Qwiic Button Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/931a585884e4ef21a40d470f7df5c553?d=retro&s=20&r=pg) El Duderino]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1108&name=SparkFun+Qwiic+Button+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1108 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Qwiic+Button+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1108&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1108&t=SparkFun+Qwiic+Button+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1108&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F8%2F15932-SparkFun_Qwiic_Button_-_Red-01.jpg&description=SparkFun+Qwiic+Button+Hookup+Guide "Pin It")

## Introduction

Buttons are a great way to add a tactile input to your project but dealing with pull-up resistors, debouncing, polling, and using GPIO pins for each button can be a hassle. Enter the [Qwiic Button (Red](https://www.sparkfun.com/products/15932) or [Green](https://www.sparkfun.com/products/16842)) and the [Qwiic Button Breakout](https://www.sparkfun.com/products/15931)! These breakouts eliminate nearly all the inconvenience of using buttons by converting everything to an easy-to-use I^2^C connection using the [Qwiic Interface](https://www.sparkfun.com/qwiic).

[![SparkFun Qwiic Button - Red LED](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/5/7/3/15932-SparkFun_Qwiic_Button_-_Red-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-button-red-led.html)

### [SparkFun Qwiic Button - Red LED](https://www.sparkfun.com/sparkfun-qwiic-button-red-led.html) 

[ BOB-15932 ]

The SparkFun Qwiic Button with red LED simplifies all of those nasty worries away into an easy to use I2C device, no solderin...

[ [\$5.50] ]

[![SparkFun Qwiic Button - Green LED](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/6/7/16842-SparkFun_Qwiic_Button_-_Green_LED-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-button-green-led.html)

### [SparkFun Qwiic Button - Green LED](https://www.sparkfun.com/sparkfun-qwiic-button-green-led.html) 

[ BOB-16842 ]

The SparkFun Qwiic Button with green LED simplifies all of those nasty worries away into an easy to use I2C device, no solder...

[ [\$4.95] ]

[![SparkFun Qwiic Button Breakout](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/5/7/2/15931-SparkFun_Qwiic_Button_Breakout-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-button-breakout.html)

### [SparkFun Qwiic Button Breakout](https://www.sparkfun.com/sparkfun-qwiic-button-breakout.html) 

[ BOB-15931 ]

The SparkFun Qwiic Button Breakout simplifies all of those nasty worries away into an easy to use I2C device, and with our Qw...

[ [\$3.95] ]

We have three versions of the Qwiic Button available. The Qwiic Button (Red) and Qwiic Button (Green) come with a pre-populated red or green pushbutton with a built in LED to illuminate the button and the Qwiic Button Breakout leaves the button unpopulated so you can choose your own tactile button.

Using the Qwiic Button is as simple as sending the command `button.isPressed()` to check the status of the button. In addition to handling status checks and debouncing, the Qwiic Button has a configurable interrupt pin which can be adjusted to activate upon a button press or click. This allows you to trigger specific behavior or functions in your code when the button is used and frees up processing time that would normally be used to constantly poll a button\'s state.

The Qwiic Button also includes a First-in First-Out ([FIFO Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))) which keeps track of when the button was pressed so if you are hosting a game show you can easily keep track of which contestant pressed their button first without needing to constantly poll the buttons!

## Required Materials

The Qwiic Button requires a Qwiic-enabled microcontroller:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![SparkFun Qwiic Micro - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/0/15423-SparkFun_Qwiic_Micro_-_SAMD21-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html)

### [SparkFun Qwiic Micro - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html) 

[ DEV-15423 ]

The SparkFun Qwiic Micro is molded to fit our standard 1\" x 1\" Qwiic board size which makes it our smallest SAMD21 micro-cont...

[ [\$22.95] ]

And you will also need a Qwiic cable:

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

Or, if you want to use a microcontroller without a Qwiic connector, you can add one using one of our Qwiic Shields, the Qwiic Adapter board, or adapter cables:

[![SparkFun Qwiic Adapter](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/5/1/14495-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-adapter.html)

### [SparkFun Qwiic Adapter](https://www.sparkfun.com/sparkfun-qwiic-adapter.html) 

[ DEV-14495 ]

The SparkFun Qwiic Adapter provides the perfect means to make any old I^2^C board into a Qwiic enabled board.

[ [\$1.60] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![Qwiic Cable - Female Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/2/9/2/14988-Qwiic_Cable_-_Female_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/products/14988)

### [Qwiic Cable - Female Jumper (4-pin)](https://www.sparkfun.com/products/14988) 

[ CAB-14988 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and female connectors o...

**Retired**

Finally, if you are using the [Qwiic Button Breakout](https://www.sparkfun.com/products/15931) you\'ll need to solder a button to the board:

[![Momentary Pushbutton Switch - 12mm Square](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/2/9/09190-03-L.jpg)](https://www.sparkfun.com/momentary-pushbutton-switch-12mm-square.html)

### [Momentary Pushbutton Switch - 12mm Square](https://www.sparkfun.com/momentary-pushbutton-switch-12mm-square.html) 

[ COM-09190 ]

This is a standard 12mm square momentary button. What we really like is the large button head and good tactile feel (it \'clic...

[ [\$0.75] ]

[![LED Tactile Button - Green](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/2/8/10440-LED_Tactile_Button_-_Green-01.jpg)](https://www.sparkfun.com/led-tactile-button-green.html)

### [LED Tactile Button - Green](https://www.sparkfun.com/led-tactile-button-green.html) 

[ COM-10440 ]

This is a simple LED-illuminated tactile button with a green cap. It\'s just like a basic tactile button, but it lights up gre...

[ [\$2.50] ]

[![LED Tactile Button - Blue](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/3/1/10443-LED_Tactile_Button_-_Blue-01.jpg)](https://www.sparkfun.com/led-tactile-button-blue.html)

### [LED Tactile Button - Blue](https://www.sparkfun.com/led-tactile-button-blue.html) 

[ COM-10443 ]

This is a simple LED-illuminated tactile button with a clear cap. It\'s just like a basic tactile button, but it lights up blu...

[ [\$2.75] ]

[![LED Tactile Button- White](https://cdn.sparkfun.com/r/140-140/assets/parts/4/9/2/7/10439-LED_Tactile_Button-_White-01.jpg)](https://www.sparkfun.com/led-tactile-button-white.html)

### [LED Tactile Button- White](https://www.sparkfun.com/led-tactile-button-white.html) 

[ COM-10439 ]

This is a simple LED-illuminated tactile button with a clear cap. It\'s just like a basic tactile button, but it lights up whi...

[ [\$2.75] ]

Realistically, you can solder any pushbutton to the Qwiic Button Breakout so long as it fits the button footprint. We have a couple other options available in our [Button Category](https://www.sparkfun.com/categories/313) that will work perfectly with the Qwiic Button Breakout.

[] **Heads Up!** If you choose an LED Tactile Button, pay close attention to the polarity marks on your button and Qwiic Button Breakout to place it correctly. If the button is inserted with reverse-polarity, the LED will not work. If you are not positive on the polarity of your LED Button, you can [**use a multimeter to check.**](https://learn.sparkfun.com/tutorials/polarity/diode-and-led-polarity)

Additional Tools for Soldering to the Qwiic Button Breakout

**Note:** If you want to use the Qwiic Button Breakout then you will need to solder a tactile button to the board. You may already have a few of these items, so feel free to modify your cart based on your needs.

[![Digital Multimeter - Basic](https://cdn.sparkfun.com/r/140-140/assets/parts/9/9/0/7/12966-01.jpg)](https://www.sparkfun.com/digital-multimeter-basic.html)

### [Digital Multimeter - Basic](https://www.sparkfun.com/digital-multimeter-basic.html) 

[ TOL-12966 ]

The digital multimeter (DMM) is an essential tool in every electronic enthusiasts arsenal. The SparkFun Digital Multimeter, h...

[ [\$21.50] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![SparkFun Beginner Tool Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/8/8/3/14681-SparkFun_Beginner_Tool_Kit.jpg)](https://www.sparkfun.com/products/14681)

### [SparkFun Beginner Tool Kit](https://www.sparkfun.com/products/14681) 

[ TOL-14681 ]

This assortment of tools is great for those of you who need a solid set of tools to start your workbench on the right foot!

**Retired**

## Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading here for an overview:

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/button-and-switch-basics)

### Button and Switch Basics 

A tutorial on electronics\' most overlooked and underappreciated component: the switch! Here we explain the difference between momentary and maintained switches and what all those acronyms (NO, NC, SPDT, SPST, \...) stand for.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1108&name=SparkFun+Qwiic+Button+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1108 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=SparkFun+Qwiic+Button+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1108&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1108&t=SparkFun+Qwiic+Button+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1108&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F1%2F0%2F8%2F15932-SparkFun_Qwiic_Button_-_Red-01.jpg&description=SparkFun+Qwiic+Button+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/hardware-overview) [Hardware Assembly](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/hardware-assembly) [Qwiic Button Arduino Library](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/qwiic-button-arduino-library) [Arduino Examples](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/arduino-examples) [Register Map](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/register-map) [Python Package](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/python-package) [Python Examples](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/python-examples) [Resources and Going Further](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/resources-and-going-further)

[Comments [9]](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-button-hookup-guide/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [ATtiny](https://learn.sparkfun.com/tutorials/tags/attiny)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Input Devices](https://learn.sparkfun.com/tutorials/tags/input-devices)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]