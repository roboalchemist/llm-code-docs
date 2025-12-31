# Source: https://learn.sparkfun.com/tutorials/openpir-hookup-guide

## Introduction

Passive Infrared (PIR) sensors detect motion in a local area and are the sensor of choice in security systems, home automation and proximity-sensing applications.

[![SparkFun OpenPIR](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/7/0/6/13968-01.jpg)](https://www.sparkfun.com/sparkfun-openpir.html)

### [SparkFun OpenPIR](https://www.sparkfun.com/sparkfun-openpir.html) 

[ SEN-13968 ]

The SparkFun OpenPIR is a highly customizable Passive Infrared (PIR) sensor based around the NCS36000 PIR controller. Passive...

**Retired**

The [SparkFun OpenPIR](https://www.sparkfun.com/products/13968) is a highly customizable PIR sensor based around the NCS36000 PIR controller. The OpenPIR allows you to set the sensitivity, trigger time and pulse mode of the motion sensor, so you can tailor-fit it to your application.

### Required Materials

To follow along with this hookup guide, a handful of components are suggested in addition to the OpenPIR. A microcontroller development board, like an [Arduino](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/13975), [Photon](https://www.sparkfun.com/products/13774) or [Teensy](https://www.sparkfun.com/products/13736) is recommended. The development board can be used to both power the OpenPIR and act on its motion triggers.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![Teensy 3.2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/9/13736-01.jpg)](https://www.sparkfun.com/products/13736)

### [Teensy 3.2](https://www.sparkfun.com/products/13736) 

[ DEV-13736 ]

The Teensy 3.2 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

You\'ll also need something to electrically connect the OpenPIR\'s power and signal pins to that microcontroller. The OpenPIR includes both a 0.1\" header and a 4-pin JST connector footprint, so you can use [male headers](https://www.sparkfun.com/products/116) or a [4-pin JST cable assembly](https://www.sparkfun.com/products/9916) to interface with the sensor.

[![Jumper Wires Premium 6\" M/M Pack of 100](https://cdn.sparkfun.com/r/140-140/assets/parts/5/9/8/2/10897-01.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html)

### [Jumper Wires Premium 6\" M/M Pack of 100](https://www.sparkfun.com/jumper-wires-premium-6-m-m-pack-of-100.html) 

[ PRT-10897 ]

These are 26 AWG jumper wires terminated as male to male. Use these to jumper from any female header on any board, to any oth...

[ [\$27.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 100](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/6/09139-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-100.html)

### [Jumper Wires Premium 6\" M/F Pack of 100](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-100.html) 

[ PRT-09139 ]

This is a SparkFun exclusive! These are 26 AWG jumper wires terminated as male to female. Use these to jumper from any male o...

[ [\$27.50] ]

[![JST Jumper 4 Wire Assembly](https://cdn.sparkfun.com/r/140-140/assets/parts/4/0/2/2/09916-02b.jpg)](https://www.sparkfun.com/jst-jumper-4-wire-assembly.html)

### [JST Jumper 4 Wire Assembly](https://www.sparkfun.com/jst-jumper-4-wire-assembly.html) 

[ PRT-09916 ]

This is a simple four wire cable. Great for jumping from board to board or just about anything else. There is a 4-pin JST con...

[ [\$1.95] ]

#### Tools

Finally, you\'ll need [soldering tools](https://www.sparkfun.com/categories/49) to electrically connect the connector of your choice to the OpenPIR. A [simple soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9163) should be all you need.

You may also need a small Phillips-head screwdriver to adjust the pair of trimpots on the back of the OpenPIR. Our [pocket screwdriver](https://www.sparkfun.com/products/12891) includes a small enough bit, as does the larger [screwdriver and bit set](https://www.sparkfun.com/products/10865).

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Tool Kit - Screwdriver and Bit Set](https://cdn.sparkfun.com/r/140-140/assets/parts/5/8/9/7/10865-01.jpg)](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html)

### [Tool Kit - Screwdriver and Bit Set](https://www.sparkfun.com/tool-kit-screwdriver-and-bit-set.html) 

[ TOL-10865 ]

There\'s nothing worse than getting ready for a good hack and then realizing that you can\'t even get the box open because you ...

[ [\$16.50] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Pocket Screwdriver Set](https://cdn.sparkfun.com/r/140-140/assets/parts/9/7/8/3/12891-01.jpg)](https://www.sparkfun.com/pocket-screwdriver-set.html)

### [Pocket Screwdriver Set](https://www.sparkfun.com/pocket-screwdriver-set.html) 

[ TOL-12891 ]

What should every hacker have available to them? That\'s right, a screwdriver (you have to get into those cases somehow). What...

[ [\$5.50] ]

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide)

### PIR Motion Sensor Hookup Guide 

An overview of passive infrared (PIR) motion detecting sensors, and how to hook them up to an Arduino.

## Hardware Overview

[![Power/output header](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_header.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_header.png)

Powering and interfacing with the OpenPIR is accomplished using the four pins broken out on the bottom of the board. Those pins are:

  Pin Label   Description
  ----------- ----------------------------------------------------
  A           Analog output of NCS36000 differential amplifiers.
  VCC         Power supply input
  GND         Ground supply input
  OUT         Digital output signal -- active-high.

More on those pins in the sections below.

#### Supplying Power

Power to the OpenPIR should be supplied to the VCC and GND pins. The OpenPIR\'s operating voltage supply range is **3V to 5.75V** \-\-- as specified by the board\'s NCS36000 PIR controller. That means it should work with any 3.3V or 5V system.

Electrical characteristics:

- **Voltage supply range:** 3VDC to 5.75VDC
- **Standby average current:** 80µA
- **Motion-detected average current:** 3mA (LED enabled)

The OpenPIR consumes relatively little power. When the sensor isn\'t triggered \-\-- and the activity LED is not illuminated \-\-- the OpenPIR will consume about 80µA. When active, the onboard LED\'s current draw dwarfs the PIR\'s operating current, consuming about 3mA. That LED can be disabled using the xLED jumper (see applicable section below).

#### Digital Motion Trigger Output

The **OUT** pin is an active-high digital signal, which indicates the OpenPIR\'s motion detection. When motion is detected, the pin is driven HIGH; otherwise it will be LOW.

This pin can drive up to 10mA \-\-- so you can hook an LED or other small load up to it. Otherwise it can be connected directly to a microcontroller input pin (no pull-up or pull-down resistor required).

The operation of this pin is mirrored by the green, reverse-entry \"DET\"-labeled LED \-\-- if the LED is on, the OUT pin should be HIGH.

The duration of a HIGH signal on the OUT pin is set by the \"OSC\" trimpot, which is discussed more in-depth later in this section.

#### Analog Output

The \"A\"-labeled output breaks out the amplified PIR signal before it\'s sent to a window comparator, and then to the OUT pin.

[![Block diagram location of \"A\" pin breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/NCS36000-block-diagram-a-highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/NCS36000-block-diagram-a-highlighted.png)

Absent of any motion, the voltage at this pin will hover around 2.1V (about 430 on a 5V Arduino\'s 10-bit ADC input). As motion is detected, though, that voltage may swing wildly.

[![Output from \"A\" pin, plotted in Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/serial-plotter-aout-example-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/serial-plotter-aout-example-2.png)

This pin can be used to get a better idea of what kind of motion triggered the PIR. Single passes by the PIR may only produce a small \"blip\" on the \"A\" pin, while vigorous motion may produce a large, spiky wave output.

### LED Output

A reverse-entry green LED is included on the board, which duplicates the status of the OUT pin. When motion is detected, the LED will illuminate; otherwise it will remain off.

[![Indicator LED On](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/Open_Pir-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/Open_Pir-03.jpg)

On initial power-up, the **LED will blink**, indicating the NCS36000 is in start-up mode. Start-up mode can last for a few seconds or a couple of minutes \-\-- the length of time spent in start-up depends on the position of the \"OSC\" trimpot. The start-up mode time upon shipment is about two minutes.

The LED can be **disabled by opening the \"xLED\" jumper**. Note that the LED will still blink during start-up mode, regardless of the jumper\'s state.

### Trimpots \-\-- Sensitivity and Oscillator Window

The pair of trimming potentiometers (trimpots) on the backside of the OpenPIR can be used to customize the behavior of your motion sensor.

[![Trimpots highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_pots.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_pots.png)

The **sensitivity trimpot** \-\-- labeled \"SEN\" \-\-- can be used to adjust the **view distance** of the OpenPIR. The more clockwise you turn this trimpot, the further your sensor should be able to see. When you receive the board, the trimpot will be centered, and the sensor will react to a person moving about in the 6 to 8 foot (2 to 2.5m) range. At the maximum sensitivity, the sensor will detect a person walking by at about 16 feet (5m).

Avoid turning the \"SEN\" trimpot all the way down (counter-clockwise). This will disable the OpenPIR\'s output -- even the most mobile environments will not trigger an active output.

The \"OSC\" trimpot ultimately controls the **length of time** the output remains HIGH. This trimpot is used to adjust the oscillator frequency of the NCS36000. Turning this trimpot clockwise **increases the length of time OUT remains high**.

With the OSC trimpot cranked all the way in the counterclockwise direction, the OUT pin will remain HIGH for about 400 milliseconds. Conversely, when the trimpot is turned to the far-clockwise, the OSC pin will remain HIGH for about 7.5 seconds. The trigger time should adjust relatively linearly between those two values. When you receive the board, it will be centered, and the trigger pulse will last a bit less than four seconds.

### Trigger Mode \-\-- Dual vs. Single

The NCS36000 supports two motion-detection modes: single-pulse and dual-pulse. Either of these modes can be selected using the switch adjacent to the trimpots on the back of the board.

[![Switch highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_switch_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_switch_1.png)

The NCS36000 uses a window comparator \-\-- a pair of [comparators](https://en.wikipedia.org/wiki/Comparator) with upper and lower voltage limits \-\-- to trigger a pulse on the OUT pin. In **single-pulse** mode, a voltage above *or* below the upper or lower comparators will trigger an output pulse. But in **dual-pulse** mode, the voltage must swing above the high comparator voltage and below the low comparator voltage \-\-- within a set time limit \-\-- to trigger an output.

These timing diagrams from the NCS36000 datasheet can help to clarify single-pulse versus dual-pulse:

[![Single vs. dual pulse mode detection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/single-vs-dual-pulse-modes.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/single-vs-dual-pulse-modes.png)

Single-pulse mode can be used to detect an object entering *or* exiting the PIR\'s field-of-view, while dual-pulse detection can be used to detect an object entering *and* leaving the view area.

## Hardware Assembly

Before you can power the OpenPIR and connect it to a project, you\'ll need to solder *something* to the quartet of pins on the bottom of the board.

New to soldering? Check out our [Through-Hole Soldering Tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) for a quick introduction!

The OpenPIR\'s power and output pins are broken out to both a standard 0.1\" header and a 4-pin JST PH connector, leaving you a number of options for what, exactly, you\'ll solder to the sensor. To the 0.1\" header, you can solder [male headers](https://www.sparkfun.com/products/116) (or the [right-angle version](https://www.sparkfun.com/products/553)), [female headers](https://www.sparkfun.com/products/115) or [wire](https://www.sparkfun.com/products/11375).

[![Right angle header pins, in a breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/Open_Pir-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/Open_Pir-01.jpg)

Or you can solder a [4-Pin JST connector](https://www.sparkfun.com/products/9916) to the smaller-pitch footprint.

[![4-pin JST shown connected to sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/Open_Pir-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/Open_Pir-02.jpg)

As a bonus, plugging our [4-wire JST cable assembly](https://www.sparkfun.com/products/9916) into the OpenPIR will logically color-code the power supply pins \-\-- VCC on red, GND on black, OUT on yellow, and the analog output connected to blue.

## Software

The firmware example below uses [Arduino](https://www.arduino.cc/) to demonstrate how both the digital output and analog output can be used. Here is the example circuit used in the example code:

[![Fritzing diagram for this sketch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/openpir_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/openpir_bb.png)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

Then upload the example code below so you can begin to get a feel for the OpenPIR\'s output pins:

    language:c
    //////////////////////////
    // Hardware Definitions //
    //////////////////////////
    #define PIR_AOUT A0  // PIR analog output on A0
    #define PIR_DOUT 2   // PIR digital output on D2
    #define LED_PIN  13  // LED to illuminate on motion

    #define PRINT_TIME 100 // Rate of serial printouts
    unsigned long lastPrint = 0; // Keep track of last serial out

    void setup() 
    

    void loop() 
    

    void readDigitalValue()
    

    void printAnalogValue()
    
    }

This code uses the Arduino\'s onboard LED \-\-- on pin 13 \-\-- to reflect the OpenPIR\'s digital motion output. When motion is detected, the Arduino\'s LED should illuminate.

Four values are printed to the serial terminal \-\-- the reading from the digital pin (multiplied by 5\...for a reason), the upper and lower comparator voltage thresholds and the reading from the analog pin. Open up your serial monitor \-\-- setting the baud rate to 115200 \-\-- to see them stream by:

[![Serial terminal output example](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/serial-terminal-example-3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/serial-terminal-example-3.png)

Since it may be difficult to visualize the sensor\'s analog output using the serial terminal, try opening up the **serial plotter** (found under the \"Tools\" \> \"Serial Plotter\" menu).

[![Serial plotter example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/2/8/serial-plotter-voltage-thresholds.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/2/8/serial-plotter-voltage-thresholds.png)

You should see two separate line graphs: the light blue indicating the analog value and the dark blue representing the digital output. The orange and red straight lines represent the upper and lower thresholds, which the analog value must exceed to trigger motion.

Wave at the sensor to get a better feel for the analog output\'s behavior. And make sure you try both single and dual modes to see how the switch alters the sensor\'s functionality.