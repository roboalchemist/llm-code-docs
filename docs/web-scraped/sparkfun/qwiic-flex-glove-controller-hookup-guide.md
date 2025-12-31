# Source: https://learn.sparkfun.com/tutorials/qwiic-flex-glove-controller-hookup-guide

## Introduction

Flex sensors are great for telling how bent something is in a project, but we\'ve been running into issues with durability when using them in wearable applications like gloves. The [Qwiic Flex Glove Controller](https://www.sparkfun.com/products/14666) isolates the weak point to allow for more permanent flex sensor applications. The board has an onboard ADS1015 ADC to I^2^C so we can get a whole bunch of analog inputs without touching our microcontroller\'s ADC pins.

[![SparkFun Qwiic Flex Glove Controller](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/6/2/14666-SparkFun_Qwiic_Flex_Glove_Controller-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-flex-glove-controller.html)

### [SparkFun Qwiic Flex Glove Controller](https://www.sparkfun.com/sparkfun-qwiic-flex-glove-controller.html) 

[ SEN-14666 ]

The SparkFun Qwiic Flex Glove Controller allows you to incorporate flex sensors into a glove to control lighting, sound, and ...

[ [\$49.95] ]

In this hookup guide, we\'ll figure out how to pull values from our fingers as well as calibrate the sensor for our range of motion. We\'ll also cover recommended placement and installation to implement these into gloves.

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

You will also need a Qwiic cable to connect the shield to your sensor, choose a length that suits your needs.

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

If you don\'t have a sewing needle, we\'d recommend grabbing one if you\'re trying to add these flex sensors to some gloves.

[![Needle Set](https://cdn.sparkfun.com/r/140-140/assets/parts/4/8/7/5/10405-04b.jpg)](https://www.sparkfun.com/needle-set.html)

### [Needle Set](https://www.sparkfun.com/needle-set.html) 

[ TOL-10405 ]

This set of sewing needles is a must-have when stitching together your next e-textile project. Each envelope contains three 4...

[ [\$2.25] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the hookup guide for the Qwiic Shield if you haven\'t already. Brushing up on your skills in I^2^C is also recommended, as all Qwiic sensors are I^2^C.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

You\'ll also most likely want to sew these boards into a wearable project, so if you\'ve never picked up a needle and thread before, we\'d recommend checking out a [how-to on hand sewing](https://www.youtube.com/watch?v=ZvzMMcKHVR4).

## Hardware Overview

Let\'s look over a few characteristics of the ADS1015 so we know a bit more about how our glove controller behaves.

  **Characteristic**      **Range**
  ----------------------- ----------------------------------
  Operating Voltage       **2.0V - 5.5V**
  Operating Temperature   -40&degC - 125&degC
  Resolution              12 bit
  Sample Rate             128 Hz - 3.3 kHz
  Current Consumption     150 &microA (Typ.)
  I^2^C Address           0x48 (default), 0x49, 0x4A, 0x4B

### Pins

The characteristics for the pins of the Qwiic flex glove controller are outlined in the table below.

  Pin Label   Pin Function         Input/Output     Notes
  ----------- -------------------- ---------------- -------------------------------------------------------------------------------------
  3.3V        Power Supply         Input            Should be between **2.2V - 3.6V**
  GND         Ground               Input            0V/common voltage.
  SDA         I^2^C Data Signal    Bi-directional   Bi-directional data line. Voltage should not exceed power supply (e.g. 3.3V).
  SCL         I^2^C Clock Signal   Input            Master-controlled clock signal. Voltage should not exceed power supply (e.g. 3.3V).

\

### Optional Features

The Qwiic Flex Glove controller has onboard I^2^C pull up resistors; if multiple sensors are connected to the bus with the pull-up resistors enabled (which they most likely will be if you\'re creating a full set of gloves), the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by cutting the traces on the corresponding jumpers highlighted below.

[![I2C Pullup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/I2CPU.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/I2CPU.png)

The I^2^C address of the board can be changed using the jumpers on the back of the board. The address selection pin is connected to the center pad of each jumper, the below table shows the addresses available when the address selection pin is tied to each of the 4 available pads.

  **Pin**   **Address**
  --------- ----------------
  GND       0x48 (Default)
  VCC       0x49
  SDA       0x4A
  SCL       0x4B

The location of the jumpers is shown in the below image.

[![Address Jumpers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/ADR.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/ADR.png)

The holes in the bottom corners of the board are used for sewing the board into the gloves of your choice.

[![Sewing holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Sewing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Sewing.png)

Make sure you don\'t crease the flex sensors as this will break the sensor!

## Hardware Assembly

If you haven\'t yet assembled your Qwiic Shield, now would be the time to head on over to that tutorial.

[Qwiic Shield for Arduino Photon Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

With the shield assembled, SparkFun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the Flex Glove Controller breakout, the other into the Qwiic Shield of your choice and you\'ll be ready to upload a sketch and figure out how bent your fingers are. It seems like it\'s too easy to use, but that\'s why we made it that way!

[![Connected Flex Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-01.jpg)

You may want to integrate this board into some gloves, after all, that\'s what it was originally designed for. If you\'re looking to get sensors on 8 fingers, you\'ll need 4 glove boards, and if you have 4 boards on the same I^s^C bus, you\'ll need to use every address available to the ADS1015. So get started by changing the addresses of your boards so no two boards share the same address.

Now we want to attach our boards to our gloves. We\'ve found it best to sandwich the board between two layers of gloves to keep the sensor flush with the finger. To accomplish this, we\'ll sew the board to the outer layer of the inner glove. First, lay the glove out flat and place the board on the glove so that the ends of the flex sensors reach the tips of the fingers.

[![Sensor Laid on Glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-04.jpg)

Once you have the sensor laid out on the glove, take a marker and mark the point where the sewing hole touches the glove.

[![Mark Sewing Points](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-05.jpg)

Now simply sew the points to the available mounting holes on the sensor, The finished product should look like the below glove.

[![Glove put together](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-06.jpg)

Now it\'s time to hide the circuitry under a second glove. Go ahead and put the just the fingers of the second glove on, then slip the flex sensor down the gap between the the two layers of fabric. Sensors are shown at various states of this process in the image below.

[![Adding glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/Qwiic_Flex_Glove_Controller-07.jpg)

Now just plug Qwiic cables to connect both boards together, then plug one board into your microcontroller so we can get readings from the glove.

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Before we get into getting data from our flex sensors, let\'s look at the available functions in the library. We\'ve written a library to control the flex sensors. You can snag this library through the Arduino Library Manager. Search for **SparkFun ADS1015 Arduino Library** and you should be able to install the latest version. If you prefer manually downloading the libraries from the [GitHub repository](https://github.com/sparkfun/SparkFun_ADS1015_Arduino_Library), you can grab them here:

[Download the SparkFun ADS1015 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_ADS1015_Arduino_Library/archive/master.zip)

Let\'s get started by looking at the functions that set up the flex controller.

### Setup and Settings

- **`boolean begin(uint8_t i2caddr = ADS1015_ADDRESS_GND, TwoWire &wirePort = Wire);`** \-\-- By default use the default I2C address and use Wire port. Otherwise, pass in a custom I^2^C address and wire port.

- **`uint16_t getAnalogData(uint8_t channel);`** \-\-- Returns the uncalibrated analog value from the sensor.

- **`float getScaledAnalogData(uint8_t channel);`** \-\-- Returns a value between 0 and 1 based on calibration. Won\'t work properly without first running `calibrate()`

- **`void calibrate();`** \-\-- Used to calibrate the sensor and map the flexible range to values given by the user. While running calibration, simply flex each sensor to the minimum and maximum that it will be used in your project.

- **`void setMode(uint16_t mode);`** \-\-- Set mode of the sensor. Mode 0 is continuous read mode, mode 1 is single-shot

- **`uint16_t getMode();`** \-\-- Get\'s the read mode of the ADS1015.

- **`getCalibration(uint8_t channel, bool hiLo)`** \-\-- Get the high or low calibration value for a certain channel. if `hiLo` is true, `getCalibration()` will return the high calibration for the given channel.

- **`setCalibration(uint8_t channel, bool hiLo, uint16_t value)`** \-\-- Sets the high or low calibration value of a channel without using the automatic calibration function. Allows for manual calibration.

- **`resetCalibration()`** \-\-- Resets the calibration to 0.

- **`void setGain(uint16_t gain);`** \-\-- Pass in different values for different gains

- **`uint16_t getGain();`** \-\-- Get\'s the gain of the ADS1015. This will return 16-bit hex value. The values and their corresponding gains are listed below.

  - **`0x0E00`**: ± 0.256V
  - **`0X0000`**: ± 6.144V
  - **`0X0200`**: ± 4.096V
  - **`0X0400`**: ± 2.048V
  - **`0X0600`**: ± 1.024V
  - **`0X0800`**: ± 0.512V
  - **`0X0A00`**: ± 0.256V

- **`void setSampleRate(uint16_t sampleRate);`** \-\-- Sets the sample rate for the ADS1015, pass in the below 16-bit values to change to the corresponding sample rate.

  - **`0X0000`**: 128 Hz
  - **`0X0020`**: 250 Hz
  - **`0X0040`**: 490 Hz
  - **`0X0060`**: 920 Hz
  - **`0X0080`**: 1600 Hz
  - **`0X00A0`**: 2400 Hz
  - **`0X00C0`**: 3300 Hz

- **`uint16_t getSampleRate();`** \-\-- Returns the sample rate according to the above list of sample rates.

## Example Code

Now that we know how our library works, let\'s go ahead and get started pulling values from our flex sensors.

### Example 1 - Basic Readings

To get started with the first example, open up **File** \> **Examples** \> **SparkFun ADS1015 Arduino Library** \> **Qwiic Flex Glove Controller** \> **Example1_BasicReadings**. In this example, we begin by creating an **`ADS1015`** object called `fingerSensor` and then initializing our sensor object in the `setup()` loop. We then get the values from each finger by looping through and reading each channel on the ADS1015. The code for this is shown below.

    language:c
    #include <SparkFun_ADS1015_Arduino_Library.h>

    ADS1015 fingerSensor;

    void setup() 

    }

    void loop() 
      Serial.println();
    }

Uploading this sketch and opening the Serial Monitor to 115200 bps will yield an output somewhat like the below image.

[![Example 1 Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/EX1.PNG)

*Single Sensor Output - click the image for a closer look*

### Example 2 - Setup hand

In this example, we\'ll see how to setup an entire hand of flex sensors. To get started with this example, open up **File** \> **Examples** \> **SparkFun ADS1015 Arduino Library** \> **Qwiic Flex Glove Controller** \> **Example2_SetupHand**. In this example, we create two `ADS1015` objects, naming them `indexSensor` and `pinkySensor` to correspond with their locations on the glove. We also create an array with 4 spots to hold the data for the hand called `hand`. We then populate `hand` with values from each sensor. The code that accomplishes this is shown below.

    language:c
    #include <SparkFun_ADS1015_Arduino_Library.h>

    ADS1015 pinkySensor;
    ADS1015 indexSensor;
    uint16_t hand[4] = ;

    void setup() 
      if (indexSensor.begin(Wire, 100000, ADS1015_ADDRESS_GND) == false)   
    }

    void loop() 
      for (int finger = 0; finger < 4; finger++)
      
      Serial.println();
    }

Uploading this sketch and opening the Serial Monitor to 115200 bps will yield an output somewhat like the below image.

[![Serial monitor output for full glove](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/EX2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/EX2.PNG)

*Full Glove Output - click the image for a closer look*

### Example 3 - Calibration

The second example will show us how to calibrate our flex sensor so we get 0 when our finger is closed and 1 when it is open. To get started, open up **File** \> **Examples** \> **SparkFun ADS1015 Arduino Library** \> **Qwiic Flex Glove Controller** \> **Example3_Calibration**. In this example we will calibrate our sensor\'s maximum and minimum values in order to find the range for our sensor.

    language:c
    #include <SparkFun_ADS1015_Arduino_Library.h>
    #include <Wire.h>

    ADS1015 fingerSensor;

    void setup() 
      Serial.println("Calibrating, send 'e' when finished");
    }

    void loop() 
      } while (incoming != 'e');
      Serial.println("Calibrated");

      for (int channel; channel < 2; channel++)
      
        }
        Serial.println();
      }
    }

The sensor is initialized in the same manner as the first example, then our `loop()` begins calibrating the sensors. To calibrate the sensors, simply flex them to their maximum and minimum bend radii, then send an `e` over the Serial Monitor when you\'re finished. This will save the current calibration and show you the values that have been saved. Uploading this sketch and opening the Serial Monitor to 115200 bps will yield an output somewhat like the below image once you\'ve sent `e` and saved the calibration.

[![Example 3 - Calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/EX3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/EX3.PNG)

*Calibration Output - click the image for a closer look*

### Example 4 - Calibrated Hand

You don\'t necessarily want to calibrate your hand every single time you put on a glove with the flex controllers built in, so let\'s figure out how to manually set our calibration if we know it already. To get started, open up **File** \> **Examples** \> **SparkFun ADS1015 Arduino Library** \> **Qwiic Flex Glove Controller** \> **Example4_ManualCalibration**. We can see in the preamble to our code that we have an array of all of our calibration values, which were obtained using the previous example sketch. We then use a loop in the setup function along with our `setCalibration()` function to set the individual calibration values. The code for this is shown below.

    language:c
    #include <SparkFun_ADS1015_Arduino_Library.h>
    #include <Wire.h>

    ADS1015 pinkySensor;
    ADS1015 indexSensor;
    float hand[4] = ;
    uint16_t handCalibration[4][2] = 
      ,//index
      ,//middle
      ,//ring
       //pinky
    };

    void setup() 
      if (indexSensor.begin(Wire, 100000, ADS1015_ADDRESS_GND) == false) 
      

      //Set the calibration values for the hand.
      for (int channel; channel < 2; channel++)
      
        Serial.println();
      }
    }

    void loop() 
      for (int finger = 0; finger < 4; finger++)
      
      Serial.println();
    }

Uploading this sketch and opening the serial monitor will show a stream of calibrated values. Use these to scale any other variable you\'d like in your project.

[![Serial monitor output showing calibrated values](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/5/EX4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/5/EX4.PNG)

*Calibrated Hand Output - click the image for a closer look*