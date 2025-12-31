# Source: https://learn.sparkfun.com/tutorials/boss-alarm

## Introduction 

It\'s a common occurrence in any office \-- you\'re on Facebook or browsing SparkFun when all of a sudden your boss walks in to see that you\'re not working.

This project aims to avoid that embarrassment and frowns from management. The Boss Alarm alerts you of anyone walking into your office and automatically changes the active program on your computer. The sensors are inconspicuously hidden in cute woodland creatures that are guaranteed to brighten up your office and definitely not creep out any of your coworkers!

[![Owl Face](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlFace.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlFace.jpg)

*Definitely not creepy*

The Boss Alarm uses an infrared breakbeam sensor made with a few common components. The design is based on schematics from [this article](http://jumperone.com/2011/11/break-beam-sensor/) with a few modifications.

There are three components to the Boss Alarm. There is a transmitter (hidden in the squirrel) that sends an invisible beam to the owl. The owl contains an infrared receiver (namely, the [TSOP38238 IR Receiver Diode](https://www.sparkfun.com/products/10266)) and also another infrared transmitter. The last component is another IR receiver connected to a [Teensy 3.2](https://www.sparkfun.com/products/13736).

[![Boss Alarm](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/BossAlarm.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/BossAlarm.jpg)

*Harmless woodland creatures!*

The Teensy is configured as a USB keyboard device. When the beam between the owl and the squirrel is broken, the owl sends a signal to the Teensy. When the Teensy receives this signal, it simply sends the Alt+Tab keyboard command to your computer to change the active program. If you are on a different operating system, you can change the key commands to whatever you want (for example, Windows Key + D to minimize all programs). You can trigger practically anything using this project.

Check out a video of the project in action below:

### Materials

You\'re going to need a few things to build this project yourself.

Along with those parts, you will need a few other parts and tools:

- Various common parts including [resistors](https://www.sparkfun.com/products/10969), [capacitors](https://www.sparkfun.com/products/13698), and [transistors](https://www.sparkfun.com/products/521) (this project uses an NPN 2N3904)
- A single LED, but just [get a whole bunch](https://www.sparkfun.com/products/12903) \'cause they\'re awesome!
- [Hookup wire](https://www.sparkfun.com/products/11375)
- [Wire strippers](https://www.sparkfun.com/products/12630) and pliers
- [Soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9325)
- It\'s always a good idea to have [desoldering wick](https://www.sparkfun.com/products/9327) in case you make mistakes (it\'s easy to forget the pinout of those IR receivers\...)
- You may need a common electric drill and bit set
- [Heat-shrink tubing](https://www.sparkfun.com/products/9353) and a source of heat

If you plan on installing the electronics in the woodland creature enclosures, you will also need access to a 3D printer and a hot glue gun. You may also wish to paint them.

I highly recommend obtaining some sort of [oscilloscope](https://www.sparkfun.com/categories/371) for troubleshooting, but it is not necessary to complete this project. You may also want to acquire a decent [multimeter](https://www.sparkfun.com/products/12966) for diagnosing any issues you encounter.

### Recommended Reading

You may need to read up on a few subjects to wrap your head around this project:

- [Through Hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering?_ga=1.135210549.564444804.1449868290)
- [How to use an Oscilloscope](https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope?_ga=1.1729457.1029302230.1445479273)
- [Infrared Light for Electrical Engineers](https://learn.sparkfun.com/tutorials/light?_ga=1.5793843.1029302230.1445479273#infrared-light)
- [Infrared Communication](https://learn.sparkfun.com/tutorials/ir-communication?_ga=1.5793843.1029302230.1445479273)
- [Getting Started with the Teensy](https://learn.sparkfun.com/tutorials/getting-started-with-the-teensy?_ga=1.39348899.1029302230.1445479273)
- [The 555 Timer](http://www.555-timer-circuits.com/an-overview.html)
- [How to Read a Schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic?_ga=1.208863762.1029302230.1445479273)
- [Transistors](https://learn.sparkfun.com/tutorials/transistors?_ga=1.203009681.1029302230.1445479273)
- [Pull-Up Resistors](https://learn.sparkfun.com/tutorials/pull-up-resistors?_ga=1.216550166.1029302230.1445479273)

## Printing the Models

[![Owl Model](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlModel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlModel.jpg)

*Sectioned owl model enclosure*

[![Squirrel Model](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelModel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelModel.jpg)

*The cute squirrel model*

I am more of an engineer than an artist, so I sourced the basic owl and squirrel models from Autodesk\'s 123Dapp website. The original artist\'s page for the owl can be [found here](http://www.123dapp.com/make/owl/3646032). And the squirrel\'s artist can be [found here](http://www.123dapp.com/123C-3D-Model/Wooden-Squirrel-Statue/593199).

[![Unpainted Models](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/ModelsUnpainted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/ModelsUnpainted.jpg)

*The elusive nuclear-green owl*

I modified the models a bit to fit the electronics inside. The owl was too tall for my printer to handle so I separated it into two parts and used printed pegs to align them. This also aids in assembly later on and isn\'t too noticeable. I used Autodesk\'s free, online program, [Tinkercad](https://www.tinkercad.com/), to create the models.

You should start the printer now, the models take a while to print!

## Making the Squirrel Transmitter

The transmitter is a simple astable 555 timer circuit. The 555 timer is a popular and versatile ([and some might say dated](https://www.sparkfun.com/news/2007)) IC found in many hobbyist projects.

The parts you need for this component of the project are:

- 220Ω, 2.2kΩ, and 10kΩ Resistors (1 each)
- 10kΩ potentiometer
- 1nF and 10nF ceramic capacitors
- Infrared LED
- 555 timer (x1)
- 9V Battery Connector and 9V Battery
- Snapable Protoboard
- Heatshrink Tubing

Here\'s the circuit diagram:

[![Squirrel Transmitter Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/SquirrelTransmitter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelTransmitter.jpg)

The infrared receivers we are using have built-in filtering that makes them very reliable for digital communication. However, in order for the receivers to see our infrared beam we need to modulate it (turn it off and on) at 38kHz.

When operated in astable mode, the 555 timer will oscillate between high and low voltage at a frequency determined by external resistors and capacitors. If you want to learn more about how to work with a 555 timer, there are several [websites](http://www.555-timer-circuits.com/) dedicated to the chip.

Let me remind you of the pinout for the infrared receiver:

[![TSOP Pinout](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/TSOPPinout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/TSOPPinout.jpg)

*Ask me why I know this by heart\...*

Solder together the circuit in the diagram, try to keep it a bit compact so it fits in the model nicely! The squirrel can accommodate a 9V battery and a circuit board about 1.25 X 1 and 0.5 inches tall.

[![Squirrel Circuit board](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelCircuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelCircuit.jpg)

*The Squirrel\'s circuit board*

Don\'t solder the infrared LED directly on the board. Instead, solder some longer-than-you-think-you-need wires onto the LED\'s terminals making sure to note which one is the anode (+) and which is the cathode (-).

[![Soldering leads on the LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/LEDSolder.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/LEDSolder.jpg)

To avoid short circuits, you should put some shrink wrap tubing on the soldered connections. You can use a heat gun or a blow dryer to shrink the tubing. I used a lighter but be careful not to melt the LED or yourself.

[![Shrink wrap on the LEDs](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/LEDShrinkWrap.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/LEDShrinkWrap.jpg)

If you are using the printed models, I recommend painting them so they blend into your desk\'s knick-knacks better.

You can install the infrared LED in the squirrel\'s acorn. You may need to drill out the hole a bit to make the LED fit. Feed the wires through the model until they come out the bottom and then use a little hot glue to keep the LED in place. Tuck the wires away, and then no one will notice the squirrel is actually a nark!

[![Squirrel Circuit board installed](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelInstalled.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelInstalled.jpg)

*The squirrel\'s circuit board installed*

[![Squirrel Overview](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelAcorn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/SquirrelAcorn.jpg)

*The finished squirrel transmitter*

## Making the Owl Transceiver

### Circuit Operation

Here\'s the circuit schematic for the owl:

[![Owl Transceiver Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/OwlTransceiver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlTransceiver_Large.jpg)

*Click the image for a closer look.*

The circuit for the owl may look really complicated but it\'s not! The owl transceiver operates in a way similar to the squirrel transmitter. Only instead of having one 555 timer circuit, the owl has TWO! Let\'s go through it step by step.

The owl has a 555 timer operating in monostable mode and another operating in astable mode. The IR Receiver Diode is an **active low** device. This means that, when it receives a signal, the output pin is pulled low. This works great with our 555 timer since the trigger pin needs to be pulled low to activate the monostable circuit.

The monostable circuit is designed to hold the output high for approximately 1 second (this timing isn\'t crucial) when triggered by the IR Receiver.

The next part of the circuit is our reset transistor. There are two current-limiting resistors (1kΩ for the base, 220Ω for the Red eye LED) and a 10kΩ pull-down resistor on the transistor\'s emitter.

Notice that the emitter is also connected to the reset pin of the second 555 timer. In most astable applications, you tie the reset pin to the supply voltage so the chip is always on. However, in this project we only want the owl to send a signal to the computer when someone walks by.

In this configuration, when the output of the first 555 is low, the transistor will be off. The pull-down resistor makes sure the voltage seen by the second 555 timer\'s reset pin is around 0V, keeping it off. When the circuit is triggered, the red LED and the transistor turn on. Since the transistor is conducting, the voltage at the emitter becomes high enough to enable the second 555 timer for about 1 second.

The second 555 timer is designed to operate in astable mode at 38kHz just like the circuit in the squirrel. This sends another infrared signal to your computer telling it that someone walked by!

The additional circuits shown in the schematic are the 5V regulator circuit and the infrared receiver filtering circuit. The regulator simply takes the 9 volts from the battery and outputs a stable 5V source that plays nicely with our infrared receiver. The filtering circuit has a couple capacitors that help stabilize the output of the receiver and a pull-up resistor to keep the output high when the receiver is off.

### Soldering Time!

The parts you need for this component of the project are:

- 100Ω, 220Ω (x2), 1kΩ, 2.2kΩ, 10kΩ (x3), and 100kΩ Resistors
- 10kΩ potentiometer
- 1nF, 10nF (x2), 0.1μF (x3), and 10μF (x2) capacitors
- Infrared LED
- Red LED
- Infrared Receiver
- 555 timer (x2)
- 2N3904 NPN Transistor
- L7805 Regulator
- 9V Battery Connector
- Snapable Protoboard
- Heatshrink Tubing

Build the circuit according to the included schematic. Make sure not to solder the red and infrared LEDs or the infrared receiver. Just like with the squirrel, solder on some long wires to these, and cover the connections with shrink tubing.

[![Owl Circuit Board](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlBoard.jpg)

*Completed owl circuit board. It looks complicated, but that\'s just because it\'s densely populated!*

Paint the owl however you want; I went with a classic brown woodland owl. Again, you may need to drill out the mounting holes to get the parts to fit. It\'s best to do this before painting the models to avoid scratching the paint off.

When your model is prepped, you can install the components. The infrared LED is mounted in the hole on the side of the log. The Red LED goes in either eye of the owl. The IR receiver goes in the other eye of the owl. Solder the components to the board, and it should be all set!

[![Owl Side of Log](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/OwlSide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlSide.jpg)

*Hot glue the infrared LED in the side of the log. I accidentally melted the paint a bit, try to avoid that!*

[![Owl Eyes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/OwlEyes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlEyes.jpg)

*The Red LED and the IR receiver get installed in the head of the owl. The split in the model makes installation much easier!*

[![Owl Overview](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/OwlOverview.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OwlOverview.jpg)

*The completed owl model. Such beautiful eyes!*

## Tuning the Transmitters

You may have noticed each astable 555 timer circuit includes a potentiometer. This allows us to fine-tune the frequency at which the circuit oscillates. We want it to be as close to 38kHz as possible so the receiver can see it in full strength.

This is where an oscilloscope comes in handy. This nice piece of kit lets you visualize voltage waveforms in (pretty much) real time. My current oscilloscope is a USB-based one called the [Analog Discovery 2 by Digilent](http://store.digilentinc.com/analog-discovery-2-100msps-usb-oscilloscope-logic-analyzer-and-variable-power-supply/). This device not only acts as a 2-channel oscilloscope but also has a 2-channel function generator, a variable power supply, a pattern generator for digital circuits, and a logic analyzer! I prefer actual lab equipment but the Analog Discovery is nice for how compact and affordable it is.

[![Analog Discovery 2](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/AnalogDisco2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/AnalogDisco2.jpg)

*Analog Discovery 2 \-- [Photo courtesy of Digilent](https://reference.digilentinc.com/analog_discovery_2:analog_discovery_2)*

Use a small screwdriver to adjust the potentiometer. When you have it tuned *just* right, you may want to hot glue the knob in place so it doesn\'t get changed accidentally. Make sure to repeat this procedure for each transmitter circuit!

[![Tuning the potentiometer](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/TuningPot.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/TuningPot.jpg)

*Tuning the transmitter frequency with a potentiometer*

### Tuning Without an Oscilloscope

To tune the circuit without an oscilloscope, you can just play with the potentiometer until the circuit operates reliably. The IR receiver *will* work with frequencies that are close enough to 38kHz.

### Tuning With an Oscilloscope

If you are lucky enough to have access to an oscilloscope, this part becomes very easy. Simply hook your probe up to the output pin of the astable 555 timer, and the waveform should appear. You can adjust the potentiometer until the frequency is about 38kHz.

With the equipment mentioned above, measure the frequency of the wave using vertical cursors, and place them one period apart. The inverse of the difference between them will be your frequency (the oscilloscope usually does this calculation for you).

[![Tuning frequency with oscilloscope](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/OscopeTuning.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/OscopeTuning.jpg)

*Checking the frequency using an oscilloscope. Notice the frequency is almost exactly 38kHz!*

If you\'re just getting started with the oscilloscope, you should read [this guide](https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope?_ga=1.1729457.1029302230.1445479273).

## Making the Computer Receiver

The computer receiver is just a copy of the IR filtering circuit used in the owl hooked up to a Teensy 3.2.

[![Computer Receiver](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/ComputerReceiver.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/ComputerReceiver.jpg)

*The IR filter and Teensy connected. I used an old servo connector to join the two boards. Notice the pins the filter board connects to. (Contrary to convention) Black is Vs, red is ground, and white is out.*

### Build the Circuit

The parts you need for this component of the project are:

- Teensy 3.2 and USB Cable
- Male headers
- 100Ω and 10kΩ Resistors
- 0.1μF, and 10μF capacitors
- Infrared Receiver
- Snapable Protoboard

Here\'s the schematic again:

[![IR Filtering Schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/1/7/IRFiltering.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/IRFiltering.jpg)

First, solder headers on your Teensy board, if you haven\'t already.

Solder together the IR filtering circuit, and use a connector to tie the Teensy\'s power and ground pins to the appropriate pins on the infrared receiver. Make sure to use the V_USB pin to get a 5V source rather than the 3.3V source on the Teensy. Connect the output of the receiver to pin 0 on the Teensy.

[![IR Filtering Board](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/IRFilterBoard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/IRFilterBoard.jpg)

*The IR filtering board. Notice I messed up with the IR receiver: it\'s soldered twice!*

### Programming the Teensy

Plug the Teensy into your computer, and get ready to program it! If you haven\'t used the Teensy before, read [this guide](http://www.pjrc.com/teensy/tutorial.html) to get started.

The Teensy is like an Arduino, but it has a unique feature \-- it can be configured as a USB device. This lets your computer \"see\" the Teensy as another device and automatically load the drivers for it. For example, you can configure the Teensy as a USB keyboard (as in this project), and, when you plug it in, your computer will see it as a keyboard \-- no special software required!

The code used in this project is almost identical to the Teensy\'s USB keyboard example sketch. We simply treat the output of the IR receiver as a switch and send key presses/releases on the falling/rising edge of the receiver\'s output.

    language:c
    /* Title: Boss Alarm
     * Date: 3/14/2016
     * Author: Don Beckstein

       Note: You must select Keyboard from the "Tools > USB Type" menu

    */

    #include <Bounce.h>

    // Helps us debounce the output from the IR receiver (helps suppress false-alarms)
    Bounce button0 = Bounce(0, 100);

    //Change these to set the key combination used
    unsigned const int modifierKey = MODIFIERKEY_ALT;
    unsigned const int combinationKey = KEY_TAB;

    //If you're on Mac you can try this code (I haven't tested it)
    //unsigned const int modifierKey = MODIFIERKEY_GUI;
    //unsigned const int combinationKey = KEY_TAB;

    //If you want it to show your desktop on Windows instead of switch windows, use this code:
    //Sends Windows Key + D
    //unsigned const int modifierKey = MODIFIERKEY_GUI;
    //unsigned const int combinationKey = KEY_D;

    void setup() 

    void loop() 

      //Release the keyboard keys when the trigger returns to normal
      if (button0.risingEdge()) 
    }

The default key combination is ALT+Tab to switch between programs on Windows. If you have multiple monitors you might want all programs to be minimized. I included a few different key combinations in the code, you can uncomment/comment lines of code to suit your needs. I also included a key combination that should work on Mac. If you want to make your own key command, [this page](http://www.pjrc.com/teensy/td_keyboard.html) provides a reference to the Teensy\'s defined keys.

Make sure to click **Tools-\>Board-\>Teensy 3.2** and **Tools-\>USB Type-\>Keyboard+Mouse+Joystick** to set up your Teensy correctly. Load the Boss Alarm code onto your Teensy, and it should be all set!

## Setting Up the Boss Alarm

The squirrel and owl should be placed across from each other at the same height for best operation. Make sure the IR LED in the owl is pointing towards your computer! The Boss Alarm should work well for typical small office spaces.

Remember that light can reflect (including infrared, we just can\'t see it)! You may find that the IR signal coming from the squirrel gets picked up by your Teensy receiver causing false-alarms. If this happens, reposition the squirrel so it is angled away from your Teensy receiver.

Plug in the Teensy board, and that\'s it!

The Boss Alarm will change your active program using Alt-Tab. Make sure the last program you had selected was work-related. Excel has some nice templates that certainly look business-y.

[![Owl wave test](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/owl-wave.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/owl-wave.gif)

*The red LED lets you know it\'s working.*

[![Screen Change](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/screen-change.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/4/1/7/screen-change.gif)

*The active program changes to something more business-y*

The Boss Alarm has the unintended benefit that when your boss walks away, it will trigger again and return your active program to whatever you were doing before!

Now you can browse SparkFun at work without fear of your boss finding out. :)