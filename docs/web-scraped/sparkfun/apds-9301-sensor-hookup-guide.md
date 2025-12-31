# Source: https://learn.sparkfun.com/tutorials/apds-9301-sensor-hookup-guide

## Introduction

The [APDS-9301](https://www.sparkfun.com/products/14350) is an I^2^C compatible luminosity sensor which returns readings in lux. It is non-instantaneous, requiring some integration time to take a measurement. SparkFun provides a library making use of the part very simple.

[![SparkFun Ambient Light Sensor Breakout - APDS-9301](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/3/5/14350-02.jpg)](https://www.sparkfun.com/products/14350)

### [SparkFun Ambient Light Sensor Breakout - APDS-9301](https://www.sparkfun.com/products/14350) 

[ SEN-14350 ]

The APDS-9301 Ambient Light Sensor Breakout is an I2C-compatible luminosity sensor board that converts light intensity to a d...

**Retired**

### Required Materials

Please check the wish list below for items required to follow this tutorial.

### Tools

No special tools are required to follow this tutorial. You will need a soldering iron, solder, and general soldering accessories.

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

### Suggested Reading

We suggest reviewing the tutorials below to ensure that you\'re up-to-date with all of the skills necessary to follow this hookup guide.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

The APDS-9301 breakout board is fairly simple, with only a few ancillary passive components in addition to the ADPS-9301 sensor IC itself.

**APDS-9301 sensor** - This is the sensor IC. Its operating voltage only extends up to 3.6V, so to use it with a 5V Arduino or Arduino clone, you\'ll need some kind of [voltage translation](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)!

[![Sensor highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/sensor_highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/sensor_highlighted.png)

**I^2^C pullup resistors** - The board includes pullup resistor so you don\'t need to add them externally.

[![I2C Pullups](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/i2c_highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/i2c_highlighted.png)

**INT pin** - The APDS-9301 can be programmed to generate an interrupt under certain conditions. This pin will be asserted low (i.e., pulled to ground) when those conditions are met. Note that this is an open collector pin, so you\'ll need to enable the pullup resistor on the processor for it to work.

[![Int pin highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/int_pin_highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/int_pin_highlighted.png)

**SparkFun standard I^2^C header** - Most boards which can be communicated to via I^2^C use this pinout, making it easy to stack them or connect them in a daisy chain.

[![I2C standard header](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/header_highlighted.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/header_highlighted.png)

**Address Select Jumpers** - On the back of the board, the only item of interest is the address select jumper. By default, this jumper is open, resulting in an I^2^C address of **0x39**. If the HIGH side of the jumper is closed, the address will be\*\* 0x29\*\*. If the LOW side of the jumper is closed, the address will be **0x49**. If a big old blob of solder closes both sides of the jumper, it will still work, and the address will be 0x49.

[![Rear of board](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/14350-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/14350-04.jpg)

## Library Overview

Here\'s a list of the most critical functions supported by the library.

- `begin(address)` - enables the IC, sets the gain and integration times to minimum (i.e., lowest sensitivity), and disables the interrupt.

- `setGain(gainLevel)` - there are two possible parameters to pass to this function: `APDS9301::LOW_GAIN` and `APDS9301::HIGH_GAIN`. High gain is 16x more sensitive than low gain.

- `gain getGain()` - returns one of the two values specified in `setGain()` above. This function actually reads the gain from the sensor and returns the true value currently being used.

- `setIntegrationTime(integrationTime)` - there are three possible parameters to pass to this function: `APDS9301::INT_TIME_13_7_MS`, `APDS9301::INT_TIME_101_MS`, and `APDS9301::INT_TIME_402_MS`. Sensitivity to light increases with integration time, and the rate at which new data is generated by the sensor is also determined by integration time. By default, the integration time is set to the lowest value (13.7ms).

- `intTime getIntegrationTime()` - returns one of the three values specfied in `setIntegrationTime()` above. This function actually reads the gain from the sensor and returns the true value currently being used.

- `enableInterrupt(intMode)` - pass either `APDS9301::INT_ON` or `APDS9301::INT_OFF` to this function to enable or disable the interrupt functionality. By default, the interrupt is disabled. If enabled, the following three functions will determine the circumstances under which an interrupt will be issued and the INT pin will be set high.

- `setCyclesForInterrupt(cycles)` - sets number of ADC cycles values must be in interrupt range for an interrupt to occur. Pass `0` to interrupt on every ADC cycle (ADC cycle time is defined by integration time as discussed above). Pass `1` to interrupt if the reading is ever above the high threshold or below the low threshold (see next two functions for information regarding threshold settings). Pass `2` through `15` to require that many cycles above or below the respective threshold before issuing an interrupt.

- `setLowThreshold(threshold)` - pass an `unsigned int` to this function between `0` and `65535`. Readings on CH0 of the sensor (which detects both visible and IR light) below this threshold for the time set by the `setCyclesForInterrupt()` will trigger an interrupt on the INT pin. To disable the low threshold, simply write `0` to this function.

- `unsigned int getLowThreshold()` - returns the current low threshold setting, read from the sensor directly.

- `setHighThreshold(threshold)` - pass an `unsigned int` to this function between `0` and `65535`. Readings on CH0 of the sensor (which detects both visible and IR light) above this threshold for the time set by the `setCyclesForInterrupt()` will trigger an interrupt on the INT pin. To disable the high threshold, simply write `65535` to this function.

- `unsigned int getHighThreshold()` - returns the current low threshold setting, read from the sensor directly.

- `float readLuxLevel()` - returns a floating point number representing the current light level in lux. Note that due to inherent inaccuracy in the sensor, this value is only accurate to within 35%-40% of the actual absolute lux value.

## Example

### Hardware Hookup

We use a hookup as pictured below for our example project. However, this basic Arduino code should work for any number of different Arduino compatible boards. In this case, we show it on an Arduino Pro 3.3V, to allow the setup to work without any level translation between the Arduino and the APDS-9301.

[![Fritzing diagram of board hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/6/fritzingview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/fritzingview.png)

Note that this setup requires some soldering. New to soldering? Check out our [through hole soldering guide](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)!

### Notes on Operation

The APDS-9301 has two internal light sensing elements: CH0, which responds to infrared and visible light, and CH1, which responds to only visible light. By combining these two channels, the sensor is able to compensate for local infrared light and provide a more accurate estimate of the current lux value.

The calculation of lux reading from CHO and CH1 sensor output readings is not straightforward. The function is piecewise, with different coefficients depending on the ratio CH1/CH0. This function is automatically implemented in the `readLuxLevel()` library function, but can be found in the datasheet if you\'re curious.

The APDS-9301 sensor works by multiplying the light input signal by a gain (either 1x or 16x) and then using an integrating ADC to measure the light input over some integration time. As such, the integration time imposes an inherent limit on the maximum reading of the ADC. For the 13.7ms integration time, this limit is 5047. For the 101ms integration time, this limit is 37177. For the full 402ms integration time, the maximum is actually defined by the size of the output variable, an 16-bit unsigned integer, at 65535. This fact should be taken into account when selecting a value for the interrupt high and low threshold values. For instance, if the integration time is 13.7ms and a high threshold of 6000 is set, that threshold will never be reached.

### Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Make sure to install the APDS-9301 Arduino library before using the example code. You can obtain the library through the Arduino Library Manager by serarching for \"**SparkFun APDS-9301 Lux Sensor**\" in order to install the latest version. The library can also be found in the [SparkFun APDS-9301 Library GitHub repository](https://github.com/sparkfun/SparkFun_APDS9301_Library) to manually install:

[SparkFun APDS-9301 GitHub Repository (ZIP)](https://github.com/sparkfun/SparkFun_APDS9301_Library/archive/master.zip)

Below is a simple example code for Arduino that uses the APDS-9301 library. First, the example code sets the gain and integration time. Then enables and sets thresholds for the interrupt. Finally, the code reads the current lux level and prints it to the serial port. It also prints a message when the light level exceeds a certain threshold. It should get you up and running in no time!

    language:c
    #include "Wire.h"
    #include <Sparkfun_APDS9301_Library.h>

    APDS9301 apds;

    #define INT_PIN 2 // We'll connect the INT pin from our sensor to the
                      // INT0 interrupt pin on the Arduino.
    bool lightIntHappened = false; // flag set in the interrupt to let the
                      //  mainline code know that an interrupt occurred.

    void setup() 
    

    void loop() 
    
      }
    }

    void lightInt()
    

After uploading code, try opening the [Arduino serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) at 115200 baud and observe the sensor\'s output.

[![Serial output](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/captured_serial.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/6/captured_serial.png)

As you can see, once per second, the sketch will print the luminous flux and whether or not the level selected for an interrupt has been exceeded.