# Source: https://learn.sparkfun.com/tutorials/tmp102-digital-temperature-sensor-hookup-guide

## Introduction

The [TMP102](https://www.sparkfun.com/products/13314) is an easy-to-use digital temperature sensor from Texas Instruments. While some temperature sensors use an analog voltage to represent the temperature, the TMP102 uses the I^2^C bus of the Arduino to communicate the temperature.

[![SparkFun Digital Temperature Sensor Breakout - TMP102](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/9/3/13314-01a.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html)

### [SparkFun Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html) 

[ SEN-13314 ]

The TMP102 is an easy-to-use digital temperature sensor from Texas Instruments. The TMP102 breakout allows you to easily inco...

[ [\$5.95] ]

### Required Materials

To follow along with this hookup guide, you will need the following:

### Suggested Reading

Before getting started, you may find the following links useful:

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

### How to Use a Breadboard 

Welcome to the wonderful world of breadboards. Here we will learn what a breadboard is and how to use one to build your very first circuit.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/temperature-sensor-comparison)

### Temperature Sensor Comparison 

A comparison of analog and digital temperature sensors. Which is better?

## Board Overview

Let\'s go over the TMP102 Breakout in detail.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/0/TMP102-TOP.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/0/TMP102-TOP.jpg)

#### TMP102 Details:

- Uses the I^2^C interface
- 12-bit, 0.0625°C resolution
- Typical temperature accuracy of ±0.5°C
- Supports up to four TMP102 sensors on the I^2^C bus at a time

### Pull-up Resistors

This breakout board has built-in 4.7 kΩ pull up resistors for I^2^C communications. If you\'re hooking up multiple I^2^C devices on the same bus, you may want to disable/enable the pull-up resistors for one or more boards. On the TMP102, the pull-ups are enabled by default. To disable them, simply use a [hobby knife](https://www.sparkfun.com/products/9200) to cut the traces connecting the left and right pads of the jumper labeled **I2C PU** on the back of the board. This will disconnect the resistors from VCC and from the I^2^C bus.

## Hardware Connections

### Connecting the TMP102 to an Arduino

Wiring the TMP102 is very easy! We recommend [soldering](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) six [male headers](https://www.sparkfun.com/products/116) to the breakout board. You can also solder [wires](https://www.sparkfun.com/products/11375) to fit your application\'s needs.

### Power

This board runs from **1.4V to 3.6V**. Be sure to power the board from the 3.3V pin! I^2^C uses an open drain signaling, so there is no need to use level shifting; the 3.3V signal will work to communicate with the Arduino and will not exceed the maximum voltage rating of the pins on the TMP102.

### Connections to the Arduino

The TMP102 breakout board has six pins, however we\'ll only be using five of the pins in today\'s example. We\'ll be connecting VCC and GND to the normal power pins, two data lines for I^2^C communication, and one digital pin to see if there is an alert. If you\'re using a newer board that has SDA and SCL broken out, you can connect the SDA and SCL pins directly to those pins. If you\'re using an older board, SDA and SCL are pins A4 and A5 respectively.

- VCC → 3.3V
- GND → GND
- SDA → SDA/A4
- SCL → SCL/A5
- ALT → A3

This would looks something like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/0/TMP102_Fritzing_Hookup_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/0/TMP102_Fritzing_Hookup_1.jpg)

The only pin that we aren\'t using is **ADD0**, this pin is used to change the address of the TMP102. If you\'re using multiple TMP102s or another device that uses that address, you\'ll want to use this pin to change the address. The **default address is 0x48**. You can change the address by cutting the ADD0 jumper on the back of the board and connecting an external jumper wire to the following pins:

- VCC → 0x49
- SDA → 0x4A
- SCL → 0x4B

## TMP102 Library and Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide). If you have not previously installed an Arduino library, please check out our [installation guide](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

SparkFun has written a library to work with the TMP102. You can obtain this library through the Arduino Library Manager by searching for **SparkFun TMP102**. If you prefer downloading libraries manually, you can grab it from the [GitHub Repository](https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library).

[TMP102 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library/archive/master.zip)

Once the library is installed, open Arduino, and expand the examples menu. You should see the TMP102 example.

[![Example from Library](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/0/TMP102_Library_Example_Selection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/4/0/TMP102_Library_Example_Selection.jpg)

### TMP102 Library Overview

#### Main functions

These are functions used to read settings and temperatures from the sensor.

`bool begin( uint8_t deviceAddress, TwoWire &wirePort )` - Takes the device address and I^2^C bus as optional inputs. If left blank, this function uses the default address 0x48, and uses the Wire bus.

`float readTempC( void )` - Returns the current temperature in Celsius.

`float readTempF( void )` - Returns the current temperature in Fahrenheit.

`float readLowTempC( void )` - Reads T_LOW register in Celsius.

`float readHighTempC( void )` - Reads T_HIGH register in Celsius.

`float readLowTempF( void )` - Reads T_LOW register in Fahrenheit.

`float readHighTempC( void )` - Reads T_HIGH register in Fahrenheit.

`void sleep( void )` - Put TMP102 in low power mode (\<0.5 uA).

`void wakeup( void )` - Return to normal power mode (\~10 uA). When the sensor powers up, it is automatically running in normal power mode, and only needs to be used after `sleep()` is used.

`bool alert( void )` - Returns the state of the Alert register. The state of the register is the **same as the alert pin**.

`void setLowTempC(float temperature)` - Sets T_LOW (in Celsius) alert threshold.

`void setHighTempC(float temperature)` - Sets T_HIGH (in Celsius) alert threshold.

`void setLowTempF(float temperature)` - Sets T_LOW (in Fahrenheit) alert threshold.

`void setHighTempF(float temperature)` - Sets T_HIGH (in Fahrenheit) alert threshold.

`void setConversionRate(uint8_t rate)` - Sets the temperature reading conversion rate. 0: 0.25Hz, 1: 1Hz, 2: 4Hz (default), 3: 8Hz.

`void setExtendedMode(bool mode)` - Enable or disable extended mode. 0: disabled (-55C to +128C), 1: enabled (-55C to +150C).

`void setAlertPolarity(bool polarity)` - Sets the polarity of the alert. 0: active LOW, 1: active HIGH

`void setFault(uint8_t faultSetting)` - Sets the number of consecutive faults before triggering alert. 0: 1 fault, 1: 2 faults, 2: 4 faults, 3: 6 faults.

`void setAlertMode(bool mode)` - Sets the type of alert. 0: Comparator Mode (Active from when temperature \> T_HIGH until temperature \< T_LOW), 1: Thermostat mode (Active from when temperature \> T_HIGH until any read operation occurs.

### Example Code

Once the library is installed, open the example code to get started! Make sure to select your board and COM port before hitting upload to begin experimenting with the temperature sensor.

    language:c
    /******************************************************************************
    TMP102_example.ino
    Example for the TMP102 I2C Temperature Sensor
    Alex Wende @ SparkFun Electronics
    April 29th 2016
    ~

    This sketch configures the TMP102 temperature sensor and prints the
    temperature and alert state (both from the physical pin, as well as by
    reading from the configuration register.

    Resources:
    Wire.h (included with Arduino IDE)
    SparkFunTMP102.h

    Development environment specifics:
    Arduino 1.0+

    This code is beerware; if you see me (or any other SparkFun employee) at
    the local, and you've found our code helpful, please buy us a round!

    Distributed as-is; no warranty is given.   
    ******************************************************************************/

    // Include the SparkFun TMP102 library.
    // Click here to get the library: http://librarymanager/All#SparkFun_TMP102

    #include <Wire.h> // Used to establied serial communication on the I2C bus
    #include <SparkFunTMP102.h> // Used to send and recieve specific information from our sensor

    // Connections
    // VCC = 3.3V
    // GND = GND
    // SDA = A4
    // SCL = A5
    const int ALERT_PIN = A3;

    TMP102 sensor0;

    void setup() 

      Serial.println("Connected to TMP102!");
      delay(100);

      // Initialize sensor0 settings
      // These settings are saved in the sensor, even if it loses power

      // set the number of consecutive faults before triggering alarm.
      // 0-3: 0:1 fault, 1:2 faults, 2:4 faults, 3:6 faults.
      sensor0.setFault(0);  // Trigger alarm immediately

      // set the polarity of the Alarm. (0:Active LOW, 1:Active HIGH).
      sensor0.setAlertPolarity(1); // Active HIGH

      // set the sensor in Comparator Mode (0) or Interrupt Mode (1).
      sensor0.setAlertMode(0); // Comparator Mode.

      // set the Conversion Rate (how quickly the sensor gets a new reading)
      //0-3: 0:0.25Hz, 1:1Hz, 2:4Hz, 3:8Hz
      sensor0.setConversionRate(2);

      //set Extended Mode.
      //0:12-bit Temperature(-55C to +128C) 1:13-bit Temperature(-55C to +150C)
      sensor0.setExtendedMode(0);

      //set T_HIGH, the upper limit to trigger the alert on
      sensor0.setHighTempF(82.0);  // set T_HIGH in F
      //sensor0.setHighTempC(29.4); // set T_HIGH in C

      //set T_LOW, the lower limit to shut turn off the alert
      sensor0.setLowTempF(81.0);  // set T_LOW in F
      //sensor0.setLowTempC(26.67); // set T_LOW in C
    }

    void loop()