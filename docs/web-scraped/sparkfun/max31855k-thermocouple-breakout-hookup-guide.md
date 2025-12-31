# Source: https://learn.sparkfun.com/tutorials/max31855k-thermocouple-breakout-hookup-guide

## Introduction

The [MAX31855K Thermocouple Breakout](https://www.sparkfun.com/products/13266) is a simple 14-bit resolution, SPI-compatible, serial interface thermocouple digitizer that makes reading a wide range of temperatures possible. We\'ve broken this device out on a breakout board along with all the necessary componets to make using it a breeze!

[![SparkFun Thermocouple Breakout - MAX31855K](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/4/8/7/13266-01.jpg)](https://www.sparkfun.com/sparkfun-thermocouple-breakout-max31855k.html)

### [SparkFun Thermocouple Breakout - MAX31855K](https://www.sparkfun.com/sparkfun-thermocouple-breakout-max31855k.html) 

[ SEN-13266 ]

The SparkFun MAX31855K Thermocouple Breakout is a simple 14-bit resolution, SPI-compatible, serial interface thermocouple dig...

[ [\$20.95] ]

This breakout is designed to be used in conjunction with a k-type thermocouple such as [this one](https://www.sparkfun.com/products/251) shown below.

[![Thermocouple Type-K - Glass Braid Insulated (Bare Wire)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/3/00251-01a.jpg)](https://www.sparkfun.com/thermocouple-type-k-glass-braid-insulated-bare-wire.html)

### [Thermocouple Type-K - Glass Braid Insulated (Bare Wire)](https://www.sparkfun.com/thermocouple-type-k-glass-braid-insulated-bare-wire.html) 

[ SEN-00251 ]

36\" high temperature Type-K Thermocouple with glass braid insulation.

[ [\$17.95] ]

In this tutorial we\'re going to get you familiar with the workings of the MAX31855K. We\'ll go over how to hook it up to a our [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114), but you can use this breakout board with nearly limitless other options. Anything that can communicate over SPI will do. It can be as \'simple\' as a custom set of logic gates, most micros, or as complicated as yours server\'s motherboard. Make sure you are **using 3.3V**, or level shifting into the range 3.0V to 3.6V. We\'ll close the tutorial out with some example Arduino code.

### Suggested Materials

To follow along with this tutorial, you\'ll need the following:

[![Arduino Pro Mini 328 - 3.3V/8MHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/4/0/11114-01.jpg)](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html)

### [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/arduino-pro-mini-328-3-3v-8mhz.html) 

[ DEV-11114 ]

SparkFun\'s minimal design approach to Arduino. This is a 3.3V Arduino running the 8MHz bootloader.

[ [\$11.25] ]

[![SparkFun FTDI Basic Breakout - 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/9/5/8/09873-01a.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html)

### [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html) 

[ DEV-09873 ]

This is the newest revision of our \[FTDI Basic\](https://www.sparkfun.com/products/retired/8772). We now use a SMD 6-pin heade...

[ [\$18.50] ]

[![Thermocouple Type-K - Glass Braid Insulated (Bare Wire)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/3/00251-01a.jpg)](https://www.sparkfun.com/thermocouple-type-k-glass-braid-insulated-bare-wire.html)

### [Thermocouple Type-K - Glass Braid Insulated (Bare Wire)](https://www.sparkfun.com/thermocouple-type-k-glass-braid-insulated-bare-wire.html) 

[ SEN-00251 ]

36\" high temperature Type-K Thermocouple with glass braid insulation.

[ [\$17.95] ]

[![SparkFun Thermocouple Breakout - MAX31855K](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/8/7/13266-01.jpg)](https://www.sparkfun.com/sparkfun-thermocouple-breakout-max31855k.html)

### [SparkFun Thermocouple Breakout - MAX31855K](https://www.sparkfun.com/sparkfun-thermocouple-breakout-max31855k.html) 

[ SEN-13266 ]

The SparkFun MAX31855K Thermocouple Breakout is a simple 14-bit resolution, SPI-compatible, serial interface thermocouple dig...

[ [\$20.95] ]

Alternatively, you may use this thermocouple probe in conjunction with the thermocouple connector

[![Thermocouple Connector - PCC-SMP-K](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/9/7/6/13612-01.jpg)](https://www.sparkfun.com/thermocouple-connector-pcc-smp-k.html)

### [Thermocouple Connector - PCC-SMP-K](https://www.sparkfun.com/thermocouple-connector-pcc-smp-k.html) 

[ PRT-13612 ]

This Thermocouple Connector is perfect for bridging the gap between Type-K thermocouples with standard connectors with a PCB....

[ [\$10.95] ]

[![Thermocouple Type-K - Stainless Steel](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/0/9/13715-01.jpg)](https://www.sparkfun.com/thermocouple-type-k-stainless-steel.html)

### [Thermocouple Type-K - Stainless Steel](https://www.sparkfun.com/thermocouple-type-k-stainless-steel.html) 

[ SEN-13715 ]

This is a stainless steel, Type-K Thermocouple probe. A thermocouple works by taking two wires made of dissimilar metals, con...

[ [\$8.50] ]

- A 3.3V Arduino board such as our [3.3V Arduino Pro Mini](https://www.sparkfun.com/products/11114), or another microcontroller running at 3.3V or any with a [logic level converter](https://www.sparkfun.com/products/12009) or two.
- [Type K Thermocouple](https://www.sparkfun.com/products/251) - These can come in a variety of forms
- [MAX31855K Breakout Board](https://www.sparkfun.com/products/13266)

To connect the breakout to the microcontroller, you will likely want some [male headers](https://www.sparkfun.com/products/116), or you could use a few pieces of [wire](https://www.sparkfun.com/products/11375).

Additionally, you may want the following:

- [PCC-SMP-K Thermocouple Connector](https://www.sparkfun.com/products/13612) - Allows one to plug in a standard thermocouple.
- [Thermocouple with Connector](http://www.phidgets.com/products.php?product_id=3108_1) - K-type thermocouple

#### Tools

In order to get a good, solid, electrically-sound connection to the breakout boards, you\'ll need to solder to the pins. That means you\'ll need at least a [basic soldering iron](https://www.sparkfun.com/products/9507) as well as [solder](https://www.sparkfun.com/products/9163). Check out our [how to solder tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) for help, if this is you first time soldering.

You will also need the following supplies, but very well might already have them, or something equivalent laying around:

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

[![Wire Strippers - 22-30AWG](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/0/0/14762-Wire_Strippers-03.jpg)](https://www.sparkfun.com/products/14762)

### [Wire Strippers - 22-30AWG](https://www.sparkfun.com/products/14762) 

[ TOL-14762 ]

These are your basic, run-of-the-mill wire strippers from Techni-Tool with a comfortable grip making them an affordable optio...

**Retired**

[![Flush Cutters - Xcelite](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/0/3/6/14782-Flush_Cutters_-_Xcelite-02.jpg)](https://www.sparkfun.com/products/14782)

### [Flush Cutters - Xcelite](https://www.sparkfun.com/products/14782) 

[ TOL-14782 ]

These are simple flush cutters from Excelite that give you a way to cut leads very cleanly and close to the solder joint.

**Retired**

### Suggested Reading

These boards aren\'t too hard to use. If you\'ve done anything with Arduino before, you\'ll be prepared to work with the MAX31855K. If you\'re not exactly sure what this \"Arduino\" thing is, or if you\'re not familiar with the topics below, consider reading their tutorials:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/binary)

### Binary 

Binary is the numeral system of electronics and programming\...so it must be important to learn. But, what is binary? How does it translate to other numeral systems like decimal?

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

## Brief Theory of Operation

Roughly a couple hundred years ago, a man named Thomas Seebeck discovered the principal that thermocouples use. He noticed that if you take two wires made of dissimilar metals, connect them at the two ends, and make a temperature gradient between one end and the other, a voltage potential formed, and current flowed. One junction is held in the environment where the temperature of interest exists. This is known as the hot junction. The other junction is referred to as the cold junction.

[![thermocouple schematic](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermocouple_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermocouple_1.png)

*K-type thermocouple with cold junction spread for voltage measurement*

There are many types of thermocouples, which mainly differ by the types of metals used in the two wires. The most common general purpose thermocouple is **type K**. They are made out of chromel and alumel. These two alloys produce a potential of approximately 41.276 µV/°C. The MAX31855K uses this linear approximation to calculate the temperature.

[![k-type linear approximation of voltage](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermo_Eqn.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermo_Eqn.png)

The thermocouple's hot junction can be read from -200°C to +700°C with an accuracy of ±2°C. The cold junction is inside the MAX31855K and can only range from -20°C to +85°C while maintaining ±2°C accuracy. The MAX31855K constantly measures the temperature of the cold junction using an internal temperature-sensing diode. The internal 14-bit ADC uses the above equation, the voltage across the internal diode, and the amplified voltage of the thermocouple to solve for the hot junction temperature.

The calculated temperature is clocked out the **SO pin** in a SPI compatible format (half-duplex). When not feeding out data, this pin is tri-stated and will ignore any inputs from the master. A reading of **0b 0000 0000 0000** corresponds to **0°C**. Whereas **0b 01 1001 0000 0000** corresponds to a measured temperature of **+1600.00°C**, and **0b 11 1100 0001 1000** corresponds to a measured temperature of **-250.00°C**.

## Hardware Hookup

Now, let\'s dive in and see how to connect the Thermocouple Breakout.

### Solder/Wire Breakout

The first assembly step is creating a reliable, electrical connection from the breakout to your control board. You\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) either headers or wires to your breakout boards, deciding if straight or right-angle headers or wire work best for you.

If you\'re going to stick the breakout board into a breadboard, other prototyping board, or an Arduino Pro Mini, [straight male headers](https://www.sparkfun.com/products/116) might be the best choice. You might want to solder some right angle headers to the short edge of the Pro Mini so it\'s easy to plugin the FTDI Basic.

### Select a Power Source

The MAX31855K requires from +3.0V to +3.6V (+3.0V nominal). Since the MAX31855K only draws 1.5 mA maximum, **this tutorial will use D14 for power**. This lets use line up all of the SPI and power pins on one compact row. One could also power the board from any similar power supply.

### Connecting an Arduino

This hookup is fairly straightforward. We need so little power, we can connect the breakout to the sequential pins D10-A1. Since the MAX31855K is read-only, pin D11(MOSI) isn\'t connected on the breakout board & can be used for other functions such as SS for a second thermocouple board.Make your connections as follows:

  Thermocouple Breakout Pin   Arduino Pin   Function
  --------------------------- ------------- -----------------------------------------------
  GND                         A1            Ground
  VCC                         A0            Digital pin set to 3.3V in
  SCK                         D13           Clock
  SO                          D12           Serial Data Out
  NC                          NC (D11)      No Connect (can float on D11 for easy hookup)
  CS                          D10           Chip Select

\

[![Image of pins used in example code](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/ArduinoProMini.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/ArduinoProMini.png)

*Pins used in example code*

### Connecting a Type K Thermocouple

As covered in the [previous section](https://learn.sparkfun.com/tutorials/max31855k-thermocouple-breakout-hookup-guide#brief-theory-of-operation), potentials are formed due to a temperature gradient between junctions of dissimilar metals. We want to minimize the number of these junctions ideally down to two: the hot at the end of the thermocouple, and the cold at the MAX31855K. Every connection in addition to these can skew the reading. The breakout board is designed to accept a [standard thermocouple connector](https://www.sparkfun.com/products/13612), for convenience and compatibility with probes you may already own. These connectors aren\'t necessary, and you could solder a thermocouple directly into the through holes labeled \'**+**\' and \'**-**\'.

If you decide to solder the thermocouple directly to the breakout board, it is recommended that the thermocouple be mounted for strain relief to avoid breaking the thin wires. Notches have been provided in the PCB opposite the header for this purpose. One could wrap the thermocouple around this part of the board and squirt on some hot glue, or a zip-tie can be wrapped around the notches to hold the thermocouple. These zip-tie notches can also be used to attach the board to your project.

[![USB to FTDI to Pro Mini to MAX31855K breakout to k-type thermocouple Fritzing diagram](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/MAX31855K_Breakout_1.svg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/MAX31855K_Breakout_1.svg)

*What your circuit might look like if you solder the thermocouple directly to the PCB.*

If you opted for the connector, your circuit will look more like this:

[![USB to FTDI to Pro Mini to MAX31855K breakout to k-type thermocouple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/MAX31855K_Thermocouple_Digitizer_Hookup_Guide-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/MAX31855K_Thermocouple_Digitizer_Hookup_Guide-06.jpg)

*USB cable to an FTDI basic, into a Pro Mini, connected to MAX31855K w/ type K thermocouple*

For ease of use in this particular application, I chose to solder female headers to all holes on the top of the Arduino. I also soldered a male header to the bottom of the breakout board.

### Mounting Options

There is no *need* to mount the breakout board, but we have provided several ways to make it easy. Hot-glue and double-sided foam tape work, as always. We also provided notches for zip-ties. Grab a zip-tie, loop it around the PCB and any object, and pull it tight. There are also notched out holes for our standard [standoffs](https://www.sparkfun.com/products/10927) and [screws](https://www.sparkfun.com/products/10453). find or make two holes 20 mm apart, center-to-center, and screw the board down. These same notches can also be used for a zip-tie, some conductive thread, or let your imagination go wild!

[![Bottom of MAX21855K Thermocouple Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/MAX31855K_Thermocouple_Digitizer_Hookup_Guide-02_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/MAX31855K_Thermocouple_Digitizer_Hookup_Guide-02_1.png)

*Bottom view of PCB showing pin header and notches*

## Reading the Temperature

### Installing the Library

The library for this product is written to be compatible with Arduino IDE versions 1.5 and greater (1.6.x). The Arduino SPI library has changed in these versions, and our library relies on the more recent version. Since you are required to be running a recent version of the IDE we can use the handy new Library Manager feature. It is found in the \'Sketch\' menu under \'Include Library\', \'Manage Libraries\...\'

[![Manage libraries menu option](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/LibraryManager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/LibraryManager.png)

*Arduino 1.5+ Library Manager Menu Option*

When you open the Library Manager you will find a large list of libraries ready for one-click install. To find the library for this product, search for \'k type\' or \'digitizer\', and the library you want will likely be the only option. Click on that library, and the \'Install\' button will appear. Click that button, and the library should install automatically. When installation finishes, close the Library Manager.

[![Example library in library manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/LibInstall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/LibInstall.png)

*Library in the Library Manager, Ready to be Installed*

Now that the library is installed, an example sketch can be found in the \'Examples\' submenu. Open this example.

[![Example sketch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/example.png)

*Example Sketch*

    language:cplusplus
    /**************** MAX31855K_Thermocouple_Digitizer_Example.ino *****************
     *                                                                             *
     * MAX31855K Thermocouple Breakout Example Code                                *
     * brent@sparkfun.com                                                          *
     * March 26th 2015                                                             *
     * https://github.com/sparkfun/MAX31855K_Thermocouple_Digitizer                *
     *                                                                             *
     * Use the "serial monitor" window to read a temperature sensor.               *
     *                                                                             *
     * Circuit:                                                                    *
     * MAX31855K breakout attached to the following pins                           *
     *  SS:   pin 10                                                               *
     *  MOSI: pin 11 (NC)                                                          *
     *  MISO: pin 12                                                               *
     *  SCK:  pin 13                                                               *
     *  VCC:  pin 14                                                               *
     *  GND:  pin 15                                                               *
     *                                                                             *
     *                                                                             *
     * Development environment specifics:                                          *
     * 1.6.4                                                                       *
     * Arduino Pro Mini 328 3.3V/8MHz                                              *
     *                                                                             *
     * This code is beerware; if you see me (or any other SparkFun employee) at    *
     * the local, and you've found our code helpful, please buy us a round!        *
     * Distributed as-is; no warranty is given.                                    *
     ******************************************************************************/

    #include <SparkFunMAX31855k.h> // Using the max31855k driver
    #include <SPI.h>  // Included here too due Arduino IDE; Used in above header

    // Define SPI Arduino pin numbers (Arduino Pro Mini)
    const uint8_t CHIP_SELECT_PIN = 10; // Using standard CS line (SS)
    // SCK & MISO are defined by Arduiino
    const uint8_t VCC = 14; // Powering board straight from Arduino Pro Mini
    const uint8_t GND = 15;

    // Instantiate an instance of the SparkFunMAX31855k class
    SparkFunMAX31855k probe(CHIP_SELECT_PIN, VCC, GND);

    void setup() 

    void loop() 

      // Read the temperature in Celsius
      temperature = probe.readTempC();
      if (!isnan(temperature)) 

      // Read the temperature in Fahrenheit
      temperature = probe.readTempF();
      if (!isnan(temperature)) 

      // Read the temperature in Kelvin
      temperature = probe.readTempK();
      if (!isnan(temperature)) 

      // Read the temperature in Rankine
      temperature = probe.readTempR();
      if (!isnan(temperature)) 

      delay(750);
    }

*MAX31855K_Thermocouple_Digitizer_Example.ino*

### Code To Note

    language:cplusplus
    // Define SPI Arduino pin numbers (Arduino Pro Mini)
    const uint8_t CHIP_SELECT_PIN = 10; // Using standard CS line (SS)
    // SCK & MISO are defined by Arduiino
    const uint8_t VCC = 14; // Powering board straight from Arduino Pro Mini
    const uint8_t GND = 15;

This block of code, found above the setup function in the main sketch, is where you will configure the pins used to communicate with the MAX31855K breakout. *If you are using another board, or another power supply, you will want to edit these!*

**Warning:** Even if you don\'t plan to use D10 as the chip select pin, the Arduino SPI library will set it as an output anyway. If it ever becomes a low input the Arduino will turn into a SPI slave and cannot communicate with the MAX31855K.

`Serial.`[`begin`]`(`[`9600`]`); `

Before using the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux), you must call `Serial.begin()` to initialize it. 9600 is the \"baud rate\", or communications speed. When two devices are communicating with each other, both must be set to the same speed.

` `[`float`]` temperature = probe.readCJT(); `

All of the temperature reading functions return [floating point](http://www.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF) values. Floating point numbers are any number that isn\'t a whole integer number. \'1\' is and integer, while \'1.01\' is a floating point number. One special floating point number is NaN, or **N**ot **a** **N**umber. It represents things that aren\'t real numbers such as 0/0 (divide by zero is \'undefined\'). If a temperature reading function returns NAN it means that a real temperature wasn\'t read, and it\'s time to check your hardware.

### Running The Code

At this point the hardware should be correctly connected, the library should be installed, and the example sketch should be opened. Select the correct serial port in the \'Port\' submenu of the \'Tools\' menu. Click the \'Upload\' button, or sleect \'Upload\' in the \'Sketch\' menu. The code should compile and be uploaded to the Arduino. Once the code upload finishes verifying, open the serial monitor (found in the \'Tools\' menu).

### What You Should See

You should be able to read the temperature your thermocouple is detecting on the serial monitor in the Arduino IDE. If it isn\'t working, make sure you have assembled the circuit correctly and verified and uploaded the code to your board.

**Example of what you should see in the Arduino IDE's serial monitor:**

    language:cplusplus
    Beginning...
    CJT is (˚C): 25.94
    Temp[C]=26.50   Temp[F]=79.70   Temp[K]=299.65  Temp[R]=539.37
    ...
    ...
    ...

`Beginning...` only prints once to mark the beginning of the code running. The next two lines show the **C**old **J**unction **T**emperature (CJT), followed by the thermocouple measurement in a handful of common units. The CJT is the temperature of the breakout board, and the other temperature reading is that of the tip of your thermocouple. These two lines of temperature readings should be updated and reprinted every 3/4 of a second.

### Troubleshooting

#### Nothing Seems to Happen

This program has no outward indication it is working. To see the results, you must open the Arduino IDE\'s serial monitor.

#### Gibberish is Displayed

This happens because the serial monitor is receiving data at a different speed than expected. To fix this, click the pull-down box that reads \"\*\*\* baud\" and change it to \"9600 baud\".

#### Temperature Value is Unchanging

Try pinching the sensor with your fingers to heat it up or pressing a bag of ice against it to cool it down. Boiling water should be about 100°C, while ice should be about 0°C.