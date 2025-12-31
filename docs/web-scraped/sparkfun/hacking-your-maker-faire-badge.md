# Source: https://learn.sparkfun.com/tutorials/hacking-your-maker-faire-badge

## Introduction

The SparkFun Faire Game Badge is not only fun at Maker Faire, but also gives you the power of a full microcontroller you can use at home! This tutorial will walk you through the process of hooking up your board to other electronics, as well as how to upload new code.

[![Maker Faire Badges](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-06.jpg)

### Suggested Reading

If you aren\'t familiar with the following concepts, you may want to read up on these additional tutorials before moving forward with hacking your badge.

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Bootloader](https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)
- [Through-hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering)
- [Pulse-Width Modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

## Board Overview

The Badge has several features you should be aware of when hacking on it.

[![Bare Badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-01.jpg)

*Bare badge, showing all features discussed below.*

### Microcontroller

The IC on this board is the ATMega328. This is the same chip that runs the [Arduino Uno](https://www.sparkfun.com/products/11021), and several of our [LilyPad boards](https://www.sparkfun.com/categories/135). However, this board relies on the internal oscillator of the 328, instead of having an external crystal like the Uno or LilyPad main board.

### Power System

The board has a battery holder for a 3V, 20mm coin cell battery. We recommend using the [CR2032](https://www.sparkfun.com/products/338), as this has a higher capacity of 250mAh at 3V. The ON/OFF switch at the bottom of the board enables the user to turn off the battery supply when the badge is not in use.

The board can also be powered off of the 3.3V and GND pins on the FTDI header on the left side of the board. This is not connected in any way to the ON/OFF switch, so the board will run as long as this is connected.

### Communication

There are several methods of communicating with your badge. The first is the FTDI header on the left hand side of the board. The board mates with a [3.3V FTDI Breakout Board](https://www.sparkfun.com/products/9873), which enables you to communicate via serial over a USB interface to the board.

You can also communicate or program the board via the ICSP header on the right side of the board. This will communicate with the board using SPI protocol.

### Participation Indicator

This is an RGB LED, located in the top center of the board (right where the lovely silk label points!). The board comes pre-programmed with this LED functioning as a participation indicator for our #makergame, but you can use this for any purpose you so desire. The blue channel of the LED is connected to pin D9 on the ATMega328, the red channel connects to pin D10, and the green channel connects to pin D11/MOSI. Keep this in mind if you decide to use the ICSP header for hacking your badge later - use of the MOSI line will restrict your ability to use the green channel on the LED.

The three pins to which the LED connects are capable of pulse-width-modulation (PWM) control, so this is a nice feature to be aware of when you are thinking how you would like to hack your board.

### Buzzer

The buzzer is located on the left side of the board. This comes pre-programmed to act as an indicator for our #makergame, just like the LED. Again, though, just like the LED, you can reprogram your board to use this for whatever application you\'d like. The buzzer is tied to D2 on the ATMega328.

### Additional I/O Pins

There are 14 additional pins broken out for you, the user, to configure on your badge. Digital pins 3-8 are broken out on the bottom right side of the board. Pins 3, 5, and 8 are capable of PWM control, which makes these useful pins for things like driving servos or other small motors.

Analog pins 0-7 are broken out on the bottom left side of the board. These pins can be used for analog-to-digital conversion, and are very helpful for interfacing with sensors that have analog signal outputs.

## Assembling the Board

Now that you are familiar with the hardware available on the badge, it\'s time to assemble it.

We will be using [male headers](https://www.sparkfun.com/products/553) for this tutorial, but keep in mind that you could use [female headers](https://www.sparkfun.com/products/115) if you so choose.

To begin, break apart six sets of 2-pin headers from the strip of male headers. Place these in the holes labeled \"Initials Boards\" on the top of the pcb. Then, *without soldering anything*, place the three initials boards onto the headers.

[![Placing letter boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-02.jpg)

You want to place the initials boards before soldering to ensure everything lines up correctly and will fit together on the front of the badge. The headers will wiggle a bit doing this, so it may help to have your pcb clamped using a [third hand](https://www.sparkfun.com/products/11784).

Now that you have the three initials boards lined up and placed on your badge, it\'s time to begin soldering. Start soldering the initials boards to the headers. Take your time and reposition the boards as needed as you go, so everything continues to line up.

[![Soldering Initials Boards](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-03.jpg)

Once all of the initials boards have been soldered to the headers, it\'s time to flip your badge over. It may be easier to only solder the back of one initials board to the badge at a time. However, since you already ensured everything will line up, this shouldn\'t be a problem!

[![Back of Badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-04.jpg)

*The back of your badge should look like this once the intials boards are soldered.*

These letter boards just act as jumpers between the headers, so keep in mind you could use hookup wire in place of the initials boards.

It\'s now time to add in additional headers. You will want to solder headers to the FTDI connection at the very least, as well as to any of the digital or analog pins broken out. If you plan on changing the bootloader on the board, you will also want to solder headers to the ICSP.

[![Back of the badge, fully soldered](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-05.jpg)

In order to allow the badge to lay relatively flat when being worn, you will want to make sure you are always soldering on the back of the badge. It should look like the picture above once you are done.

Once you have that complete, flip your badge back over and be proud of your work! Your badge is ready to act as a full Arduino and be hacked!

[![Completed Badge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/8/Maker_Faire_Badge_Hacking_Tutorial-06.jpg)

## Uploading Code

With your board soldered and ready to go, you can now program your badge just like you would any other Arduino!

As mentioned previously, this board does not have an external crystal on it. For production runs of this board,the bootloader from the [OpenSegment](https://github.com/sparkfun/OpenSegment) was used. Keep this in mind if you decide to overwrite the bootloader via the ICSP or ever need to [reinstall the bootloader](https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader). Setting the fuse bits incorrectly for an external oscillator will lead to a bricked badge, so be very careful to double check before writing over the bootloader!

When uploading code to your board from the Arduino IDE, you will want to select the \"Pro or Pro Mini (3.3V, 8MHz) w/ ATmega328\" board option. Keep in mind as you write new code for your board that you do have some pins that are not available as they are on a standard Arduino, as described previously in the #Board Overview.