# Source: https://learn.sparkfun.com/tutorials/qwiic-grid-eye-infrared-array-amg88xx-hookup-guide

## Introduction

The [Grid-EYE](https://www.sparkfun.com/products/14607) from Panasonic is an 8x8 thermopile array. This means you have a square array of 64 pixels each capable of independent temperature detection. It's like having thermal camera (or [Predator's vision](https://www.youtube.com/watch?v=OW1gGDbO_1U)), just in really low resolution. It\'s part of SparkFun\'s [Qwiic system](https://www.sparkfun.com/categories/399), so it is easier to connect to get your low-resolution infrared image.

[![SparkFun Grid-EYE Infrared Array Breakout - AMG8833 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/7/5/14607-SparkFun_GridEYE_Infrared_Array_-_AMG8833__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-grid-eye-infrared-array-breakout-amg8833-qwiic.html)

### [SparkFun Grid-EYE Infrared Array Breakout - AMG8833 (Qwiic)](https://www.sparkfun.com/sparkfun-grid-eye-infrared-array-breakout-amg8833-qwiic.html) 

[ SEN-14607 ]

The SparkFun Grid-EYE Infrared Array Breakout board is an 8x8 thermopile array, giving you a square of 64 pixels capable of i...

[ [\$47.50] ]

In this hookup guide, we\'ll connect our sensor up to our microcontroller of choice and read the array simply as 0\'s and 1\'s in an Arduino Serial Monitor. We\'ll also read the interrupt array to find out which pixels are detecting a value higher than a certain threshold. We\'ll go over how to check the temperature of the chip itself using the built in thermistor. Once we figure out how to interface with the GRID-Eye in our Arduino IDE, we\'ll move over to Processing to get some neat visuals from our pixel array, and actually get a nice looking thermal camera.

### Required Materials

To get started, you\'ll need a microcontroller to control everything in your project.

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

Now to get your microcontroller into the Qwiic ecosystem, the key will be one of the following Qwiic shields to match your preference of microcontroller:

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

You will also need a Qwiic cable to connect the shield to your GRID-Eye, choose a length that suits your needs.

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

If you aren\'t familiar with our new Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic). We would also recommend taking a look at the hookup guide for the Qwiic Shield if you haven\'t already. Brushing up on your skills in I^2^C is also recommended, as all Qwiic sensors are I^2^C. Since we\'ll also be using Processing in one of these demos, we\'d recommend looking up the tutorial on hooking your Arduino up to Processing.

[](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing)

### Connecting Arduino to Processing 

Send serial data from Arduino to Processing and back - even at the same time!

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

## Hardware Overview

Let\'s look over a few characteristics of the Qwiic Grid-EYE so we know a bit more about how it behaves.

  **Characteristic**               **Range**
  -------------------------------- ---------------------------------------------------------
  Operating Voltage(Startup)       1.6V - 3.6V
  Operating Voltage(Timekeeping)   1.5V - 3.6V
  Operating Temperature            -40&degC - 85&degC
  Time Accuracy                    &plusmn2.0 ppm
  Temperature Accuracy             &plusmn2.5&degC
  Current Consumption              4.5 mA
  I^2^C Address                    **0x69 (open jumper, default)** or 0x68 (closed jumper)

### Pins

The characteristics of the available pins on the Grid-EYE are outlined in the table below.

  Pin Label   Pin Function         Input/Output     Notes
  ----------- -------------------- ---------------- -------------------------------------------------------------------------------------
  3.3V        Power Supply         Input            Should be between **1.95 - 3.6V**
  SDA         I^2^C Data Signal    Bi-directional   Bi-directional data line. Voltage should not exceed power supply (e.g. 3.3V).
  SCL         I^2^C Clock Signal   Input            Master-controlled clock signal. Voltage should not exceed power supply (e.g. 3.3V).
  INT         Interrupt            Output           Interrupt pin, digital output.
  GND         Ground               Input            0V/common voltage.

\

### Optional Features

#### Pull-Up Resistors

The Qwiic GRID-Eye has onboard I^2^C pull-up resistors; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by removing the solder on the corresponding jumpers highlighted below.

[![I2C Pullup Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/6/I2CPU.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/I2CPU.png)

#### I^2^C Address

There is an additional jumper on the back of the board that allows the I^2^C to be changed from the default **0x69** to 0x68 if you have multiple GRID-Eye cameras on the same I^2^C bus. Normally open, the jumper sets the I^2^C address to 0x69. Closing the jumper with solder will give an I^2^C address of 0x68. However, if you have more than 2 GRID-Eye\'s, you\'ll need the [Qwiic Mux](https://www.sparkfun.com/products/14293) to have them all on the same I^2^C bus. The jumper is highlighted below.

[![Address Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/6/ADDR.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/ADDR.png)

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the GRID-Eye breakout, the other into the Qwiic Shield of your choice and you\'ll be ready to upload a sketch and figure out how far away you are from that thing over there. It seems like it\'s too easy too use, but that\'s why we made it that way!

[![Connected GridEYE to Arduino](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/4/6/Qwiic_GridEYE-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/Qwiic_GridEYE-03.jpg)

## Arduino Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to control the Qwiic GRID-Eye. You can obtain these libraries through the Arduino Library Manager. Search for **SparkFun GridEYE AMG88 Library** and you should be able to install the latest version. If you prefer downloading the libraries manually you can grab them from the [GitHub repository](https://github.com/sparkfun/SparkFun_GridEYE_Arduino_Library/):

[Download the SparkFun GRID-Eye Library (ZIP)](https://github.com/sparkfun/SparkFun_GridEYE_Arduino_Library/archive/master.zip)

### Example 1 - Serial Visualizer

Once you\'ve installed the Grid-EYE library, restart Arduino. Then go to **File** \> **Examples** \> **SparkFun GridEYE AMG88 Library** \> **Example1-SerialVisualizer** to open the example sketch.

Once you\'ve set your Board and Serial Port, upload the sketch to your Arduino. Then **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**. You\'ll begin to see an 8x8 array of numbers between 0 and 3. The Arduino is mapping the values in between the temperatures between `HOT` and `COLD` to values between 0 and 3, these values are then represented by a `.` for 0, `o` for 1, `0`for 2, and `O` for 3. Try moving in front of the camera and see if any values change. Play around with the values of `HOT` and `COLD` as well to see different ranges of temperatures mapped from 0 to 3. Notice how we use the function `grideye.getPixelTemperature(i)` to get the temperature of pixel `i`, where `i` is between 0 and 64. With these temperatures mapped to a grid, the output should look something like the below image.

[![Serial Pixel Visualizer](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX1.PNG)

### Example 2 - Using Interrupts

To pull up the next example, go to **File** \> **Examples** \> **SparkFun GridEYE AMG88 Library** \> **Example2-UsingInterrupts** to open the example sketch.

Once you\'ve loaded this example up to your microcontroller, go ahead and check out the `void setup()` loop. We set up how the Interrupts are triggered with the following code.

    language:c
    grideye.setInterruptModeAbsolute();
    grideye.setUpperInterruptValue(UPPER_LIMIT);
    grideye.setLowerInterruptValue(LOWER_LIMIT);
    grideye.setInterruptHysteresis(HYSTERESIS);

Where `UPPER_LIMIT`, `LOWER_LIMIT`, and `HYSTERESIS` are declared above. Opening the serial monitor will display a table of which interrupts have been fired, if any. Play around with the values of `UPPER_LIMIT`, `LOWER_LIMIT`, and `HYSTERESIS` and observe their effect on the firing of interrupts. The interrupt table should look similar to the below image, obviously with different interrupts firing depending on what the Grid-EYE is looking at.

[![Interrupt Table](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX2.PNG)

### Example 3 - Device Temperature

To pull up the next example, go to **File** \> **Examples** \> **SparkFun GridEYE AMG88 Library** \> **Example3-DeviceTemperature** to open the example sketch. This example is relatively simple, and merely checks the devices temperature. To get device temperature, there are 3 functions we can use, `getDeviceTemperature()`, which returns our temperature in Celsius, `getDeviceTemperatureFahrenheit()`, which returns our temperature in Fahrenheit `getDeviceTemperatureRaw()` returns the raw binary content of the thermistor register. Opening the serial monitor should yield an image similar to the one below.

[![Device Temperature](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX3.PNG)

### Example 4 - Processing Heat Cam

**Note:** Processing is a software that enables visual representation of data, among other things. If you\'ve never dealt with Processing before, we recommend you also check out the [Arduino to Processing tutorial](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing). Follow the below button to go ahead and download and install Processing.\
\

[Download Processing IDE](https://processing.org/download/)

This next example involves the Processing IDE. Processing listens for serial data, so we\'ll need to get our Arduino producing serial data that makes sense to Processing. To pull up the next example, go to **File** \> **Examples** \> **SparkFun GridEYE AMG88 Library** \> **Example4-ProcessingHeatCam** to open the example sketch. This sketch simply prints a comma separated list of our temperatures over serial for Processing to listen to.

Once this sketch is uploaded, we need to tell Processing how to turn this data into a visualization. The Processing sketch to do this is located in the same folder as Example 4. So go to **Documents** \> **Arduino** \> **SparkFun_GridEYE_AMG88_Library** \> **examples** \> **Example4-ProcessingHeatCam** \> **HeatCam** and open the **HeatCam** file in Processing. Attempting to run the sketch will show us available serial ports in the debug window.

[![COM Port Selection](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-DEBUG.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-DEBUG.PNG)

Identify which serial port your Arduino is on, for instance, my RedBoard is on COM6, which corresponds to `[1]` in the above image, so I will need to change 0 to 1 in the following line to ensure Processing is listening in the right location.

    language:c
    myPort = new Serial(this, Serial.list()[0], 115200);

Once I\'ve done this, we should be able to run the Processing sketch and it will give us a nice visualization of the pixels on our Grid-EYE. Move your face or hand in front of the sensor and see what it looks like on the screen. The output should look similar to the below image, which is output from the Grid-EYE being pointed at a glass of ice water and a lava lamp.

[![Processing Heat Cam](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-HEATCAM.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX4-HEATCAM.PNG)

### Example 5 - Hot Pixel

To pull up the next example, go to **File** \> **Examples** \> **SparkFun GridEYE AMG88 Library** \> **Example5-HotPixel** to open the example sketch. This example runs through each pixel and finds the hottest one, then outputs the location and temperature of that pixel. It does this by comparing the current `hotPixelValue` temperature to the temperature of the current pixel. If the current pixel is hotter, its value is stored in `hotPixelValue`. The output of this sketch should look something like the below image.

[![Hot Pixel](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX5.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/4/6/EX5.PNG)