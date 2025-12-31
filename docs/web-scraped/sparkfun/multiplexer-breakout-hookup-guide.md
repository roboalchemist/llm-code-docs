# Source: https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide

## Introduction

The [SparkFun Multiplexer Breakout](https://www.sparkfun.com/products/13906) provides access to all pins and features of the 74HC4051, an 8-channel analog multiplexer/demultiplexer. The 74HC4051 allows you to turn four I/O pins into eight multi-functional, individually-selectable signals, which can be used do everything from driving eight LEDs to monitoring eight potentiometers.

[![SparkFun Multiplexer Breakout - 8 Channel (74HC4051)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/6/3/13906-01.jpg)](https://www.sparkfun.com/sparkfun-multiplexer-breakout-8-channel-74hc4051.html)

### [SparkFun Multiplexer Breakout - 8 Channel (74HC4051)](https://www.sparkfun.com/sparkfun-multiplexer-breakout-8-channel-74hc4051.html) 

[ BOB-13906 ]

The SparkFun Multiplexer Breakout provides access to all pins and features of the 74HC4051, an 8-channel analog multiplexer/d...

[ [\$3.50] ]

A multiplexer, commonly abbreviated down to **\"mux\"**, is an electronically-actuated switch, which can turn one signal into many. It routes a common input signal to any number of separate outputs. Similarly, a *de*multiplexer routes any number of selectable inputs to a single common output.

The 74HC4051 can function as either a multiplexer or a demultiplexer, and it features **eight channels** of selectable inputs/outputs. The routing of common signal to independent I/O is set by digitally controlling three **select lines**, which can be set either high or low into one of eight [binary](https://learn.sparkfun.com/tutorials/binary) combinations.

### Covered In This Tutorial

This tutorial covers everything you should need to assemble the Multiplexer Breakout then wire it and integrate it into your project. Included in the tutorial are a pair of Arduino examples, which demonstrate how to use the mux for both digital output and analog input. The tutorial is split into the following sections, which you can navigate through using the bar on the right.

- [74HC4051 Breakout Overview](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide#74hc4051-breakout-overview) \-- A quick introduction to the workings of the 74HC4051 and the extra features of the breakout board.
- [Board Assembly](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide#board-assembly) \-- Tips and tricks for soldering headers or wires to your breakout and mounting it into your project.
- [Arduino Example: Output](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide#arduino-example-output) \-- An Arduino circuit and example code demonstrating how to use the multiplexer to drive eight LEDs.
- [Arduino Example: Input](https://learn.sparkfun.com/tutorials/multiplexer-breakout-hookup-guide#arduino-example-input) \-- Circuit and an Arduino sketch explaining how to use the board to read eight analog voltage-producing photocells.

### Suggested Reading

Muxes are a great tool for electronics users of all experience levels \-- anyone who needs to multiply their project\'s pin count. There are a few subjects you should be familiar with before diving into multiplexing, though. If the subjects below sound foreign to you, consider browsing through that tutorial before continuing on.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/digital-logic)

### Digital Logic 

A primer on digital logic concepts in hardware and software.

## 74HC4051 Breakout Overview 

The Multiplexer Breakout\'s [schematic](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/SparkFun-Mux-Breakout-74HC4051.pdf) is just about as simple as it gets: There\'s the chip, a decoupling capacitor, a pull-up resistor, and all of the pins are broken out (some broken out twice):

[![Board top](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/breakout-top-rotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/breakout-top-rotated.jpg)

One half of the board breaks out the control signals ([E], S0-S2) and common input/output (Z). The other side provides access to all eight independent I/O\'s (Y0-Y7). Both sides include supply and ground connections (V~CC~, V~EE~, GND). The table below summarizes each pin and its function.

  ------------------------------------------------------------------------------------------------------------------------------------
  Pin Label                                Function          Input/Output\   Notes
                                                             (to board)      
  ---------------------------------------- ----------------- --------------- ---------------------------------------------------------
  [E]   Enable            Input           Active low enable

  S2, S1, S0                               Select Controls   Input           Select inputs, S2 is the msb and S0 is the lsb

  Z                                        Common I/O        Input/Output    Common output or input

  GND                                      Ground            Supply          Ground supply voltage (0V)

  VCC                                      Positive supply   Supply          Positive supply voltage (2-10V)

  VEE                                      Negative supply   Supply          Negative supply voltage (Jumpered to ground by default)

  Y7, Y6, Y5, Y4,\                         Independent I/O   Input/Output    Selectable I/O to be routed to common pin
  Y3, Y2, Y1, Y0                                                             
  ------------------------------------------------------------------------------------------------------------------------------------

### 74HC4051 Logic Table

The select pins (S2-S0), in addition to the enable pin ([E]), control which (if any) of the eight independent I/O pins (Y0-Y7) are connected to the common pin (Z). The function table below shows how those pins work together to select the I/O.

  ----------------------------------------------------------------------------
  [E]   S2   S1   S0   I/O Connected to Z
  ---------------------------------------- ---- ---- ---- --------------------
  L                                        L    L    L    Y0

  L                                        L    L    H    Y1

  L                                        L    H    L    Y2

  L                                        L    H    H    Y3

  L                                        H    L    L    Y4

  L                                        H    L    H    Y5

  L                                        H    H    L    Y6

  L                                        H    H    H    Y7

  H                                        X    X    X    None
  ----------------------------------------------------------------------------

Assuming the mux is powered at 5V, \"L,\" for \"low\", is any voltage between 0 and about 2V and \"H\" \-- \"high\" \-- is any voltage between around 3 and 5V. \"X\" means it doesn\'t matter what the logic level of the pin is (because it will be trumped by the enable pin).

The **enable ([E])** pin is pulled low on the breakout board via a 10kΩ resistor. If your project doesn\'t require enabling/disabling the mux, you can leave that pin unused.

### Power Supply Limits

The 74HC4051 supports a wide supply range, but the presence of the optional negative voltage supply \-- V~EE~ \-- has the potential to make things a little complicated. Here are the basic rules that govern the 74HC4051\'s power supplies:

- V~CC~ must be at least 2.0V (above GND).
- V~CC~ must not exceed 10V (above GND).
- V~EE~ must be less than V~CC~ \-- anywhere between 2.0V and 10V below V~CC~.

The operating area graph below \-- figure 7 in the [datasheet](http://www.nxp.com/documents/data_sheet/74HC_HCT4051.pdf) \-- represents those ranges visually:

[![Safe voltage supply operating area](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/operating-area.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/operating-area.png)

For example, the 74HC4051 supports standard 3.3V, 5V, and 9V supplies, as well as bipolar supplies, like ±5V (but not ±9V).

### JP1 \-- Connecting V~EE~ to GND

We expect that the majority of multiplexer-equipped projects may not need the 74HC4051\'s bipolar supply support. So, to make the board easier to get quickly up-and-running, we\'ve added a jumper to the top side, which **shorts V~EE~ to GND**.

[![JP1 highlighted on top side of board](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/jp1-highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/jp1-highlighted.jpg)

By connecting V~EE~ to GND, you can satisfy both V~CC~-GND and V~CC~-V~EE~ limits by keeping V~CC~ between 2.0 and 10.0V. **Unless you need a bipolar supply, you can leave this jumper closed and ignore V~EE~ entirely.**

#### Using a Bipolar Power Supply

The 74HC4051 supports bi-polar power supplies, with a positive supply on V~CC~ and a negative supply on V~EE~. The difference between V~CC~ and V~EE~ can be as much as 10V (e.g. ±5V), but V~CC~ must be somewhere between 2V and 10V.

To use a bipolar supply, you must first **open JP1**, disconnecting V~EE~ from GND.

[![JP1 jumper open](https://cdn.sparkfun.com/r/500-500/assets/learn_tutorials/5/5/3/overview-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/overview-jumper.jpg)

*A quick hit of a soldering iron on some [solder wick](https://www.sparkfun.com/products/8775) should lift that solder right up.*

Once the jumper is open, your supplies can be connected. The logic levels of the select and enable pins will still be limited by V~CC~, but your common pin and eight I/O pins will be able to range between V~EE~ and V~CC~.

## Board Assembly

There is no one correct way to assemble the breakout, but you do need to solder *something* to the supply, select, common, and I/O pins. We recommend either [male](https://www.sparkfun.com/products/116) or [female headers](https://www.sparkfun.com/products/115), but [wire](https://www.sparkfun.com/products/11375) may be better suited to some projects.

[![Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/0/8/11367-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html)

### [Hook-Up Wire - Assortment (Solid Core, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-solid-core-22-awg.html) 

[ PRT-11367 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of solid core wire in a cardboard dispe...

[ [\$22.95] ]

[![Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/1/2/0/11375-Hook-Up_Wire_-_Assortment__Solid_Core__22_AWG_-01.jpg)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html)

### [Hook-Up Wire - Assortment (Stranded, 22 AWG)](https://www.sparkfun.com/hook-up-wire-assortment-stranded-22-awg.html) 

[ PRT-11375 ]

An assortment of colored wires: you know it\'s a beautiful thing. Six different colors of stranded wire in a cardboard dispens...

[ [\$23.95] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

If you\'ve never soldered before, this is a great place to start! Check out our [How to Solder - Through-hole Soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) tutorial for help guiding that soldering iron!

The Multiplexer Breakout is breadboard-compatible, as the two header rows can span a breadboard\'s inner trough. If you throw male headers onto the board\...

[![Male headers soldered to both headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/3/assembly-headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/assembly-headers.jpg)

\...you can plug it in, and use [jumper wires](https://www.sparkfun.com/products/9194) to connect the mux to an Arduino.

[![Example breadboard/Arduino circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/3/assembly-circuit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/assembly-circuit.jpg)

## Arduino Example: Output

Now that you\'ve got a handle on how to use the Multiplexer works and have the board assembled, here are a few quick example Arduino sketches to help demonstrate both output and input capabilities of the chip.

### The Circuit

To get the most out of this example, you\'ll need to connect some sort of output device to each of the independent I/O pins (Y0-Y7). For example, grab a [pack of LEDs](https://www.sparkfun.com/products/12062) and some [330Ω resistors](https://www.sparkfun.com/products/11507) for a quick hardware-verifying circuit.

[![Digital output circuit example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/3/digital-output-example-circuit_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/digital-output-example-circuit_bb.png)

In this example, S0, S1, and S2 are connected to Arduino pins 2, 3 and 4 respectively. \"Z\" is connected to pin 5, which the example uses to produce PWM \"analog output\" signals.

VCC is connected to the Arduino 5V pin, and GND goes to GND. The breakout board\'s JP1 is left intact, shorting V~EE~ to GND.

Finally, the Y0-Y7 pins are all connected to LED/resistor pairs, with the positive anode end of the LED connected to the Y-pin and the resistor connecting the LED\'s cathode to ground. This way, when the output is selected and \"Z\" goes high, the LED on that output will turn on.

### The Sketch

Here\'s the code for the above circuit. Upload it, and enjoy the cycling, breathing LEDs!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    Mux_Analog_Output
    SparkFun Multiplexer Output Example
    Jim Lindblom @ SparkFun Electronics
    August 15, 2016
    https://github.com/sparkfun/74HC4051_8-Channel_Mux_Breakout

    This sketch demonstrates how to use the SparkFun Multiplexer
    Breakout - 8 Channel (74HC4051) to drive eight outputs using
    four digital pins.

    Hardware Hookup:
    Mux Breakout ----------- Arduino
         S0 ------------------- 2
         S1 ------------------- 3
         S2 ------------------- 4
         Z -------------------- 5
        VCC ------------------- 5V
        GND ------------------- GND
        (VEE should be connected to GND)

    Development environment specifics:
    Arduino 1.6.9
    SparkFun Multiplexer Breakout - 8-Channel(74HC4051) v10
    (https://www.sparkfun.com/products/13906)
    ******************************************************************************/
    /////////////////////
    // Pin Definitions //
    /////////////////////
    const int selectPins[3] = ; // S0~2, S1~3, S2~4
    const int zOutput = 5; // Connect common (Z) to 5 (PWM-capable)

    const int LED_ON_TIME = 500; // Each LED is on 0.5s
    const int DELAY_TIME = ((float)LED_ON_TIME/512.0)*1000;
    void setup() 
    
      pinMode(zOutput, OUTPUT); // Set up Z as an output
    }

    void loop() 
    
        // Then bring the analog output value down:
        for (int intensity=255; intensity>=0; intensity--)
        
      }
      // Now cycle from pins Y6 to Y1
      for (int pin=6; pin>=1; pin--)
      
        // Then ramp the output down:
        for (int intensity=255; intensity>=0; intensity--)
        
      }
    }

    // The selectMuxPin function sets the S0, S1, and S2 pins
    // accordingly, given a pin from 0-7.
    void selectMuxPin(byte pin)
    
    }

The magic part of this code is the `selectMuxPin(byte pin)` function at the bottom.

    language:c
    const int selectPins[3] = ; // S-pins to Arduino pins: S0~2, S1~3, S2~4
    ...
    // The selectMuxPin function sets the S0, S1, and S2 pins to select the give pin
    void selectMuxPin(byte pin)
    
    }

Given a pin number between 0 and 7, `selectMuxPin` configures the S0-S2 pins to connect that Y-pin to Z. If you take nothing else from this example, that function may prove the most handy in your future multiplexing endeavors.

## Arduino Example: Input

In this example, we\'ll switch gears and test out the 74HC4051\'s analog signal support. By connecting \"Z\" to an analog input on the Arduino, we can turn one ADC pin into eight!

### The Circuit

You can leave the select pins (S0-S2) tied to Arduino pins 2, 3, and 4, but re-route the Z jumper wire to **A0**. As for the Y-pins, you can connect [potentiometers](https://www.sparkfun.com/products/9806), [photocells](https://www.sparkfun.com/products/9088), or create [voltage dividers](https://learn.sparkfun.com/tutorials/voltage-dividers) on all eight inputs.

[![Example analog input circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/3/analog-input-example-circuit_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/analog-input-example-circuit_bb.png)

*Connect the Multiplexer Breakout up to eight photocells to create a single-octave, touchless keyboard!*

In lieu of a collection of eight analog input devices, you can just use jumper wires to short the input pins to either VCC or GND. That way you can at least prove to yourself that it works.

### The Sketch

Here\'s the sketch for the above circuit:

    language:c
    /******************************************************************************
    Mux_Analog_Input
    SparkFun Multiplexer Analog Input Example
    Jim Lindblom @ SparkFun Electronics
    August 15, 2016
    https://github.com/sparkfun/74HC4051_8-Channel_Mux_Breakout

    This sketch demonstrates how to use the SparkFun Multiplexer
    Breakout - 8 Channel (74HC4051) to read eight, separate
    analog inputs, using just a single ADC channel.

    Hardware Hookup:
    Mux Breakout ----------- Arduino
         S0 ------------------- 2
         S1 ------------------- 3
         S2 ------------------- 4
         Z -------------------- A0
        VCC ------------------- 5V
        GND ------------------- GND
        (VEE should be connected to GND)

    The multiplexers independent I/O (Y0-Y7) can each be wired
    up to a potentiometer or any other analog signal-producing
    component.

    Development environment specifics:
    Arduino 1.6.9
    SparkFun Multiplexer Breakout - 8-Channel(74HC4051) v10
    (https://www.sparkfun.com/products/13906)
    ******************************************************************************/
    /////////////////////
    // Pin Definitions //
    /////////////////////
    const int selectPins[3] = ; // S0~2, S1~3, S2~4
    const int zOutput = 5; 
    const int zInput = A0; // Connect common (Z) to A0 (analog input)

    void setup() 
    
      pinMode(zInput, INPUT); // Set up Z as an input

      // Print the header:
      Serial.println("Y0\tY1\tY2\tY3\tY4\tY5\tY6\tY7");
      Serial.println("---\t---\t---\t---\t---\t---\t---\t---");
    }

    void loop() 
    
      Serial.println();
      delay(1000);
    }

    // The selectMuxPin function sets the S0, S1, and S2 pins
    // accordingly, given a pin from 0-7.
    void selectMuxPin(byte pin)
    
    }

After uploading the sketch, open your **serial monitor** and set the baud rate to 9600. Here you\'ll see the analog values from all eight independent I/O (Y0-Y7) read and printed out once a second.

[![Example serial monitor output](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/example-2-serial.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/3/example-2-serial.png)

Toggle your inputs, or switch out some jumper wires to see the values change.

This example uses that same `selectMuxPin` function to set the S0, S1, and S2 pins. But instead of writing out to the Z pin, we read from it.