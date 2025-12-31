# Source: https://learn.sparkfun.com/tutorials/qwiic-human-presence-sensor-ak9753-hookup-guide

## Introduction

The [AK9753 Human Presence sensor](https://www.sparkfun.com/products/14349) is a Qwiic enabled, 4-channel [Nondispersive Infrared Sensor (NDIR)](https://en.wikipedia.org/wiki/Nondispersive_infrared_sensor). Each channel has a different field of view, so not only can the AK9753 detect a human, but it can also tell which direction the person is moving.

[![SparkFun Human Presence Sensor Breakout - AK9753 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/3/1/14349-01.jpg)](https://www.sparkfun.com/sparkfun-human-presence-sensor-breakout-ak9753-qwiic.html)

### [SparkFun Human Presence Sensor Breakout - AK9753 (Qwiic)](https://www.sparkfun.com/sparkfun-human-presence-sensor-breakout-ak9753-qwiic.html) 

[ SEN-14349 ]

This is not your normal PIR! The SparkFun AK9753 Human Presence Sensor Breakout is a Qwiic enabled, 4-channel Nondispersive I...

[ [\$22.50] ]

This hookup guide will show you how to get started taking basic reading from the sensor. We will cover both a serial output of readings as well as nice graph of the [derivative](https://en.wikipedia.org/wiki/Derivative) of our readings from a single channel.

### Required Materials

To get started, you\'ll need a microcontroller to, well, control everything.

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![SparkFun ESP32 Thing](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/5/6/4/13907-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing.html)

### [SparkFun ESP32 Thing](https://www.sparkfun.com/sparkfun-esp32-thing.html) 

[ DEV-13907 ]

The SparkFun ESP32 Thing is a comprehensive development platform for Espressif's ESP32, their super-charged version of the ...

[ [\$30.85] ]

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

[![Raspberry Pi 3](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/4/1/8/13825-01.jpg)](https://www.sparkfun.com/products/13825)

### [Raspberry Pi 3](https://www.sparkfun.com/products/13825) 

[ DEV-13825 ]

Everyone knows and loves Raspberry Pi, but what if you didn\'t need additional peripherals to make it wireless. The Raspberry ...

**Retired**

Now to get into the Qwiic ecosystem, the key will be one of the following Qwiic shields to match your preference of microcontroller:

[![SparkFun Qwiic HAT for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/5/14459-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html)

### [SparkFun Qwiic HAT for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-hat-for-raspberry-pi.html) 

[ DEV-14459 ]

The SparkFun Qwiic HAT for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and still u...

[ [\$6.95] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

You will also need a Qwiic cable to connect the shield to your human presence sensor, choose a length that suits your needs.

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

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

## Hardware Overview

Listed below are some of the characteristics and operating ranges of the AK9753 Human Presence Sensor.

  Characteristic             Range
  -------------------------- ---------------------------------
  Operating Voltage          **3.3V**
  Operating Temperature      -30°C to 85°C
  Current Consumption        10 μA (typ.), 100 μA (max) (5V)
  Spectral Sensitivity       5-7 μm (5V)
  Detection Range            3 m (5V)
  Temperature Sensor Range   -10° to 60°C

### Pins

  Pin                                        Description                                                                      Direction
  ------------------------------------------ -------------------------------------------------------------------------------- -----------
  GND                                        Ground                                                                           In
  3.3V                                       Power                                                                            In
  SDA                                        Data                                                                             In
  SCL                                        Clock                                                                            In
  [INT]   Interrupt, goes high when data is ready. After data is read, the pin pulls low   Out

### Optional Features

There are several jumpers on board that can be changed to facilitate several different functions. The first of which is the I^2^C pull-up jumper, highlighted below. If multiple sensors are connected to the I^2^C bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by [removing the solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering#advanced-techniques-and-troubleshooting) from this jumper.

[![Top View of Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/9/i2cpu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/i2cpu.png)

The JP8 jumper on the back of the board (highlighted below) can be sliced with a [hobby knife](https://www.sparkfun.com/products/9200) to disable the interrupt capability. The \"Field of View\" text and box shows the field of view of each of the 4 sensors. From the sensor\'s point of view, channel 1 is on top, 2 is on left, 3 is on bottom, and 4 is on the right.

[![Bottom of Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/9/int.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/int.png)

Addresses 0 and 1 can be used to change the I^2^C address of the board in case you have multiple devices using the same address. The below table shows the addresses that correspond to the different combinations of opened and closed jumpers.

[![Top View with Jumpers for Address](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/9/adr.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/adr.png)

  Address 0   Address 1   I^2^C Address
  ----------- ----------- ---------------
  0           0           0x64
  0           1           0x65
  1           0           0x67
  1           1           Switch Mode

Switch mode is available if you want to avoid using I^2^C altogether. In switch mode, data is written to the interrupt pin. The pin pulls high when the difference between two outputs (ex. IR1-IR3 or IR2-IR4) is greater than the upper or lower thresholds set in EEPROM by the manufacturer. This mode is a good solution if your project doesn\'t need much accuracy.

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head over to that tutorial. With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the AK9753 Human Presence Sensor, the other into the Qwiic Shield and you\'ll be ready to upload a sketch and start sensing humans. It seems too easy, but thats why we made it this way!

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you\'ll need to download and install the [SparkFun AK975X Arduino library](https://github.com/sparkfun/SparkFun_AK975x_Arduino_Library), this can be done using the button below or by using the Arduino Library Manager.

[Download the SparkFun AK975X Arduino Library](https://github.com/sparkfun/SparkFun_AK975X_Arduino_Library/archive/master.zip)

Before we get started developing a sketch, let\'s look at the available functions of the library.

- `int16_t getIR1();` \-\-- Returns the value from channel 1, there are also functions `getIR2();` and so on and so forth.
- `void refresh();` \-\-- Reads the dummy register telling the sensor to calculate the next reading.
- `boolean available();` \-\-- Returns `true` if data is ready.
- `boolean overrun();` \-\-- Returns true if the overrun bit is set.
- `void softReset();` \-\-- Resets the IC via software.
- `void setMode(uint8_t mode = AK975X_MODE_0);` \-\-- Set mode of the sensor. Mode 0 is continuous read mode.
- `void setCutoffFrequency(uint8_t frequency = AK975X_FREQ_8_8HZ);` \-\-- Sets the filtering frequency. 8Hz is the fastest and least filtered.
- `float getTemperature();` \-\-- Returns sensor temperature in °C.
- `float getTemperatureF();` \-\-- Returns sensor temperature in °F.
- `void enableDebugging(Stream &debugPort = Serial);` \-\-- Self explanatory, allows the output various extra messages to help with debugging.
- `void disableDebugging();` \-\-- Disables debugging messages.
- `uint8_t readRegister(uint8_t location);` \-\-- Basic read of I^2^C register.
- `void writeRegister(uint8_t location, uint8_t val);` \-\-- Writes to an I^2^C register.
- `uint16_t readRegister16(byte location);` \-\-- Reads a 16-bit value from an I^2^C register.

### Example 1: Basic Serial Readings

The example code shown below will get you started taking basic serial readings from the Human Presence Sensor. This sketch is relatively simple, pulling values using the `getIRX();` functions and printing them over a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) at 9600 baud.

    language:c
    #include <Wire.h>

    #include "SparkFun_AK975X_Arduino_Library.h" //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_AK975X_Arduino_Library

    AK975X movementSensor; //Hook object to the library

    int ir1, ir2, ir3, ir4, temperature;

    void setup()
    
    }

    void loop()
    
      delay(1);
    }

The output should look similar to the image below, with the values of each channel, temperature, and timestamp of the reading in each row.

[![Serial Output](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/example1_basicserialoutput.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/example1_basicserialoutput.PNG)

*Click the image for a closer look.*

### Example 2: Graphing the Human Presence Sensor Serial Data

The next example takes the derivative of a single channel and displays this on the serial plotter. The code for this example is shown below. Notice how you can change the sensitivity of the Human Presence Sensor using the `sensitivity` value. It is set at 50 by default, and values lower than this will yield higher sensitivity.

    language:c
    #include <Wire.h>

    #include "SparkFun_AK975X_Arduino_Library.h" //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_AK975X_Arduino_Library

    AK975X movementSensor; //Hook object to the library

    unsigned int upValue; // current proximity reading
    unsigned int averageValue;   // low-pass filtered proximity reading
    signed int fa2;              // FA-II value;
    signed int fa2Derivative;     // Derivative of the FA-II value;
    signed int fa2DerivativeLast;     // Last value of the derivative (for zero-crossing detection)
    signed int sensitivity = 50;  // Sensitivity of touch/release detection, values closer to zero increase sensitivity

    #define LOOP_TIME 30  // Loop duration in ms. 30ms works well.

    //Exponential average weight parameter / cut-off frequency for high-pass filter
    //#define EA 0.3  //Very steep
    //#define EA 0.1  //Less steep
    #define EA 0.05  //Less steep

    void setup()
    

      upValue = movementSensor.getIR3(); //Get one of the latest IR values
      averageValue = upValue;
      fa2 = 0;
      movementSensor.refresh(); //Read dummy register after new data is read
    }

    void loop()
    
        else if (fa2 > sensitivity) // maximum
        
        else
        
      }
      else
      

      Serial.println();

      // Do this last
      averageValue = EA * upValue + (1 - EA) * averageValue;
      while (millis() < startTime + LOOP_TIME); // enforce constant loop time
    }

Once again, the output for this example code should look something like the below image. This graph is the [derivative](https://en.wikipedia.org/wiki/Derivative) of a single channel on our presence sensor, so any variance from 0 shows the rate of change of the signal.

[![Serial Plotter](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/example2_derivativegraph.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/9/example2_derivativegraph.PNG)

*Click the image for a closer look.*

### Example 3: Configuration Settings

The third example simply shows you how to set your AK9753 up on different addresses, baud rates, and I^2^C speeds. Simply call the non-default `begin()` function by including the arguments for wire port, I^2^C speed, I^2^C address and baud rate. For example, calling `movementSensor.begin(Wire, I2C_SPEED_FAST, 0x64, 115200);` will start the sensor with a fast I^2^C speed on address 0x64 with a baud of 115200 bps. Output of this example should look similar to Example 1.

### Example 4: Threshold Tests

In this example, we\'ll go over how to set up the differential interrupt capabilities of the AK9753. To get started, go ahead and open up the example in `File` \> `Examples` \> `SparkFun AK9750 Human Presence Sensor Library` \> `Example4_ThresholdTests`. Let\'s also connect the interrupt on our AK9753 to pin **`A3`** on our Arduino, as this will read the status of the interrupt pin. Uploading this code to our Arduino and opening the Serial monitor to a baud of 115200 will open up a menu showing how to change the various settings related to interrupts. By sending Serial commands to our Arduino, we can change the interrupt characteristics around until they\'re just how we like them. The table of available Serial commands is shown below.

  **Characteristic**      **Command (byte, \[Range\])**
  ----------------------- -------------------------------
  High Threshold          1, \[-2048, 2048\]
  Low Threshold           2, \[-2048, 2048\]
  Hysteresis              3, \[0, 31\]
  Interrupt Enable        4, \[0, 31\]
  Read Interrupt Status   5
  Begin Readings          6
  Stop Readings           7

For example, to set the high threshold, send the command `1,x` where `x` is any number from -2048 to 2048. Play around with. The only place where sending Serial commands gets tricky is with the Interrupt Enable as we should be sending a binary value, but the Serial monitor is an ASCII interface, so we\'ll have to convert the binary for the interrupts we want to enable into decimal values. A chart to help you out is shown below. (IR13HI means the high threshold interrupt between 1 and 3, the H will be an L for the low threshold interrupts)

  **Interrupt**   **Decimal Value**
  --------------- -------------------
  IR13HI          16
  IR13LI          8
  IR24HI          4
  IR24LI          2
  DATAREADY       1

If you wanted to enable `DATAREADY` and `IR13LI` you would add 1 to 8 and send the command `4, 9` over Serial.