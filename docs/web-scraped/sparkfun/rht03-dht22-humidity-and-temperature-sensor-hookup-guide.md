# Source: https://learn.sparkfun.com/tutorials/rht03-dht22-humidity-and-temperature-sensor-hookup-guide

## Introduction

Measure relative humidity and temperature with the [RHT03 (a.k.a DHT22)](https://www.sparkfun.com/products/10167) low cost sensor on a single wire digital interface connected to an Arduino!

[![Humidity and Temperature Sensor - RHT03](https://cdn.sparkfun.com/r/600-600/assets/parts/4/4/7/2/10167-01.jpg)](https://www.sparkfun.com/products/10167)

### [Humidity and Temperature Sensor - RHT03](https://www.sparkfun.com/products/10167) 

[ SEN-10167 ]

The RHT03 (also known by DHT-22) is a low cost humidity and temperature sensor with a single wire digital interface. The sens...

**Retired**

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

### How to Install FTDI Drivers 

How to install drivers for the FTDI Basic on Windows, Mac OS X, and Linux.

## Hardware Overview

### Pinout

The pins of the RHT03 (DHT22) are labeled in the image below.

[![Annotated RHT03](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/10167-02_pinout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/10167-02_pinout.jpg)

  Pin   RHT03 (DHT22)   Notes
  ----- --------------- -------------------------------------
  1     VCC             Input Voltage between **3.3-6V DC**
  2     DAT             Data Output
  3     N/C             Not Connected
  4     GND             Ground

## Hardware Hookup

**Heads up!** The sensor\'s pins are small. For a more secure connection, you may want to think about eventually [soldering](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) this to a [protoboard](https://www.sparkfun.com/products/12702) after prototyping.

Connect the RHT03 to your Arduino as shown below. Since we are using a 5V Arduino, we will be using 5V to power the sensor. If you are using a 3.3V Arduino, you will need to connect it to a 3.3V pin for your respective development board.

[![Fritzing Diagram of Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/6/SparkFun_Arduino_RHT03_DHT22_Humidity_Temperature_Fritzing_Circuit_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/SparkFun_Arduino_RHT03_DHT22_Humidity_Temperature_Fritzing_Circuit_bb.jpg)

**Note:** A [10k pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors/all) can be added to the data pin, though it seems to work without it. If you really need, you can still add a pull-up resistor between VCC and the data pin.\
\

[![Fritzing Circuit with Pull Up Resistor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/7/6/SparkFun_Arduino_RHT03_DHT22_Resistor_Humidity_Temperature_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/SparkFun_Arduino_RHT03_DHT22_Resistor_Humidity_Temperature_Fritzing_bb.jpg)

**Head\'s Up!** The Fritzing part for the RHT03 (DHT22) can be found in the Fritzing software! Simply type **RHT03** in the parts search.

## Library Installation

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We've written an Arduino library to make reading the RHT03 a breeze. You will need to manually install the [RHT03 Arduino library](https://github.com/sparkfun/SparkFun_RHT03_Arduino_Library) from the GitHub repository by downloading a **\*.zip**. Once downloaded, click **Sketch** \> **Include Library** \> **Add .ZIP Library\...** to have the Arduino IDE unzip the library into it\'s respective folder.

[SparkFun RHT03 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_RHT03_Arduino_Library/archive/master.zip)

## Arduino Example

After installing the library, open the example from the Arduino IDE by clicking **File** \> **Examples** \> **SparkFun RHT03 Arduino Library** \> **RHT03-Example-Serial**. Select the board that you are using (if you are using the RedBoard with the ATmega328P, select **Arduino/Genuino Uno**) and COM port that the board enumerated on and hit upload.

[![Arduino IDE with Upload Button Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/Arduino_IDE_Upload_RHT03_DHT22.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/Arduino_IDE_Upload_RHT03_DHT22.jpg)

Open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) at **9600 baud** to view the output. You should see the relative humidity and temperature in °F and °C. Try blowing some air at the sensor. The sensor should react to the water vapor contained in the exhaled air.

[![Example Output Relative Humidity and Temeprature](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/Arduino_RHT_03_DHT22_Example_Output_Humidity_Temperature.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/7/6/Arduino_RHT_03_DHT22_Example_Output_Humidity_Temperature.jpg)

**Heads up!** You\'ll want to be patient as your Arduino reads the sensor. The example code checks to see if we receive a valid output from the sensor. If we receive a valid reading, the values will update respectively. If you check the [datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Weather/RHT03.pdf), the sensor\'s output is typically is 2 seconds.

## More Examples

Looking for more examples? Check out the following tutorials to read the sensor with other development boards!

### ESP8266

If you are using the ESP8266 with the RHT03 (DHT22), try checking out [experiment 1 of the Internet of Things Experiment Guide](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-1-temperature-and-humidity-logging) to capture temperature and humidity data from a sensor and post it to our ThingSpeak channel.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![ESP8266 Thing Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/4/Exp_01_bb.png)](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-1-temperature-and-humidity-logging)
  *ESP8266 Example [](https://learn.sparkfun.com/tutorials/internet-of-things-experiment-guide/experiment-1-temperature-and-humidity-logging)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Particle Photon

If you are using the Particle Photon with the RHT03 (DHT22), try checking out [experiment 6 of the SparkFun Inventor\'s Kit for Photon Experiment Guide](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-photon-experiment-guide/experiment-6-environment-monitor) to read the serial data with a photocell.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Particle Photon Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/2/EnvironmentLoggerPhoto.jpg)](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-photon-experiment-guide/experiment-6-environment-monitor)
  *Particle Photon Example[](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-photon-experiment-guide/experiment-6-environment-monitor)*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------