# Source: https://learn.sparkfun.com/tutorials/real-time-clock-module-hookup-guide

## Introduction

The [SparkFun Real Time Clock Module](https://www.sparkfun.com/products/12708) is a simple breakout board for the DS1307 real-time clock (RTC). It can accurately keep track of seconds, minutes, hours, days, months, and years for almost a decade, so your microcontroller doesn\'t have to. It\'s the perfect component for clocks, calendars, or any other time-keeping project.

[![SparkFun Real Time Clock Module](https://cdn.sparkfun.com/r/600-600/assets/parts/9/4/5/4/12708-01.jpg)](https://www.sparkfun.com/sparkfun-real-time-clock-module.html)

### [SparkFun Real Time Clock Module](https://www.sparkfun.com/sparkfun-real-time-clock-module.html) 

[ BOB-12708 ]

This is the SparkFun Real Time Clock (RTC) Module, a small breakout that utilizes the DS1307 to track the current year, month...

[ [\$8.50] ]

The IC on the SparkFun RTC Module is the [Maxim DS1307](https://cdn.sparkfun.com/datasheets/BreakoutBoards/DS1307.pdf). It features a two-wire I^2^C interface and even includes a square wave output pin. Plus, with a battery backup, the DS1307 can **keep time for almost a decade or more** (typically 17 years)!

This tutorial serves as a general introduction to the DS1307 and the SparkFun Real Time Clock Module. It covers both the hardware and firmware requirements of the breakout \-- documenting both example wiring and Arduino code for the chip.

### Suggested Materials

You\'ll need a handful of extra parts to get the RTC Module up-and-running. Below are the components used in this tutorial, if you want to follow along.

A microcontroller that supports [I^2^C](https://learn.sparkfun.com/tutorials/i2c) is required to communicate with the DS1307 and relay the RTC\'s data to the user. The [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or [Arduino Uno](https://www.sparkfun.com/products/11021) are popular options for this role, but just about any microcontroller development board should work. (The firmware examples use an Arduino library, if that serves as any extra motivation to use an Arduino.)

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![Pro Micro - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/9/3/2/6/12640-01a.jpg)](https://www.sparkfun.com/pro-micro-5v-16mhz.html)

### [Pro Micro - 5V/16MHz](https://www.sparkfun.com/pro-micro-5v-16mhz.html) 

[ DEV-12640 ]

Here at SparkFun, we refuse to leave \'good enough\' alone. That\'s why we\'re adding to our line-up of Arduino-compatible microc...

[ [\$22.50] ]

[![Arduino Uno - R3](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/4/3/11021-01.jpg)](https://www.sparkfun.com/arduino-uno-r3.html)

### [Arduino Uno - R3](https://www.sparkfun.com/arduino-uno-r3.html) 

[ DEV-11021 ]

This is the new Arduino Uno R3. In addition to all the features of the previous board, the Uno now uses an ATmega16U2 instead...

[ [\$27.60] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/9/5/1/8/12757-01.jpg)](https://www.sparkfun.com/products/12757)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/products/12757) 

[ DEV-12757 ]

At SparkFun we use many Arduinos and we\'re always looking for the simplest, most stable one. Each board is a bit different an...

**Retired**

**5V Recommended!** The DS1307 should nominally be powered at a voltage around 5V. It doesn\'t support 3.3V. If your development board runs at 3.3V, you may need to do some level-shifting to get the module communicating.

Four or five [jumper wires](https://www.sparkfun.com/products/13870) and a [breadboard](https://www.sparkfun.com/products/12002) help interface the RTC Module to your Arduino. To insert the breakout into the breadboard, you\'ll need to solder [headers](https://www.sparkfun.com/products/116) to the pins. (Don\'t forget [a soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9163)!)

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Jumper Wires Premium 4\" M/M - 20 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/8/8/13870-01.jpg)](https://www.sparkfun.com/products/13870)

### [Jumper Wires Premium 4\" M/M - 20 AWG (30 Pack)](https://www.sparkfun.com/products/13870) 

[ PRT-13870 ]

These are 101mm long 20AWG jumpers with male connectors on both ends. Use these to jumper from any female header on any board...

**Retired**

The RTC Module *does* include a [12mm Coin Cell Battery](https://www.sparkfun.com/products/337). You shouldn\'t need one for a long while, but if you want to stock up on the lithium batteries, the option is there.

### Suggested Reading

The SparkFun RTC Module is a very beginner-friendly breakout board. There are, however, still a few concepts you should be familiar with. If any of the tutorial titles below sound foreign to you, consider giving them a look-through:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

The RTC Module surrounds the DS1307 with all of the components it needs to count time, communicate, and maintain power. The communication and power pins are all broken out to a single, 5-pin header, with pin labels on the top side of the board.

[![RTC Module Breakout top view](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/top.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/top.jpg)

The bottom side of the breakout consists almost entirely of the 12mm coin cell battery holder.

[![RTC Module Breakout bottom view](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/bottom.jpg)

### Pinout

The five pin breakouts on the board provide access to the communication interface and allow you to supply the chip\'s primary power source.

  Pin Label   Input/Output     Description
  ----------- ---------------- ---------------------------------
  SDA         Bi-directional   I^2^C bus data line
  SCL         Input            I^2^C bus clock line
  SQW         Output           Configurable square-wave output
  GND         Supply Input     Ground (0V) supply
  5V          Supply Input     DS1307 V~CC~ power supply input

### Powering the DS1307

The RTC module breakout board does not include any voltage regulation, so power supplied to the \"5V\" pin should be kept within the DS1307\'s recommended operating range: **4.5 to 5.5V**.

The chip is designed to be as low-power as possible. During communication bursts, the chip may consume upward of 1.5mA, but it will run at closer to 200µA.

When the primary power supply is removed and the chip is running off its backup battery, it will consume between 300-800nA (depending on whether the SQW pins is configured as an output).

Assuming it has capacity of 47mAh, a fully charged [12mm coin cell battery](https://www.sparkfun.com/products/337) can keep the DS1307 running for up to **17.88 years** if the chip consumes its minimum 300nA!

(47mAh / 300nA = 156666.67 hours = 6527.78 days = 17.87 years)

### Using the SQW (Square Wave) Output Pin

Aside from its I^2^C pins, the DS1307 also features a configurable square wave output pin \-- SQW. This pin can be configured to produce one of six signals, or it can be turned off.

  SQW State    Description
  ------------ ---------------------------
  1 Hz         Square wave at 1Hz
  4.096 kHz    Square wave at 4.096 kHz
  8.192 kHz    Square wave at 8.192 kHz
  32.768 kHz   Square wave at 32.768 kHz
  0            Pin driven LOW (0V)
  1            Pin driven high (5V)

In order to use the SQW pin as an output driver, it must be connected to a [pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors). A [10kΩ resistor](https://www.sparkfun.com/products/11508), connected between SQW and 5V, should do the job.

#### I^2^C Pull-Up Resistor Disable

A small 3-way jumper, located on the top side of the board (below the brown-ish capacitor) is connects the on-board 4.7kΩ pull-up resistors to the 5V supply. If you need to deactivate these pull-ups, the jumper can be cleared --- effectively removing the resistors from the circuit.

A little bit of [solder wick](https://www.sparkfun.com/products/8775) and a touch of your soldering iron should remove the jumper\'s solder blob.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/jumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/jumper.jpg)

*Pull-up resistor solder jumper*

## Hardware Hookup

Before you can insert the RTC Module into a breadboard, or otherwise connect it to your microcontroller, you\'ll need to solder *something* to the 5-pin header. If you plan on breadboarding with the chip, we recommend [straight male headers](https://www.sparkfun.com/products/116). [Female headers](https://www.sparkfun.com/products/115) or even a few strips of [wire](https://www.sparkfun.com/products/11375) are other good options.

Headers can be assembled on either side of the board \-- one will give you easy view of the pin labels, the other easy access to the coin cell. If you choose the label-view, you may need to add a little air gap between the header shroud and the board, so the header/breadboard can clear the height of the coin cell.

[![Headers soldered to breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/2/headers-soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/headers-soldered.jpg)

Breadboards can make a great \"third hand\" while you\'re soldering these headers \-- especially in this case, where you need to take the height of the battery holder into consideration.

### Example Circuit

The DS1307\'s I^2^C interface means, to interface with the chip, all you need is four wires between your microcontroller and the breakout board: **power, ground, data, and clock**. The SQW pin can optionally be wired to the Arduino and used as a pulse-counter.

Here is an example hookup diagram demonstrating how to connect the board up to an SparkFun RedBoard:

[![RTC Module example fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/2/rtc-module-example-circuit_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/rtc-module-example-circuit_bb.png)

## Using the SparkFun DS1307 Arduino Library

We\'ve written an Arduino library for the DS1307, which takes care of all of the I^2^C communication, bit-shifting, register-writing, and clock-managing; it even sets the time of your RTC automatically! Grab the most recent version of the library from our [SparkFun_DS1307_RTC_Arduino_Library GitHub repository](https://github.com/sparkfun/SparkFun_DS1307_RTC_Arduino_Library):

[Download the SparkFun DS1307 Arduino Library](https://github.com/sparkfun/SparkFun_DS1307_RTC_Arduino_Library/archive/master.zip)

Then follow along with our [How to Install an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) for help installing the library. If you download the library\'s ZIP file, you can use Arduino\'s \"Add ZIP Library\...\" feature to install the source and example files with just a couple clicks.

[![Adding library via ZIP file](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/add-zip-library.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/add-zip-library.png)

### Using the DS1307_RTC_Demo Example

Once you\'ve downloaded the library, open the DS1307_Demo by navigating to **File** \> **Examples** \> **SparkFun DS1307 Real Time Clock (RTC)** \> **DS1307_RTC_Demo**:

[![Opening the example file](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/library-open-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/library-open-example.png)

Once the demo\'s loaded, make sure your board and port are set correctly \-- no modifications required \-- and upload! Then click over to the **Serial Monitor**. Make sure the baud rate is set to 9600 bps, and you should begin to see the seconds fly by:

[![Example serial monitor output](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/serial-monitor-output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/2/serial-monitor-output.png)

### Using the SparkFun DS1307 Arduino Library

The example demonstrates almost all of the DS1307\'s functionality. Here\'s a quick primer on how to incorporate the library into your project:

#### Initialization

To begin, make sure you include the `SparkFunDS1307RTC.h` library. Above that, you\'ll need to include `Wire.h` the Arduino I^2^C library:

    language:c
    #include <SparkFunDS1307RTC.h>
    #include <Wire.h>

The DS1307 library defines an object conveniently named `rtc` to access all of the functions and data of the RTC module. To initialize the RTC, begin by calling the `rtc.begin()` function in your `setup()` area:

    language:c
    void setup()
    

#### Setting the Time

Once the RTC is initialized, you can set the time in the clock. There are a few options here. We recommend using either the `rtc.autoTime()` function, which sets the RTC\'s clock your computer\'s date and time (based on the time of compilation), or `rtc.setTime(second, minute, hour, day, date, month, year)`, which allows you to precisely set the clock.

The demo example defaults to using `rtc.autoTime()`, which sets your RTC\'s time and date to your computer\'s time and date (may be a dozen seconds off).

##### Set and Forget!

Once the RTC\'s time and date register have been set -- using either the `autoTime` or `setTime` functions -- you may never have to set the clock again!

Consider commenting out the `autoTime` or `setTime` entirely once you\'ve perfectly configured the clock.

If you want to manually set the time, use the `setTime()` function. For example:

    language:c
    // Set to 13:37:42 (1:37:42 PM)
    int hour = 13;
    int minute = 37;
    int second = 42;
    // Set to Monday October 31, 2016:
    int day = 2; // Sunday=1, Monday=2, ..., Saturday=7.
    int date = 31; 
    int month = 10;
    int year = 16;

    rtc.setTime(second, minute, hour, day, date, month, year);

##### 12-Hour Mode

The RTC defaults to 24-hour mode, but does support 12-hour mode with an AM/PM bit. If you'd like to use 12-hour mode, simply call `rtc.set12Hour()` (or `rtc.set24Hour()` to switch back to 24-hour mode).

To set the time in 12-hour mode, an extra parameter -- `AM` or `PM` -- should be added after ther \`hour\` variable. For example:

    setTime(14, 42, 7, PM, 1, 28, 12, 16); // Set time to 7:42:14 PM, Sunday December, 28 

setTime(14, 42, 7, PM, 1, 28, 12, 16); // Set time to 7:42:14 PM, Sunday December, 28

#### Reading the Time

Once the clock is set, it will automatically begin incrementing second-by-second, minute-by-minute, etc. To read the time and date values, begin by calling `rtc.update()`. This will command the DS1307 to read all of its data registers in one, fell swoop.

After the RTC data is updated, you can read those updated values by calling `rtc.hour()`, `rtc.minute()`, `rtc.second()`, etc. For example:

    language:c
    rtc.update(); // Update RTC data

    // Read the time:
    int s = rtc.second();
    int m = rtc.minute();
    int h = rtc.hour();

    // Read the day/date:
    int dy = rtc.day();
    int da = rtc.date();
    int mo = rtc.month();
    int yr = rtc.year();

\"Day\" is as in \"day of the week\", e.g. Sunday, Monday, Tuesday\... `rtc.day()` returns an integer between 1 and 7, where 1 is Sunday and 7 is Saturday (sorry week-starts-on-Monday truthers). Alternatively, you can call `rtc.dayChar()` or `rtc.dayStr()`, which return a character or full-string representation of the day of the week.

------------------------------------------------------------------------

For more on using the SparkFun DS1307 Arduino Library consider reading through the [header file](https://github.com/sparkfun/SparkFun_DS1307_RTC_Arduino_Library/blob/master/src/SparkFunDS1307RTC.h), which documents all of the Arduino sketch-available functions.