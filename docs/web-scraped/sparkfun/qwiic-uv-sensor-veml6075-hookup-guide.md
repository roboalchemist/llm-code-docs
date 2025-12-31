# Source: https://learn.sparkfun.com/tutorials/qwiic-uv-sensor-veml6075-hookup-guide

## Introduction

The [VEML6075](https://www.sparkfun.com/products/15089) is SparkFun\'s latest [UV](https://en.wikipedia.org/wiki/Ultraviolet) sensing solution. The VEML6075 implements a simple photodiode to measure the levels of UVA (320-400 nm) and UVB (280-320 nm) radiation. We can read the intensity of this light in [irradiance](https://en.wikipedia.org/wiki/Irradiance), and from there, calculate the [UV Index](https://en.wikipedia.org/wiki/Ultraviolet_index). The Qwiic UV Sensor has two spectrum ranges of measurement, UVA (365 ±10nm), and UVB. (330 ±10nm)

[![SparkFun UV Light Sensor Breakout - VEML6075 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/4/4/7/15089-SparkFun_UV_Light_Sensor_Breakout_-_VEML6075__Qwiic_-01.jpg)](https://www.sparkfun.com/products/15089)

### [SparkFun UV Light Sensor Breakout - VEML6075 (Qwiic)](https://www.sparkfun.com/products/15089) 

[ SEN-15089 ]

The VEML6075 UV Light Sensor Breakout is SparkFun's latest ultraviolet sensing solution.

**Retired**

### Required Materials

To get started, you\'ll need a microcontroller to control everything. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

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

You will also need a Qwiic cable to connect the shield to your UV sensor, choose a length that suits your needs.

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

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

## Hardware Overview

First let\'s check out some of the characteristics of the [VEML6075 sensor](https://cdn.sparkfun.com/assets/e/5/8/d/7/veml6075.pdf) we\'re dealing with, so we know what to expect out of the board.

  **Characteristic**   **Range**
  -------------------- ----------------------
  Operating Voltage    **1.7V-3.6V**
  Supply Current       480 µA
  UVA Resolution       0.93 counts/µW/cm^2^
  UVA Resolution       2.1 counts/µW/cm^2^
  I^2^C Address        **0x10**

### Pins

The following table lists all of the VEML6075\'s pins and the direction of data flow.

  Pin    Description   Direction
  ------ ------------- ----------------
  GND    Ground        In
  3.3V   Power         In
  SDA    Data          Bi-directional
  SCL    Clock         In

### Optional Features

The VEML6075 breakout has pull up resistors attached to the I^2^C bus; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by cutting the traces on the corresponding jumpers highlighted below.

[![Pullup Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/PU.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/PU.png)

*Pull-Up Jumper*

The onboard LED (highlighted below) will light up when the board is powered, and the sensor (also highlighted below) should be left uncovered in your application.

[![Sensor and Power LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/LED.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/LED.png)

*Sensor and Power LED*

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. Depending on the microcontroller and shield you\'ve chosen, your assembly may be different, but here\'s a handy link to the Qwiic Shield for Arduino and Photon Hookup Guide to get you started!

[Qwiic Shield for Arduino Photon Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

With the shield assembled, SparkFun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the Qwiic UV Sensor, the other into the Qwiic Shield and you\'ll be ready to upload a sketch and figure out how much sunscreen you need to put on to keep yourself from turning into a lobster. It seems like it\'s too easy to use, but that\'s why we made it that way!

[![Connected Qwiic Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/SparkFun_UV_Light_Sensor_Breakout_-_VEML6075__Qwiic__Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/SparkFun_UV_Light_Sensor_Breakout_-_VEML6075__Qwiic__Hookup_Guide-03.jpg)

*SparkFun RedBoard and Qwiic Shield with the Qwiic UV Sensor Attached*

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

First, you\'ll need the **SparkFun VEML6075 Arduino library**. You can obtain these libraries through the Arduino Library Manager. Search for **Sparkfun VEML6075 Arduino Library** to install the latest version. If you prefer downloading the [library from the GitHub repository](https://github.com/sparkfun/SparkFun_VEML6075_Arduino_Library) and manually installing it, you can grab them here:

[DOWNLOAD THE SPARKFUN VEML6075 ARDUINO LIBRARY (ZIP)](https://github.com/sparkfun/SparkFun_VEML6075_Arduino_Library/archive/master.zip)

Before we get started developing a sketch, let\'s look at a pertinent **enum**, `VEML6075_error_t`. Many of our functions will return this data type as a way of pointing out errors. The **enum** is shown below, notice how negative numbers are returned for errors, while a `1` is returned for a success.

    language:c
    typedef enum  VEML6075_error_t;

### Setup

- **`boolean begin(void)`** \-\-- Returns true if the VEML6075 is attached properly.

- **`VEML6075_error_t begin(TwoWire &wirePort)`** \-\-- Give `begin()` a TwoWire port to specify the I^2^C port

- **`void setDebugStream(Stream &debugPort = Serial)`** \-\-- Enables debug statements, defaults to Serial for output

- **`boolean isConnected(void)`** \-\-- Returns true if the VEML6075 is attached properly.

### Configuration

- **`VEML6075_error_t setIntegrationTime(veml6075_uv_it_t it)`** \-\-- Set integration time for a measurement to 50, 100, 200, 400, or 800 ms. The options for the `veml6075_uv_it_t` enum are shown below. IT_50MS,
  - `IT_50MS`
  - `IT_100MS`
  - `IT_200MS`
  - `IT_400MS`
  - `IT_800MS`
  - `IT_RESERVED_0`
  - `IT_RESERVED_1`
  - `IT_RESERVED_2`
  - `IT_INVALID`    \
    \

- **`veml6075_uv_it_t getIntegrationTime(void)`** \-\-- Returns the current integration time

- **`VEML6075_error_t setHighDynamic(veml6075_hd_t hd)`** \-\-- Changes to high dynamic mode by passing in `DYNAMIC_HIGH` and normal dynamic mode by passing in `DYNAMIC_NORMAL`. High dynamic mode increases the resolution by a factor of 2.

- **`veml6075_hd_t getHighDynamic(void)`** \-\-- Returns the current high dynamic setting.

- **`VEML6075_error_t setTrigger(veml6075_uv_trig_t trig)`** \-\-- Set\'s trigger to continuos read (`NO_TRIGGER`) or (`TRIGGER_ONE_OR_UV_TRIG`)

- **`veml6075_uv_trig_t getTrigger(void)`** \-\-- Returns current trigger mode as `NO_TRIGGER`, `TRIGGER_ONE_OR_UV_TRIG` or `TRIGGER_INVALID`.

- **`VEML6075_error_t trigger(void)`** \-\-- Triggers once.

- **`VEML6075_error_t setAutoForce(veml6075_af_t af)`** \-\-- With auto force enabled, the UV sensor will conduct one measurement whenever the host writes `TRIGGER_ONE_OR_UV_TRIG` to `setTrigger()`, otherwise, the VEML6075 continuously takes measurements. Passing in `AF_DISABLE` or `AF_ENABLE` will disable and enable the auto force mode.

- **`veml6075_af_t getAutoForce(void)`** \-\-- Returns the current auto force setting as `AF_DISABLE`, `AF_ENABLE`, or `AF_INVALID`

- **`VEML6075_error_t powerOn(boolean enable = true)`** \-\-- Powers the VEML6075 on from shutdown mode.

- **`VEML6075_error_t shutdown(boolean shutdown = true)`** \-\-- Puts the VEML6075 in shutdown mode (800 nA)

- **`uint16_t rawUva(void)`** \-\-- Reads raw UVA data

- **`uint16_t rawUvb(void)`** \-\-- Reads raw UVB data

- **`float uva(void)`** \-\-- Returns UVA data, adjusted with values from the UV compensation registers.

- **`float uvb(void)`** \-\-- Returns UVA data, adjusted with values from the UV compensation registers.

- **`float index(void)`** \-\-- Returns the UV index.

- **`float a(void)`** \-\-- Returns UVA data, adjusted with values from the UV compensation registers.

- **`float b(void)`** \-\-- Returns UVA data, adjusted with values from the UV compensation registers.

- **`float i(void)`** \-\-- Returns the UV index.

- **`uint16_t uvComp1(void)`** \-\-- Gets value for UV compensation

- **`uint16_t uvComp2(void)`** \-\-- Gets value for UV compensation

- **`uint16_t visibleCompensation(void)`** \-\-- Gets value for visible compensation

- **`uint16_t irCompensation(void)`** \-\-- Gets value for IR compensation

- **`VEML6075_error_t deviceID(uint8_t * id)`** \-\-- Prints device ID on debug stream.

- **`VEML6075_error_t deviceAddress(uint8_t * address)`** \-\-- Prints device address on debug stream.

## Example Code

Now that we have our library installed and we understand the basic functions, let\'s run some examples for our UV sensor to see how it behaves.

### Example 1 - Stream UV

To get started with the first example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun VEML6075 UV Sensor** \> **Example1_Stream_UV**. In this example, we begin by creating a **`VEML6075`** object called `uv` and then initializing our sensor object in the `setup()` loop. The code to do this is shown below.

    language:c
    VEML6075 uv; // Create a VEML6075 object 

    void setup() 
      Serial.println("UVA, UVB, UV Index");
    }

Once we\'ve initialized our sensor, we can start grabbing measurements from it. We pull the UVA and UVB values as well as the index using `uv.uva`, `uv.uvb` and `uv.index` The `void loop()` function that does this is shown below.

    language:c
    void loop() 

Opening your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to a baud rate of **9600** should show the calibrated UVA and UVB levels as well as the current UV index

[![Example 1 Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX1.PNG)

*Example 1 Output*

### Example 2 - Configure UV

To get started with the second example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun VEML6075 UV Sensor** \> **Example2_Configure_UV**. In this example, we begin by creating and initializing a **`VEML6075`** object called `uv`. We then change the integration time (the amount of time over which a measurement is taken) and change to high dynamic mode (which increases the resolution) using the following lines of code (contained in the `setup()` loop)

    language:c
    void setup() 

      // Integration time: The VEML6075 features five selectable integration times. This is the amount of
      // time the sensor takes to sample UVA/UVB values, before integrating the readings into averages.
      // Valid integration times are:
      //      VEML6075::IT_50MS -- 50ms
      //      VEML6075::IT_100MS -- 100ms
      //      VEML6075::IT_200MS -- 200ms
      //      VEML6075::IT_400MS -- 400ms
      //      VEML6075::IT_800MS -- 800ms
      // The library defaults integration time to 100ms. (Set on every call to begin().)
      uv.setIntegrationTime(VEML6075::IT_200MS);

      // High dynamnic: The VEML6075 can either be set to normal dynamic or high dynamic mode.
      // In high dynamic mode, the resolution is increased by about a factor of two.
      // Valid dynamic settings are:
      //      VEML6075::DYNAMIC_NORMAL -- Normal dynamic mode
      //      VEML6075::DYNAMIC_HIGH -- High dynamic mode
      // The library defaults the dynamic to normal
      uv.setHighDynamic(VEML6075::DYNAMIC_HIGH);
    }

Now that we\'ve changed around a few of our UV sensors settings, we will read the raw UVA and UVB values along with their compensation values from visible and infrared noise, which are used to calculate the values we obtain from `uv.uva` and `uv.uvb`. The below code reads both raw values as well as calibrated values.

    language:c
    void loop() 

Opening your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) to a baud rate of **9600** will show both raw values as well as calibrated values in the order of **Time, raw UVA, raw UVB, visible compensation, IR compensation, calculated UVA, calculated UVB, calculated UV Index**.

[![Example 2 Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/EX2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX2.PNG)

*Example 2 Output*

### Example 3 - Shutdown

To get started with the third example, open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun VEML6075 UV Sensor** \> **Example3_Shutdown**. In this example, we\'ll go over how to put the sensor into low power shutdown mode. We begin by creating and initializing a **`VEML6075`** object called `uv`. We initialize the object in setup the exact same way as the first example. We then loop through, reading our calibrated UVA and UVB values. Every 50 reads, we switch the power state of the UV sensor. When we put the VEML6075 in shutdown mode, it only draws 800 nA of current while ignoring any reads we attempt to throw at it. The code that handles this is shown below.

    language:c
    const unsigned int READINGS_BETWEEN_SHUTDOWN = 50;

    void loop()  else 
      }
      Serial.println(String((float)millis() / 1000.0) + ": " + String(uv.uva()) + ", " + String(uv.uvb()) + ", " + String(uv.index()));
      numReadings++;

      delay(200);
    }

The part in our serial output where we shut the VEML6075 down is shown below. notice how after the sensor goes into shutdown mode, we always pull the exact same reading from it. This is because it is not longer updating those registers.

[![Example 3 Shutdown](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX3-ShutDown.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX3-ShutDown.PNG)

*Example 3 Shutdown*

After 50 more readings, the UV sensor powers back on and starts taking readings. This process looks like the image below in serial. Notice how the first reading after we turn the sensor back on is garbage.

[![Example 3 Power Up](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/EX3-PowerUp.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX3-PowerUp.PNG)

*Example 3 Power Up*

### Example 4 - Calculate UVI

In this example we will go through the steps of calculating the UV Index from our raw UVA and UVB values, which the library does for you. However, it\'s always good to take a bit of a deeper dive into these things. To begin, go ahead and open up **File** \> **Examples** \> **Examples from Custom Libraries** \> **SparkFun VEML6075 UV Sensor** \> **Example4_Calculate_UVI**. The UV index can be calculated based on the average irradiance of our UVA and UVB light. This irradiance has a linear relation to our UV index, check out the chart below from the VEML6075 Application Guide to see the relationship between irradiance and UV index.

[![UV Index](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/UVIndex.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/UVIndex.PNG)

The VEML6075 is based around a silicon photodiode, which is susceptible to not only UV, but also visible light and wavelengths as low as infrared. This generates undesirable noise in our UV signal, so we factor in values from visible (`uv.visibleCompensation()`) and infrared (`uv.irCompensation()`) noise compensation registers. To get a little more accuracy out of this signal, you\'ll have to calibrate it against the golden sample under a solar simulator like a [Newport LCS-100](https://www.newport.com/f/small-area-solar-simulators), using a calibrated UVI meter such as a [Davis 6490 UVI sensor](https://www.davisinstruments.com/product/uv-sensor/) changing the values of the below constants, located at lines 32-35.

    language:c
    const float CALIBRATION_ALPHA_VIS = 1.0; // UVA / UVAgolden
    const float CALIBRATION_BETA_VIS  = 1.0; // UVB / UVBgolden
    const float CALIBRATION_GAMMA_IR  = 1.0; // UVcomp1 / UVcomp1golden
    const float CALIBRATION_DELTA_IR  = 1.0; // UVcomp2 / UVcomp2golden

The numerator in each of these constants will be the value from your VEML6075 UV sensor, while the denominator will be the value from the Davis UVI sensor. For example, if you were to change the value of α you would divide the UVA measurement from the VEML6075 by the UVA measurement from the Davis 6490. Setting these constants to 1.0 essentially eliminates this calibration. In 90% of cases, this \"golden sample\" calibration won\'t be used, but if you do use it, make sure you calibrate your values once the Qwiic UV Sensor has been placed into it\'s final enclosure.

The main calibration occurs by adjusting the values of the visible and infrared noise compensation we obtain from the UV sensor. The application manual gives us values for the coefficients, shown in lines 47-50.

    language:c
    const float UVA_VIS_COEF_A = 2.22; // a
    const float UVA_IR_COEF_B  = 1.33; // b
    const float UVB_VIS_COEF_C = 2.95; // c
    const float UVB_IR_COEF_D  = 1.75; // d

The responsivity converts the raw 16-bit data from the chip into something in units of W/m^2^. Changing the dynamic and integration time will change the responsivity of the sensor, so be careful changing these values, as you\'ll have to change the responsivity on lines 41-42.

    language:c
    const float UVA_RESPONSIVITY = 0.00110; // UVAresponsivity
    const float UVB_RESPONSIVITY = 0.00125; // UVBresponsivity

After we have all of these constants set up, we initialize our UV sensor like we normally do, then begin reading values from our sensor and doing the necessary math to convert our irradiance values into UV indices. The code in the `void loop()` that accomplishes this is shown below.

    language:c
    void loop() 

The serial output of this example (at a baud rate of **9600**) should look something like the image below.

[![Calculate UVI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/3/8/EX4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/3/8/EX4.PNG)

*Calculate UVI*