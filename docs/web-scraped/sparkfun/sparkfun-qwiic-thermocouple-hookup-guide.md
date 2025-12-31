# Source: https://learn.sparkfun.com/tutorials/sparkfun-qwiic-thermocouple-hookup-guide

## Introduction

How many times have you asked yourself, \"Self? How can I measure both the ambient temperature as well as that thing over there, AND set temperature limits to trigger interrupts so I don\'t have to constantly poll over I^2^C? And how can I make it as easy as possible?\" Well, we\'ve got your answer. SparkFun has 2 new thermocouple amplifier boards - the [SparkFun Qwiic Thermocouple - PCC](https://www.sparkfun.com/products/16294) and the [SparkFun Qwiic Thermocouple - Screw Terminals](https://www.sparkfun.com/products/16295); both of which do all of the above with a resolution of 0.0625°C, and an accuracy of ±1.5°C (worst-case). The boards come ready to accept a K-type thermocouple, which gives a temperature range of -200°C to 1350°C. Additionally, the MCP9600 has four onboard temperature alerts for those interrupt triggers as well as the ability to enter alternate operation modes in order to save power.

Let\'s dig in and see how all this works!

[![SparkFun Qwiic Thermocouple Amplifier - MCP9600 (PCC Connector)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/9/8/3/16294-Qwiic_Thermocouple_Amplifier_-_MCP9600_-_PCC_Connector-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-thermocouple-amplifier-mcp9600-pcc-connector.html)

### [SparkFun Qwiic Thermocouple Amplifier - MCP9600 (PCC Connector)](https://www.sparkfun.com/sparkfun-qwiic-thermocouple-amplifier-mcp9600-pcc-connector.html) 

[ SEN-16294 ]

The MCP9600 Breakout is a high accuracy Thermocouple Amplifier equipped with a PCC Connector and I2C interface, accessed over...

[ [\$39.95] ]

[![SparkFun Qwiic Thermocouple Amplifier - MCP9600 (Screw Terminals)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/9/8/5/16295-Qwiic_Thermocouple_Amplifier_-_MCP9600_-_Screw_Terminals-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-thermocouple-amplifier-mcp9600-screw-terminals.html)

### [SparkFun Qwiic Thermocouple Amplifier - MCP9600 (Screw Terminals)](https://www.sparkfun.com/sparkfun-qwiic-thermocouple-amplifier-mcp9600-screw-terminals.html) 

[ SEN-16295 ]

The MCP9600 Breakout is a high accuracy Thermocouple Amplifier equipped with screw terminals and I2C interface, accessed over...

[ [\$30.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing. If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/processor-interrupts-with-arduino)

### Processor Interrupts with Arduino 

What is an interrupt? In a nutshell, there is a method by which a processor can execute its normal program while continuously monitoring for some kind of event, or interrupt. There are two types of interrupts: hardware and software interrupts. For the purposes of this tutorial, we will focus on hardware interrupts.

## A Brief Theory of Operation

Thermocouples are fairly ubiquitous, being used in everything from industrial kilns and diesel engines to pilot light sensors and thermostats in your home or office. Let\'s take a brief moment to go over how they work.

Roughly a couple hundred years ago, a man named Thomas Seebeck discovered the principal that thermocouples use. He noticed that if you take two wires made of dissimilar metals, connect them at the two ends, and make a temperature gradient between one end and the other, a voltage potential formed and current flowed. One junction is held in the environment where the temperature of interest exists. This is known as the hot junction. The other junction is referred to as the cold junction.

[![thermocouple schematic](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermocouple_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermocouple_1.png)

*K-type thermocouple with cold junction spread for voltage measurement*

There are many types of thermocouples, which mainly differ by the types of metals used in the two wires. The most common general purpose thermocouple is **type K**. They are made out of chromel and alumel. These two alloys produce a potential of approximately 41.276 µV/°C, and voltage out can be calculated using the equation below.

[![k-type linear approximation of voltage](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermo_Eqn.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/thermo_Eqn.png)

K-type thermocouples can read between from −200 °C to +1350 °C (−330 °F to +2460 °F) and are fairly stable.

## Hardware Overview

### MCP9600

At the heart of this board is the MicroChip Technology Inc MCP9600 Thermocouple EMF to Temperature Converter. Inside this chip are two temperature sensors, one for the thermocouple itself (the hot junction) and one for the chip itself (the cold junction). In addition, the MCP9600 has four onboard temperature alerts that allow you to set a temperature limit to trigger an interrupt when the temperature reaches a certain value. This frees up your microcontroller and your I^2^C bus. The MCP9600 can also be put into alternate operation modes in order to save power. The sensor supports a burst mode, where it will take a specifiable number of samples, return the results, and then go to sleep. More information can be found in the [MCP9600 Datasheet (PDF)](https://cdn.sparkfun.com/assets/9/0/b/0/3/MCP9600_Datasheet.pdf).

  [![MCP9600 Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_MCP9600-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_MCP9600-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_MCP9600-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_MCP9600-HiRes.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                    *Screw Terminal*

### Power

Ideally, power will be supplied via the Qwiic connectors on either side of the board. Alternatively, power can be supplied through the header along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **2.7**-**5.5V**.

⚡ **Note:** There is no onboard voltage regulation on either of these boards. If you choose to provide power via the plated through holes, ensure that your voltage does not exceed **5.5V**.

  [![Top View of Input Power](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Power-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Power-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Power-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Power-HiRes.jpg)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                      *Screw Terminal*

### Qwiic Connectors

There are two Qwiic connectors on either end of the SparkFun Qwiic Thermocouple boards to provide power and I^2^C connectivity simultaneously. The I^2^C address of the board is **0x60 by default** , but has 7 other addresses the board can be configured to use.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Qwiic-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Qwiic-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Qwiic-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Qwiic-HiRes.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                  *Screw Terminal*

### I^2^C Pins

The I^2^C pins break out the functionality of the Qwiic connectors. Depending on your application, you can connect to these pins via the plated through holes for SDA and SCL.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_I2C-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_I2C-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_I2C-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_I2C-HiRes.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                              *Screw Terminal*

### Alert Pins

The Qwiic Thermocouple Amplifier has four configurable alert pins. Each alert can be configured for:

- Temperature
- Hysteresis
- Junction Alert - hot (thermocouple) or cold (internal MCP9600 sensor)
- Edge - from cold to hot, or from hot to cold
- Logic Level - active high or active low
- Alert Mode - interrupt or comparator

Check out the Temperature Alerts section of the [Arduino library](https://learn.sparkfun.com/tutorials/sparkfun-qwiic-thermocouple-hookup-guide#software-setup-and-programming) function descriptions to learn more about how to use the alert pins.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_INTPins-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_INTPins-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_INTPins-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_INTPins-HiRes.jpg)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                      *Screw Terminal*

### Jumpers

#### I^2^C Jumper

These boards are both equipped with pull-up resistors. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted below.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_I2CJumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_I2CJumper-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_I2CJumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_I2CJumper-HiRes.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                          *Screw Terminal*

#### ADDR Jumper

The MCP9600 uses an analog voltage to set the I^2^C address. By default, the ADDR jumper pulls the address pin low, which gives the board a **default address of 0x60**. Cutting the jumper pulls the address pin high through a 10K resistor, which will change the address to 0x67.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_ADDRJumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_ADDRJumper-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_ADDRJumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_ADDRJumper-HiRes.jpg)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                            *Screw Terminal*

For addresses other than 0x67, a resistor will need to be soldered. Refer to the table below for the resistor value and corresponding address.

  **Address**   **Resistor (kΩ)**
  ------------- -------------------
  0x60          0
  0x61          2.2
  0x62          4.3
  0x63          7.5
  0x64          13
  0x65          22
  0x66          43
  0x67          N/A

\
\
Resistor location on each board:

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Resistor-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_Resistor-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Resistor-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_Resistor-HiRes.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                        *Screw Terminal*

#### LED Jumper

Wanna turn off that pesky power LED? Cut this jumper.

  [![I2C Input Highlight](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_LEDJumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_PCC_LEDJumper-HiRes.jpg)   [![Bottom View of Qwiic Connectors](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_LEDumper-HiRes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/16294-Qwiic_Thermocouple_MCP9600_Screw_LEDumper-HiRes.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  *PCC Connector*                                                                                                                                                                                                                                                          *Screw Terminal*

### Board Dimensions

Feel free to click on either of the images below for a closer look!

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/SparkFun_Qwiic_Thermocouple_Amplifier_PCC.png "Qwiic Thermocouple Amplifier PCC")](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/SparkFun_Qwiic_Thermocouple_Amplifier_PCC.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/SparkFun_Qwiic_Thermocouple_Amplifier_Screw_Terminals.png "Qwiic Thermocouple Amplifier Screw Terminals")](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/SparkFun_Qwiic_Thermocouple_Amplifier_Screw_Terminals.png)\

  *Qwiic Thermocouple Amplifier PCC*                                                                                                                                                                                                                                 *Qwiic Thermocouple Amplifier Screw Terminals*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Hardware Hookup

For this tutorial, we\'ll use the Amplifier board with the PCC connector. Grab your Qwiic cable and plug one end into the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) and the other end into the Thermocouple Amplifier.

[![image of redboard with qwiic cable plugged into thermocouple qwiic connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/Thermocouple_Images-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/Thermocouple_Images-02.jpg)

Then you can connect the K-type Thermocouple into the PCC connector as so:

[![plugging in the thermocouple to the amplifier board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/Thermocouple_Images-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/Thermocouple_Images-03.jpg)

*Click for a closer view.*

Plug in the RedBoard Qwiic When you are all set up, you should have something that looks like this:

[![Picture of board, plugged into a redboard, plugged into a K-type thermocouple](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/Thermocouple_Image.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/Thermocouple_Image.jpg)

*Click for a closer view.*

## Software Setup and Programming

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.10. Otherwise, make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the Qwiic Thermocouple. You can obtain this library through the Arduino Library Manager by searching for **MCP9600**. Find the one written by **SparkFun Electronics** and install the latest version. If you prefer downloading libraries manually, you can grab them from the [GitHub Repository](https://github.com/sparkfun/SparkFun_MCP9600_Arduino_Library).

[Download the SparkFun MCP9600 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MCP9600_Arduino_Library/archive/master.zip)

### MCP9600 Library Overview

#### Device Status

- **`bool begin( uint8_t address = DEV_ADDR, TwoWire &wirePort = Wire )`** - Sets device I2C address to a user-specified address, over whatever port the user specifies. If left blank, the default address 0x60 is used on the Wire bus.
- **`bool available( void )`** - Also referred to as the data ready bit, returns true if the thermocouple (hot) junction temperature has been updated since last checked.
- **`bool isConnected( void )`** - Returns true if the thermocouple will acknowledge over I2C, and false otherwise.
- **`uint16_t deviceID( void )`** - Returns the contents of the device ID register. The upper 8 bits are constant, but the lower contain revision data.
- **`bool checkDeviceID( void )`** - Returns true if the constant upper 8 bits in the device ID register are what they should be according to the datasheet.
- **`bool resetToDefaults( void )`** - Resets all device parameters to their default values. Returns 1 if there was an error, 0 otherwise.

#### Sensor measurements

- **`float getThermocoupleTemp( bool units = true )`** - Returns the thermocouple temperature, and clears the data ready bit. Set units to true for Celcius (default), or false for freedom units (Fahrenheit).
- **`float getAmbientTemp( bool units = true )`** - Returns the ambient (IC die) temperature. Set units to true for Celcius (default), or false for freedom units (Fahrenheit).
- **`float getTempDelta( bool units = true )`** - Returns the difference in temperature between the thermocouple and ambient junctions. Set units to true for Celcius (default), or false for freedom units (Fahrenheit).
- **`signed long getRawADC( void )`** - Returns the raw contents of the ADC register.
- **`bool isInputRangeExceeded( void )`** - Returns true if the MCP9600\'s EMF range has been exceeded, and false otherwise.

#### Measurement configuration

- **`bool setAmbientResolution( Ambient_Resolution res )`** - Changes the resolution on the cold (ambient) junction, for either 0.0625 or 0.25 degree C resolution. Lower resolution reduces conversion time.
- **`Ambient_Resolution getAmbientResolution( void )`** - Returns the resolution on the cold (ambient) junction, for either 0.0625 or 0.25 degree C resolution. Lower resolution reduces conversion time.
- **`bool setThermocoupleResolution( Thermocouple_Resolution res )`** - Changes the resolution on the hot (thermocouple) junction, for either 12, 14, 16, or 18-bit resolution. Lower resolution reduces conversion time.
- **`Thermocouple_Resolution getThermocoupleResolution( void )`** - Returns the resolution on the hot (thermocouple) junction, for either 12, 14, 16, or 18-bit resolution. Lower resolution reduces conversion time.
- **`uint8_t setThermocoupleType( Thermocouple_Type type )`** - Changes the type of thermocouple connected to the MCP9600. Supported types are K, J, T, N, S, E, B, R.
- **`Thermocouple_Type getThermocoupleType( void )`** - Returns the type of thermocouple connected to the MCP9600 as found in its configuration register. Supported types are K, J, T, N, S, E, B, R.
- **`uint8_t setFilterCoefficient( uint8_t coefficient )`** - Changes the weight of the on-chip exponential moving average filter. Set this to 0 for no filter, 1 for minimum filter, and 7 for maximum filter.
- **`uint8_t getFilterCoefficient( void )`** - Returns the weight of the on-chip exponential moving average filter.
- **`bool setBurstSamples( Burst_Sample samples )`** - Changes the amount of samples to take in burst mode. Returns 0 if set sucessfully, 1 otherwise.
- **`Burst_Sample getBurstSamples( void )`** - Returns the amount of samples to take in burst mode, according to the device\'s configuration register.
- **`bool burstAvailable( void )`** - Returns true if all the burst samples have been taken and the results are ready. Returns false otherwise.
- **`bool startBurst( void )`** - Initiates a burst on the MCP9600.
- **`bool setShutdownMode( Shutdown_Mode mode )`** - Changes the shutdown \"operating\" mode of the MCP9600. Configurable to Normal, Shutdown, and Burst. Returns 0 if properly set, 1 otherwise.
- **`Shutdown_Mode getShutdownMode( void )`** - Returns the shutdown \"operating\" mode of the MCP9600. Configurable to Normal, Shutdown, and Burst.

#### Temperature Alerts

- **`bool configAlertTemp( uint8_t number, float temp )`** - Configures the temperature at which to trigger the alert for a given alert number.
- **`bool configAlertJunction( uint8_t number, bool junction )`** - Configures the junction to monitor the temperature of to trigger the alert. Set to zero for the thermocouple (hot) junction, or one for the ambient (cold) junction.
- **`bool configAlertHysteresis( uint8_t number, uint8_t hysteresis )`** - Configures the hysteresis to use around the temperature set point, in degrees Celcius.
- **`bool configAlertEdge( uint8_t number, bool edge )`** - Configures whether to trigger the alert on the rising (cold -\> hot) or falling (hot -\> cold) edge of the temperature change. Set to 1 for rising, 0 for falling.
- **`bool configAlertLogicLevel( uint8_t number, bool level )`** - Configures whether the hardware alert pin is active-high or active-low. Set to 1 for active-high, 0 for active-low.
- **`bool configAlertMode( uint8_t number, bool mode )`** - Configures whether the MCP9600 treats the alert like a comparator or an interrrupt. Set to 1 for interrupt, 0 for comparator. More information is on pg. 34 of the datasheet.
- **`bool configAlertEnable( uint8_t number, bool enable )`** - Configures whether or not the interrupt is enabled or not. Set to 1 to enable, or 0 to disable.
- **`bool clearAlertPin( uint8_t number )`** - Clears the interrupt on the specified alert channel, resetting the value of the pin.
- **`bool isTempGreaterThanLimit( uint8_t number )`** - Returns true if the interrupt has been triggered, false otherwise

## Example Code

Once you\'ve installed the library, you should be able to find the examples in Arduino under **File** \> **Examples** \> **SparkFun MCP9600 Thermocouple Library**.

[![MCP9600 Arduino Examples](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/ArduinoMCP9600Examples-Cropped.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/ArduinoMCP9600Examples-Cropped.png)

### Example 1: Basic Readings

While all of the examples are well commented, let\'s quickly run through example 1 just to get your feet wet. The best part? It\'s pretty much plug and play. So go ahead and open up Example 1, or alternatively, copy and paste the code below into an Arduino window:

    language:c
    /*
      Temperature Measurements with the MCP9600 Thermocouple Amplifier
      By: Fischer Moseley
      SparkFun Electronics
      Date: July 8, 2019
      License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware License).

      This example outputs the ambient and thermocouple temperatures from the MCP9600 sensor.

      Hardware Connections:
      Attach the Qwiic Shield to your Arduino/Photon/ESP32 or other
      Plug the sensor onto the shield
      Serial.print it out at 115200 baud to serial monitor.
    */

    #include <SparkFun_MCP9600.h>
    MCP9600 tempSensor;

    void setup()
        else 

        //check if the Device ID is correct
        if(tempSensor.checkDeviceID())
        else 
    }

    void loop()
        delay(20); //don't hammer too hard on the I2C bus
    }

#### What You Should See

Open up the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and make sure your baud rate is 115200. You should see something like the image below. If you move the hot junction (ie, the thermocouple wand) closer to a heat source, you should see the Thermocouple temperature go up.

[![Serial Monitor Output for Example 1](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/1/0/Thermocouple_Output.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/1/0/Thermocouple_Output.png)

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.