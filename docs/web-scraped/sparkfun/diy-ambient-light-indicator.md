# Source: https://learn.sparkfun.com/tutorials/diy-ambient-light-indicator

## Introduction

In this tutorial, we'll walk through how to use the SparkFun Ambient Light Sensor - VEML7700 (Qwiic) to accurately detect the brightness of your surroundings. This sensor measures light intensity in lux, giving output values that closely match human eye sensitivity from very dim to direct sunlight. With its easy I²C Qwiic connection, the VEML7700 makes it simple to integrate ambient light sensing into your projects for display dimming, energy-efficient lighting systems, or environmental data logging.

[![SparkFun Ambient Light Sensor - VEML7700 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/3/1/0/8/8/29211-Ambient-Light-Sensor-Feature_1.jpg)](https://www.sparkfun.com/sparkfun-ambient-light-sensor-veml7700-qwiic.html)

### [SparkFun Ambient Light Sensor - VEML7700 (Qwiic)](https://www.sparkfun.com/sparkfun-ambient-light-sensor-veml7700-qwiic.html) 

[ SEN-29211 ]

The SparkFun Qwiic VEML7700 Ambient Light Sensor delivers precise 16-bit lux readings via I2C, featuring Arduino and Python l...

[ [\$6.95] ]

If you are looking for the full Hookup Guide for the SparkFun Ambient Light Sensor - VEML7700 Qwiic, click the button bellow. This guide only covers a simple project to get you started quickly, while the full Hookup Guide goes over every detail of the sensor.

[View the Full Hookup Guide](https://docs.sparkfun.com/SparkFun_Ambient_Light_Sensor-VEML7700/introduction/)

 

------------------------------------------------------------------------

## Hardware Needed

[![Redboard to Ambient Light Sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/7/0/Ambient-Light-Sensor-QCC-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/7/0/Ambient-Light-Sensor-QCC-1.jpg)

For this project, you\'ll need:

- [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

- [SparkFun Ambient Light Sensor (VEML7700)](https://www.sparkfun.com/sparkfun-ambient-light-sensor-veml7700-qwiic.html)

- [SparkFun Qwiic Button - Green LED](https://www.sparkfun.com/sparkfun-qwiic-button-green-led.html)

- [Qwiic cables - 2x](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html)

- [USB cable to connect RedBoard → computer](https://www.sparkfun.com/catalogsearch/result/?q=usb+cable)

------------------------------------------------------------------------

## Software Setup

### Getting Started with the Arduino IDE

This guide assumes users are utilizing the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino IDE, library, or board add-on, please review the following tutorials:

- [Installing the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [Installing Board Definitions in the Arduino IDE](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

## Installing the Required Libraries and Sketch

- **Install the SparkFun_Qwiic_Button and SparkFun_VEML7700_Arduino_Library**: Open the Arduino IDE and navigate to **Sketch \> Include Library \> Manage Libraries**. In the Library Manager, search for **\"SparkFun Qwiic Button and Sparkfun VEML7700\"** and install the latest versions of each from SparkFun.

You can now copy and paste the code below into a fresh Arduino sketch:

    #include <Wire.h>
    #include <SparkFun_Qwiic_Button.h>
    #include <SparkFun_VEML7700_Arduino_Library.h>

    QwiicButton button;
    VEML7700 lightSensor;

    void setup() 
        Serial.println("Button found.");

        // Initialize the ambient light sensor
        if (!lightSensor.begin()) 
        Serial.println("Light sensor found.");

        button.LEDon(0); // Start with LED on, but low brightness
    }

    void loop() 

            Serial.println("Button released.");
        } else 

If you can\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) is a great place to search product forums and ask questions.

**Account Registration Required:** If this is your first visit to our forum, you\'ll need to create a [Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to post questions.