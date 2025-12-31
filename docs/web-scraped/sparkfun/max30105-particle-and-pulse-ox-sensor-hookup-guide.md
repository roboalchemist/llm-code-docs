# Source: https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide

## Introduction

The [SparkFun MAX30105 Particle Sensor](https://www.sparkfun.com/products/14045) is a flexible and powerful sensor enabling sensing of distance, heart rate, particle detection, even the blinking of an eye. This tutorial will get you up and running to get the raw data from the sensor.

[![SparkFun Particle Sensor Breakout - MAX30105](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/8/7/4/14045-01.jpg)](https://www.sparkfun.com/products/14045)

### [SparkFun Particle Sensor Breakout - MAX30105](https://www.sparkfun.com/products/14045) 

[ SEN-14045 ]

The SparkFun MAX30105 Particle Sensor is a flexible, powerful sensor enabling sensing of distance, heart rate, particle detec...

**Retired**

Behind the window on the left, the MAX30105 has three LEDs. On the right is a very sensitive photon detector. The idea is that you obstruct the different LEDs, detecting what light shines back at the detector, and, based on the signature, you can tell the presence of different types of particles or materials (such as oxygenated blood or smoke from a fire).

[![Close up photo of the MAX30105 sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/MAX30105_Close_up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_Close_up.jpg)

*Close up photo of the MAX30105 sensor.*

### Suggested Materials

You\'ll need a handful of extra parts to get the MAX30105 breakout up-and-running. Below are the components used in this tutorial, if you want to follow along.

A microcontroller that supports [I^2^C](https://learn.sparkfun.com/tutorials/i2c) is required to communicate with the MAX30105 and relay the data to the user. The [SparkFun RedBoard](https://www.sparkfun.com/products/12757) or [Arduino Uno](https://www.sparkfun.com/products/11021) are popular options for this role, but just about any microcontroller development board should work. (The firmware examples use an Arduino library, if that serves as any extra motivation to use an Arduino.)

[![Arduino Pro Mini 328 - 5V/16MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/3/9/11113-01b.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html)

### [Arduino Pro Mini 328 - 5V/16MHz](https://www.sparkfun.com/arduino-pro-mini-328-5v-16mhz.html) 

[ DEV-11113 ]

SparkFun\'s minimal design approach to Arduino. This is a 5V Arduino running the 16MHz bootloader.

[ [\$11.25] ]

[![SparkFun SAMD21 Mini Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/9/2/13664-01.jpg)](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html)

### [SparkFun SAMD21 Mini Breakout](https://www.sparkfun.com/sparkfun-samd21-mini-breakout.html) 

[ DEV-13664 ]

If you're ready to step your Arduino game up from older 8-bit/16MHz microcontrollers, the SparkFun SAMD21 Mini Breakout is ...

[ [\$24.95] ]

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

**5V Recommended!** The MAX30105 can run at 3.3V to 5V and can communicate with 3.3V and 5V microcontrollers. Most USB based development boards have a 5V pin that will power the MAX30105 nicely.

Four or five [jumper wires](https://www.sparkfun.com/products/13870) and a [breadboard](https://www.sparkfun.com/products/12002) help interface the sensor to your Arduino. To insert the breakout into the breadboard, you\'ll need to solder [headers](https://www.sparkfun.com/products/116) or cut jumper wires to the pins. (Don\'t forget [a soldering iron](https://www.sparkfun.com/products/9507) and [solder](https://www.sparkfun.com/products/9163)!)

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

### Suggested Reading

The MAX30105 is designed for a handful of uses including [Pulse Oximetry](https://en.wikipedia.org/wiki/Pulse_oximetry). If you\'re unfamiliar with optical pulse detection there are some very good app notes from [TI](http://www.ti.com/lit/an/slaa655/slaa655.pdf) and [NXP](http://www.nxp.com/files/32bit/doc/app_note/AN4327.pdf) that have great starter information.

The MAX30105 communicates over I^2^C. We've got a great library to make it easy to use. And, we're going to be using a breadboard to connect the breakout board to the RedBoard. If any of these subjects sound foreign to you, consider browsing through that tutorial before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## MAX30105 Breakout Overview

The MAX30105 has three on-board LEDs (seen on the left). Maxim recommends these LEDs be powered from 5V, but we\'ve found the LEDs work fine at 3.3V. The red and IR LEDs are [guaranteed to work at 3.3V](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/LED_Supply_Headroom.jpg), but the green LED may need 3.5V. It\'s best to try out your board at 3.3V and see if the green LED illuminates.

[![Close up view of MAX30105](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/MAX30105_Close_up.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_Close_up.jpg)

The IC itself runs at 1.8V, so we've included the interface logic to allow you to hook the MAX30105 Breakout Board to any board that has 5V, 3.3V, even 1.8V level I/O.

  Pin Label                                  Input/Output     Description
  ------------------------------------------ ---------------- -----------------------
  [INT]   Output           Interrupt, active low
  GND                                        Supply Input     Ground (0V) supply
  5V                                         Supply Input     Power supply
  SDA                                        Bi-directional   I^2^C bus clock line
  SCL                                        Input            I^2^C bus clock line

The GND/5V/SDA/SCL pin-out is the standard I^2^C connection on most of our products. This allows you to easily connect I^2^C boards to many of our platforms.

[![The I2C Pins on the MAX30105](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/I2C_Pins_MAX30105.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/I2C_Pins_MAX30105.jpg)

There are two jumpers on the back of the PCB:

[![Rear jumpers on MAX30105 Breakout Board](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Rear_Jumpers_MAX30105.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Rear_Jumpers_MAX30105.jpg)

- The **PU** jumper is used on many I^2^C boards to allow the user to disconnect the 4.7k Ohm pull-up (**PU**) resistors from the SDA and SCL lines. By default, this jumper is closed meaning there are 4.7k pull-up resistors on SDA and SCL. If this is the only device on the I^2^C bus, then this jumper should be left closed. If there are multiple I^2^C devices or breakout boards on the bus with pull-up resistors, then the traces in this jumper should be cut to remove the 4.7k Ohm resistors from the bus. If needed, the jumper can be re-soldered to close it again in the future.

- The **INT** jumper is used to control the pull-up resistor on the interrupt pin. The INT jumper is closed by default, which means a 4.7k resistor is pulling up the interrupt pin. The INT pin on the MAX30105 is an open drain pin. If there is only one board on your I^2^C bus, this jumper should be left closed. If there are multiple boards on the I^2^C bus sharing a single interrupt pin, this jumper can be cut to disconnect the pull up resistor.

## Hardware Hookup

[![MAX30105 in a fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Fritzing_Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Fritzing_Hookup.jpg)

*Four wires is all you need but consider using connecting the board with soldered wires instead of a breadboard!*

Because this sensor can be used in a multitude of ways, consider how you\'re going to use the MAX30105 before soldering. If you plan to use the sensor for pulse oximetry, we recommend soldering short wires to the board to enable some movement when the sensor is attached to a finger. If you\'re more interested in static sensing like particle or air monitoring, consider soldering male headers to the board.

Here\'s an example of using jumper wires to make a robust connection to the MAX30105 board.

These [jumper wires](https://www.sparkfun.com/products/11026) contain stranded wire, which make them more flexible and less prone to breaking from repeated movement.

[![Four jumper wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Jumper_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Jumper_Wires.jpg)

Pick four different color wires, and cut them to your desired length. We use red, black, yellow and blue to make things easy to identify.

[![Cut jumper wires](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Cut_Jumper_Wires.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Cut_Jumper_Wires.jpg)

[Strip](https://learn.sparkfun.com/tutorials/working-with-wire/how-to-strip-a-wire) the ends of the wire, and solder them into their various spots. A connection to the INT pin is optional and not needed for the Arduino examples below.

Getting small gauge wires to stay in place can be tough. I like to use sticky tack to hold everything in place while I solder.

[![Soldering stripped wire using sticky tack](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Soldering_MAX3015-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Soldering_MAX3015-3.jpg)

*Sticky tack is your friend!*

You can pick any colors you want, but using different colors for each pin will make it easier to distinguish between connections.

[![Soldering wires onto MAX30105](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Soldering_MAX3015-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Soldering_MAX3015-2.jpg)

*Recommended wire colors: Red-VCC, Black-GND, Yellow-SCL, Blue-SDA*

[Stranded wire](https://learn.sparkfun.com/tutorials/working-with-wire#stranded-vs-solid) is better at flexing than solid core wire. However, without stress relief, even these stranded wires may break due to lots of flexing.

[![Stranded wire soldered into place](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Wires_into_MAX30105.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Wires_into_MAX30105.jpg)

*Wires soldered into place*

Adding a bit of hot-glue where the wires meet the PCB will make the board even more robust and resistant to damage when you start \"speaking\" with your hands.

[![PCB with hot glue as stress reflief](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Hot_Glue_Stress_Relief_MAX30105.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Hot_Glue_Stress_Relief_MAX30105.jpg)

## Using the SparkFun MAX30105 Arduino Library

Let's get right to it! We\'ve written an Arduino library for the MAX30105 and MAX30102 (it should work with the MAX30101 as well), which takes care of all of the I^2^C communication, bit-shifting, register-writing, and sample-reading. The library supports the MAX30102 (Red and IR LEDs only) and the MAX30105 (Red, IR, and Green LEDs).

The easiest way to install the library is through the Arduino Library manager.

[![Manage Arduino libraries](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Arduino_Libraries.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Arduino_Libraries.jpg)

Type **MAX30105** into the Search box and select the SparkFun Library.

[![MAX30105 Arduino Library](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/MAX30105_Arduino_Library.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_Arduino_Library.jpg)

Click on the SparkFun library to highlight it, then click on the Install button.

[![MAX30105 Example Menu](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/MAX30105_Examples_Menu-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_Examples_Menu-1.jpg)

Once you've downloaded the library, you should see the Example sketches by navigating to

    File > Examples > SparkFun MAX3010x Pulse and Proximity Sensor Library > Examples

While you\'re there, go ahead and open **Example1 Basic Readings**.

If you\'d rather grab the most recent version of the library from our [SparkFun MAX3010x Sensor GitHub repository](https://github.com/sparkfun/SparkFun_MAX3010x_Sensor_Library), you can do that too!

[Download the SparkFun MAX3010x Arduino Library](https://github.com/sparkfun/SparkFun_MAX3010x_Sensor_Library/archive/master.zip)

Then follow along with our [How to Install an Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) for help installing the library. If you download the library\'s ZIP file, you can use Arduino\'s \"Add ZIP Library\...\" feature to install the source and example files with just a couple clicks.

## Example 1 - Reading Red/IR/Green

Once you\'ve got the library installed, open the **Example1 Basic Readings** sketch. You can find it under

    File > Examples > SparkFun MAX3010x Pulse and Proximity Sensor Library > Examples

Then load it onto your RedBoard or Uno. Open your favorite [Serial Terminal](https://learn.sparkfun.com/tutorials/terminal-basics) to see the printed values.

[![Screen shot of MAX30105 readings](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example1a.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example1a.jpg)

This example outputs the raw values read by the sensor. With the sensor pointing up, use your hand to hover over the sensor. You should see a change in values as your hand reflects different amounts of light. Note that the IR readings will probably change before the Red and Green readings. IR is better at sensing distance changes.

Completely cover the sensor with your finger. Note the very large readings. This is one of the features that sets the MAX30105 from other reflectance sensors. The IC is capable of reading up to 18-bits or values up to 262,144. An extremely small change in light can be detected!

The MAX30105 is easy to use! Calling `particleSensor.getGreen()` will take a reading and return the reflected amount of green light.

## Example 2 - Presence Sensing

Open the **Example2 Presence Sensing** sketch, and load it onto your RedBoard or Uno.

[![IR readings and distance sensing from MAX30105](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example2.jpg)

This example takes a handful of readings during setup and averages them together. It uses this average as a baseline. If the sensor detects a significant change from the average, then "Something is there!" is printed. This is useful when you need to detect if a ball drops through a channel or other photo-gate situations. It\'s also handy for testing the range at which the sensor can detect something.

    language:c
    //Setup to sense up to 18 inches, max LED brightness
    byte ledBrightness = 0xFF; //Options: 0=Off to 255=50mA
    byte sampleAverage = 4; //Options: 1, 2, 4, 8, 16, 32
    byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
    byte sampleRate = 400; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
    int pulseWidth = 411; //Options: 69, 118, 215, 411
    int adcRange = 2048; //Options: 2048, 4096, 8192, 16384

    particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings

*What is this block of code doing?*

During setup this code initializes the sensor. There are many different options and configurations for the MAX30105. You can define as many or as few as you\'d like. You can also skip them all:

    language:c
    particleSensor.setup(); //Configure sensor with default settings

The sensor will be configured with the default settings. The default settings work for most applications.

## Example 3 - Temperature Sensor

Open the **Example3 Temperature Sense** sketch, and load it onto your RedBoard or Uno.

[![Temperature output from MAX3015 sensor](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example3.jpg)

This example outputs readings from the on-board temperature sensor in both Celsius and Fahrenheit. The temp sensor is accurate to +/-1 C but has an astonishing precision of 0.0625 C.

The temperature is used internally by the sensor to calibrate its samples but can be useful if you need a sensitive and fast responding temp sensor.

## Example 4 - Heart Beat Plotting

This is where the fun really begins! Hemoglobin reflects IR light really well, and the MAX3015 is capable of detecting such small changes in IR reflectance that it can detect blood flowing through your finger at different rates. Let\'s graph it! Open the **Example4 HeartBeat Plotter** sketch, and load it on your Redboard or Uno.

**Arduino v1.6.6 or Higher Required.** The Serial Plotter is only available in Arduino versions v1.6.6 or later.

For this demo, you\'ll need a rubber band small enough to go through the mounting holes on the breakout.

[![Rubber band inserted through two holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/Rubber_Band_through_MAX30105.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Rubber_Band_through_MAX30105.jpg)

Loop the band back onto itself, and pull gently. You want a little bit of pressure holding your finger against the sensor. If the end of your finger turns pale, you\'ve tightened too much!

[![Pulse Oximetry MAX30105 cinched to finger](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/7/7/MAX30105_Pulse_Oximetry.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_Pulse_Oximetry.jpg)

**I\'ll just hold my finger on the sensor instead\...**

Humans are bad at applying consistent pressure to a thing. Without a rubber band the pressure varies enough to cause the blood in your finger to flow differently which causes the sensor readings to go wonky. It is best to attach the sensor to your finger using a rubber band or other tightening device.

[![Graph of heart beat](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/HeartBeat.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/HeartBeat.jpg)

*Graph of IR data - That\'s my pulse!*

Instructions:

1.  Load code onto Redboard
2.  Attach sensor to your finger with a rubber band
3.  Open Tools-\>*Serial Plotter*
4.  Make sure the drop down is set to 115200 baud
5.  Checkout the blips!
6.  Feel the pulse on your neck and watch it mimic the blips

Now that we have seen the blips, Example 5 will try to calculate the time between blips and show us beats per minute (BPM).

## Example 5 - HeartRate

**Hey!** Let\'s have a brief chat about what this code does. We\'re going to try to detect heart-rate optically. This is tricky and prone to give false readings. We really don\'t want to get anyone hurt, so use this code only as an example of how to process optical data. Build fun stuff with our MAX30105 breakout board, but don\'t use it for actual medical diagnosis.

Open the **Example5 HeartRate** sketch, and load it on your Redboard or Uno.

[![Heart rate output](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/Example5.jpg)

This example runs a filter called the PBA or Penpheral Beat Amplitude algorithm on the IR data. This algorithm is able to pull out the blips from all the noise and calculate the time between blips to get a heart rate. The output is your instantaneous heart rate and your average heart rate (BPM).

As one might expect the human body isn\'t as precise as a metronome. The time between pulses can vary quite a bit so this sketch takes a running average of 4 readings to try to smooth out the variance.

**Trouble?** Try moving the sensor to a different finger. The rubber rand should be snug but not tight. The algorithm takes a few seconds to determine the peaks and troughs, so each time you move the sensor, wait a few seconds for the readings to make sense.

## Advanced Functions

The MAX30105 is highly configurable, and there are a large number of functions exposed in the library to the user. Checkout the MAX30105.h file for all the functions, but here are the major ones. Read the [MAX30105 datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_3.pdf) for more information.

The library supports the following functions:

- `.begin(wirePort, i2cSpeed)` - If you have a platform with multiple I^2^C ports, pass the port object when you call begin. You can increase the I^2^C speed to 400kHz by including I2C_SPEED_FAST when you call `.begin()` as well.
- `.setup()` - Initializes the sensor with various settings. See the [Example 2](https://learn.sparkfun.com/tutorials/max30105-particle-and-pulse-ox-sensor-hookup-guide#example-2---presence-sensing) for a good explanation of the options.
- `.getRed()` - Returns the immediate red value
- `.getIR()` - Returns the immediate IR value
- `.getGreen()` - Returns the immediate Green value
- `.available()` - Returns how many new samples are available
- `.readTemperature()` - Returns the temperature of the IC in C
- `.readTemperatureF()` - Returns the temperature of the IC in F
- `.softReset()` - Resets everything including data and configuration
- `.shutDown()` - Powers down the IC but retains all configuration
- `.wakeUp()` - Opposite of shutDown
- `.setLEDMode(mode)` - Configure the sensor to use 1 (Red only), 2 (Red + IR), or 3 (Red + IR + Green) LEDs
- `.setADCRange(adcRange)` - Set ADC to be at 2048, 4096, 8192, or 16384
- `.setSampleRate(sampleRate)` - Configure the sample rate: 50, 100, 200, 400, 800, 1000, 1600, 3200

**Interrupts**

- `.getINT1()` - Returns the main interrupt group
- `.getINT2()` - Returns the temp ready interrupt

Enable/disable individual interrupts. See page 13 and 14 of the [datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/5/7/7/MAX30105_3.pdf) for an explanation of each interrupt:

- `.enableAFULL()`
- `.disableAFULL()`
- `.enableDATARDY()`
- `.disableDATARDY()`
- `.enableALCOVF()`
- `.disableALCOVF()`
- `.enablePROXINT()`
- `.disablePROXINT()`
- `.enableDIETEMPRDY()`
- `.disableDIETEMPRDY()`

**FIFO**

The MAX30105 has a 32 byte FIFO. This allows us do other things on our microcontroller while the sensor is taking measurements. See **Example 6** for an explanation of how to poll the FIFO.

- `.check()` - Call regularly to pull data in from sensor
- `.nextSample()` - Advances the FIFO
- `.getFIFORed()` - Returns the FIFO sample pointed to by tail
- `.getFIFOIR()` - Returns the FIFO sample pointed to by tail
- `.getFIFOGreen()` - Returns the FIFO sample pointed to by tail