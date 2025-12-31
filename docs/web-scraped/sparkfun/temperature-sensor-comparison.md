# Source: https://learn.sparkfun.com/tutorials/temperature-sensor-comparison

## Introduction

It all started when I wanted to measure the temperature of a room at SparkFun. But what is the best? Well, it depends on what you are looking for in your project. There are a lot of temperatures available. This article will compare a few of the more popular ones we carry.

[![Comparing Three Temperature Sensors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_TMP117_on_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_TMP117_on_Arduino.jpg)

### Required Materials

To follow along with this comparison guide, you will need the following parts at a minimum to connect to the sensors. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Qwiic Cable - Breadboard Jumper (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/1/14425-Qwiic_Cable_-_Breadboard_Jumper__4-pin_-01.jpg)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html)

### [Qwiic Cable - Breadboard Jumper (4-pin)](https://www.sparkfun.com/qwiic-cable-breadboard-jumper-4-pin.html) 

[ PRT-14425 ]

This is a jumper adapter cable that comes pre-terminated with a female Qwiic JST connector on one end and a breadboard hookup...

**Retired**

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![Breadboard - Mini Modular (Blue)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/6/2/8/12045-01.jpg)](https://www.sparkfun.com/breadboard-mini-modular-blue.html)

### [Breadboard - Mini Modular (Blue)](https://www.sparkfun.com/breadboard-mini-modular-blue.html) 

[ PRT-12045 ]

This blue Mini Breadboard is a great way to prototype your small projects! With 170 tie points there\'s just enough room to bu...

[ [\$4.60] ]

[![Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/2/14426-Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-50mm.html)

### [Qwiic Cable - 50mm](https://www.sparkfun.com/qwiic-cable-50mm.html) 

[ PRT-14426 ]

This is a 50mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together ...

**Retired**

### Tools

Depending on your project, you may need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

### Suggested Reading

If you aren't familiar with the following concepts below or linked throughout the comparison guide, we recommend checking out these tutorials before continuing if you decide to recreate these tests.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

## Analog vs Digital Sensor

Before we compare temperature sensors, it would be good to know differences between an analog and digital sensor.

#### Analog Sensor

An analog sensor takes a reading and outputs a smooth, continuous signal.

[![example analog signal that is smoooth](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Analog_Signal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Analog_Signal.png)

*Example of a smooth, continuous analog signal.*

These are usually low cost and easy to use, which is great for beginners. However, they do require an analog-to-digital converter (ADC) to read the output. Microcontrollers (like an Arduino Uno/RedBoard Qwiic) have this built in (I\'ve yet to come across one without an analog input). Single board computers (like the Raspberry Pi) on the other hand, do not have a hardware ADC and requires a dedicated chip to read the sensor.

Depending on the sensor, you may need to build an additional circuit to read or filter the signal. Sensor readings are more susceptible to noise from power supplies and other components in the circuit. The wire length may also affect the readings over long distances.

#### Digital Sensor

A digital sensor outputs a signal with discrete steps.

[![example digital signal that is discrete](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Digital_Signal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Digital_Signal.png)

*Example of a discrete digital signal.*

These can cost more. However, they are easier to include in a design since they require a serial protocol to the output. Microcontrollers and single board computers should have the basic serial protocols (I^2^C, UART, SPI) built in. You\'ll just need to make sure there is a library for the architecture and your preferred programming language.

Digital sensors may include additional features. No additional circuitry needs to be built if the chip is on a breakout board. These sensors are not as likely to be affected by the power supply and other components in the circuit. While serial protocols have limitations in the overall length, the sensor readings are not affect by the wire length like an analog sensor.

**Note:** For more information, check out our [Analog vs. Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital) and [Analog to Digital Conversion](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) tutorials.\
\

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

July 18, 2013

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

February 7, 2013

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

## Round 1: TMP117 vs TMP102 vs TMP36

For simplicity, let\'s compare three [temperature sensors from the SparkFun catalog](https://www.sparkfun.com/categories/305) in this round! We\'ll be measuring the ambient temperature of the air using these sensors.

[ ![Temperature Sensor - TMP36](https://cdn.sparkfun.com/r/600-600/assets/parts/4/1/8/8/10988-01.jpg) ]

### Temperature Sensor - TMP36 

[ SEN-10988 ]

This is the same temperature sensor that is included in our \[SparkFun Inventor\'s Kit\](http://www.sparkfun.com/products/12060)...

**Retired**

[![SparkFun Digital Temperature Sensor Breakout - TMP102](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/9/3/13314-01a.jpg)](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html)

### [SparkFun Digital Temperature Sensor Breakout - TMP102](https://www.sparkfun.com/sparkfun-digital-temperature-sensor-breakout-tmp102.html) 

[ SEN-13314 ]

The TMP102 is an easy-to-use digital temperature sensor from Texas Instruments. The TMP102 breakout allows you to easily inco...

[ [\$5.95] ]

[![SparkFun High Precision Temperature Sensor - TMP117 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/4/3/0/15805-SparkFun_High_Precision_Temperature_Sensor_-_TMP117__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-high-precision-temperature-sensor-tmp117-qwiic.html)

### [SparkFun High Precision Temperature Sensor - TMP117 (Qwiic)](https://www.sparkfun.com/sparkfun-high-precision-temperature-sensor-tmp117-qwiic.html) 

[ SEN-15805 ]

The SparkFun Qwiic TMP117 Breakout is a high precision temperature sensor equipped with an I2C interface.

[ [\$16.95] ]

### TMP36

We\'ll connect the TMP36 using the [circuit from the SIK](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41/circuit-4b-temperature-sensor).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Fritzing Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_Temperature_Sensor_Comparison_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_Temperature_Sensor_Comparison_bb.jpg)   [![RedBoard Qwiic and TMP36 Connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_on_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_on_Arduino.jpg)
  *Fritzing Circuit Diagram*                                                                                                                                                                                                                                                          *RedBoard Qwiic and TMP36 Connected*
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is the modified example code from the SIK to output to the serial monitor. Grab the code and upload to your Arduino if you are trying to follow along!

    language:c
    /******************************************************************************
      TMP36.ino
      Written by Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: Nov 4, 2019
      https://gist.github.com/bboyho/c30b70fc308f41b92a6f1b07e5a54838

      Description: This sketch configures temperature sensor and prints the
      temperature in degrees celsius and fahrenheit. Simply adjust the `output_select`
      to view the °C, °F, or both. Open the Serial Monitor or Plotter at 115200 baud 
      to view the data.

      Development Environment Specifics:
      Arduino 1.8.9+

      License:
      This code is released under the MIT License (http://opensource.org/licenses/MIT)
      Distributed as-is; no warranty is given.

    ******************************************************************************/

    //variables for TMP36
    float tmp36_voltage = 0;                      //the voltage measured from the TMP36
    float tmp36_degC = 0;                         //the temperature in Celsius, calculated from the voltage
    float tmp36_degF = 0;                         //the temperature in Fahrenheit, calculated from the voltage

    //0 = output degrees °C
    //1 = output degrees °F
    //any other number = output degrees °C and °F
    int output_select = 1; //select output

    void setup() 
      else if (output_select == 1) 
      else 
    }// end setup

    void loop() 
      else if (output_select == 1) 
      else 

      delay(5); // Delay added for easier readings

    }//end loop

Let\'s observe the output that was taken at that moment to measure the ambient temperature of the room. The temperature reading seems to jump around between 75.5°F and 76.5°F. Other times, the output would spike. (This was probably due to the TMP36 being built on a breadboard or noise from the power supply). Adding a decoupling capacitor between Vcc and GND helped smooth the signal but I would still get small spikes in the readings.

[![TMP36 Output on the Arduino Serial Plotter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_Noisy.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_Noisy.png)

*Click image for a closer view.*

### TMP102 vs TMP36

Can we get a more precise reading? Why yes we can! Let\'s try using a digital temperature sensor to compare. I soldered headers to the TMP102 and included it on the breadboard [based off the TMP102 hookup guide](https://learn.sparkfun.com/tutorials/tmp102-digital-temperature-sensor-hookup-guide#hardware-connections). Using the Qwiic cable to breadboard adapter made it quick to connect the sensor to the RedBoard.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Fritzing Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_TMP102_Temperature_Sensor_Comparison_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_TMP102_Temperature_Sensor_Comparison_bb.jpg)   [![RedBoard Qwiic, TMP36, and TMP102 Connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_on_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_on_Arduino.jpg)
  *Fritzing Circuit Diagram*                                                                                                                                                                                                                                                                        *RedBoard Qwiic, TMP36, and TMP102 Connected*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The code was adjusted to output both the TMP36 and TMP102 in the serial monitor for comparison. Additionally, address of the TMP102 was adjusted to **0x49** to compare with the TMP117. Grab the code and upload it to your Arduino if you are trying to follow along!

    language:c
    /******************************************************************************
      TMP102vsTMP36.ino
      Written by: Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: Nov 4, 2019

      Description: This sketch configures temperature sensors and prints the
      temperature in degrees celsius and fahrenheit. For comparison, the
      TMP102 and TMP36 temperature sensor is also printed to compare the output
      in degrees celsius and fahrenheit. Simply adjust the `output_select`
      to view the °C, °F, or both. Open the Serial Monitor or Plotter at 115200 baud 
      to view the data.

      Resources/Libraries:
      Wire.h (included with Arduino IDE)
      SparkFunTMP102.h (included in the src folder) https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library

      Development Environment Specifics:
      Arduino 1.8.9+

      License:
      This code is released under the MIT License (http://opensource.org/licenses/MIT)
      Distributed as-is; no warranty is given.

    ******************************************************************************/

    #include <Wire.h>            // Used to establish serial communication on the I2C bus
    #include "SparkFunTMP102.h" // Used to send and recieve specific information from our sensor

    // The default address of the device is 0x48 = (GND) like the TMP117
    // but it's already being used so we use a different address
    TMP102 sensor0; //initialize sensor

    //variables for TMP36
    float tmp36_voltage = 0;                          //the voltage measured from the TMP36
    float tmp36_degC = 0;                         //the temperature in Celsius, calculated from the voltage
    float tmp36_degF = 0;                         //the temperature in Fahrenheit, calculated from the voltage

    //0 = output degrees °C
    //1 = output degrees °F
    //any other number = output degrees °C and °F
    int output_select = 1; //select output

    void setup()
    
      else if (output_select == 1) 
      else 
    }

    void loop()
    
      else if (output_select == 1) 
      else 

      delay(50); // Delay added for easier readings
    }

After taking a set of datapoints at a different moment to measure the ambient temperature of the room, the TMP102 performed better. The temperature readings remained stable and was not as noisy. It is a bit difficult to see in the graph but by opening the serial monitor, the temperature readings only jump around 76.52°F and 76.64°F.

[![TMP36 and TMP102 Output on the Arduino Serial Plotter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_TMP102.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_TMP102.png)

*Click image for a closer view.*

### TMP117 vs TMP102 vs TMP36

Not bad but can we get an even better temperature reading? Why yes we can! Connecting the TMP117 was easier since all that was needed for the [circuit was to add a Qwiic cable](https://learn.sparkfun.com/tutorials/qwiic-tmp117-high-precision-digital-temperature-sensor-hookup-guide#hardware-hookup) between the RedBoard Qwiic and the TMP117.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Fritzing Circuit Diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_TMP102_TMP117_Temperature_Sensor_Comparison_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Fritzing_Arduino_TMP36_TMP102_TMP117_Temperature_Sensor_Comparison_bb.jpg)   [![RedBoard Qwiic, TMP36, TMP102, and TMP117 Connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_TMP117_on_Arduino.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Temperature_TMP36_TMP102_TMP117_on_Arduino.jpg)
  *Fritzing Circuit Diagram*                                                                                                                                                                                                                                                                                      *RedBoard Qwiic, TMP36, TMP102, and TMP117 Connected*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The code was adjusted once again to compare the TMP117 against the other sensors. Grab the code and upload it to your Arduino if you are trying to follow along!

    language:c
    /******************************************************************************
      TMP117vsTMP102vsTMP36.ino
      Written by: Ho Yun "Bobby" Chan
      @ SparkFun Electronics
      Date: Nov 4, 2019

      Description: This sketch configures temperature sensors and prints the
      temperature in degrees celsius and fahrenheit. For comparison, the
      TMP117, TMP102, and TMP36 temperature sensor is also printed to compare the output
      in degrees celsius and fahrenheit. Simply adjust the `output_select`
      to view the °C, °F, or both. Open the Serial Monitor or Plotter at 115200 baud 
      to view the data.

      Resources/Libraries:
      Wire.h (included with Arduino IDE)
      SparkFunTMP117.h (included in the src folder) http://librarymanager/All#SparkFun_TMP117
      SparkFunTMP102.h (included in the src folder) https://github.com/sparkfun/SparkFun_TMP102_Arduino_Library

      Development Environment Specifics:
      Arduino 1.8.9+

      License:
      This code is released under the MIT License (http://opensource.org/licenses/MIT)
      Distributed as-is; no warranty is given.

    ******************************************************************************/

    /*
      NOTE: For the most accurate readings using the TMP117:
      - Avoid heavy bypass traffic on the I2C bus
      - Use the highest available communication speeds
      - Use the minimal supply voltage acceptable for the system
      - Place device horizontally and out of any airflow when storing
      For more information on reaching the most accurate readings from the sensor,
      reference the "Precise Temperature Measurements with TMP116" datasheet that is
      linked on Page 35 of the TMP117's datasheet
    */

    #include <Wire.h>            // Used to establish serial communication on the I2C bus
    #include <SparkFun_TMP117.h> // Used to send and recieve specific information from our sensor
    #include "SparkFunTMP102.h" // Used to send and recieve specific information from our sensor

    // The default address of the device is 0x48 = (GND)
    TMP117 sensor; // Initalize sensor

    // The default address of the device is 0x48 = (GND) as well
    // but it's already being used so we use a different address
    TMP102 sensor0; //initialize sensor

    //variables for TMP36
    float tmp36_voltage = 0;                          //the voltage measured from the TMP36
    float tmp36_degC = 0;                         //the temperature in Celsius, calculated from the voltage
    float tmp36_degF = 0;                         //the temperature in Fahrenheit, calculated from the voltage

    //0 = output degrees °C
    //1 = output degrees °F
    //any other number = output degrees °C and °F
    int output_select = 1; //select output

    void setup()
    
        else if (output_select == 1) 
        else 
      }
      else
      
    }

    void loop()
    
        else if (output_select == 1) 
        else 

        //delay(5); // Delay added for easier readings
      }
    }

After taking another set of datapoints at a different time, the TMP117 performed better than the TMP102 and TMP36. The datapoints were more smooth and less prone to noise. Looking closer at the values via the serial monitor, the temperature readings would jump between 75.99°F and 76.02°F with the TMP117. In one instance, the TMP36\'s output started spiking just was we saw in the initial tests using a TMP36.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![TMP36, TMP102, TMP117 Output on the Arduino Serial Plotter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_TMP102_TMP117.png "TMP36, TMP102, TMP117 Output on the Arduino Serial Plotter")](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/Arduino_Serial_Plotter_TMP36_TMP102_TMP117.png) | [![TMP36, TMP102, TMP117 Output with Spikes in Readings on the Arduino Serial Plotter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/6/4/TMP36_Spikes_Temperature_Sensor.png "TMP36, TMP102, TMP117 Output with Spikes in Readings on the Arduino Serial Plotter")](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/6/4/TMP36_Spikes_Temperature_Sensor.png) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Click image for a closer view.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Good, Better, Best? Which is the Best?

So, you might ask, which of the three temperature sensors is the best? Well, that really depends on how you plan to use it. In my opinion, the Qwiic TMP117 is a winner in my eyes for this round. It is able to measure the temperature of a room without a lot of jitter and it was easy to connect with the Qwiic system. The sensors performed as expected when looking at the datasheet. The board did not require any soldering. There was no additional circuitry that needed to build or code needed to average the temperature sensor readings. The power supply did not cause as much of a fluctuation with the digital temperature sensors like the analog temperature sensor.

The TMP102 could work as well if I was not looking for such precise temperature reading of the room. While it is not as expensive as the TMP117, it does require some soldering for this version of the TMP102 board ^[\[\ 1\ \]](#qwiic_tmp102)^. The TMP36 is good but it would require a bit more effort to filter out the errors.

[\[ 1 \]](#qwiic_tmp102) **Note:** At the time of writing, we had not released the Qwiic version of the TMP102. Check ont the \"qwiic-er\" way to connect with the [Qwiic TMP102](https://www.sparkfun.com/products/16304)!

### Other Considerations

For simplicity, three sensors were used as a comparison out of the box to measure the ambient temperature of the air. This did not take into account other factors such as:

- offset temperature of each sensor
- other microcontrollers with higher ADC to compare the analog sensor
- range (e.g. are you measuring the temperature of an object at room temperature or in an oven)
- medium (e.g. are you measuring the temperature of an object in air or submerged in water)
- current consumption
- temperature sensors that have the ability to also measure the humidity, barometric pressure, and altitude

#### [] [Improving TMP36 Readings](#improving_tmp36_readings)

There are also techniques to improve on the TMP36 temperature readings that were:

- [averaging the TMP36 values](https://gist.github.com/bboyho/2dced710f24ce3aeb021c8607af05f1e)
- adding [decoupling capacitor](https://learn.sparkfun.com/tutorials/capacitors/application-examples#decoupling)
- adjusting the analog reference voltage to 3.3V for the TMP36