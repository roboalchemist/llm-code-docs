# Source: https://learn.sparkfun.com/tutorials/lis3dh-hookup-guide

## Introduction

[![SparkFun Triple Axis Accelerometer Breakout - LIS3DH](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/6/8/0/13963-02.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-lis3dh.html)

### [SparkFun Triple Axis Accelerometer Breakout - LIS3DH](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-lis3dh.html) 

[ SEN-13963 ]

The LIS3DH Breakout is a smart, low-power, three-axis, capacitive micro-machined accelerometer with 12 bits of resolution tha...

[ [\$7.75] ]

The [LIS3DH](https://www.sparkfun.com/products/13963) is a triple axis accelerometer you can use to add translation detection to your project. The \"3D\" in LIS3DH refers to the fact that it is a 3DoF, or 3 Degrees of Freedom. Additionally, it has a few analog inputs to play with, and it has some built in movement detection features to detect things like free-fall, and to indicate if the FIFO buffers are full.

If you\'re looking for something small and inexpensive, and are only measuring acceleration, this is the product for you. Other inertial measurement units (or IMUs), such as the [LSM9DS1](https://www.sparkfun.com/products/13284); the [LSM6DS3](https://www.sparkfun.com/products/13339); or the [LSM303C](https://www.sparkfun.com/products/13303), can provide additional space location data such as gyroscopic or magnetometric.

This guide presents the basics of plugging the board into a RedBoard, shows how to use the Arduino library to get acceleration data live or by FIFO collection, and describes the library usage.

### Required Materials

To follow along, you\'ll need the following materials:

- [LIS3DH Breakout Board](https://www.sparkfun.com/products/13963)
- [Arduino UNO](https://www.sparkfun.com/products/11021), [RedBoard](https://www.sparkfun.com/products/11575), or another [Arduino-compatible board](https://learn.sparkfun.com/tutorials/arduino-comparison-guide)
- [Straight Male Headers](https://www.sparkfun.com/products/116) \-- Or wire. Something to connect between the breakout and a breadboard.
- [Breadboard](https://www.sparkfun.com/products/12002) \-- Any size (even mini) should do.
- [M/M Jumper Wires](https://www.sparkfun.com/products/11026) \-- To connect between Arduino and breadboard.

**The LIS3DH is a 3.3V device!** Supplying voltages greater than \~3.6V can permanently damage the IC. As long as your Arduino has a 3.3V supply output, and you\'re OK with using I^2^C; you shouldn\'t need any extra level shifting. But, if you want to use SPI, you may need a [level shifter](https://www.sparkfun.com/products/12009).

A logic level shifter is required for any 5V-operating Arduino (UNO, RedBoard, Leonardo, etc). If you use a 3.3V-based \'duino \-- like the [Arduino Pro 3.3V](https://www.sparkfun.com/products/10914) or [3.3V Pro Mini](https://www.sparkfun.com/products/11114) \-- there is no need for level shifting.

### Suggested Reading

If you\'re not familiar with some of the concepts below, we recommend checking out that tutorial before continuing on.

- [Accelerometer Basics](https://learn.sparkfun.com/tutorials/accelerometer-basics)
- [Gyroscopes](https://learn.sparkfun.com/tutorials/gyroscope)
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Inter-IC Communication (I^2^C)](https://learn.sparkfun.com/tutorials/i2c)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Bi-Directional Level Shifter Hookup Guide](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)

Also, the following ST documents are helpful for advanced users:

- [LIS3DH_Datasheet](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/LIS3DH_Datasheet_DocID_17530rev1.pdf) \-- Hardware information and register map.
- [LIS3DH_AppNote](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/LIS3DH_AppNote_DocID_18198rev1.pdf) \-- Descriptive material showing basic usage.

## Hardware Overview and Assembly

There are a few different methods with which you can use the LIS3DH.

The top side of the board has the LIS3DH sensor, some bypass caps and pull-up resistors.

[![board pinout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/topNotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/topNotated.jpg)

*The pin connections*

This table gives more information as to each pins functionality. The serial port can be connected as either SPI or I2C, and it uses the same physical pins for both. To get going, just wire up your choice of interface, supply 3.3v, and ground. Note that you will not need to use all the pins no matter which communication method you choose.

+------------+---------+-----------+--------------------------------------+-----------------+
|            |         |           |                                      | Connection      |
+============+=========+===========+======================================+========+========+
| Group      | Name    | Direction | Description                          | I2C    | SPI    |
+------------+---------+-----------+--------------------------------------+--------+--------+
| Serial     | !CS     | I         | Chip select (for SPI)                | NC     | !CS    |
|            +---------+-----------+--------------------------------------+--------+--------+
|            | SDO     | O         | Data output (MISO for SPI)           | NC     | MISO   |
|            +---------+-----------+--------------------------------------+--------+--------+
|            | SCL     | I         | Data clock                           | SCL    | SCK    |
|            +---------+-----------+--------------------------------------+--------+--------+
|            | SDA/SDI | I/O       | Data in (SDA for I2C, MOSI for SPI)  | SDA    | MOSI   |
+------------+---------+-----------+--------------------------------------+--------+--------+
| Interrupts | I1      | O         | Primary int has FIFO + motion        | Optional MCU    |
|            +---------+-----------+--------------------------------------+-----------------+
|            | I2      | O         | Secondary int has motion             | Optional MCU    |
+------------+---------+-----------+--------------------------------------+-----------------+
| ADC        | A1      | I         | Analog in                            | Optional        |
|            +---------+-----------+--------------------------------------+-----------------+
|            | A2      | I         | Analog in                            | Optional        |
|            +---------+-----------+--------------------------------------+-----------------+
|            | A3      | I         | Analog in (unused for temp readings) | Optional        |
+------------+---------+-----------+--------------------------------------+-----------------+
| Power      | VCC     | I         | 3.3V input                           | Supply          |
|            +---------+-----------+--------------------------------------+-----------------+
|            | GND     | I         | Ground connection (either PTH)       | Supply          |
+------------+---------+-----------+--------------------------------------+-----------------+

On the bottom, there are two jumpers that correspond to the I2C address and pull-up enable.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/botNotated.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/botNotated.jpg)

The following options are available:

- **The I2C Address Jumper** \-- Bridge to use alternate address 0x18, otherwise leave open for 0x19. Leave open for SPI use.
- **The I2C Pull-up Enable** \-- Closed by default, this connects a pull-up resistor between the I2C lines and VCC. This generally doesn\'t interfere with SPI operation, but, if less power consumption is required, carefully cut the copper traces.

### Working with a Breadboard

This sensor works nicely with a breadboard for easy connection, and, because it gives some mass to the accelerometer, it more closely matches what might be expected from a project or cellphone.

To add headers, break off two 6-pin lengths of [0.1 inch male headers](https://www.sparkfun.com/products/116), and set them into a breadboard to use as a soldering jig.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-03.jpg)

*Two rows of headers placed and ready to solder.*

Drop the breakout board onto the pins, and solder down the rows.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-04.jpg)

*Soldering on the rows of pins.*

Congratulations! You\'re now ready to connect the sensor to a microcontroller of your choosing.

## Getting the Arduino Library

The examples in the guide use the Arduino IDE and a RedBoard to communicate with the LIS3DH.

To get the Arduino library, download from Github, or use the Arduino Library Manager.

### Download the Github Repository

Visit the [GitHub repository](https://github.com/sparkfun/SparkFun_LIS3DH_Arduino_Library) to download the most recent version of the library, or click the link below:

[Download the Arduino Library](https://github.com/sparkfun/SparkFun_LIS3DH_Arduino_Library/archive/master.zip)

### Library Manager

For help installing the library, check out our [How To Install An Arduino Library tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library).

If you don\'t end up using the manger, you\'ll need to move the *SparkFun_LIS3DH_Arduino_Library* folder into a *libraries* folder within your Arduino sketchbook.

## Example: I2C, analog, and interrupts

The first circuit allows a RedBoard to talk to the LIS3DH over I2C and provides connections on the interrupt and ADC pins.

The interrupts are useful to indicate conditions like extreme Gs or freefall, and to tell the RedBoard that the FIFO is full and needs to be serviced. The analog input pins are useful to measure various voltages similar to the RedBoard\'s analog inputs, but have a more constrained voltage range (about 0.9V to 1.8V). If you don\'t need either of these, just connect power, ground, and communication pins, and ignore the interrupt and ADC examples.

Use these two pictures as a guide for building the circuit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-02.jpg)

*The circuit built on a RedBoard*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/I2C_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/I2C_bb.jpg)

*The connections shown in Fritzing*

### Basic Accelerometer Data Collection:

Start with just the basic accelerometer sketch, also called \"[MinimalistExample](https://github.com/sparkfun/SparkFun_LIS3DH_Arduino_Library/blob/master/examples/MinimalistExample/MinimalistExample.ino)\" from the library. This will periodically samples the sensor and displays data as number of Gs detected. Remember, the vertical axis will read 1G while sitting at rest.

    language:c
    #include "SparkFunLIS3DH.h"
    #include "Wire.h"
    #include "SPI.h"

    LIS3DH myIMU; //Default constructor is I2C, addr 0x19.

    void setup() 

    void loop()
    

Example output:

    Processor came out of reset.

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

When run, the sketch will display data in Gs to the [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics). Every second, the data is collected and printed.

### Using the ADC

To try out the analog inputs, load the example called \"[ADCUsage](https://github.com/sparkfun/SparkFun_LIS3DH_Arduino_Library/blob/master/examples/ADCUsage/ADCUsage.ino)\", or copy paste from the following section. This example also shows some of the additional settings that can be applied within the `begin()` function.

    language:c
    #include "SparkFunLIS3DH.h"
    #include "Wire.h"
    #include "SPI.h"

    LIS3DH myIMU; //Default constructor is I2C, addr 0x19.

    void setup() 

    void loop()
    

Example output:

    Processor came out of reset.

    ADC:
     1 = 1020
     2 = 522
     3 = 506

    ADC:
     1 = 1020
     2 = 544
     3 = 516

    ADC:
     1 = 1020
     2 = 540
     3 = 517

The sketch prints the three ADC values every 300ms. Move the knob to see how the values change and how the effective voltage range is somewhat in the middle of the full range. Move the wire from on ADC pin to another to see that the controlled value changes.

### Using the Interrupt Pins

Interrupt behavior is highly configurable and is thus omitted as basic library functions. Instead, LIS3DH registers are directly written in accordance with the datasheet.

An example is provided that has the relevant registers configured with comments in a template function that can be copied into a project and modified. Run the example named [IntUsage](https://github.com/sparkfun/SparkFun_LIS3DH_Arduino_Library/blob/master/examples/IntUsage/IntUsage.ino), which will throw an interrupt on one pin when an exceeded acceleration is detected and a pulse on the other when a tap is detected.

## Example: SPI and FIFO usage

The second method in which to communicate with the LIS3DH is with the SPI interface. The SPI interface operates at 3.3v, so use a [logic level converter](https://www.sparkfun.com/products/12009?_ga=1.39639146.831177436.1424112780) or a MCU that operates at 3.3V. Use the following pictures to help build the circuit.

[![Circuit Wired in SPI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/Wifi_Cheeseburger_Project-01.jpg)

*The circuit built on a RedBoard*

[![LIS3DH_SPI](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/LIS3DH_SPI_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/LIS3DH_SPI_bb.png)

*The connections shown in Fritzing*

### Basic Accelerometer Data Collection:

SPI is not the default configuration, so you\'ll have to pass extra information to the library by constructing with parameters. Modify \"MinimalistExample\" by changing `LIS3DH myIMU;` to `LIS3DH myIMU(SPI_MODE, 10);` for SPI mode with the !CS pin connected to pin 10.

The modified \"MinimalistExample\" is listed here:

    language:c
    #include "SparkFunLIS3DH.h"
    #include "Wire.h"
    #include "SPI.h"

    LIS3DH myIMU(SPI_MODE, 10); // constructed with parameters for SPI and cs pin number

    void setup() 

    void loop()
    

Example output:

    Processor came out of reset.

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

    Accelerometer:
     X = -0.1481
     Y = -0.1361
     Z = 0.9768

When run, the sketch will display data in Gs to the serial terminal. Every second, the data is collected and printed.

### FIFO usage:

The SPI bus can operate faster than I2C, so for high speed data collections where periodic sampling is required, SPI is advisable.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/9/6/CSVGraph.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/9/6/CSVGraph.jpg)

*This graph was made by taking the output of the example and copy-pasting it into a spreadsheet program, then creating a chart. During the data collection, the sensor was moved about a foot back and forth on each axis.*

    language:c
    #include "SparkFunLIS3DH.h"
    #include "Wire.h"
    #include "SPI.h"

    LIS3DH myIMU(SPI_MODE, 10); //Constructing with SPI interface information
    //LIS3DH myIMU(I2C_MODE, 0x19); //Alternate constructor for I2C

    uint32_t sampleNumber = 0; //Used to make CSV output row numbers

    void setup() 

    void loop()
    ;  //Wait for watermark

      //Now loop until FIFO is empty.
      //If having problems with the fifo not restarting after reading data, use the watermark
      //bits (b5 to b0) instead.
      //while(( myIMU.fifoGetStatus() & 0x1F ) > 2) //This checks that there is only a couple entries left
      while(( myIMU.fifoGetStatus() & 0x20 ) == 0) //This checks for the 'empty' flag
      

    }

Example output:

    Processor came out of reset.

    Configuring FIFO with no error checking...Done!
    Clearing out the FIFO...Done!
    0,-0.15,-0.14,1.04
    1,-0.17,-0.12,1.02
    2,-0.21,-0.10,0.95
    3,-0.21,-0.10,1.01
    4,-0.22,-0.12,1.07
    5,-0.17,-0.12,0.99
    6,-0.12,-0.15,0.96
    7,-0.18,-0.12,0.94
    8,-0.19,-0.10,0.98
    9,-0.20,-0.14,1.04
    10,-0.19,-0.12,0.99
    11,-0.20,-0.10,0.95
    12,-0.21,-0.12,1.06
    13,-0.14,-0.12,0.98
    14,-0.10,-0.11,0.95
    15,-0.12,-0.10,0.94
    16,-0.14,-0.09,0.90
    ...

Notice that the output produces batches of data periodically. Even though the data waits to be collected, it is still sampled periodically. The data is collected when the FIFO is past the watermark configured in the line `myIMU.settings.fifoThreshold = 20;`.

## Extra Examples and Arduino Library Reference

The following examples are included in the Arduino library:

- **ADCUsage** - Demonstrates analog in reads and has notes about temperature collection
- **FifoExample** - Demonstrates using the built-in buffer to burst-collect data - **Good demonstration of settings**
- **FullSettingExample** - Shows all settings, with non-used options commented out
- **IntUsage** - shows configuration of interrupt bits
- **LowLevelExample** - Demonstrates using only the core driver without math and settings overhead
- **MinimalistExample** - The **easiest** configuration
- **MultiI2C** - Using two LIS3DHs over I2C
- **MultiSPI** - Using two LIS3DHs over SPI

### Library Usage

Take the following steps to use the library

- construct an object in the global space with one of these constructions
  - No parameters \-- I2C mode at address 0x19
  - I2C_MODE, address
  - SPI_MODE, pin number
- With in begin, set the .settings. values
- run `.begin()`

Example:

    language:c
    LIS3DH myIMU; //This creates an instance the library object.

    void setup()
    

#### Settings

The main LIS3DH class has a public member, which is named settings. To configure settings, use the format `myIMU.settings.accelSampleRate = (...);`. Then, call `.begin()` to apply.

Settings contains the following members:

- `uint8_t adcEnabled` \-- Set to 1 to enable ADCs
- `uint8_t tempEnabled` \-- Set to 1 to override ADC3 with delta temperature information
- `uint16_t accelSampleRate` \-- Can be: 0,1,10,25,50,100,200,400,1600,5000 Hz
- `uint8_t accelRange` \-- Max G force readable. Can be: 2, 4, 8, 16
- `uint8_t xAccelEnabled` \-- Set to 1 to enable x axis
- `uint8_t yAccelEnabled` \-- Set to 1 to enable y axis
- `uint8_t zAccelEnabled` \-- Set to 1 to enable z axis
- `uint8_t fifoEnabled` \-- Set to 1 to enable FIFO
- `uint8_t fifoMode` \-- Can be 0x0,0x1,0x2,0x3
- `uint8_t fifoThreshold` \-- Number of bytes read before watermark is detected (0 to 31)

### Functions

**Advanced programmers:** The LIS3DH class inherits the LIS3DHCore, which can be used to communicate without all these functions, so you can write your own. This class is not covered in this hookup guide.

#### uint8_t begin( void );

Call after providing settings to start the wire or SPI library as indicated by construction and runs `applySettings()`. Returns 0 for success.

#### void applySettings( void );

This configures the IMU\'s registers based on the contents of .settings.

#### int16_t readRawAccelX( void );

#### int16_t readRawAccelY( void );

#### int16_t readRawAccelZ( void );

These functions return axis acceleration information as a 16 bit, signed integer.

#### float readFloatAccelX( void );

#### float readFloatAccelY( void );

#### float readFloatAccelZ( void );

These functions call the Raw functions, then apply math to convert to a float expressing acceleration in number of Gs.

#### uint16_t read10bitADC1( void );

#### uint16_t read10bitADC2( void );

#### uint16_t read10bitADC3( void );

These functions return the ADC values read from the pins. Values will be 10 bit and the detectable range is about 0.9V to 1.8V.

Note: When `tempEnabled == 1`, ADC3 reads as an unreferenced temperature in degrees C. Read twice and calculate the change in temperature.

#### void fifoBegin( void );

This enables the FIFO by writing the proper values into the FIFO control reg, and control reg 5. This does not start the data collection to the FIFO, run `fifoStartRec()` when ready.

Sample rate depends on data rate selected in .settings.

#### void fifoClear( void );

This reads all data until the status says none is available, discarding the data. Use to start with new data if the FIFO fills with old data.

#### void fifoStartRec( void )

This enables FIFO data collection. Run this before starting to check if data is available.

After fifoStartRec is used, data from the X, Y, Z registers is not real time, but is the next available sample.

#### uint8_t fifoGetStatus( void )

This returns the FIFO status byte. The contents of the byte are as follows:

- bit 7: Watermark exceeded
- bit 6: FIFO has overflowed
- bit 5: FIFO is empty
- bit 4 through 0: Number of samples available (0 to 31)

#### void fifoEnd( void );

This stops the FIFO and returns the device to regular operation.