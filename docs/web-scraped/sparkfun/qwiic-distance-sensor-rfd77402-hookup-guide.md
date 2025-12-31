# Source: https://learn.sparkfun.com/tutorials/qwiic-distance-sensor-rfd77402-hookup-guide

## Introduction

The [RFD77402](https://www.sparkfun.com/products/14539) uses an infrared VCSEL ([Vertical Cavity Surface Emitting Laser](https://en.wikipedia.org/wiki/Vertical-cavity_surface-emitting_laser)) TOF ([Time of Flight](https://en.wikipedia.org/wiki/Time_of_flight)) module capable of millimeter precision distance readings up to 2 meters. It\'s also part of SparkFun\'s [Qwiic system](https://www.sparkfun.com/categories/399), so you won\'t have to do any soldering to figure out how far away things are.

[![SparkFun Distance Sensor Breakout - RFD77402 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/5/9/14539-SparkFun_Distance_Sensor_Breakout_-_RFD77402__Qwiic_-01.jpg)](https://www.sparkfun.com/products/14539)

### [SparkFun Distance Sensor Breakout - RFD77402 (Qwiic)](https://www.sparkfun.com/products/14539) 

[ SEN-14539 ]

The SparkFun Distance Sensor Breakout utilizes the RFD77402 3D ToF sensor module from Simblee to give you the most accurate m...

**Retired**

In this hookup guide, we\'ll first get started with some basic distance readings, then we\'ll add in a confidence value to ensure the sensor isn\'t returning \"garbage\" data. Finally, we\'ll increase our sample rate to obtain readings as fast as we can.

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

You will also need a Qwiic cable to connect the shield to your distance sensor, choose a length that suits your needs.

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

Let\'s first check out some of the characteristics of the [RFD77402 sensor](https://cdn.sparkfun.com/assets/a/d/3/e/2/Simblee_RFD77402_Datasheet_Rev_1-8__1_.pdf) we\'re dealing with, so we know what to expect out of the board.

  **Characteristic**      **Range**
  ----------------------- -------------------------------------------
  Operating Voltage       **3.3V**
  Current                 7 mA average at 10Hz
  Measurement Range       \~50mm to 2,000mm
  Precision               +/-10%
  Light Source            850nm VCSEL
  I^2^C Address           0x4C
  Field of View           55°
  Field of Illumination   23°
  Max Read Rate           10Hz (We\'ve seen up to 20Hz in practice)

### Pins

The following table lists all of the RFD77402\'s pins and their functionality.

  Pin                                        Description                               Direction
  ------------------------------------------ ----------------------------------------- -----------
  GND                                        Ground                                    In
  3.3V                                       Power                                     In
  SDA                                        Data                                      In
  SCL                                        Clock                                     In
  [INT]   Interrupt, goes low when data is ready.   Out

### Optional Features

The RFD77402 breakout has onboard I^2^C pull up resistors; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by removing the solder on the corresponding jumpers highlighted below.

[![Pull Up Resistors Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/9/PU.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/PU.png)

## Hardware Assembly 

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the RFD77402 breakout, the other into the Qwiic Shield and you\'ll be ready to upload a sketch and figure out how far away you are from that thing over there. It seems like it\'s too easy too use, but that\'s why we made it that way!

[![Qwiic Distance Sensor Connected to Qwiic Shield Stacked on RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/2/9/Distance_Sensor-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/Distance_Sensor-02.jpg)

## Library Overview 

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you\'ll need to download SparkFun\'s RFD77402 Library. This can be done by using the below button or by utilizing the Arduino library manager. You can also grab the latest, greatest version over on the [library\'s GitHub repository](https://github.com/sparkfun/SparkFun_RFD77402_Arduino_Library).

[Download SparkFun RFD77402 Library (ZIP)](https://github.com/sparkfun/SparkFun_RFD77402_Arduino_Library/archive/master.zip)

Before getting started, let\'s check out the publicly available functions of our library.

- **`boolean begin(TwoWire &wirePort = Wire, uint32_t i2cSpeed = I2C_SPEED_STANDARD);`** \-\-- Initializes the RFD77402 sensor on a given I^2^C bus, with a given I^2^C speed. This function will default to the primary I^2^C bus and standard I^2^C speed if called without any arguments.
- **`uint8_t takeMeasurement();`** \-\-- Takes a single measurement and sets the global variables with new data.
- **`uint16_t getDistance();`** \-\-- Returns the local variable `distance` to the caller.
- **`uint8_t getValidPixels();`** \-\-- Returns the number of valid pixels found when taking measurement.
- **`uint16_t getConfidenceValue();`** \-\-- Returns the qualitative value representing how confident the sensor is about its reported distance.
- **`uint8_t getMode();`** \-\-- Read the command opcode and convert to the corresponding mode.
- **`boolean goToStandbyMode();`** \-\-- Tell MCPU to go to standby mode. Return true if successful.
- **`boolean goToOffMode();`** \-\-- Tell MCPU to go to off state. Return true if successful.
- **`boolean goToOnMode();`** \-\-- Tell MCPU to go to on state. Return true if successful.
- **`boolean goToMeasurementMode();`** \-\-- Tell MCPU to go to measurement mode. Takes a measurement. If measurement data is ready, return true.
- **`uint8_t getPeak();`** \-\-- Returns the VCSEL peak 4-bit value.
- **`void setPeak(uint8_t peakValue);`** \-\-- Sets the VCSEL peak 4-bit value.
- **`uint8_t getThreshold();`** \-\-- Returns the VCSEL Threshold 4-bit value.
- **`void setThreshold(uint8_t threshold);`** \-\-- Sets the VCSEL Threshold 4-bit value.
- **`uint8_t getFrequency();`** \-\-- Returns the VCSEL Frequency 4-bit value.
- **`void setFrequency(uint8_t threshold);`** \-\-- Sets the VCSEL Frequency 4-bit value.
- **`uint16_t getMailbox();`** \-\-- Gets whatever is in the \'MCPU to Host\' mailbox. Check Interrupt Control Status Register bit 5 before reading.
- **`void reset();`** \-\-- Software reset the device
- **`uint16_t getChipID();`** \-\-- Returns the chip ID. Should be 0xAD01 or higher.
- **`boolean getCalibrationData();`** \-\-- Retrieves 2 sets of 27 bytes from MCPU for computation of calibration parameters. 54 bytes are read into the calibration array, true is returned if new calibration data is loaded successfully.
- **`uint16_t readRegister16(uint8_t addr);`** \-\-- Reads two bytes from a given location from the RFD77402.
- **`uint8_t readRegister(uint8_t addr);`** \-\-- Reads from a given location from the RFD77402.
- **`void writeRegister16(uint8_t addr, uint16_t val);`** \-\-- Write a 16 bit value to a spot in the RFD77402.
- **`void writeRegister(uint8_t addr, uint8_t val);`** \-\-- Write a value to a spot in the RFD77402.

## Example Code

You should have downloaded the SparkFun RFD77402 Library in the previous step, if not, go back to the previous step and go ahead and download it as you\'ll be needing it shortly. This hookup guide goes over the 3 examples contained within the library.

### Example 1 - Basic Readings

Example 1 gets us started taking some basic distance readings from the sensor. Simply upload the example code below, open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with a baud rate of 9600 and start getting readings!

    language:c
    #include <SparkFun_RFD77402_Arduino_Library.h> //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_RFD77402_Arduino_Library
    RFD77402 myDistance; //Hook object to the library

    void setup()
    
      Serial.println("Sensor online!");
    }

    void loop()
    

The first example simply outputs distances one after another, the output should look something like the image below.

[![Qwiic Distance Sensor Example 1 Output](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex1.PNG)

### Example 2 - Confidence Values

The second example gets us going on rejecting or accepting our data as a successful reading (i.e. the sensor is not maxed out). This is done simply by using the `getConfidenceValue()` function, which returns a value anywhere between 0 and 2047, with 2047 being the \"most confident\". In other words, a confidence value of 2047 means that the sensor is getting a very strong, clean, TOF flight reading. This is a great way to ignore any data that is out of the sensors range. The below example code will get you started taking these confidence readings. This sketch will also check the distance value against error codes to see if the sensor is giving us an error, and if so, which one.

    language:c
    #include <SparkFun_RFD77402_Arduino_Library.h> //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_RFD77402_Arduino_Library
    RFD77402 myDistance; //Hook object to the library

    void setup()
    
      Serial.println("Sensor online!");
    }

    void loop()
    
      else if (errorCode == CODE_FAILED_PIXELS)
      
      else if (errorCode == CODE_FAILED_SIGNAL)
      
      else if (errorCode == CODE_FAILED_SATURATED)
      
      else if (errorCode == CODE_FAILED_NOT_NEW)
      
      else if (errorCode == CODE_FAILED_TIMEOUT)
      

      Serial.println();
    }

Opening the serial monitor to 9600 baud should yield an output similar to the one shown earlier.

[![Qwiic Distance Sensor Example 2 Output](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex2.PNG)

### Example 3 - Fast Readings

The following example allows you to use your distance sensor not only to measure distance but time in between samples as well. Enabling a faster I^2^C speed cuts down on the time where we are talking to the sensor, so we are able to accurately guage time in between readings. This allows the user to compute velocity and even acceleration if they\'d like. Check out the [Equations of Motion](https://en.wikipedia.org/wiki/Equations_of_motion) for a little bit better explanation if you\'re new to physics.

In the below example, make note of two things, the first is in the `setup()` function. Notice how we call a non-default `begin()` function that initializes the sensor with `I2C_SPEED_FAST`, which increases the clock speed on the I^2^C bus. The second thing to make note of are the three lines at the beginning of our `void loop()`, which starts the timer function and allows us to know the time in between readings.

    language:c
    #include <SparkFun_RFD77402_Arduino_Library.h> //Use Library Manager or download here: https://github.com/sparkfun/SparkFun_RFD77402_Arduino_Library
    RFD77402 myDistance; //Hook object to the library

    void setup()
    
      Serial.println("Sensor online!");
    }

    void loop()
    
      else if (errorCode == CODE_FAILED_PIXELS)
      
      else if (errorCode == CODE_FAILED_SIGNAL)
      
      else if (errorCode == CODE_FAILED_SATURATED)
      
      else if (errorCode == CODE_FAILED_NOT_NEW)
      
      else if (errorCode == CODE_FAILED_TIMEOUT)
      

      Serial.println();
    }

Opening the serial monitor to 115200 baud should yield something like the below image.

[![Qwiic Distance Sensor Example 3 Output](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/9/ex3.PNG)