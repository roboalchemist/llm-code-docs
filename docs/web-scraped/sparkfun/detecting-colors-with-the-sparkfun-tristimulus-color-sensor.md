# Source: https://learn.sparkfun.com/tutorials/detecting-colors-with-the-sparkfun-tristimulus-color-sensor

## Introduction

In this tutorial, we\'ll show you how to use the SparkFun Tristimulus Color Sensor - OPT4048DTSR (Qwiic) to detect and classify colors based on their CIE XYZ color space values. The sensor is capable of measuring the color intensity in the X, Y, and Z channels, which correspond to red, green, and blue components in a simplified form.

[![SparkFun Tristimulus Color Sensor - OPT4048DTSR (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/2/7/9/8/22638-_SEN_SparkFun_Tristimulus_Color_Sensor-_01.jpg)](https://www.sparkfun.com/sparkfun-tristimulus-color-sensor-opt4048dtsr-qwiic.html)

### [SparkFun Tristimulus Color Sensor - OPT4048DTSR (Qwiic)](https://www.sparkfun.com/sparkfun-tristimulus-color-sensor-opt4048dtsr-qwiic.html) 

[ SEN-22638 ]

The SparkFun Qwiic Tristimulus Color Sensor is built around the OPT4048 High Speed High Precision Tristimulus XYZ Color Senso...

[ [\$13.50] ]

[![SparkFun Mini Tristimulus Color Sensor - OPT4048DTSR (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/2/2/7/9/9/22639-_SEN_SparkFun_Mini_Tristimulus_Color_Sensor-_01.jpg)](https://www.sparkfun.com/sparkfun-mini-tristimulus-color-sensor-opt4048dtsr-qwiic.html)

### [SparkFun Mini Tristimulus Color Sensor - OPT4048DTSR (Qwiic)](https://www.sparkfun.com/sparkfun-mini-tristimulus-color-sensor-opt4048dtsr-qwiic.html) 

[ SEN-22639 ]

The SparkFun Mini Tristimulus Color Sensor - OPT4048DTSR (Qwiic) is built around the OPT4048 High Speed High Precision Tristi...

[ [\$11.50] ]

If you are looking for the full Hookup Guide for the SparkFun Tristimulus Color Sensor - OPT4048DTSR (Qwiic), click the button bellow. This guide only covers a simple project to get you started quickly, while the full Hookup Guide goes over every detail of the sensor.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_Tristimulus_Color_Sensor-OPT4048/introduction/)

 

------------------------------------------------------------------------

## Hardware Needed

To follow this experiment, you will need the following materials. While this is a simple project we wanted to make sure that you have everything you need to get started before we get to the code. For this simple project we chose the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) but you could choose from many of our development boards such as the [Qwiic Pro Micro](https://www.sparkfun.com/products/15795) as well.

 

 

------------------------------------------------------------------------

## Software Setup

**Note:** If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

## Installing the Required Libraries

- **Install the SparkFun OPT4048 Library**: Open the Arduino IDE and navigate to **Sketch \> Include Library \> Manage Libraries**. In the Library Manager, search for **\"OPT4048\"** and install the latest version from SparkFun.

## Read Measurements with a Serial Monitor

Now that we\'ve installed the Arduino library, it\'s time to upload our first sketch to make sure everything is working properly and you are able to read basic measurements with your Serial Monitor in the Arduino IDE.

For this example you will need the [SparkFun Tristimulus Color Sensor - OPT4048DTSR (Qwiic)](https://www.sparkfun.com/products/22638), a [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123), a [Qwiic Cable](https://www.sparkfun.com/products/14427), and a [USB Micro-B Cable](https://www.sparkfun.com/products/10215).

Using the Qwiic system, assembling the hardware is simple. Connect the RedBoard to one of the SparkFun Tristimulus Color Sensor Qwiic ports using your Qwiic cables (please remember to insert this cable in the correct orientation). Then connect the RedBoard to your computer via the MicroUSB cable and voila! You\'re ready to rock!

[![SparkFun Tristimulus Color Sensor to RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/22638-SparkFun_Tristimulus_Color_Sensor-Hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/4/2/24805-Ultrasonic-Distance-Sensor-Action-2.jpg)

*SparkFun Tristimulus Color Sensor to RedBoard*

 

Alternatively, you can copy and paste the code below into a shiny new Arduino sketch:

    #include "SparkFun_OPT4048.h"  // Include the SparkFun OPT4048 library
    #include <Wire.h>  // Include the Wire library for I2C communication

    SparkFun_OPT4048 colorSensor;  // Create an instance of the OPT4048 color sensor

    void setup() 

     colorSensor.setBasicSetup();  // Apply basic setup configuration to the sensor

     Serial.println("Sensor initialized and ready!");  // Print a success message
    }

    void loop() 

    String classifyColor(float x, float y, float z) 

Make sure you\'ve selected the correct board and port in the Tools menu and then hit the upload button. Once the code has finished uploading, go ahead and open a [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics). Set the baud rate to 115200. You should see output like this:

[![Color Readings](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/Color_reading_.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/Color_reading_.png)

## Interpreting the Results

- **CIEx, CIEy, CIEz**: These are the values from the CIE 1931 color space which represent the color\'s chromaticity.
- **Detected Color**: Based on the values, the code attempts to classify the color into a basic category like \"Red,\" \"Green,\" \"Blue,\" etc.

The CIEx and CIEy values are going to fall somewhere between 0 and 1. Page 35 of the [datasheet](https://docs.sparkfun.com/SparkFun_Tristimulus_Color_Sensor-OPT4048/assets/board_files/opt4048.pdf) gives more detail on this, but generally speaking, you can map the predominant color of the space you\'re measuring using the following:

[![CIE Y and X Color Readings](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/CIE-YX-Color-Readings.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/CIE-YX-Color-Readings.jpg)

[![CIE V and U Color Readings](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/CIE-VU-Color-Readings.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/4/4/2/CIE-VU-Color-Readings.jpg)

CIE XY and CIE UV space plots of color coordinates

For more information on the CIE and CIY values, refer to the CIE 1931 [Color Space Wiki Page](https://en.wikipedia.org/wiki/CIE_1931_color_space).

If you see unexpected values or the sensor isn't detected, double-check your wiring and ensure the sensor is properly connected to the I2C bus.