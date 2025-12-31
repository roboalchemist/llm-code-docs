# Source: https://learn.sparkfun.com/tutorials/spectral-triad-as7265x-hookup-guide

## Introduction

The [SparkFun Triad Spectroscopy Sensor](https://www.sparkfun.com/products/15050) is a powerful optical inspection sensor. Three AS7265x sensors are combined alongside a visible, UV, and IR LEDs to illuminate and test various surfaces for light spectroscopy.

[![SparkFun Triad Spectroscopy Sensor - AS7265x (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/3/9/3/15050-SparkFun_Triad_Spectroscopy_Sensor_-_AS7265x__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triad-spectroscopy-sensor-as7265x-qwiic.html)

### [SparkFun Triad Spectroscopy Sensor - AS7265x (Qwiic)](https://www.sparkfun.com/sparkfun-triad-spectroscopy-sensor-as7265x-qwiic.html) 

[ SEN-15050 ]

The SparkFun Triad Spectroscopy Sensor is a powerful optical inspection sensor with three sensors combined alongside LEDs us...

[ [\$69.95] ]

AMS has combined the power of three sensors to cover the measurement of light from 410nm to 940nm in 18 individual bands.

[![18 Channel Spectral Response from the Datasheet](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/Spectral_Detection_Frequencies.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/Spectral_Detection_Frequencies.jpg)

### What Can You Do with Light Spectroscopy?

It's an amazing field of study, and the SparkFun Triad brings what used to be prohibitively expensive equipment to the desktop. The AS7265x should not be confused with highly complex mass spectrometers, but the sensor array does give the user the ability to measure and characterize how different materials absorb and reflect 18 different frequencies of light.

### Required Materials

To follow along with this hookup guide, you will need one of the following Qwiic shields with an Arduino. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

**Note:** If you are looking to reduce the cost and avoid soldering headers to the Qwiic shield, try taking a look at the RedBoard Qwiic. It is essentially a RedBoard with Qwiic connector.\
\

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

You will also need a Qwiic cable to connect the shield to your AS726X, choose a length that suits your needs.

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/5/14429-Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/products/14429)

### [Qwiic Cable - 500mm](https://www.sparkfun.com/products/14429) 

[ PRT-14429 ]

This is a 500mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

## Hardware Overview

### Sensors

The Triad is made up of three sensors; AS72651 (UV), AS72652 (VIS), and AS72653 (NIR). The AS72651 communicates with the x2 and x3 sensors over a dedicated I^2^C bus (the AS72651 is the master, the AS72652 and AS72653 are slaves). The AS72651 combines its sensor data with the data from the x2 and x3 sensors and exposes the datums to the user as a single array of registers. The SparkFun AS7265x Spectral Library makes it seamless to read any of the 18 frequencies of sensing.

[![Three sensors arranged in a circle](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS72651_AS72652_AS72651_Spectroscopy_Triad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS72651_AS72652_AS72651_Spectroscopy_Triad.jpg)

#### EEPROM

These sensors from AMS are interesting in that they ship without firmware. The firmware to drive the system is loaded onto a 4Mbit EEPROM that is read by the AS72651 at power on.

[![EEPROM containing the Spectral Triad firmware](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Spectroscopy_Triad-EEPROM.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Spectroscopy_Triad-EEPROM.jpg)

### LEDs / Bulbs

The Triad contains a 5700k white LED, a 405nm UV LED, and a 875nm IR LED mounted alongside the sensors. These LEDs were chosen to illuminate the target with the largest swath of visible and invisible light. The LEDs are individually enabled with software configurable drive current.

[![Three LEDs on Spectral Triad](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-LEDs.jpg)

The board also has multiple ways for you to illuminate the object that you are trying to measure for a more accurate spectroscopy reading. If you aren't satisfied with the on-board, LEDs you can grab your own through hole incandescent bulbs. While you should find a bulb rated for 3.3V, a bulb rated for higher voltage, like 5V, will still work, but will not run as bright as it normally would with 5V. We've found that [Mouser](https://www.mouser.com/Optoelectronics/Lamps-Holders/Lamps/_/N-5g6r?P=1yzs1o7Z1z0wtyvZ1z0w0pvZ1yyg4qyZ1yyg4rqZ1z0ws3kZ1z0wa5iZ1yzubgzZ1yyg4r3Z1z0w8xrZ1z0yt45) is a good place to look for these. If you are going to go that route and use your own bulb, be sure to disable the onboard LED by removing cutting the jumper to any \'bulb\' footprint that is used. [Cut the jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#cutting-a-trace-between-jumper-pads) next to each bulb footprint to disconnect the LED from the controller IC and solder in a bulb. We use the word 'bulb' to indicate any DC device (limited to 100mA max) but this signal pin could also be used to activate a larger MOSFET or control device to activate a much larger current device.

[![Jumper to cut to enable an external bulb](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Spectroscopy_Triad-Bulbs_and_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Spectroscopy_Triad-Bulbs_and_Jumpers.jpg)

In addition to the illumination LEDs, there is a power LED and a status LED. The blue status LED indicates various states of the AS72651 sensor and can be disabled through the SparkFun library. The red power LED is provided to indicate the board is properly energized. If the red light is interfering with readings it can be disabled by cutting the neighboring jumper.

[![Jumper to cut to disable the power LED](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-Power_and_Stat_LEDs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-Power_and_Stat_LEDs.jpg)

### I^2^C / Qwiic Interface

The [Qwiic connectors](https://www.sparkfun.com/qwiic) provide a quick and easy way to connect the Triad over I^2^C. Alternatively, you can [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) to the four pins: GND/3.3V/SDA/SCL. The sensors are 3.3V compatible so don't use with a 5V Arduino Uno without proper conversion (use the [Qwiic shield](https://www.sparkfun.com/products/14352) instead!). If you\'re using a 3.3V development platform that doesn\'t have a Qwiic connector, consider using the [Qwiic Breadboard Cable](https://www.sparkfun.com/products/14425).

[![Qwiic connectors and I2C jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-I2C_Connections.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-I2C_Connections.jpg)

### Serial UART Interface

⚡ **Warning:** You should only use a **3.3V** USB-to-serial converter when connecting to the serial port. Using a 5V USB-to-serial converter may damage the components on the board.\
\

[![SparkFun FTDI Basic Breakout - 3.3V](https://cdn.sparkfun.com/r/140-140/assets/parts/3/9/5/8/09873-01a.jpg)](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html)

### [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-3-3v.html) 

[ DEV-09873 ]

This is the newest revision of our \[FTDI Basic\](https://www.sparkfun.com/products/retired/8772). We now use a SMD 6-pin heade...

[ [\$18.50] ]

[![SparkFun Beefy 3 - FTDI Basic Breakout](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/7/6/13746-01.jpg)](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html)

### [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/sparkfun-beefy-3-ftdi-basic-breakout.html) 

[ DEV-13746 ]

This is SparkFun Beefy 3 FTDI Basic Breakout for the FTDI FT231X USB to serial IC. The pinout of this board matches the FTDI ...

[ [\$18.95] ]

[![SparkFun Serial Basic Breakout - CH340G](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/8/8/14050-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html)

### [SparkFun Serial Basic Breakout - CH340G](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340g.html) 

[ DEV-14050 ]

The SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G IC from WCH.

[ [\$9.25] ]

A serial interface is also available for those users who prefer using AT commands. Please refer to the [AS7265x datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Datasheet.pdf) for a full list of commands. To enable the serial interface (and disable the I^2^C interface) you must modify two jumpers:

1.  The I^2^C jumper on the front of the board must be opened to remove the pull-up resistors from the TX and RX lines.
2.  The *JP2* on the rear of the board must be closed with a solder jumper.

[![Serial Jumpers needing modification](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_Jumpers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_Jumpers.jpg)

Next, solder in a 6-pin [right angle male header](https://www.sparkfun.com/products/553) to the serial port.

[![Serial Pins and interface jumper on SparkFun Triad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_Connection1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_Connection1.jpg)

The [SparkFun Serial Basic](https://www.sparkfun.com/products/14050) connects directly to the Triad. The Serial Basic is set to 3.3V by default but if you're using a different board, be sure it provides 3.3V on VCC and uses 3.3V logic signals.

[![Serial Basic connected to the serial connector on SparkFun Triad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-Serial_Attached.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy_Triad-Serial_Attached.jpg)

The serial interface operates at **115200**. To test the connection, open [TeraTerm](https://learn.sparkfun.com/tutorials/terminal-basics/tera-term-windows) or your favorite terminal and connect to the Serial Basic. Send the command `AT` and look for an `OK` response. You're all set! Check the [AS7265x datasheet]() for a full list of AT commands.

[![Ok shown on the terminal window](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_OK.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/SparkFun_AS7265x_Spectroscopy-Serial_OK.jpg)

## AS7265x Arduino Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We've written an Arduino library to make reading the Triad a breeze. The easiest way to install the library is by searching **SparkFun Spectral Triad** within the Arduino library manager. You can also manually install the [AS7265x library](https://github.com/sparkfun/SparkFun_AS7265x_Arduino_Library) by downloading a zip:

[Download the SparkFun AS7265X Library (ZIP)](https://github.com/sparkfun/SparkFun_AS7265x_Arduino_Library/archive/main.zip)

Example 1 provided with the library demonstrates how to read all 18 channels. The higher examples demonstrate all the features available through the SparkFun library on the Spectral Triad:

- **Example 1** - Basic readings of all 18 channels
- **Example 2** - Controlling the onboard LEDs
- **Example 3** - Changing the many settings on the AS7652x
- **Example 4** - Output the raw sensor readings without calibration adjustment
- **Example 5** - Setting the sensor up for maximum read speed
- **Example 6** - Reading the temperatures of the three ICs
- **Example 7** - Reading the various hardware and firmware versions

Below are the various functions that can be called from the library. Most of these functions are demonstrated in the examples so we recommend you go through each example first.

- **`boolean begin(TwoWire &wirePort = Wire);`** \-- Inits the sensor with default settings. Optional pass of wire port.

- **`boolean isConnected();`** \-- Returns true if the sensor is detected on the I2C bus

- **`boolean dataAvailable();`** \-- Returns true when data is available

- **`uint8_t getTemperature(uint8_t deviceNumber = 0);`** \-- Get temp in C of the master IC

- **`float getTemperatureAverage();`** \-- Get average of all three ICs

- **`void takeMeasurements();`** \-- Tell sensor to take one-shot measurement

- **`void takeMeasurementsWithBulb();`** \-- Take one-shot measurement with all three LEDs illuminated

- **`float getCalibratedA();` to `getCalibratedW();`** \-- Returns the various calibration data

- **`uint16_t getA();` to `getW();`** \-- Get the various raw readings

- **`void enableIndicator();`** \-- Enable the blue status LED

- **`void disableIndicator();`** \-- Disable the status LED. Handy when taking snesitive readings

- **`void enableBulb(uint8_t device);`** \-- Turn on a given LED. 0 = White, 1 = IR, 2 = UV

- **`void disableBulb(uint8_t device);`** \-- Turn off a given LED

- **`void setGain(uint8_t gain);`** \-- 1 to 64x

- **`void setMeasurementMode(uint8_t mode);`** \-- 4 channel, other 4 channel, 6 chan, or 6 chan one shot

- **`void setIntegrationCycles(uint8_t cycleValue);`** \-- 2.78ms to 711ms

- **`void setBulbCurrent(uint8_t current, uint8_t device);`** \-- 12.5mA to 100mA

- **`void setIndicatorCurrent(uint8_t current);`** \-- 1 to 8mA

- **`void enableInterrupt();`** \-- Enable the interrupt pin (active low)

- **`void disableInterrupt();`**

- **`void softReset();`** \-- Reset the device via software

- **`uint8_t getDeviceType();`** \-- Should return 0x41

- **`uint8_t getHardwareVersion();`** \-- Should return 0x40

- **`uint8_t getMajorFirmwareVersion();`** \-- Returns the current firmware version, currently 0x0C

- **`uint8_t getPatchFirmwareVersion();`**

- **`uint8_t getBuildFirmwareVersion();`**

## Example: Taking A Banana Reading

Let\'s get the Triad hooked up over Qwiic and begin illuminating a target to take some readings. Using a [BlackBoard](https://www.sparkfun.com/products/14669) and a [Qwiic Cable](https://www.sparkfun.com/products/14427) we\'re able to attach to the Triad quickly without soldering. Let\'s open and use Example 2 from the library so that the Triad will take all 18 readings while illuminating the target.

Once you have a series of readings, plug them into your favorite graph utility. For our purposes, we like to use Google spreadsheets. You can paste the comma delimited output from the sketch directly into a sheet. Once there, drop the small menu down and select *Split text to columns*.

[![Splitting text to columns](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/Sensor-Output-SplittingInGoogleDocs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/Sensor-Output-SplittingInGoogleDocs.jpg)

You can access our [data here](https://docs.google.com/spreadsheets/d/1A5W0ep32b5e5qerUcy06DxL7Uc4Sz7UOMYw5aUDT5PM/edit?usp=sharing). The graph of the 18 frequencies is pretty neat!

[![Graph of various items spectral response](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/Sensor-Output-Graph.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/Sensor-Output-Graph.jpg)

Now that we have a baseline we can take a reading from an unknown thing (in this case, Uranium ore we had sitting around used for testing the [Pocket Geiger Counter](https://www.sparkfun.com/products/14209)). Note that the distance to your sample will cause the amplitude of the readings to increase or decrease. We took our readings holding the Triad about **1 inch away** from the surface of the target sample but a 3D printed shroud would remove background illumination and remove read distance variations.

As you can see the unknown sample follows closely to the Uranium Ore signature.

[![Reading an unknown sample](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/0/Sensor-Output-Graph-Unknown.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/Sensor-Output-Graph-Unknown.jpg)

*Science!* The Triad is a fantastic tool that will have you looking around your house for interesting things to measure.