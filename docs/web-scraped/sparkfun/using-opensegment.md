# Source: https://learn.sparkfun.com/tutorials/using-opensegment

## Basics

[![OpenSegment 7-segment serial display](https://cdn.sparkfun.com/r/600-600/assets/d/5/5/2/9/514de190ce395fbd39000000.png)](https://cdn.sparkfun.com/assets/d/5/5/2/9/514de190ce395fbd39000000.png)

[OpenSegment](https://www.sparkfun.com/products/11644) is a simple to use 7-segment display. It has the ability to communicate over serial, I^2^C, SPI, as well as analog and counter modes. It is super easy to use if you just need to display a number but have a lot of features including setting brightness levels and individual segment control built in.

[![OpegSegment as boxing counter](https://cdn.sparkfun.com/r/600-600/assets/1/a/6/3/b/514dd074ce395f8561000002.JPG)](https://cdn.sparkfun.com/assets/1/a/6/3/b/514dd074ce395f8561000002.JPG)

*OpenSegment displaying the number of speed bag hits.*

The OpenSegment is the big brother to the [Serial7Segment](https://www.sparkfun.com/products/11442) by Jim Lindblom. Both products use the same firmware but have different hardware layouts. Therefor, you can rely heavily on Jim's [datasheet](https://github.com/sparkfun/Serial7SegmentDisplay/wiki/Serial-7-Segment-Display-Datasheet) for Serial7Segment and all the example code [located here](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples).

### Suggested Reading

Things you may need to know before working with one of these boards:

- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [JST Connectors](https://learn.sparkfun.com/tutorials/connector-basics/power-connectors)
- [Wire stripping](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire)
- [Soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

## Hardware Info

[![Mounted 7 segment display](https://cdn.sparkfun.com/r/600-600/assets/a/6/5/9/8/514dd1ddce395f0a61000000.JPG)](https://cdn.sparkfun.com/assets/a/6/5/9/8/514dd1ddce395f0a61000000.JPG)

*SparkFun boxes make great enclosures!*

OpenSegment can be powered from 4V (less bright) to 12V, but we recommend 5 to 6V. The default communication is 9600bps over serial.

**Note:** At any time the device can be reset to factory defaults (9600bps) by tying the RX pin to GND and powering up the device. See the [Factory Reset](https://learn.sparkfun.com/tutorials/using-opensegment/factory-reset) section for more information.

[![Hardware Backpack](https://cdn.sparkfun.com/assets/2/e/a/b/e/514dd243ce395f3761000003.png)](https://cdn.sparkfun.com/assets/2/e/a/b/e/514dd243ce395f3761000003.png)

The onboard regulator will regulate down to 5V. The regulator will protect against shorts, reverse power, over current, and overheating. Powering the board with more than 7V is ok, but the regulator will begin to dissipate the extra power by heating up and\--depending on the brightness setting and input voltage\--may cause the board to flicker.

The OpenSegment has an ATmega328 running a modified Optiboot bootloader. It's basically a little Arduino running at 8MHz. You can reprogram the board using a standard serial connection. We always have an [FTDI basic](https://www.sparkfun.com/products/9716) handy to make code changes, but you shouldn't ever have to reprogram the display unless you *really* want to tweak the code.

## Serial Communication

[![Serial pins](https://cdn.sparkfun.com/assets/b/6/8/b/a/514dd29ece395f2061000000.png)](https://cdn.sparkfun.com/assets/b/6/8/b/a/514dd29ece395f2061000000.png)

*The serial connection pins*

The easiest way to control OpenSegment is over serial. You need only 3 pins: PWR, GND and RX. The RX pin on OpenSegment should be connected to the TX pin of your microcontroller.

[![JST Pins](https://cdn.sparkfun.com/assets/4/7/e/d/0/514dd29fce395f6961000001.png)](https://cdn.sparkfun.com/assets/4/7/e/d/0/514dd29fce395f6961000001.png)

*The basic 3 pins, ready for a JST connector*

The easiest way to physically connect to OpenSegment is through a [3-pin JST connector](https://www.sparkfun.com/products/9915).

[![JST connector soldered](https://cdn.sparkfun.com/r/600-600/assets/6/7/8/5/c/514dd29fce395f2261000000.JPG)](https://cdn.sparkfun.com/assets/6/7/8/5/c/514dd29fce395f2261000000.JPG)

*[3-pin JST connector](https://www.sparkfun.com/products/9915) soldered in and ready to go!*

Solder the JST onto the backpack, plug the JST cable in, and then plug the red wire to 5V to 7V, black wire to GND, and yellow wire to the TX pin of your development board.

## Serial Example

[![Basic serial hookup](https://cdn.sparkfun.com/assets/3/b/5/7/e/514dd380ce395f1061000002.png)](https://cdn.sparkfun.com/assets/3/b/5/7/e/514dd380ce395f1061000002.png)

*Connect 3 wires to your Arduino*

Using an OpenSegment display with Arduino is very straightforward. Power the display from the 5V pin, GND, and connect the RX pin of the display to pin 8 on the Arduino.

Here is an example to get you started immediately.

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /*
     9-23-2012
     Spark Fun Electronics
     Nathan Seidle

     This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

     Serial7Segment is an open source seven segment display. 

     This is example code that shows how to display basic numbers on the display.

     Note: This code expects the display to be listening at 9600bps. If your display is not at 9600bps, you can
     do a software or hardware reset. See the Wiki for more info: 
     http://github.com/sparkfun/Serial7SegmentDisplay/wiki/Special-Commands#wiki-baud

     To get this code to work, attached an Serial7Segment to an Arduino Uno using the following pins:
     Pin 8 on Uno (software serial TX) to RX on Serial7Segment
     VIN to PWR
     GND to GND

    */

    #include <SoftwareSerial.h>

    SoftwareSerial Serial7Segment(7, 8); //RX pin, TX pin

    int cycles = 0;

    void setup() 

    void loop() 
    

Load the above example code onto your Arduino, and watch the display count up!

You can find many [more examples here](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples) on GitHub. There are sketches to show you:

- Basic counting
- Controlling the colon and dots on a display
- Changing the mode
- Fun Predator mode
- Changing the baud rate
- Doing a software serial reset

## I2C/SPI Communication

If you need to control lots of displays at the same time, OpenSegment has the ability to communicate over I^2^C and SPI.

### I^2^C Communication

[![I2C pins](https://cdn.sparkfun.com/assets/8/d/4/7/8/514dd886ce395f2b3a000000.png)](https://cdn.sparkfun.com/assets/8/d/4/7/8/514dd886ce395f2b3a000000.png)

*I^2^C communication requires 4 pins: SDA, SCL, PWR, and GND.*

[![I2C side pins](https://cdn.sparkfun.com/assets/2/5/f/e/8/514dd886ce395faf3a000000.png)](https://cdn.sparkfun.com/assets/2/5/f/e/8/514dd886ce395faf3a000000.png)

The I^2^C pins are labeled on the edge of the backpack and on the sides to make it easier to chain many displays together.

The default 7-bit I^2^C address is 113 in base10 or `0x71` in HEX or `01110001` in binary.

**Heads up!** 0x71 is the 7-bit I2C address. If you are using a different language than Arduino you will probably need to add the Read/Write bit to the end of the address. This means the default read address for the OpenSegment is 0b.1110.0011 or 0xE3 and the write address is 0b.1110.0010 or 0xE2. For more information see our [tutorial on I^2^C](https://learn.sparkfun.com/tutorials/i2c)

OpenSegment supports standard 100kHz as well as Fast 400kHz I2C speeds. Use the following code to enable Fast I2C within Arduino:

    Wire.begin(); //Join the bus as controller. 
    //By default .begin() will set I2C SCL to Standard Speed mode of 100kHz
    Wire.setClock(400000); //Optional - set I2C SCL to High Speed Mode of 400kHz

Checkout the [I^2^C examples](https://github.com/sparkfun/Serial7SegmentDisplay/blob/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_I2C_Basic/S7S_Example_I2C_Basic.ino) on GitHub for good code to start from.

You can find many [more I^2^C examples here](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples) on GitHub. There are sketches to show you:

- [Basic counting](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_I2C_Basic)
- [Changing the I^2^C Address](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_I2C_ChangeAddress)
- [Changing the brightness and other settings](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_I2C_Settings)

### SPI Communication

[![SPI pins](https://cdn.sparkfun.com/assets/b/6/a/d/d/514dd9d0ce395feb3a000000.png)](https://cdn.sparkfun.com/assets/b/6/a/d/d/514dd9d0ce395feb3a000000.png)

*Bank of SPI pins*

SPI communication requires 6 pins: SDO, SDI, SCK, CS, PWR, and GND. We may add a feature in the future, but for now OpenSegment does not pass data out of the SDO (serial data out) pin and can be left disconnected. If you're hooking multiple OpenSegments together on the same SPI bus, the CS pin on each display must be connected to a different GPIO on your microcontroller.

You can find many [more SPI examples here](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples) on GitHub. There are sketches to show you:

- [Basic counting](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_SPI_Basic)
- [Changing the brightness and other settings](https://github.com/sparkfun/Serial7SegmentDisplay/tree/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_SPI_Settings)

## Counter/Analog Modes

OpenSegment has three modes:

- **Data mode** (where you send commands and data over Serial/SPI/I^2^C)
- **Counter mode** (count up/down based on SDI/SDO)
- **Analog meter mode** (display analog voltages on A6/A7)

We've covered the basic data mode; let's cover the other two modes.

To control the mode of the display, send the command `0x82` over serial followed by:

- 0 for data mode
- 1 for analog meter mode
- 2 for counter mode

An example of how to do this over serial is [available here](https://github.com/sparkfun/Serial7SegmentDisplay/blob/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_Serial_Mode_Change/S7S_Example_Serial_Mode_Change.ino).

You *do not* need to solder the jumper to control the mode. Please read the solder jumper section below for more information.

### Counter Mode

[![alt text](https://cdn.sparkfun.com/assets/5/9/0/1/0/514ddc3ece395f123a000002.png)](https://cdn.sparkfun.com/assets/5/9/0/1/0/514ddc3ece395f123a000002.png)

*The counter jumper and the two pins that control the count.*

When the display is in *Counter* mode, the display will increase by one every time the SDI pin (**i** is for increase!) is pulled low and will decrease by one every time the SDO pin is pulled low. This mode was created to monitor and count the number of times a [button](https://www.sparkfun.com/products/9336) is pressed or a [reed switch](https://www.sparkfun.com/products/8642) is closed. The display must be power cycled to reset the count.

### Analog Meter Mode

[![Analog pins on OpenSegment](https://cdn.sparkfun.com/assets/d/5/3/2/0/514ddc3fce395ff43a000000.png)](https://cdn.sparkfun.com/assets/d/5/3/2/0/514ddc3fce395ff43a000000.png)

When the display is in *Analog* mode the instantaneous analog voltage on pins A7 and A6 will be shown on the display with 1/10th volt resolution (0.0V to 5.0V).

The voltage on A6 is displayed on the left and A7 is displayed on the right. This mode was created to monitor basic voltages (0 to 5V) without the need of a multimeter.

### Solder Jumpers

[![Solder jumpers](https://cdn.sparkfun.com/assets/b/d/f/c/e/514dde24ce395fd13a000000.png)](https://cdn.sparkfun.com/assets/b/d/f/c/e/514dde24ce395fd13a000000.png)

You can use OpenSegment as a counter and as an analog meter without any software configuration. By closing a solder jumper on the back of the display OpenSegment will enter one of two modes: Counter or Analog Meter mode.

Closing a solder jumper will override any software settings and will force the display into that mode after power up. If *both* jumpers are closed the display will startup in Counter mode.

## Factory Reset

Have you forgotten what baud rate the device has been configured to? Don't worry! The device can be reset to factory defaults by tying the RX pin to GND and then powering up the device.

[![Dashes during reset](https://cdn.sparkfun.com/r/300-300/assets/1/7/d/6/a/514ddea6ce395fa63a000000.JPG)](https://cdn.sparkfun.com/assets/1/7/d/6/a/514ddea6ce395fa63a000000.JPG) [![Dashes during reset](https://cdn.sparkfun.com/r/300-300/assets/7/0/e/c/f/514ddea5ce395f133a000000.JPG)](https://cdn.sparkfun.com/assets/7/0/e/c/f/514ddea5ce395f133a000000.JPG)

Once powered up you will see alternating - (dashes) and \_ (underscores) for 1 second.

[![Reset state](https://cdn.sparkfun.com/r/300-300/assets/4/c/f/3/7/514ddea6ce395fa93a000000.JPG)](https://cdn.sparkfun.com/assets/4/c/f/3/7/514ddea6ce395fa93a000000.JPG) [![Reset state](https://cdn.sparkfun.com/r/300-300/assets/2/1/7/6/0/514ddea6ce395fc739000000.JPG)](https://cdn.sparkfun.com/assets/2/1/7/6/0/514ddea6ce395fc739000000.JPG)

Once you see a rotating display of *0-00* you will know the device has been reset to 9600bps. You can now release the RX pin from ground, and the display will continue to function normally.

There is also an example sketch to show you how to do a [reset over serial](https://github.com/sparkfun/Serial7SegmentDisplay/blob/master/firmware/Serial%207-Segment%20Display/Arduino_Examples/S7S_Example_Serial_SoftwareReset/S7S_Example_Serial_SoftwareReset.ino). This can be handy if the display is installed in an application and you can't pull the RX line low during power up.