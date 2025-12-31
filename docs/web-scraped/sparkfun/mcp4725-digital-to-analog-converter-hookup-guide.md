# Source: https://learn.sparkfun.com/tutorials/mcp4725-digital-to-analog-converter-hookup-guide

## To DAC, or Not to DAC\... 

When learning about the world of microcontrollers, you will come across analog-to-digital converters quite frequently. These allows us to read in signals from analog sensors and convert them into a digital language our microcontrollers and other computational devices can understand. However, what if you need to do the opposite? What if you need your Arduino to speak the language of analog signals? Enter the [MCP4725 Digital-toAnalog Converter Breakout](https://www.sparkfun.com/products/12918).

[![SparkFun I2C DAC Breakout - MCP4725](https://cdn.sparkfun.com/r/600-600/assets/parts/9/8/3/2/12918-01.jpg)](https://www.sparkfun.com/sparkfun-i2c-dac-breakout-mcp4725.html)

### [SparkFun I2C DAC Breakout - MCP4725](https://www.sparkfun.com/sparkfun-i2c-dac-breakout-mcp4725.html) 

[ BOB-12918 ]

Most microcontrollers (like the standard Arduino Uno) can't output true analog voltages; they only simulate them using Puls...

[ [\$6.95] ]

This tiny IC allows you to do just that. By using the Arduino\'s I^2^C lines, you can create a wide variety of analog waveforms on the other end.

### Covered in This Tutorial

In this tutorial, we will overview the breakout and discuss additional hardware details. Then an assembly section will discuss how to connect this breakout to a microcontroller. Last, the firmware will be broken down to help you understand how the digital to analog conversion happens.

### Suggested Reading

- [Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Pull-up Resistors](https://learn.sparkfun.com/tutorials/pull-up-resistors)
- [Analog to Digital Conversion (ADC)](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)
- [I^2^C](https://learn.sparkfun.com/tutorials/i2c)
- [How to Use an Oscilloscope](https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope)

## Board Overview 

Before we discuss hooking up the breakout, let\'s go over some of the features of this board.

#### Pinout

The first thing to point out is the pinout on this breakout now conforms to the standard I^2^C pinout we\'ve started using on most devices that use the two-wire interface. Thus, it is easy to solder some headers on the breakout and plug it directly into an Arduino with the same pinout for the I^2^C pins. There is also the signal out and a GND pin grouped together to connect to an oscilloscope or whatever other device you\'re hooking up to the breakout.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/front-pinout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/front-pinout.png)

#### Power

The breakout can be powered anywhere between 2.7V to 5.5V, making it great for both 5V and 3.3V microcontrollers.

#### I^2^C Communication

A few features have been added to this breakout to give the user more flexibility with the IC, particularly when it comes to adding multiple DACs to one bus. First, we\'ve broken out the address selection pin (A0) to a jumper pad. By default, this pin is pulled LOW to GND. To change the address of your other device, simply de-solder the jumper and add a blob of solder to the middle pad and the Vcc pad.

[![address selection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/front-highlighted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/front-highlighted.jpg)

If you\'re going to have more than one MCP4725 on a bus, you\'ll also want to disable the pull-up resistors on **all but one** breakout. To make this easier, we\'ve added another jumper on the back of the board. The pull-ups are enabled by default. If you need to disable them, you\'ll need to cut the traces on the jumper pad with an [Xacto knife](https://www.sparkfun.com/products/9200). If you ever need to re-enable the pull-ups, simply solder the three pads back together.

[![pullup enable](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/back-highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/back-highlighted.png)

Last, there are two mounting holes to mount this board inside the enclosure of your choice.

## Hooking it Up 

To use the MCP4725, all you\'ll need is some [male headers](https://www.sparkfun.com/products/553), a [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or other microcontroller, and a means to see your signal. Using an [oscilloscope](https://www.sparkfun.com/search/results?term=oscilloscope) will be the easiest way to get started.

First, [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the headers onto your breakout. We recommend using a 4-pin header facing downward for the power and communication connections and using a 2-pin header facing up for the Out and GND pins. See the below image for an example.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-01fff.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-01fff.jpg)

Most Arduino boards have the I^2^C on the A4 and A5 pins. Then, in the firmware we\'ll uplaod in the next section, we can set pins A2 and A3 as GND and Vcc respectively to power the breakout. If you prefer to wire everything to a breadboard, you can solder a 6-pin header and connect everything with some jumper wires.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-02.jpg)

Last, it\'s time to connect the MCP4725 to whatever device you\'ll be sending analog signals. In this tutorial, we\'ll be visualizing the signal with an oscilloscope. Using the o-scope probes, you could connect to the headers directly, or you could use some jumper wires. Make sure to not mix up the Out and GND pins.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-03.jpg)

## Firmware

With everything hooked up, it\'s time to upload some code to the Arduino that will allow the breakout to send analog signals. In this example, the code will generate a simple sine wave.

Open up the Arduino IDE, and copy in this snippet of code:

    language:c
    /****************************************************************************** 
    MCP4725 Example Waveform Sketch
    Joel Bartlett
    SparkFun Electronics
    Sept. 11, 2014
    https://github.com/sparkfun/MCP4725_Breakout

    This sketch takes data from a lookup table to provide 
    waveforms to be generated by the MCP4725 DAC. 

    Development environment specifics:
    Arduino 1.0+
    Hardware Version V14

    This code is beerware; if you see me (or any other SparkFun employee) at the local, 
    and you've found our code helpful, please buy us a round!

    Distributed as-is; no warranty is given. 

    This code builds off the sketch written by Mark VandeWettering, which can be found here:
    http://brainwagon.org/2011/02/24/arduino-mcp4725-breakout-board/
    */

    #include <Wire.h>//Include the Wire library to talk I2C

    //This is the I2C Address of the MCP4725, by default (A0 pulled to GND).
    //Please note that this breakout is for the MCP4725A0. 
    #define MCP4725_ADDR 0x60   
    //For devices with A0 pulled HIGH, use 0x61

    //Sinewave Tables were generated using this calculator:
    //http://www.daycounter.com/Calculators/Sine-Generator-Calculator.phtml

    int lookup = 0;//varaible for navigating through the tables

    int sintab2[512] = 
    ;

    void setup()
    
    //---------------------------------------------------
    void loop()
    

Once the sketch is uploaded, fire up the o-scope, connect the probe, if you haven\'t yet, and you should be greeted with a nice looking sine wave.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/9/MCP4725_Breakout_Board_Tutorial-04.jpg)