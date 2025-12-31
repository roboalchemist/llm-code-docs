# Source: https://learn.sparkfun.com/tutorials/air-velocity-sensor-breakout---fs3000-hookup-guide

## Introduction

Need to keep track of the airflow in your data center or around your servers? How about making sure your HVAC and air control systems are functioning at full capacity? Or, if you\'re more fun, what about figuring out how fast your RC airplane is going? Well, the SparkFun Air Velocity Sensor Breakout - [FS3000-1005](https://www.sparkfun.com/products/18377) and [FS3000-1015](https://www.sparkfun.com/products/18768) can help you with all that and more! It\'s super easy, super Qwiic to hookup, and super fun to play with. Let\'s have a look!

[![SparkFun Air Velocity Sensor Breakout - FS3000-1005 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/7/5/9/18377-SparkFun_Air_Velocity_Sensor_Breakout_-_FS3000__Qwiic_01.jpg)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-breakout-fs3000-1005-qwiic.html)

### [SparkFun Air Velocity Sensor Breakout - FS3000-1005 (Qwiic)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-breakout-fs3000-1005-qwiic.html) 

[ SEN-18377 ]

The SparkFun FS3000-1005 Qwiic Air Velocity Sensor Breakout can help you accurately determine the speed and consistency of ai...

[ [\$60.95] ]

[![SparkFun Air Velocity Sensor Breakout - FS3000-1015 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/3/2/3/18768-_SEN_SparkFun_Air_Velocity_Sensor-_01.jpg)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-breakout-fs3000-1015-qwiic.html)

### [SparkFun Air Velocity Sensor Breakout - FS3000-1015 (Qwiic)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-breakout-fs3000-1015-qwiic.html) 

[ SEN-18768 ]

The SparkFun FS3000-1015 Qwiic Air Velocity Sensor Breakout can help you accurately determine the speed and consistency of ai...

[ [\$79.50] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

**Note:** If you decide to use the [Artemis RedBoard Nano](https://learn.sparkfun.com/tutorials/hookup-guide-for-the-sparkfun-redboard-artemis-nano), make sure to [install the Arduino Board Add-On in Arduino](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide/installing-a-third-party-board-definition) and select the appropriate board when uploading code!\
\

[![SparkFun Air Velocity Sensor Qwiic Kit - FS3000-1005](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/1/0/1/21309-_KIT_SparkFun_Air_Velocity_Sensor_Qwiic_Kit-_01.jpg)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-qwiic-kit-fs3000-1005.html)

### [SparkFun Air Velocity Sensor Qwiic Kit - FS3000-1005](https://www.sparkfun.com/sparkfun-air-velocity-sensor-qwiic-kit-fs3000-1005.html) 

[ KIT-21309 ]

The SparkFun Air Velocity Sensor Qwiic Kit comes with everything you need to get started using the FS3000-1005 Air Velocity S...

**Retired**

[![SparkFun Air Velocity Sensor Qwiic Kit - FS3000-1015](https://cdn.sparkfun.com/r/600-600/assets/parts/2/1/1/0/2/21310-_KIT-_01.jpg)](https://www.sparkfun.com/sparkfun-air-velocity-sensor-qwiic-kit-fs3000-1015.html)

### [SparkFun Air Velocity Sensor Qwiic Kit - FS3000-1015](https://www.sparkfun.com/sparkfun-air-velocity-sensor-qwiic-kit-fs3000-1015.html) 

[ KIT-21310 ]

The SparkFun Air Velocity Sensor Qwiic Kit comes with everything you need to get started using the FS3000-1015 Air Velocity S...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, take a look [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

### FS3000

The FS3000 is a surface-mount type air velocity module utilizing a MEMS thermopile-based sensor. It features a digital output with 12-bit resolution and comprises a "solid" thermal isolation technology and silicon carbide coating to protect it from abrasive wear and water condensation.

There are two versions of this sensor with different upper ranges (1005/1015). The 1005 version which can sense 0 to 7.23m/s (0 to 16.17mph) and 1015 version which can sense 0 to 15m/s (0 to 33.6mph). By looking at the PCB, there will be a solder blob indicating which version that you ordered and received. You can also check out the markings labeled on the IC. You\'ll also notice the arrow on the matching the silkscreen indicating what direction air should flow for a measurement. For the scope of this tutorial, we will be using the FS3000-1005 mostly to highlight the board and connect.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![FS3000-1005](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1005.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1005.jpg)   [![FS3000-1015](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18768-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1015.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18768-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1015.jpg)
  *FS3000-1005 \[ [SEN-18377](https://www.sparkfun.com/products/18377) \]*                                                                                                                                                                                     *FS3000-1015 \[ [SEN-18768](https://www.sparkfun.com/products/18768) \]*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is a table of a few of the specifications taken from the datasheet. For more in depth information on this chip, please refer to the [datasheet](https://cdn.sparkfun.com/assets/c/9/f/8/3/REN_FS3000_DST_20220531.pdf) linked in the Resources and Going Further.

+-------------------------------------------+----------------------------+----------------------------+
| **Characteristic**                        | **FS3000-1005**            | FS3000-1015                |
+:=========================================:+:==========================:+:==========================:+
| Operating Voltage                         | 2.7V to 3.3V, **typically 3.3V via Qwiic Connector**    |
+-------------------------------------------+---------------------------------------------------------+
| Current Consumption                       | 10mA                                                    |
+-------------------------------------------+----------------------------+----------------------------+
| Air Flow Speed                            | 0 to 7.23 m/s\             | 0 to 15 m/s\               |
|                                           | (0 to 16.17 mph)           | (0 to 33.6 mph)            |
+-------------------------------------------+----------------------------+----------------------------+
| Digital Output (Min to Max of Flow Range) | 409 to 3686 \"count\"                                   |
+-------------------------------------------+---------------------------------------------------------+
| Flow Accuracy                             | 5% @ 25°C                                               |
+-------------------------------------------+---------------------------------------------------------+
| Resolution                                | 12-bit                                                  |
+-------------------------------------------+---------------------------------------------------------+
| I^2^C Address                             | 0x28                                                    |
+-------------------------------------------+---------------------------------------------------------+
| Operating Temperature                     | -20°C to 85°C                                           |
+-------------------------------------------+---------------------------------------------------------+

### Qwiic Connectors

Our Qwiic Ecosystem makes sensors pretty much plug and play. There are two Qwiic connectors on either side of the Qwiic Air Velocity Sensor board to provide power and I^2^C connectivity simultaneously. The sensor\'s I^2^C lines are connected to two 2.2kΩ pull-up resistors. The I^2^C address of the board is **0x28**.

[![Qwiic connectors on either side of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_Qwiic.jpg)

### Pins

#### Power

Ideally, power will be supplied via the Qwiic connectors on either side of the board. Alternatively, power can be supplied through the header along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **2.7**-**3.3V**. The usual current draw is around 10mA.

[![Power pins are the two pins on the far right of the six pins at the bottom of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_PwrPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_PwrPins.jpg)

#### I^2^C

The I^2^C pins break out the functionality of the Qwiic connectors. Depending on your application, you can connect to these pins via the plated through holes for SDA and SCL.

[![I2C Pins are the two pins in the middle of the six pins at the bottom of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_I2CPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_I2CPins.jpg)

#### VCM and ADCR

VCM is an output from the sensor that provides a common bias voltage. With a power supply voltage at 3.3V (usual for Qwiic), the VCM pin will output 1.25V. The current datasheet does not provide any more information about this pin, however, it is most likely a bias voltage used with some sort of analog gain stage internal to the sensor (prior to it\'s internal ADC). This can be useful for unique more advanced projects that may benefit from having a known bias voltage tied to another analog system.

ADCR stands for ADC Reference. This is an input to the FS3000 which allows you to provide a reference voltage for the sensor\'s internal ADC. Note, you must first cut the \"ADC-REF\" jumper (on the bottom side of the board) before providing a custom voltage to this pin. By default, it is connected to VDD.

[![VCM and ADCR pins are the two pins on the far right of the six pins at the bottom of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_VCADCRPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_VCADCRPins.jpg)

### Jumpers

#### LED

If power consumption is an issue, cutting this jumper will disable the Power LED on the front of the board.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![LED](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1005-LED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000-1005-LED.jpg)   [![LED Jumper is located on the right side of the board](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_LEDJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_LEDJumper.jpg)

  *PWR LED\                                                                                                                                                                                                                                                    *LED Jumper\
  on Top Side*                                                                                                                                                                                                                                                 on Bottom Side*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### ADC-REF

Cut the ADC-REF jumper to provide your own custom ADC reference voltage on the ADCR header pin. By default (jumper closed), it is connected to VDD.

[![ADC Ref Jumper is at the top of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_ACDRefJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_ACDRefJumper.jpg)

#### I^2^C

The SparkFun Air Velocity Sensor has pull up resistors attached to the I^2^C bus; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by cutting the traces on the corresponding jumpers highlighted below.

[![I2C Jumper is on the left side of the board](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_I2CJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/18377-SparkFun-Air-Velocity-Sensor-Breakout-FS3000_I2CJumper.jpg)

### Board Outline

[![The board measures 1\" x 1\"](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/3/AirVelocitySensorBreakoutBoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/AirVelocitySensorBreakoutBoardOutline.png)

## Hardware Hookup

Using the Qwiic system, assembling the hardware is simple. All you need to do is connect your Air Velocity Sensor Breakout to your chosen development board with a Qwiic cable or [adapter cable](https://www.sparkfun.com/products/14425). Otherwise, you can use the I^2^C pins broken out if you do not have a Qwiic connector on your development board or if you do not want to use a Qwiic connection. If you are not using a Qwiic-enabled board, make sure your input voltage and logic are either running at **3.3V** or you are shifting the [logic level](https://learn.sparkfun.com/tutorials/logic-levels) from whatever logic your controller runs at to **3.3V**.

[![Plug the qwiic connector to the sensor and the redboard - voila!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/3/SparkFun_Air_Velocity_Sensor_Breakout_-_FS3000__Qwiic__Hookup_Guide.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/SparkFun_Air_Velocity_Sensor_Breakout_-_FS3000__Qwiic__Hookup_Guide.jpg)

## Software Setup and Programming

**Note:** Make sure you are using the latest stable version of the Arduino IDE on your desktop.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the Qwiic Air Velocity Sensor. You can obtain this library through the Arduino Library Manager by searching for \"**SparkFun FS3000**\". Find the one written by SparkFun Electronics and install the latest version. If you prefer downloading libraries manually, you can grab them from the [GitHub Repository](https://github.com/sparkfun/SparkFun_Air_Velocity_Sensor_FS3000_Qwiic) or by clicking on the button below.

[SparkFun Air Velocity Sensor Breakout - FS3000 (Qwiic) Arduino Library GitHub](https://github.com/sparkfun/SparkFun_Air_Velocity_Sensor_FS3000_Qwiic/archive/refs/heads/main.zip)

### Readings

The FS3000 has a response time of 125ms. In the provided example, we are only taking readings from the sensor once per second, so this is well above the response time. If you wish to take a higher frequency of readings, make sure to add in at least a 125ms delay in between each read.

To calculate or understand airflow and how it relates to diameter, you can use [this tool](https://www.engineering.com/calculators/airflow.htm).

### Functions

Below is a list of the functions that can be used with the Air Velocity Sensor, along with a description of what each function does and how to use it.

- **FS3000()** - Base constructor
- **begin()** \-- Initialize the sensor. Returns false if sensor is not detected.
- **isConnected()** \-- Returns true if I2C device ack\'s
- **fs.setRange()** \-- Sets the range for the IC that is connected to the Arduino microcontroller. You can input `AIRFLOW_RANGE_7_MPS` for the FS3000-1005 or `AIRFLOW_RANGE_15_MPS`for the FS3000-1015.
- **readRaw()** \-- Read from sensor, checksum, return raw data (409-3686)
- **readMetersPerSecond()** \-- Read from sensor, checksum, return m/s (0-7.23)
- **readMilesPerHour()** \-- Read from sensor, checksum, return mph (0-33ish)

**Note:** If you are using a board with an Apollo core, please note that 100KHz on the Apollo 2.1.1 doesn\'t currently work. You will need to use 400KHz, or jump back to Apollo 2.1.0.

## Example Code

Once you\'ve installed the FS3000 library, you should see **File** \> **Examples** \> **SparkFun_FS3000_Arduino_Library** \> **Example01_BasicReadings** to open the example sketch.

[![Finding the example](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/LibraryExample.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/LibraryExample.png)

\

Alternatively, you can copy and paste the code below into a fresh Arduino sketch.

    language:c
    /******************************************************************************
      Example_01_BasicReadings.ino

      Read values of air velocity from the FS3000 sensor, print them to terminal.
      Prints raw data, m/s and mph.
      Note, the response time on the sensor is 125ms.

      SparkFun FS3000 Arduino Library
      Pete Lewis @ SparkFun Electronics
      Original Creation Date: August 5th, 2021
      https://github.com/sparkfun/SparkFun_FS3000_Arduino_Library

      Development environment specifics:

      IDE: Arduino 1.8.15
      Hardware Platform: SparkFun RedBoard Qwiic
      SparkFun Air Velocity Sensor Breakout - FS3000 (Qwiic) Version: 1.0

      Artemis RedBoard @ 400KHz (Core v2.1.0) 
      (note, v2.1.1 has a known issue with clock stretching at 100KHz)  

      Do you like this library? Help support SparkFun. Buy a board!

        SparkFun Air Velocity Sensor Breakout - FS3000-1005 (Qwiic)
        https://www.sparkfun.com/products/18377

        SparkFun Air Velocity Sensor Breakout - FS3000-1015 (Qwiic)
        https://www.sparkfun.com/products/18768

      Hardware Connections:
      Use a Qwiic cable to connect from the RedBoard Qwiic to the FS3000 breakout (QWIIC).
      You can also choose to wire up the connections using the header pins like so:

      ARDUINO --> FS3000
      SDA (A4) --> SDA
      SCL (A5) --> SCL
      3.3V --> 3.3V
      GND --> GND

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
    ******************************************************************************/

    #include <Wire.h>
    #include <SparkFun_FS3000_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_FS3000

    FS3000 fs;

    void setup()
    

      // Set the range to match which version of the sensor you are using.
      // FS3000-1005 (0-7.23 m/sec) --->>>  AIRFLOW_RANGE_7_MPS
      // FS3000-1015 (0-15 m/sec)   --->>>  AIRFLOW_RANGE_15_MPS
      fs.setRange(AIRFLOW_RANGE_7_MPS);
      //fs.setRange(AIRFLOW_RANGE_15_MPS); 

      Serial.println("Sensor is connected properly.");
    }

    void loop()
    

Set your Board and Serial Port, and then upload the sketch to your Arduino. Then **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics)**. Make sure your **baud rate** is set to *115200*. You\'ll begin to see output, including raw data and translated miles per second and miles per hour.

[![Serial Monitor Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/9/9/3/SerialMonitorOutput.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/9/9/3/SerialMonitorOutput.png)

Note that peak in the middle of the readings? That\'s where I pointed the sensor at the fan!

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.