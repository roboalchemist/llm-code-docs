# Source: https://learn.sparkfun.com/tutorials/shift-registers

## Overview

Have you ever found yourself wanting to control lots of LED\'s? Or just needed more I/O in general? Well, this tutorial will cover the basics you need to know about a technology that will let you do just that. It\'s called the shift register. So what exactly is it? Why are they useful? How do I use it? These are all questions we will attempt to answer in this tutorial.

### Suggested Reading

Here is some background material you may consider reading before moving on:

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)

### Series and Parallel Circuits 

An introduction into series and parallel circuits.

## What is a Shift Register?

A shift register is a device that allows additional inputs or outputs to be added to a microcontroller.

[![Shift Register 8-Bit - SN74HC595](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/7/5/13699-01.jpg)](https://www.sparkfun.com/shift-register-8-bit-sn74hc595.html)

### [Shift Register 8-Bit - SN74HC595](https://www.sparkfun.com/shift-register-8-bit-sn74hc595.html) 

[ COM-13699 ]

The SN74HC595N is a simple 8-bit shift register IC.

[ [\$1.05] ]

This is accomplished by converting data between parallel and serial formats. A microprocessor communicates with a shift register using serial information, and the shift register gathers or outputs information in a parallel (multi-pin) format.

[![Tactile button assortment](https://cdn.sparkfun.com/assets/3/c/d/d/1/518c1d71ce395f5162000000.jpg)](https://cdn.sparkfun.com/assets/3/c/d/d/1/518c1d71ce395f5162000000.jpg)

*Got a lot of buttons? Consider using a shift register.*

### SIPO or PISO Shift Registers

Shift registers come in two basic types, either SIPO, Serial-In-Parallel-Out, or PISO, Parallel-In-Serial-Out. SparkFun carries both types. Here is a SIPO, the [74HC595](https://www.sparkfun.com/products/733), and the PISO, the [74HC165](https://www.sparkfun.com/products/9519). The first type, SIPO, is useful for controlling a large number of outputs, including LEDs, while the latter type, PISO, is good for gathering a large number of inputs, like buttons.

SparkFun carries an easy to use breakout versions for both these chips as well. If you need more than 8 additional I/O lines, you can easily chain multiple shift registers together by connecting the output side of the breakout board to the right side of another board.

[![SparkFun Shift Register Breakout - 74HC595](https://cdn.sparkfun.com/r/600-600/assets/parts/5/4/7/7/10680-01.jpg)](https://www.sparkfun.com/sparkfun-shift-register-breakout-74hc595.html)

### [SparkFun Shift Register Breakout - 74HC595](https://www.sparkfun.com/sparkfun-shift-register-breakout-74hc595.html) 

[ BOB-10680 ]

This is a breakout for the SOIC version of the 74HC595 shift register IC. Clock in data and latch it to free up IO pins on yo...

[ [\$4.95] ]

## Why Shift Bits?

Shift registers are often used for the purpose of saving pins on a microcontroller. Every microcontroller has a limited number of pins for general inputs and outputs (GPIO).

If a project needs needs to control 16 LEDs, that would normally require 16 pins of a microcontroller. In the event that you don\'t have 16 available I/O pins, this is where the shift register comes in handy. With two shift registers connected in series, we can accomplish the task of controlling the 16 LED\'s with only using 4 I/O pins. That is quite a difference, and you can save even more pins the more shift registers you have chained together.

[![This uses the same hardware as the original NES, a shift register to gather button states](https://cdn.sparkfun.com/assets/d/3/6/4/e/518c1f67ce395f4962000003.jpg)](https://cdn.sparkfun.com/assets/d/3/6/4/e/518c1f67ce395f4962000003.jpg)

*[Sparkfun\'s large NES controller](https://www.sparkfun.com/tutorials/35).*

A real world example of using a shift register to gather inputs is the original Nintendo controller. The main microcontroller of the NES needed to get button presses from the controller, and it used a shift register to accomplish that task.

## Example

### Hardware Hookup

We will use the [74HC165 breakout board](https://www.sparkfun.com/products/11512) and an [Arduino Uno](https://www.sparkfun.com/products/11021) to show how to do a parallel-in to serial-out for this example.

[![these can easily be chained together for more inputs](https://cdn.sparkfun.com/assets/b/0/1/9/3/518c21dbce395f2962000000.jpg)](https://cdn.sparkfun.com/assets/b/0/1/9/3/518c21dbce395f2962000000.jpg)

*74HC165 breakout reference for the pinout.*

An 8-bit shift register needs 4 lines of a microcontroller. One for the Clock to time the data transfer, one to the enable the clock, one for loading/latching/shifting the bits, and one for the serial data transfer.

[![Make sure to double check the connections](https://cdn.sparkfun.com/r/600-600/assets/1/9/2/5/3/5193b6e9ce395f5259000001.jpg)](https://cdn.sparkfun.com/assets/1/9/2/5/3/5193b6e9ce395f5259000001.jpg)

*Fritzing wiring diagram.*

Connect clock (CLK) to pin 12 and clock enable ([CE]) to pin 9. The clock sets the frequency that bits are shifted while the clock enable line allows the clock signal to propagate through to the shifting circuitry.

Connect shift/load (SH/[LD]) to pin 8. A transition to low on the load pin tells the shift register to grab the current state of the 8 input pins(A-H). Pins A-H can be connected to some type of input like buttons, switches, or a digital transistor circuit. If you are testing them, it\'s recommended to just directly tie them to power or ground to make sure everything is working correctly. For the sake of this example, I\'ll connect one to a button with a pull up resistor and the rest to power or ground.

Connect the serial out (SER_OUT) to pin 11. This pin is where we receive the serial information from the shift register. Also, connect serial in (SER_IN) to ground. If you were chaining multiple shift registers together, serial in would be attached to the serial out of the last register. The first register in line would still have its serial in pin connected to ground while the last in the chain would have its serial out connected back to the microprocessor instead of another shift register.

Don\'t forget to connect power (**2V-6V**) and ground as well. With everything hooked up, let\'s take a look at the firmware.

### Firmware

Here\'s a brief rundown of what the code does. It first initializes all the pins we connected to outputs with the exception of the pin we receive serial information on. We set the clock and shift pin to initial states (HIGH) as described by the datasheet. In order to read the state of the pins A-H, we need to tell the shift register to capture the state of the pins. We do this by pulling the load pin LOW briefly (5 microseconds). Once the pins are loaded, we make sure the rest of the pins are in the starting state as described by the datasheet and use the Arduino `shiftIn` function to pull all 8 A-H pin values into a byte called incoming. The values are printed out cleanly on the Serial Terminal. It then waits and repeats. If you\'re connecting pins like we did above, it should be easy to test if your hardware is working correctly.

Here\'s the code:

    language:cpp
    // HARDWARE CONNECTIONS
    // Connect the following pins between your Arduino and the 74HC165 Breakout Board
    // Connect pins A-H to 5V or GND or switches or whatever
    const int data_pin = 11; // Connect Pin 11 to SER_OUT (serial data out)
    const int shld_pin = 8; // Connect Pin 8 to SH/!LD (shift or active low load)
    const int clk_pin = 12; // Connect Pin 12 to CLK (the clock that times the shifting)
    const int ce_pin = 9; // Connect Pin 9 to !CE (clock enable, active low)

    byte incoming; // Variable to store the 8 values loaded from the shift register

    // The part that runs once
    void setup() 
    

    // The part that runs to infinity and beyond
    void loop() 

    // This code is intended to trigger the shift register to grab values from it's A-H inputs
    byte read_shift_regs()
    

    // A function that prints all the 1's and 0's of a byte, so 8 bits +or- 2
    void print_byte(byte val)
    
        Serial.print("\n"); // Go to the next line, do not collect $200
    }

Here\'s example output:

    language:text
    The incoming values of the shift register are: 
    ABCDEFGH : 11110000

Now, try connecting each input to buttons or adding another shift register into the mix. If you chain more together, you\'ll have to modify the code slightly by doing the loading once, then doing a `shiftIn` for each shift register you have before loading again.