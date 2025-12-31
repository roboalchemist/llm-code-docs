# Source: https://learn.sparkfun.com/tutorials/tech-prank-hardware-mouse-jiggler

## Introduction

If you\'re looking for a way to prank your friends, coworkers, or classmates, messing with their computer is a sure bet. Changing the background or flipping the screen is so 2003. To help modernize your practical jokes, here is a USB stick that shows up as a regular mouse and moves the pointer around every 10-20 seconds. Perfect for annoying your victims.

[![April Fools\' Prank: hardware mouse jiggler using an Arduino Pro Micro](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-08.jpg)

### Required Materials

To follow along with this project tutorial, you will need the following materials:

You will also need some 30 AWG wire to connect the breakout board to the Pro Micro.

### Tools

To build this project, you will need the following tools:

- [3D Printer](https://www.sparkfun.com/products/13256)
- [Hot Air Rework Station](https://www.sparkfun.com/products/14557)
- [Soldering Iron](https://www.sparkfun.com/products/11704)
- [Solder](https://www.sparkfun.com/products/10243)
- [Flux](https://www.sparkfun.com/products/14579)
- [Tweezers](https://www.sparkfun.com/products/10602)
- [Wire Strippers](https://www.sparkfun.com/products/12630)
- Double-Sided Foam Tape or Servo Tape

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing:

[](https://learn.sparkfun.com/tutorials/pcb-basics)

### PCB Basics 

What exactly IS a PCB? This tutorial will breakdown what makes up a PCB and some of the common terms used in the PCB world.

[](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide)

### Pro Micro & Fio V3 Hookup Guide 

An overview of the Atmega32U4-based Pro Micro and FioV3, how to install it, and how to use it with Arduino.

It will also help to understand how to [program your Pro Micro to act as a USB Mouse](https://www.sparkfun.com/tutorials/337).

## Build the USB Breakout Board

The first thing you\'ll need to do is make a tiny USB type A male connector breakout board that\'s the same width as the Pro Micro.

I\'ve included the KiCad files and zipped Gerbers. You can order them directly from [OSH Park](https://oshpark.com/shared_projects/jdgNiU7e) or mill them yourself using something like the [Bantam Tools Milling Machine](https://www.bantamtools.com/products/bantam-tools-desktop-pcb-milling-machine). To get them, click on the button to download the GitHub repository and search for the \"*USB_Male-gerbers.zip*\" file in the **\.../USB_Male/gerbers** directory.

[Download Hardware Mouse Jiggler Repository](https://github.com/ShawnHymel/Hardware_Mouse_Jiggler/archive/master.zip)

Once you have the board made, solder on the USB connector. If you make a 1-sided board like I did, you\'ll need to solder the connector on the top side.

[![Built USB Type A Male connector breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-10.jpg)

## Build the Case

In order to hide the prank in plain sight, you will want to create a case for it that obscures the bright red board. You\'re welcome to wrap it in electrical tape or spray paint it (I recommend black, as it will likely hide it among most USB cables).

I took the extra steps and made a simple 3D printed case for it. You can find the design files on [Tinkercad](https://www.tinkercad.com/things/0UCciUgonUd). Alternatively, you can download the ready-to-print files on [Thingiverse](https://www.thingiverse.com/thing:2817144) or the **.stl** and **.obj** files can be found in the **\.../Case** directory in the [project repository](https://github.com/ShawnHymel/Hardware_Mouse_Jiggler/archive/master.zip). Simply import them into your slicer tool of choice and run the print to get an enclosure for your hardware.

[![The 3D printed case can hold the Pro Micro and USB breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-09.jpg)

## Hardware Assembly

To assemble the entire project, you will first want to de-solder the USB connector from the Pro Micro. Do this by applying flux to all the pads and using a hot air rework station to reflow all the joints while carefully lifting up on the connector with a set of tweezers.

[![Use a hot air rework station to remove the USB connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-01.jpg)

Place the USB connector breakout next to the Pro Micro, and carefully [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) 30 AWG wires from the bare USB micro pads on the Pro Micro to the through holes on the breakout board. Note that you\'ll need to have the wires cross over each other to make sure the right connections are made (otherwise you might fry your Pro Micro, like I did on my first attempt). The connections that you need to make are found in the diagram below.

[![Arduino Pro Micro to USB breakout wiring diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/Circuit_Diagram_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/Circuit_Diagram_annotated.png)

Carefully bend the wires so that the USB breakout board and Pro Micro are flush next to each other.

[![Solder some 30 AWG wire to connect the Pro Micro to the USB breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-03.jpg)

Apply some foam tape or servo tape to the bottom of the Pro Micro and USB board.

[![Double-sided tape on the Pro Micro and USB breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-04.jpg)

Place them inside the 3D printed case, pressing down to adhere them to the enclosure.

[![Arduino Pro Micro and USB breakout board inside the enclosure](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-05.jpg)

Slide the enclosure\'s top into the grooves to cover the boards.

[![Slide the top into the case\'s grooves to make your USB stick](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-06.jpg)

The hardware assembly is done! You should be able to plug it into your computer like this to program it from the Arduino software.

[![Completed USB stick hardware with Arduino Pro Micro and USB breakout board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-07.jpg)

## Programming

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Follow the instructions found in the [Pro Micro Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide) to ensure you can upload programs to the Pro Micro from Arduino. From there, copy the following code into Arduino and upload it to your Pro Micro:

    language:c
    /**
     * April Fools' Mouse Prank
     * Date: February 27, 2018
     * Author: Shawn Hymel (SparkFun Electronics)
     * 
     * Upload this to a SparkFun Pro Micro, and plug it into an 
     * unsuspecting computer. That's it!
     * 
     * This sketch was written by SparkFun Electronics, with lots of
     * help from the Arduino community. This code is completely free
     * for any use.
     */

    #include "Mouse.h"

    #define DEBUG 0

    // Parameters
    const int NUM_STATES = 3;             // Number of possible animations
    const unsigned long WAIT_MIN = 10000; // ms (inclusive)
    const unsigned long WAIT_MAX = 20000; // ms (exclusive)
    const unsigned long JUMP_MIN = -1000; // Pixels (inclusive)
    const unsigned long JUMP_MAX = 1000;  // Pixels (exclusive)
    const int DIR_MIN = 0;                // Degrees (inclusive)
    const int DIR_MAX = 360;              // Degrees (exclusive)
    const int SPD_MIN = 1;                // Pixels (inclusive)
    const int SPD_MAX = 5;                // Pixels (exclusive)
    const int LINE_ACC = 10;              // Number of times to accumulate
    const int LINE_NUM_MIN = 50;          // Min number of times to move in line
    const int LINE_NUM_MAX = 300;         // Max number of times to move in line
    const int JITTER_MIN = -4;            // Pixels (inclusive)
    const int JITTER_MAX = 5;             // Pixels (exclusive)
    const int JITTER_NUM_MIN = 50;        // Min number of times to jitter
    const int JITTER_NUM_MAX = 300;       // Max number of times to jitter

    // Patterns
    typedef enum  mouse_states;

    void setup() 

    void loop() 
    }

    void mouseJump() 

    void mouseLine() 
        Mouse.move((int)(x_acc + 0.5), (int)(y_acc + 0.5), 0);

        delay(10);
      }

    #if DEBUG
      Serial.print("Moving x:");
      Serial.print((int)(x_acc + 0.5));
      Serial.print(" y:");
      Serial.println((int)(y_acc + 0.5));
    #endif
    }

    void mouseJitter() 
    }

You are welcome to play around with the numbers in the `Parameters` section if you want to make the delay longer between movements or make the jumps farther.

## Run It!

Find an unsuspecting target and plug the device into an open USB port. I highly recommend targeting someone with a desktop, as the USB ports on most laptops are quite visible. On a desktop, you have a shot at hiding the device among all the other cables:

[![Hiding the USB prank box among other cables](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/April_Fools_Tutorial-11.jpg)

Now, when your target comes back, their mouse pointer should randomly jump, jitter, and move once every few seconds!

[![The Mouse Jiggler in action](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/mouse_jiggler.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/3/mouse_jiggler.gif)