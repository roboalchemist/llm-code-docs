# Source: https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide

## Introduction

Is your Arduino running low on GPIO? Looking to control the brightness of 16 LEDs individually? Maybe blink or breathe a few autonomously? Want to delegate scanning an 8x8 matrix of 64 buttons to another controller? These are all tasks the for which the [SX1509 16-IO Expander](https://www.sparkfun.com/products/13601) was made!

[![SparkFun 16 Output I/O Expander Breakout - SX1509](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/9/5/6/13601-01.jpg)](https://www.sparkfun.com/sparkfun-16-output-i-o-expander-breakout-sx1509.html)

### [SparkFun 16 Output I/O Expander Breakout - SX1509](https://www.sparkfun.com/sparkfun-16-output-i-o-expander-breakout-sx1509.html) 

[ BOB-13601 ]

Are you low on I/O? No problem! The SX1509 Breakout is a 16-channel GPIO expander with an I2C interface -- that means with j...

[ [\$7.50] ]

The SX1509 is a **16-channel** GPIO expander with an **I^2^C interface** \-- that means with just two wires, your microcontroller can interface with 16 fully configurable digital input/output pins.

But, the SX1509 can do so much more than just simple digital pin control. It can produce **PWM** signals, so you can dim LEDs. It can be set to **blink** or even **breathe** pins at varying rates. And, with a built-in keypad engine, it can interface with up to 64 buttons set up in an 8x8 matrix.

[![SX1509 Demo circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/example-circuit-demo.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/example-circuit-demo.jpg)

*An SX1509 controlling three LEDs, monitoring three buttons and a 12-button keypad, and producing SPI signals to drive a Serial 7-Segment Display.*

It\'s a really cool chip and a great tool for expanding the capability of your Arduino or any other I^2^C-capable microcontroller.

### Covered In this Tutorial

This tutorial will serve to familiarize you with all things SX1509 and the SparkFun Breakout. Then we\'ll demonstrate how take advantage of all of the I/O expander\'s features using an Arduino-compatible microcontroller and our [SX1509 Arduino Library](https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library).

The tutorial is split into the following sections:

- [SX1509 Breakout Board Overview](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#sx1509-breakout-board-overview) \-- An overview of the features of the SX1509 and the SparkFun breakout.
- [Hardware Assembly](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#hardware-assembly) \-- Tips and tricks for soldering headers or wires to the SX1509 Breakout.
- [Installing the SparkFun SX1509 Arduino Library](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#installing-the-sparkfun-sx1509-arduino-library) \-- We\'ve written an Arduino library to abstract all of the ugly register bit-operations.
  - [Example: Digital In/Out and PWM](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#-example-digital-inout-and-pwm) \-- An example circuit and Arduino sketch demonstrating some of the simpler I/O expander features.
  - [Example: LED Driving](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#example-led-driving) \-- Examples demonstrating how to autonomously blink and breathe LEDs.
  - [Example: Button Matrices](https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide#example-button-matrices) \-- How to use the SX1509\'s keypad engine to monitor a [12-button keypad](https://www.sparkfun.com/products/8653).

### Suggested Reading

Before delving into this tutorial, there are a few concepts you should already be somewhat familiar with. Check out these related tutorials:

- [I^2^C Communication](https://learn.sparkfun.com/tutorials/i2c) \-- The SX1509 is controlled over an I^2^C interface. Learn all about this powerful 2-wire interface.
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels) \-- While most Arduino\'s operate at 5V, the SX1509 works at 3.3V. The GPIO are, at least, 5V tolerant!
- [Pulse-Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) \-- All of the SX1509\'s output pins are capable of producing a PWM signal. That means you can control the brightness of [LEDs](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)!

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## SX1509 Breakout Board Overview

There\'s a lot going on on the SX1509 Breakout. GPIO and power buses are broken out in every-which direction, and configurable jumpers cover most of the rest of the board.

[![Top side of the SX1509 Breaokut](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/hardware-top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/hardware-top.jpg)

This section will cover all things SX1509 Breakout, so you can get the most out of the board\'s features.

### I^2^C and Power Input Headers

These two headers at the top and bottom of the breakout board are the **input and control** headers to the board. This is where you can supply power to the SX1509, and where your I^2^C signals \-- SDA and SCL \-- will terminate.

[![Input headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/hardware-input-headers-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/hardware-input-headers-2.jpg)

These headers break out the following pins:

  Pin Label                                 Type           Description
  ----------------------------------------- -------------- -----------------------------------------------------------
  [INT]   Output         Active low programmable interrupt
  [RST]   Input          Active low reset (pulled high on-board)
  GND                                       Power          Ground (0V)
  3V3                                       Power          Main supply voltage (1.425-3.6V)
  SDA                                       I^2^C          I^2^C serial data line
  SCL                                       I^2^C          I^2^C serial clock line
  OSC                                       Clock In/Out   Optional clock input, or programmable clock signal output

The SDA and SCL pins each have 10kΩ resistors pulling them up to 3.3V. These resistors can be disconnected by cutting the SJ1 jumpers.

[RST] \-- the SX1509\'s **active-low reset input** \-- works just like an Arduino reset pin. If the pin is pulled LOW, the SX1509 will power down. When [RST] rises, the SX1509 will turn back on, but all of its settings will be cleared out. The breakout board includes a 10kΩ resistor pulling [RST] HIGH, so you ignore this pin if you don\'t need the reset functionality.

[INT] is a very handy **interrupt output**, especially if you\'re using any SX1509 pins as inputs. It can be configured to go LOW whenever a pin state changes. The breakout board includes a 10kΩ resistor pulling [INT] HIGH.

Finally, OSC breaks out the SX1509\'s **OSCIO** pin \-- the **oscillator input/output**. This highly-configurable pin can be used as either the clock input for the SX1509 (if you don\'t want to use its internal 2MHz clock), a clock output (producing an up to 2MHz square wave signal), or a simple digital I/O.

**Required and optional pins:** The pairs of power and I^2^C pins are the only ones *required* for interfacing with the SX1509. [RST], [INT], and OSC are all **optional**, they can be left disconnected if you don\'t need the feature they provide.

### I/O and GND/VCC Breakouts

The real meat of the breakout board are the pairs of rows breaking out all sixteen I/O pins plus the power rails.

[![GPIO Breakouts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/hardware-gpio-headers-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/hardware-gpio-headers-3.jpg)

The SX1509 breaks its 16 I/O into two **banks** \-- bank A and bank B. Each bank can operate on a separate power supply, but by default they\'re both set to 3.3V. Bank A is powered by VCC1, and bank B is supplied by VCC2. VCC1 and VCC2 can range between 1.2V and 3.6V, if you want to supply them externally. Check out the \"Jumpers\" section for more information on that.

Every I/O pin is **capable of PWM and blink** outputs, but only half of them can be set to \"breathe\" (blink with smooth transitions from on to off). Also, if you plan on using the SX1509 keypad driver, each I/O is relegated to either a row or column interface.

+-----+------------------------+--------------+
|     | LED Driver             | Keypad       |
+=====+======+=======+=========+=====+========+
| I/O | PWM  | Blink | Breathe | Row | Column |
+-----+------+-------+---------+-----+--------+
| 0   | ✓    | ✓     |         | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 1   | ✓    | ✓     |         | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 2   | ✓    | ✓     |         | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 3   | ✓    | ✓     |         | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 4   | ✓    | ✓     | ✓       | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 5   | ✓    | ✓     | ✓       | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 6   | ✓    | ✓     | ✓       | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 7   | ✓    | ✓     | ✓       | ✓   |        |
+-----+------+-------+---------+-----+--------+
| 8   | ✓    | ✓     |         |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 9   | ✓    | ✓     |         |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 10  | ✓    | ✓     |         |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 11  | ✓    | ✓     |         |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 12  | ✓    | ✓     | ✓       |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 13  | ✓    | ✓     | ✓       |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 14  | ✓    | ✓     | ✓       |     | ✓      |
+-----+------+-------+---------+-----+--------+
| 15  | ✓    | ✓     | ✓       |     | ✓      |
+-----+------+-------+---------+-----+--------+

### Ground (or Power) Rails

Running alongside the I/O breakouts are a pair of power rails. These rails can be distinguished by the **bars of white silkscreen** running between each pad.

[![GND or VCC rails](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/hardware-gnd-vcc-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/hardware-gnd-vcc-jumper.jpg)

By default, these rails are both set to **ground** \-- handy if you want to fan out some active-low buttons, or current-sourced LEDs. Jumpers on the back side allow you to switch the rails from GND to either VCC1 or VCC2. You\'ll need to cut the jumper between GND and the rail, then blob solder between the rail and VCC.

This bus is completely optional. Just don\'t solder male pins into both rows of headers if you plan on using the breakout in a breadboard!

### Address-Select Jumpers

Up to four SX1509\'s can be connected to a single I^2^C bus, by configuring them to different addresses. The SX1509 has two pins devoted to I^2^C address selection: ADD0 and ADD1. Each of those pins are broken out to a jumper on the bottom of the board.

[![Address select jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/hardware-addr-jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/hardware-addr-jumper.jpg)

The board defaults each of those pins to GND, which sets the I^2^C address to **0x3E**. To set either jumper to \"1\" (HIGH), grab a [hobby knife](https://www.sparkfun.com/products/9200), cut the trace connecting to \"0\", and blob some solder between the center pad and \"1\".

The four configurable addresses are listed on the back of the board, but for quick reference, they are:

  ADD1   ADD0   I^2^C address
  ------ ------ ---------------
  0      0      0x3E
  0      1      0x3F
  1      0      0x70
  1      1      0x71

### VCC1 and VCC2 Jumpers

SJ2 and SJ3 on the back-side of the board connect VCC2 and VCC1, respectively, to the 3V3 voltage supply input. So, if you\'re delivering 3.3V to the board, each of the I/O banks will operate at 3.3V.

If you want to take advantage of the SX1509\'s **level-shifting** capabilities by powering these banks at something other than VCC, cut the jumpers and plug any voltage between 1.2V and 3.6V into the VCC1 and/or VCC2 pins.

These supply buses are completely independent \-- so they *can* operate at different voltages.

## Hardware Assembly

You\'ll need to solder *something* into the SX1509 Breakout to use it, whether that something is [male](https://www.sparkfun.com/products/116) or [female](https://www.sparkfun.com/products/115) headers or [wire](https://www.sparkfun.com/products/11367) is completely up to you and your intended application. If you\'ve never soldered before, check out our [PTH soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering).

One option we like, which keeps the board as breadboard-compatible as can be, is soldering male headers on the I/O banks, and female headers on either (or both) of the power/I^2^C headers.

[![Headers soldered into the SX1509](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/headers-soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/headers-soldered.jpg)

Then you can use [male-to-male jumper wires](https://www.sparkfun.com/products/12795) to connect between your microcontroller and the breakout, and breadboard the rest of the I/O.

## Installing the SparkFun SX1509 Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Now that you\'ve got the hardware all mostly figured out, it\'s time to start programming! To help make using the SX1509 as painless as possible, we\'ve written an Arduino library to help interface with it. Open the Arduino Library Manager and search for **SparkFun SX1509**. You can also manually install the [SparkFun SX1509 Arduino Library](https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library) from the GitHub repository by clicking on the button below to download the latest version of the library.

[Download the SparkFun SX1509 Arduino Library!](https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library/archive/master.zip)

For help installing the library, check out our [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial. If you downloaded the library as a ZIP, you can use Arduino\'s **Sketch** \> **Include Library** \> **Add .ZIP Library** tool to automatically add it to your Arduino sketchbook.

The SparkFun SX1509 Arduino library includes all sorts of examples, which demonstrate specific features of the I/O expander. Navigate to **File** \> **Examples** \> **SparkFun SX1509 IO Expander** to check them out.

[![SX1509 Library examples](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/library-examples.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/library-examples.png)

Quickly, we\'ll walk you through a few quick examples that show off the I/O expander\'s range of features.

## Example: Digital In/Out and PWM 

As with almost any I/O expander, each of the SX1509\'s GPIO can be configured as simple digital inputs or outputs. So you can toggle LEDs on or off, monitor for button presses, or even bit-bang more advanced digital interfaces like SPI (probably nothing that\'s timing-dependent though).

Here\'s a quick example that shows how you can `digitalWrite` or `digitalRead` using the SX1509. If you want to follow along, hook up a circuit like below:

[![Fritzing circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/fritzing-example-1_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/fritzing-example-1_bb.png)

Match up 3.3V, GND, SDA, and SCL between your Arduino and the SX1509 Breakout. Then connect an LED to I/O 15 \-- you can either configure it to source or sink current. And connect an active-low button to I/O 0.

Then throw this code onto your Arduino:

    language:c
    /*************************************************************
      digitalReadWrite_Combined.ino
      SparkFun SX1509 I/O Expander Example: digital I/O (digitalRead/digitalWrite)
      Jim Lindblom @ SparkFun Electronics
      Original Creation Date: September 21, 2015
      https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library

      This example demonstrates the SX1509's digitalRead and digitalWrite
      functionality. We'll attach an active-low button to an
      INPUT_PULLUP input and attach an LED to a pin set as an OUTPUT.
      Then whenever the button read's LOW, we'll toggle the LED.
      Note that the code will wait until the button is released
      before reading the SX1509 pins again.

      After uploading the sketch, open your serial monitor and set
      it to 115200 baud.

      Hardware Hookup:
      SX1509 Breakout ------ Arduino -------- Breadboard
            GND -------------- GND
            3V3 -------------- 3.3V
            SDA ------------ SDA (A4)
            SCL ------------ SCL (A5)
            0 ---------------------------------]BTN[----GND
            15 -------------------------------- LED+
                                           LED- -/\/\/\- GND
                                                   330
      Development environment specifics:
      IDE: Arduino 1.6.5
      Hardware Platform: Arduino Uno
      SX1509 Breakout Version: v2.0

      This code is beerware; if you see me (or any other SparkFun
      employee) at the local, and you've found our code helpful,
      please buy us a round!

      Distributed as-is; no warranty is given.
    *************************************************************/

    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

    // SX1509 pin definitions:
    // Note: these aren't Arduino pins. They're the SX1509 I/O:
    const byte SX1509_LED_PIN = 15; // LED connected to 15 (source ing current)
    const byte SX1509_BUTTON_PIN = 0; // Button connected to 0 (Active-low button)

    bool ledState = false;

    void setup()
    

      // Call io.pinMode(<pin>, <mode>) to set any SX1509 pin as
      // either an INPUT, OUTPUT, INPUT_PULLUP, or ANALOG_OUTPUT
      // Set output for LED:
      io.pinMode(SX1509_LED_PIN, OUTPUT);
      // Use a pull-up resistor on the button's input pin. When
      // the button is pressed, the pin will be read as LOW:
      io.pinMode(SX1509_BUTTON_PIN, INPUT_PULLUP);

      // Blink the LED a few times before we start:
      for (int i = 0; i < 5; i++)
      
    }

    void loop()
    
    }

When you press the button down, the LED state should toggle. Opening the [Arduino Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **115200** will also give you the serial output. Check through the code to see how easy it is! Not all that different from Arduino code you may already be familiar with.

[![Arduino Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/SX1509_Example_Digital_IO_Blink_Button_Arduino_Serial_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/SX1509_Example_Digital_IO_Blink_Button_Arduino_Serial_Output.jpg)

#### Getting Started with the SX1509 Library

To begin, include the \"SparkFunSX1509.h\" library (and the \"Wire.h\" library as well), and create an `SX1509` object in the global area:

    language:c
    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

You\'ll use that `io` object from here on out. In the `setup()`, make sure to join the I^2^C bus using `Wire.begin()`. To initialize the I/O expander \-- and to make sure it\'s communicating correctly \-- you will then need to call `io.begin(<address>)`, where `<address>` is the I^2^C address of the expander (0x3E by default). In this case, we defined SX1509_ADDRESS earlier in the code. Check the return value of `begin()` to make sure everything is hunky-dory.

    language:c
      Wire.begin(); //Initialize I2C bus

      pinMode(13, OUTPUT); // Use pin 13 LED as debug output
      digitalWrite(13, LOW); // Start it as low

      // Call io.begin(<address>) to initialize the SX1509. If it
      // successfully communicates, it'll return 1.
      if (io.begin(SX1509_ADDRESS) == false)
      

**Note:** Please be aware that v3 of the library breaks previous version compatiblity on a few things:\
\

- `Wire.begin()` must be called explicitly within the Arduino sketch before `io.begin()` is called. This may break code that does not have `Wire.begin()`.
- `io.begin()` has been expanded to include `io.begin(deviceAddress, wirePort, resetPin)`. This may break code where `resetPin` was the 2nd argument.

Then you can use functions you should already be mostly familiar with to control the I/O. Just tag the `io` object onto the beginning of `pinMode`, `digitalWrite` and `digitalRead`, and go about your Arduino-business as normal!

### Analog Output (PWM)

You can also use any I/O as an \"analog\" (PWM) output by using the `analogWrite(<pin>, <0-255>)` function \-- just like Arduino analog output! There are just a couple differences to be aware of:

- **ANALOG_OUTPUT**: If you want a pin to produce PWM signals, call `pinMode(<pin>, ANALOG_OUTPUT)` in your setup. That will tell the SX1509 to initialize the pin as an \"LED driver\".
- **Sinking Current**: `analogWrite(<pin>, <0-255>)` assumes that the LED is hooked up in a current-sinking fashion \-- meaning the LED\'s cathode (negative pin) is terminated into the SX1509. Thus, `analogWrite`ing to 255 will actually pull the pin LOW, and 0 will set it HIGH.

Here\'s some example code:

    language:c
    /*************************************************************
      analogWrite.ino
      SparkFun SX1509 I/O Expander Example: pwm output (analogWrite)
      Jim Lindblom @ SparkFun Electronics
      Original Creation Date: September 21, 2015
      https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library

      This example demonstrates the SX1509's analogWrite function.
      Connect an LED to the SX1509's pin 15 (or any other pin, they
      can all PWM!). The SX1509 can either sink or source current,
      just don't forget your limiting resistor!

      Hardware Hookup:
      SX1509 Breakout ------ Arduino -------- Breadboard
            GND -------------- GND
            3V3 -------------- 3.3V
          SDA ------------ SDA (A4)
          SCL ------------ SCL (A5)
          15 -------------------------------- LED+
                                         LED- -/\/\/\- GND
                                                    330

      Development environment specifics:
      IDE: Arduino 1.6.5
      Hardware Platform: Arduino Uno
      SX1509 Breakout Version: v2.0

      This code is beerware; if you see me (or any other SparkFun
      employee) at the local, and you've found our code helpful,
      please buy us a round!

      Distributed as-is; no warranty is given.
    *************************************************************/

    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

    // SX1509 Pin definition:
    const byte SX1509_LED_PIN = 15; // LED to SX1509's pin 15

    void setup()
    

      // Use the pinMode(<pin>, <mode>) function to set our led
      // pin as an ANALOG_OUTPUT, which is required for PWM output
      io.pinMode(SX1509_LED_PIN, ANALOG_OUTPUT);
    }

    void loop()
    
      delay(500); // Delay half-a-second

      // Ramp brightness down, from 255-0, delay 2ms in between
      // analogWrite's
      for (int brightness = 255; brightness >= 0; brightness--)
      
      delay(500); // Delay half-a-second
    }

That\'s a real fine breathing LED! But the SX1509 is so much more than a simple digital I/O expander. Its LED-driving capabilities mean you can offload all of that breathing to the SX1509, leaving your `loop()` for more important tasks!

## Example: LED Driving

One of the SX1509\'s coolest features is its built-in LED-driving support. Beyond digital or even PWM output, the SX1509 can also autonomously blink or breathe LEDs! Just tell it how long to blink, or how fast to rise/fall, and it\'ll do the rest for you.

[![Driving an LEDs with the SX1509](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/example-circuit-led.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/example-circuit-led.jpg)

For this example, grab four LEDs and wire them up to pins 8, 13, 14, and 15.

**Source vs. Sink:** The SX1509 can either source or sink current, but it has a much higher capacity for *sinking* current. It can source up to 8mA per I/O, or sink up to 15mA. If you\'re driving LEDs, we recommend hooking them up to sink current.

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/source-vs-sink.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/source-vs-sink.png)

Here\'s an example that sets an LED tied to pin 15 to blink:

    language:c
    /*************************************************************
    blink.ino
    SparkFun SX1509 I/O Expander Example: blink output
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: September 21, 2015
    https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library

    This example demonstrates the SX1509's set-it-and-forget-it
    blink function. We'll set the pin up as an OUTPUT, and call
    io.blink() all in setup(), then watch the LED blink by itself
    in loop().

    Hardware Hookup:
        SX1509 Breakout ------ Arduino -------- Breadboard
              GND -------------- GND
              3V3 -------------- 3.3V
              SDA ------------ SDA (A4)
              SCL ------------ SCL (A5)
              15 -------------------------------- LED+
                                             LED- -/\/\/\- GND
                                                    330

    Development environment specifics:
        IDE: Arduino 1.6.5
        Hardware Platform: Arduino Uno
        SX1509 Breakout Version: v2.0

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, 
    please buy us a round!

    Distributed as-is; no warranty is given.
    *************************************************************/

    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

    // SX1509 Pin definition:
    const byte SX1509_LED_PIN = 15; // LED to SX1509's pin 15

    void setup()
    

      // Set up the SX1509's clock to use the internal 2MHz
      // oscillator. The second parameter divides the oscillator
      // clock to generate a slower LED clock. 4 divides the 2MHz
      // clock by 2 ^ (4-1) (8, ie. 250kHz). The divider parameter
      // can be anywhere between 1-7.
      io.clock(INTERNAL_CLOCK_2MHZ, 4);

      io.pinMode(SX1509_LED_PIN, OUTPUT); // Set LED pin to OUTPUT

      // Blink the LED pin -- ~1000 ms LOW, ~500 ms HIGH:
      io.blink(SX1509_LED_PIN, 1000, 500);
      // The timing parameters are in milliseconds, but they
      // aren't 100% exact. The library will estimate to try to
      // get them as close as possible. Play with the clock
      // divider to maybe get more accurate timing.
    }

    void loop()
    

The `io.blink(<pin>, <low_ms>, <high_ms>)` function works most of the magic in this example \-- setting the LED pin to blink LOW for 1000ms and HIGH for 500ms. Those timing values will not end up being exact. The SX1509\'s timing mechanism is dependent on dividing the clock (we\'re using the internal 2MHz oscillator), and doesn\'t always divide down perfectly.

Before configuring the pin to blink, we call `io.clock(<source>, <divider>)` to set the clock that drives our LEDs. In this example we use the SX1509\'s internal 2MHz clock as the source, and divide that down to 250kHz for the LED clock. Play with that second parameter to see just how much the blink timing depends on it.

Try using the `blink` function to blink the other LEDs!

### LED Breathing

Half of the SX1509\'s I/O pins are capable of producing \"breathing\" outputs \-- where a pin fades in and out at a set rate. Pins 4-7 and 12-15 have this capability.

Using the same circuit as before, here\'s a quick example showing off the SX1509\'s breathe feature:

    language:c
    /*************************************************************
    breathe.ino
    SparkFun SX1509 I/O Expander Example: breathe output
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: September 21, 2015
    https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library

    This example demonstrates the SX1509's set-it-and-forget-it
    breathe function. The SX1509 will pulse an LED, smoothly
    ramping its brightness up-then-down. We'll set the pin up as
    an ANALOG_OUTPUT, and call io.breathe() all in setup(), then
    watch the LED pulse by itself in loop().

    Hardware Hookup:
        SX1509 Breakout ------ Arduino -------- Breadboard
              GND -------------- GND
              3V3 -------------- 3.3V
              SDA ------------ SDA (A4)
              SCL ------------ SCL (A5)
              15 --------------------------------- LED+
                                             LED- -/\/\/\- GND
                                                    330

    Development environment specifics:
        IDE: Arduino 1.6.5
        Hardware Platform: Arduino Uno
        SX1509 Breakout Version: v2.0

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, 
    please buy us a round!

    Distributed as-is; no warranty is given.
    *************************************************************/

    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

    // SX1509 Pin definition:
    const byte SX1509_LED_PIN = 15; // LED to SX1509's pin 15

    void setup()
    

      // Use the internal 2MHz oscillator.
      // Set LED clock to 500kHz (2MHz / (2^(3-1)):
      io.clock(INTERNAL_CLOCK_2MHZ, 3);

      // To breathe an LED, make sure you set it as an
      // ANALOG_OUTPUT, so we can PWM the pin:
      io.pinMode(SX1509_LED_PIN, ANALOG_OUTPUT);

      // Breathe an LED: 1000ms LOW, 500ms HIGH,
      // 500ms to rise from low to high
      // 250ms to fall from high to low
      io.breathe(SX1509_LED_PIN, 1000, 500, 500, 250);
      // The timing parameters are in milliseconds, but they
      // aren't 100% exact. The library will estimate to try to
      // get them as close as possible. Play with the clock
      // divider to maybe get more accurate timing.
    }

    void loop()
    

Make sure you set the pin as an `ANALOG_OUTPUT` using the `pinMode()` function. Then call `io.breathe(<pin>, <low_ms>, <high_ms>, <rise_ms>, <fall_ms)` to set the LOW and HIGH time as well as the number of milliseconds it takes to rise from LOW to HIGH and fall from HIGH to LOW.

Easy-peasy! And now you have the `loop()` left free for more important tasks. (As if! Nothing\'s more important than blinking LEDs.)

## Example: Button Matrices

Blinking and breathing LEDs can be fun, but the SX1509\'s real power lies in its keypad engine. By wiring up buttons in a row/column matrix, you can connect up to 64 buttons to the SX1509.

Keypad matrices are very common \-- they allow you to save immensely on GPIO. You could monitor a [16-button, 4x4 keypad pad](https://www.sparkfun.com/products/7835) with 8 I/O, or four of those keypads (a 64-button/8x8 matrix) with just 16 I/O.

In this example, we\'ll use **seven SX1509 I/O** to monitor a [12-button Keypad](https://www.sparkfun.com/products/8653) \-- which is a matrix of four rows and three columns. We\'ll also use the SX1509\'s **interrupt** output, so we don\'t constantly have to poll the I/O expander. Here\'s the circuit:

[![Keypad fritzing example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/fritzing-example-3_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/fritzing-example-3_bb.png)

There isn\'t a lot of flexibility in the SX1509\'s keypad engine. The rows of you matrix have to be connected, sequentially, to pins 0-7, and the columns wire up to pins 8-15. Our four row buses must route to pins 0-3, and the three columns are connected to 8-10. That still leaves plenty of pins for LED driving!

Here\'s the example code:

    language:c
    /*************************************************************
    keypadInterrupt.ino
    SparkFun SX1509 I/O Expander Example: keypad matrix with int
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: September 21, 2015
    https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library

    This example demonstrates how to use the SX1509's keypad
    engine to monitor a matrix of button inputs. The SX1509's
    interrupt output is monitored to check for button presses.

    For this example, we use the 12-button keypad
      (https://www.sparkfun.com/products/8653).

    After uploading the sketch, open your serial monitor and 
    set it to 115200 baud.

    Hardware Hookup:
        SX1509 Breakout ------ Arduino -------- Keypad Pin
              INT --------------- D2
              GND -------------- GND
              3V3 -------------- 3.3V
              SDA ------------ SDA (A4)
              SCL ------------ SCL (A5)
              0 ---------------------------------- 2 (row 1)
              1 ---------------------------------- 7 (row 2)
              2 ---------------------------------- 6 (row 3)
              3 ---------------------------------- 4 (row 4)
              8 ---------------------------------- 3 (col 1)
              9 ---------------------------------- 1 (col 2)
              10 --------------------------------- 5 (col 3)

    Development environment specifics:
        IDE: Arduino 1.6.5
        Hardware Platform: Arduino Uno
        SX1509 Breakout Version: v2.0

    This code is beerware; if you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, 
    please buy us a round!

    Distributed as-is; no warranty is given.
    *************************************************************/

    #include <Wire.h>           // Include the I2C library (required)
    #include <SparkFunSX1509.h> //Click here for the library: http://librarymanager/All#SparkFun_SX1509

    // SX1509 I2C address (set by ADDR1 and ADDR0 (00 by default):
    const byte SX1509_ADDRESS = 0x3E; // SX1509 I2C address
    SX1509 io;                        // Create an SX1509 object to be used throughout

    #define KEY_ROWS 4 // Number of rows in the keypad matrix
    #define KEY_COLS 3 // Number of columns in the keypad matrix

    // keyMap maps row/column combinations to characters:
    char keyMap[KEY_ROWS][KEY_COLS] = ,
        ,
        ,
        };

    const byte ARDUINO_INTERRUPT_PIN = 2;

    void setup()
    

      // Scan time range: 1-128 ms, powers of 2
      byte scanTime = 8; // Scan time per row, in ms
      // Debounce time range: 0.5 - 64 ms (powers of 2)
      byte debounceTime = 1; // Debounce time
      // Sleep time range: 128 ms - 8192 ms (powers of 2) 0=OFF
      byte sleepTime = 0;
      // Scan time must be greater than debounce time!
      io.keypad(KEY_ROWS, KEY_COLS,
                sleepTime, scanTime, debounceTime);

      // Set up the Arduino interrupt pin as an input w/
      // internal pull-up. (The SX1509 interrupt is active-low.)
      pinMode(ARDUINO_INTERRUPT_PIN, INPUT_PULLUP);
    }

    // Compared to the keypad in keypad.ino, this keypad example
    // is a bit more advanced. We'll use these varaibles to check
    // if a key is being held down, or has been released. Then we
    // can kind of emulate the operation of a computer keyboard.
    unsigned int previousKeyData = 0;         // Stores last key pressed
    unsigned int holdCount, releaseCount = 0; // Count durations
    const unsigned int holdCountMax = 15;     // Key hold limit
    const unsigned int releaseCountMax = 100; // Release limit

    void loop()
    
        else // If the button's beging held down:
        
        releaseCount = 0;          // Clear the releaseCount variable
        previousKeyData = keyData; // Update previousKeyData
      }

      // If no keys have been pressed we'll continuously increment
      //  releaseCount. Eventually creating a release, once the
      // count hits the max.
      releaseCount++;
      if (releaseCount >= releaseCountMax)
      
      delay(1); // Gives releaseCountMax a more intuitive unit
    }

After uploading the code, open the serial monitor and press some keys!

[![Example serial monitor output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/4/SX1509_Example_Keypad_Button_Arduino_Serial_Output.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/4/SX1509_Example_Keypad_Button_Arduino_Serial_Output.jpg)

Now just hook up a [cellular shield](https://www.sparkfun.com/products/15087) and go make some prank calls!

------------------------------------------------------------------------

Keep in mind any of these SX1509 features can be combined, as long as you don\'t run out of I/O (then just cascade another expander!). Check out the library\'s examples for demonstrations of other features \-- like the clock output, or input debouncing.

[SparkFun SX1509 Arduino Library Examples](https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library/tree/master/examples)