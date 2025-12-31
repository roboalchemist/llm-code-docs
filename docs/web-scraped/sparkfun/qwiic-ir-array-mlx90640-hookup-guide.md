# Source: https://learn.sparkfun.com/tutorials/qwiic-ir-array-mlx90640-hookup-guide

## Introduction

The Melexis MLX90640 ([110°](https://www.sparkfun.com/products/14843) and [55°](https://www.sparkfun.com/products/14844) FOV) contains a 32x24 array of thermopile sensors creating, in essence, a low resolution thermal imaging camera. As the images show, you can detect surface temperatures from many feet away with an accuracy of ±1.5°C (best case). We've packaged the MLX90640 on an easy to use Qwiic board with mounting holes and a smattering of decoupling caps.

[![SparkFun IR Array Breakout - 110 Degree FOV, MLX90640 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/1/3/14843-SparkFun_IR_Array_Breakout_-_110_Degree_FOV__MLX90640__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-ir-array-breakout-110-degree-fov-mlx90640-qwiic.html)

### [SparkFun IR Array Breakout - 110 Degree FOV, MLX90640 (Qwiic)](https://www.sparkfun.com/sparkfun-ir-array-breakout-110-degree-fov-mlx90640-qwiic.html) 

[ SEN-14843 ]

The MLX90640 SparkFun IR Array Breakout is equipped with a 110° FOV, 32x24 array of thermopile sensors creating a low resolu...

[ [\$69.95] ]

[![SparkFun IR Array Breakout - 55 Degree FOV, MLX90640 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/1/1/4/14844-SparkFun_IR_Array_Breakout_-_55_Degree_FOV__MLX90640__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-ir-array-breakout-55-degree-fov-mlx90640-qwiic.html)

### [SparkFun IR Array Breakout - 55 Degree FOV, MLX90640 (Qwiic)](https://www.sparkfun.com/sparkfun-ir-array-breakout-55-degree-fov-mlx90640-qwiic.html) 

[ SEN-14844 ]

The MLX90640 SparkFun IR Array Breakout is equipped with a 55° FOV, 32x24 array of thermopile sensors creating a low resolut...

[ [\$69.95] ]

In this guide, we\'ll go over how to connect your Qwiic IR Array with MLX90640 and get it communicating with Processing to produce a nice thermal image.

### Required Materials

**Not Uno Compatible:** The MLX90640 requires complex calculations by the host platform. A regular Uno doesn\'t have enough RAM or flash to complete the complex computations required to turn the raw pixel data into temperature data. You will need a microcontroller with 20,000 bytes or more of RAM. We recommend a Teensy 3.1 or above. Make sure to grab headers if you get a headerless version of the Teensy.

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Teensy 3.2](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/4/9/13736-01.jpg)](https://www.sparkfun.com/products/13736)

### [Teensy 3.2](https://www.sparkfun.com/products/13736) 

[ DEV-13736 ]

The Teensy 3.2 is a breadboard-friendly development board with loads of features in a, well, teensy package.

**Retired**

[![Teensy 3.5 (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/6/14056-01.jpg)](https://www.sparkfun.com/products/14056)

### [Teensy 3.5 (Headers)](https://www.sparkfun.com/products/14056) 

[ DEV-14056 ]

The Teensy 3.5 is larger, faster and capable of more projects, especially with its onboard micro SD card port and pre-soldere...

**Retired**

[![Teensy 3.6 (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/8/9/8/14058-01.jpg)](https://www.sparkfun.com/products/14058)

### [Teensy 3.6 (Headers)](https://www.sparkfun.com/products/14058) 

[ DEV-14058 ]

The Teensy 3.6 is larger, faster and capable of more complex projects, especially with its onboard micro SD card port, ARM Co...

**Retired**

We don\'t have any Qwiic shields available for Teensy, so you should snag yourself a breadboard and a breadboard friendly Qwiic cable if you haven\'t already to get the Teensy connected to the MLX90640.

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Breadboard - Classic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/2/112-_PRT-_01.jpg)](https://www.sparkfun.com/breadboard-classic.html)

### [Breadboard - Classic](https://www.sparkfun.com/breadboard-classic.html) 

[ PRT-00112 ]

Your first exposure to electrical engineering - the bread board. Who knew it would bring so much frustration? This is your ...

[ [\$16.95] ]

[![Breadboard - Translucent Self-Adhesive (Clear)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/3/4/5/09567-01-Working.jpg)](https://www.sparkfun.com/breadboard-translucent-self-adhesive-clear.html)

### [Breadboard - Translucent Self-Adhesive (Clear)](https://www.sparkfun.com/breadboard-translucent-self-adhesive-clear.html) 

[ PRT-09567 ]

\*\*Description\*\*: Ever wonder what goes on inside these things? Well this clear bread board might enlighten. Beyond the cl...

[ [\$6.95] ]

### Tools

Depending on your setup, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49) if you bought a headerless Teensy.

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

Since we\'ll also be using Processing in one of these demos, we\'d recommend looking up the tutorial on hooking your Arduino up to Processing. We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing)

### Connecting Arduino to Processing 

Send serial data from Arduino to Processing and back - even at the same time!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

First, let\'s check out some of the characteristics of the [MLX90640 IR Array](https://cdn.sparkfun.com/assets/7/b/f/2/d/MLX90640-Datasheet-Melexis.pdf) we\'re dealing with, so we know what to expect out of the board. Keep in mind that there are two options for the field of view **110°x75°** and **55°x35°**

  **Characteristic**    **Range**
  --------------------- ----------------
  Operating Voltage     **3V-3.6V**
  Current Consumption   \~18 mA
  Measurement Range     -40 °C - 300°C
  Resolution            ±1.5°C
  Refresh Rate          0.5Hz - 64 Hz
  I^2^C Address         0x33

## Pins

The following table lists all of the MLX90640\'s pins and their functionality.

  Pin    Description   Direction
  ------ ------------- -----------
  GND    Ground        In
  3.3V   Power         In
  SDA    Data          In/Out
  SCL    Clock         In

### Optional Features

The MLX90640 IR Array has pull up resistors attached to the I^2^C bus; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by cutting the traces on the corresponding jumpers highlighted below.

[![I2C Pull Up Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/5/i2cpu1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/5/i2cpu1.png)

*I^2^C Pull Up Jumper*

The onboard LED (highlighted below) will light up when the board is powered, and the sensor (also highlighted below) should be left uncovered in your application.

[![Power LED](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/5/PWRLED1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/5/PWRLED1.png)

*Power LED*

## Hardware Assembly

Since we don\'t have a Qwiic shield for the Teensy at this point in time, we\'ll need to connect our Qwiic Infrared Array through the [breadboard compatible Qwiic cable](https://www.sparkfun.com/products/14425). Check out the following table if you\'re unsure of how to connect your Qwiic cable. The Teensy 3.5 pinout is available [here](https://cdn.sparkfun.com/datasheets/Dev/Arduino/Boards/teensy35_front.pdf). For more pin assigments, refer to the [Teensy\'s reference page](https://www.pjrc.com/teensy/pinout.html).

   **Color**   **Function**     **Pin**
  ----------- -------------- --------------
     Black        Ground      Any GND pin
      Red      Power (3.3V)   Any 3.3V pin
    Yellow        Clock            19
     Blue          Data            18

Once you have your cable hooked up to the breadboard, go ahead and plug it into your MLX90640 IR Array and you\'ll be ready to go.

[![MLX90640 Plugged into Breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/0/5/Qwiic_IR_Array_Teensy_Hardware_Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/5/Qwiic_IR_Array_Teensy_Hardware_Hookup.jpg)

*MLX90640 Plugged into Breadboard*

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Teensyduino Add-On

If you haven\'t used Teensy before, you\'ll probably need to download and install the extension for the Arduino IDE called [Teensyduino, located here.](https://www.pjrc.com/teensy/td_download.html)

### Library

Melexis has written a library to control the Qwiic IR Array with MLX90640. You can obtain these libraries by clicking the below button, which also includes the SparkFun written example sketches from the [GitHub repository](https://github.com/sparkfun/SparkFun_MLX90640_Arduino_Example). Just makes sure the associated files are in the same path when opening each example.

[MLX90640 Library and Examples (ZIP)](https://github.com/sparkfun/SparkFun_MLX90640_Arduino_Example/archive/master.zip)

### Example 1 - Basic Readings

Once you\'ve downloaded the example sketches and library, go ahead and open the first example under **SparkFun_MLX90640_Arduino_Example-master** \> **Firmware** \> **Example1_BasicReadings** \> **Example1_BasicReadings**. To initialize the sensor, we first attempt to talk to the MLX90640 with the `isConnected()` function. Looking closer at our `setup()` loop reveals that we extract a set of paramaters from the MLX using `MLX90640_DumpEE` and `MLX90640_ExtractParamaters`. This only needs to be done once in the `setup()` loop before the board is ready to use, the code is shown below.

    language:c
    void setup()
    
      Serial.println("MLX90640 online!");

      //Get device parameters - We only have to do this once
      int status;
      uint16_t eeMLX90640[832];
      status = MLX90640_DumpEE(MLX90640_address, eeMLX90640);
      if (status != 0)
        Serial.println("Failed to load system parameters");

      status = MLX90640_ExtractParameters(eeMLX90640, &mlx90640);
      if (status != 0)
        Serial.println("Parameter extraction failed");

      //Once params are extracted, we can release eeMLX90640 array
    }

Once you\'ve selected your board and serial port, upload the sketch to your Teensy. Then **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)** set at 115200 baud. The output should look something like the below image, with the temperature values of each pixel being displayed in °C.

[![Example 1 Output](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/5/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/0/5/EX1.PNG)

*Example 1 Output*

### Example 2 - Output To Processing

**Note:** Processing is a software that enables visual representation of data, among other things. If you\'ve never dealt with Processing before, we recommend you also check out the [Arduino to Processing tutorial](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing). Follow the below button to go ahead and download and install Processing.\
\

[Download Processing IDE](https://processing.org/download/)

This next example involves the Processing IDE. Processing listens for serial data, so we\'ll need to get our Arduino producing serial data that makes sense to Processing. To pull up the next example, go to **SparkFun_MLX90640_Arduino_Example-master** \> **Firmware** \> **Example2_OutputToProcessing** \> **Example2_OutputToProcessing** to open the example sketch. This sketch simply prints a comma separated list of our temperatures over serial for Processing to listen to.

Once this sketch is uploaded, we need to tell Processing how to turn this data into a visualization. The Processing sketch to do this is located in the same folder as Example 2. So go to the sketch folder to open the **MLXHeatCam** file in Processing. Attempting to run the sketch will show us available serial ports in the debug window.

[![COM Port Selection](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-DEBUG.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-DEBUG.PNG)

Identify which serial port your Teensy is on. For instance, my Teensy is on COM6, which corresponds to `[1]` in the above image, so I will need to change 0 to 1 in the following line to ensure Processing is listening in the right location.

    language:c
    myPort = new Serial(this, Serial.list()[0], 115200);

Once I\'ve done this, we should be able to run the Processing sketch and it will give us a nice visualization of the pixels on our Qwiic IR Array with MLX90640. Move your face or hand in front of the sensor and see what it looks like on the screen. The output should look similar to the image below. Note that the camera can only hit about 4 Hz due to the data rate over I^2^C. The hypothetical refresh rate of the MLX90640 is 64 Hz, but unless you have a microcontroller capable of a much faster I^2^C rate, you won\'t be hitting framerates anywhere near that.

[![IR Camera](https://cdn.sparkfun.com//assets/parts/1/3/0/1/4/SparkFun_MLX90640_Thermal_Imaging_Camera-Demo.gif)](https://cdn.sparkfun.com//assets/parts/1/3/0/1/4/SparkFun_MLX90640_Thermal_Imaging_Camera-Demo.gif)

*IR Camera Display*