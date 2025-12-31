# Source: https://learn.sparkfun.com/tutorials/qwiic-vr-imu-bno080-hookup-guide

## Introduction

**Note:** Unfortunately the BNO080 is EOL. For users looking for a replacement, try checking out the Qwiic VR IMU Breakout (BNO086) that is available as a drop-in replacement. There are also a few additional features available for the BNO086. For more information, check out the [SparkFun VR IMU Breakout - BNO086 (Qwiic) Hookup Guide](https://docs.sparkfun.com/SparkFun_VR_IMU_Breakout_BNO086_QWIIC/).

Bosch\'s [BNO080](https://www.sparkfun.com/products/14686) is a combination triple axis accelerometer/gyro/magnetometer packaged with an ARM Cortex M0+ running powerful algorithms. The BNO080 Inertial Measurement Unit (IMU) produces accurate rotation vector headings, excellently suited for VR and other heading applications with a static rotation error of 2 degrees or less. It's what we've been waiting for: all the sensor data is combined and drift corrected into meaningful, accurate IMU information. It\'s perfect for any project that needs to sense orientation or motion. We\'ve taken this IMU and stuck it on a [Qwiic enabled](https://www.sparkfun.com/categories/399) breakout board, in order to make interfacing with the tiny, QFN package a bit easier to connect.

[![SparkFun VR IMU Breakout - BNO080 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/9/1/14686-Qwiic_VR_IMU_BN0080-01.jpg)](https://www.sparkfun.com/products/14686)

### [SparkFun VR IMU Breakout - BNO080 (Qwiic)](https://www.sparkfun.com/products/14686) 

[ SEN-14686 ]

The SparkFun VR IMU Breakout is a cutting edge triple axis accelerometer/gyro/magnetometer all in a single package that you c...

**Retired**

In this hookup guide, we\'ll connect our sensor up to our microcontroller of choice and separately read the rotation vectors (which is what we will mainly want), acceleration vectors, gyro values, and magnetometer vectors. We\'ll check out how to implement the step counter on the BNO080 in order to use it as a pedometer. We\'ll also read Q values and various other metadata from the sensor. Knowing what activity you\'re performing is important so we\'ll learn how to classify what activity the IMU is performing (i.e. Sitting still, moving, biking, walking, running, etc\...) and how confident the IMU is that each activity is being performed. The examples will also show how to calibrate our hardware to give us the most accurate readings possible. Printing out raw packets will also be examined for debugging purposes. Finally, we\'ll examine how to configure the sensor on different I^2^C ports and addresses. A bonus example is provided in Processing to show us how to use quaternion data to orient a cube.

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

You will also need a Qwiic cable to connect the shield to your accelerometer, choose a length that suits your needs.

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

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them. We also delve into Processing in this tutorial, if you aren\'t familiar, check out the below tutorial on Processing.

[](https://learn.sparkfun.com/tutorials/serial-communication)

### Serial Communication 

Asynchronous serial communication concepts: packets, signal levels, baud rates, UARTs and more!

[](https://learn.sparkfun.com/tutorials/gyroscope)

### Gyroscope 

Gyroscopes measure the speed of rotation around an axis and are an essential part in determines ones orientation in space.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

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

Let\'s look over a few characteristics of the BNO080 sensor so we know a bit more about how it behaves.

  **Characteristic**             **Range**
  ------------------------------ -------------------------------------------------
  Operating Voltage              1.65V - 3.6V
  Linear Acceleration Accuracy   ±.35m/s^2^
  Gyroscope Accuracy             ±.35m/s^2^
  I^2^C Address                  **0x4B (S0 Pulled High)** or 0x4A (S0 grounded)

### Pins

There are multiple rows of pins on the BNO080, the first row, used for the default I^2^C interface (configurable up to 400 kHz) is explained in the table below.

  Pin Label   Pin Function         Input/Output     Notes
  ----------- -------------------- ---------------- -------------------------------------------------------------------------------
  PS0         Protocol Selection   Input            Configuration of the communication interface (Default: 0, I^2^C)
  PS1         Protocol Selection   Input            Configuration of the communication interface (Default: 0, I^2^C)
  GND         Ground               Input            0V/common voltage.
  3V3         Power Supply         Input            Should be between **1.65 - 3.6V**
  SDA         I^2^C Data Signal    Bi-directional   Bi-directional data line. Voltage should not exceed power supply (e.g. 3.3V).
  SCL         I^2^C Clock Signal   Input            Clock signal. Voltage should not exceed power supply (e.g. 3.3V).
  RST         Reset Signal         Input            Reset signal, active low, pull low to reset IC
  INT         Interrupt            Output           Interrupt, active low, pulls low when the BNO080 is ready for communication.

\

Also broken out on the board is a [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) which can run data up to 3MHz. The pins for this interface are outlined below. On any pin, the voltage should not exceed that supplied on the **3V3** pin.

**Note:** You may not recognize the COPI/CIPO labels for SPI pins. SparkFun has joined with other members of OSHWA in a resolution to move away from using \"Master\" and \"Slave\" to describe signals between the controller and the peripheral. Check out [this page](https://www.sparkfun.com/spi_signal_names) for more on our reasoning behind this change. You can also see OSHWA\'s resolution [here](https://www.oshwa.org/a-resolution-to-redefine-spi-signal-names).

  Pin Label   Pin Function   Input/Output   Notes
  ----------- -------------- -------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  GND         Ground         Input          0V/Common Voltage
  3V3         Power          Input          Should be between **1.65 - 3.6V**
  SCK         Clock          Input          Clock signal to synchronize controller and peripheral.
  SO          CIPO           Output         Controller in, peripheral out. Device sends data to the controller on this line.
  SI          COPI/ADDR      Input          Controller out, peripheral in. Device receives data from the microcontroller on this line. Tie to 3.3V to change I^2^C address from 0x4A to 0x4B
  CS          Chip Select    Input          Chip select, active low, used as chip select on SPI
  WAK         Wake           Input          Active low, Used to wake the processor from a sleep mode.
  RST         Reset Signal   Input          Reset signal, active low, pull low to reset IC

\

You can also use the UART interface at up to 3 Mbps or a simplified UART called UART-RVC (Used for robotic vacuum cleaners) which can run at a data rate of 115200 kbps. The UART interface is in the middle of the board, with the black and green pins labeled on the back of the board as shown below. These serial pins have been arranged to work with our [Serial Basic](https://www.sparkfun.com/products/14050) board to make interfacing to a computer simple and fast. The *GRN* and *BLK* labels help align the serial connection properly.

Also note the [BOOT] pin next to the Qwiic connector, which is necessary for configuration of the communication mode. If the [BOOT] pin is low upon reset or power up, the chip will go into bootloader mode to allow for programming of new firmware.

[![Boot Pin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/BOOT.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/BOOT.png)

### Optional Features

#### Pull-Up Resistor Jumper

The Qwiic VR IMU has onboard I^2^C pull up resistors; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by removing the solder on the corresponding jumpers highlighted below.

[![I2C Pullup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/I2C.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/I2C.png)

#### Protocol Selection Jumpers

You can use the `PS0` and `PS1` jumpers to change the communication protocol that the BNO080 is using. The jumpers are left open (0) by default, and the following configurations will allow for their corresponding communications protocols.

  PS0   PS1   Interface
  ----- ----- -----------
  0     0     I^2^C
  1     0     UART-RVC
  0     1     UART
  1     1     SPI

\

The jumpers themselves are located on the back of the board, shown below

[![Protocol Selection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/PS.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/PS.png)

#### I^2^C Jumper

You can also change the address of the BNO080 from **0x4B (default)** to 0x4A by connecting the `I2C ADR` jumper. The jumper itself is shown in the below image.

[![Address Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/ADR.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/ADR.png)

#### Axis Reference

Also, be sure to check out the labeling on the front of the board that indicates the orientation of the positive X, Y, and Z axes so you know which way your data is pointing.

[![Axis Reference Photo](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/XYZ.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/XYZ.png)

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. With the shield assembled, SparkFun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the BNO080 breakout, the other into the Qwiic Shield of your choice and you\'ll be ready to upload a sketch and figure out how you\'re moving that board. It seems like it\'s too easy too use, but that\'s why we made it that way!

[![Connected IMU](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/SparkFun_VR_IMU_Breakout_-_BNO080__Qwiic__-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/SparkFun_VR_IMU_Breakout_-_BNO080__Qwiic__-01.jpg)

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Before we get into programming our IMU, let\'s download and check out the available functions in our library. SparkFun has written a library to control the Qwiic VR IMU. You can obtain these libraries through the Arduino Library Manager. Search for **SparkFun BNO080 Cortex Based IMU** and you should be able to install the latest version. If you prefer manually downloading the libraries from the [GitHub repository](https://github.com/sparkfun/SparkFun_BNO080_Arduino_Library), you can grab them here:

[Download the SparkFun BNO080 Cortex Based IMU Library (ZIP)](https://github.com/sparkfun/SparkFun_BNO080_Arduino_Library/archive/main.zip)

Let\'s get started by looking at the functions that set up the IMU.

### Setup and Settings

- **`boolean begin(uint8_t deviceAddress = BNO080_DEFAULT_ADDRESS, TwoWire &wirePort = Wire);`** \-\-- By default use the default I2C address, and use Wire port, otherwise, pass in a custom I^2^C address and wire port.

- **`void enableDebugging(Stream &debugPort = Serial);`** \-\-- Turn on debug printing. If user doesn\'t specify method of printing then Serial will be used.

- **`void enableRotationVector(uint16_t timeBetweenReports);`** \-\-- Enables the rotation vector to give a report every `timeBetweenReports` ms.

- **`void enableGameRotationVector(uint16_t timeBetweenReports);`** \-\-- Enables the game rotation vector to give a report every `timeBetweenReports` ms.

- **`void enableAccelerometer(uint16_t timeBetweenReports);`** \-\-- Enables the accelerometer with `timeBetweenReports` in ms.

- **`void enableGyro(uint16_t timeBetweenReports);`** \-\-- Enables the gyroscope with `timeBetweenReports` in ms.

- \*\*`void enableMagnetometer(uint16_t timeBetweenReports);` \-\-- Enables the magnetometer with `timeBetweenReports` in ms.

- **`void enableStepCounter(uint16_t timeBetweenReports);`** \-\-- Enables the step counter with `timeBetweenReports` in ms.

- **`void enableStabilityClassifier(uint16_t timeBetweenReports);`** \-\-- Enables the stability classifier with `timeBetweenReports` in ms.

- **`void enableActivityClassifier(uint16_t timeBetweenReports, uint32_t activitiesToEnable,`**\
       **`uint8_t (&activityConfidences)[9]);`** \-\-- Enables the activity classifier with a `timeBetweenReports` (in ms), the `activitiesToEnable` (0x1F to enable all activities) and the `activityConfidences[9]` array to store the IMU\'s confidence that the activity is occurring.

- **`void softReset();`** \-\-- Try to reset the IMU via software

- **`uint8_t resetReason();`** \-\-- Query the IMU for the reason it last reset

- **`float qToFloat(int16_t fixedPointValue, uint8_t qPoint);`** \-\-- Given a Q value, converts fixed point floating to regular floating point number

- **`void setFeatureCommand(uint8_t reportID, uint16_t timeBetweenReports();`** \-\-- Used to enable different sensors and functions (features) of the IMU with to report with `timeBetweenReports` ms between reports.

- **`void setFeatureCommand(uint8_t reportID, uint16_t timeBetweenReports, uint32_t specificConfig);`** \-\-- Used to enable different sensors and functions (features) of the IMU with to report with `timeBetweenReports` ms between reports.

- **`void sendCommand(uint8_t command);`** \-\-- Sends a command to the sensor.

- **`void sendCalibrateCommand(uint8_t thingToCalibrate);`** \-\-- Sends calibrations commands to the sensor of choice. Possible arguments are listed below.
  - **`CALIBRATE_ACCEL`**
  - **`CALIBRATE_GYRO`**
  - **`CALIBRATE_MAG`**
  - **`CALIBRATE_PLANAR_ACCEL`**
  - **`CALIBRATE_ACCEL_GYRO_MAG`** \-\-- Calibrates all sensors.
  - **`CALIBRATE_STOP`** \-\-- Stops all calibration.

### Communication and Data Handling

- **`boolean waitForI2C();`** \-\-- Delay based polling for I2C traffic

- **`boolean receivePacket(void);`** \-\-- Receives an I^2^C packet from the IMU.

- **`boolean getData(uint16_t bytesRemaining);`** \-\-- Given a number of bytes, send the requests in `I2C_BUFFER_LENGTH` chunks

- **`boolean sendPacket(uint8_t channelNumber, uint8_t dataLength);`** \-\-- Sends a packet of length `dataLength` to `channelNumber`.

- **`void printPacket(void);`** \-\-- Prints the current shtp header and data packets

- **`bool dataAvailable(void);`** \-\-- Checks if new data is available from the IMU.

- **`void parseInputReport(void);`** \-\-- Takes the data from the IMu and places it into the proper variable so they can be properly read.

### Getting Values

- **`float getQuatI();`** \-\-- Retrieves the i-axis quaternion from the IMU.

- **`float getQuatJ();`** \-\-- Retrieves the j-axis quaternion from the IMU.

- **`float getQuatK();`** \-\-- Retrieves the k-axis quaternion from the IMU.

- **`float getQuatReal();`** \-\-- Retrieves the real component of the quaternion from the IMU.

- **`float getQuatRadianAccuracy();`** \-\-- Retrieves the accuracy of the quaternion from the IMU in radians.

- **`uint8_t getQuatAccuracy();`** \-\-- Retrieves the accuracy of the quaternion from the IMU.

- **`float getAccelX();`** \-\-- Retrieves the x-axis acceleration.

- **`float getAccelY();`** \-\-- Retrieves the y-axis acceleration.

- **`float getAccelZ();`** \-\-- Retrieves the z-axis acceleration.

- **`uint8_t getAccelAccuracy();`** \-\-- Retrieves the accuracy of the accelerometer readings.

- **`float getGyroX();`** \-\-- Retrieves the x-axis gyroscope reading.

- **`float getGyroY();`** \-\-- Retrieves the y-axis gyroscope reading.

- **`float getGyroZ();`** \-\-- Retrieves the z-axis gyroscope reading.

- **`uint8_t getGyroAccuracy();`** \-\-- Retrieves the accuracy of the gyroscope reading.

- **`float getMagX();`** \-\-- Retrieves the x-axis magnetometer reading.

- **`float getMagY();`** \-\-- Retrieves the y-axis magnetometer reading.

- **`float getMagZ();`** \-\-- Retrieves the z-axis magnetometer reading.

- **`uint8_t getMagAccuracy();`** \-\-- Retrieves the accuracy of the magnetometer reading.

### Sensor Calibration

Check the [calibration procedure](https://cdn.sparkfun.com/assets/c/6/f/4/9/Sensor-Calibration-Procedure-v1.1.pdf) in order to calibrate the IMU with the functions listed below.

- **`void calibrateAccelerometer();`** \-\-- Begins the calibration function for the IMU\'s accelerometer.
- **`void calibrateGyro();`** \-\-- Begins the calibration function for the IMU\'s gyroscope.
- **`void calibrateMagnetometer();`** \-\-- Begins the calibration function for the IMU\'s magnetometer.
- **`void calibratePlanarAccelerometer();`** \-\-- Begins the planar calibration function for the IMU\'s accelerometer.
- **`void calibrateAll();`** \-\-- Begins all calibration functions.
- **`void endCalibration();`** \-\-- Ends the active calibration functions.
- **`void saveCalibration();`** \-\-- Saves data from current calibration.

### Special Functions

- **`uint16_t getStepCount();`** \-\-- Gets the number of steps from the BNO080\'s onboard pedometer.
- **`uint8_t getStabilityClassifier();`** \-\-- Retrieves the stability classification, a number between 0 and 6.
  - **0** \-\-- Unknown classification
  - **1** \-\-- On table
  - **2** \-\-- Stationary
  - **3** \-\-- Stable
  - **4** \-\-- Motion
  - **5** \-\-- Reserved
- **`uint8_t getActivityClassifier();`** \-\-- Retrieves the Activity classification, a number between 0 and 8, based on a comparison of the confidence levels in each activity.
  - **0** \-\-- Unknown
  - **1** \-\-- In Vehicle
  - **2** \-\-- On Bicycle
  - **3** \-\-- On Foot
  - **4** \-\-- Still
  - **5** \-\-- Tilting
  - **6** \-\-- Walking
  - **7** \-\-- Running
  - **8** \-\-- On stairs

### Metadata Handling Functions

- **`int16_t getQ1(uint16_t recordID);`** \-\-- Given a record ID, read the Q1 value from the metaData record in the Flash Record System (FRS). Q1 is used for all sensor data calculations.
- **`int16_t getQ2(uint16_t recordID);`** \-\-- Given a record ID, read the Q2 value from the metaData record in the FRS. Q2 is used in sensor bias.
- **`int16_t getQ3(uint16_t recordID);`** \-\-- Given a record ID, read the Q3 value from the metaData record in the FRS. Q3 is used in sensor change sensitivity.
- **`float getResolution(uint16_t recordID);`** \-\-- Given a record ID, reads the resolution value from the sensors metadata
- **`float getRange(uint16_t recordID);`** \-\-- Given a record ID, read the range value from the metaData record in the FRS for a given sensor
- \*\*\*\*`uint32_t readFRSword(uint16_t recordID, uint8_t wordNumber);`\*\* \-\-- Given a record ID and a word number, find the word data. Used in `getQ1()`, `getResolution()`, etc..
- **`void frsReadRequest(uint16_t recordID, uint16_t readOffset, uint16_t blockSize);`** \-\-- Ask the sensor for data from the Flash Record System.
- **`bool readFRSdata(uint16_t recordID, uint8_t startLocation, uint8_t wordsToRead);`** \-\-- Reads data from the Flash Record System.

### Global Variables

- **`uint8_t shtpHeader[4];`** \-\-- In Hillcrest\'s Sensor Hubtransfer Protocol, each packet has a header of 4 bytes
- **`uint8_t shtpData[MAX_PACKET_SIZE];`** \-\-- Creates an array for SHTP data to be stored.
- **`uint8_t sequenceNumber[6] = ;`** \-\-- There are 6 com channels. Each channel has its own sequence number.
- **`uint8_t commandSequenceNumber = 0;`** \-\-- Commands have a sequence number as well. These are inside command packet, the header uses its own sequence number for each channel.
- **`uint32_t metaData[MAX_METADATA_SIZE];`** \-\-- There is more than 10 words in a metadata record but we\'ll stop at Q point 3

## Arduino Example Code

Now that we have our library installed, we can get started playing around with our examples to learn more about how the IMU behaves. From there we\'ll be able to build our own custom code to integrate the sensor into a project.

### Example 1 - Rotation Vector

This first example gets us started taking a reading of our complex valued rotation vector, or [quaternion](https://en.wikipedia.org/wiki/Quaternion), which tells us how we are oriented. To get started, open up **Example1-RotationVector** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example1-RotationVector**. To access all of the functions in the BNO080 library we\'ll have to include the library and create an IMU object, this is accomplished in the following lines of code.

    language:c
    #include "SparkFun_BNO080_Arduino_Library.h"
    BNO080 myIMU;

In our `setup()`, we\'ll have to initialize the sensor and enable the parts of the sensor (gyro, accelerometer, magnetometer) that we want to obtain readings from. We\'ll also tell the IMU how often we want a reading from our sensor of choice by passing this value into our enable function in ms. The code outlining this sensor setup is shown below. Pay attention to this as we\'ll be performing a similar setup in many of the remaining examples.

    language:c
    Serial.begin(9600); //Don't forget to enable Serial to talk to your microcontroller
    Serial.println();
    Serial.println("BNO080 Read Example");

    Wire.begin(); //Begin the I2C bus
    Wire.setClock(400000); //Increase I2C data rate to 400kHz

    myIMU.begin();
    myIMU.enableRotationVector(50); //Send data update every 50ms

Now that our sensor is setup, we can look at our `void loop()` to see how we obtain and print data. When the loop executes, it begins by checking to see if the sensor has new data with `myIMU.dataAvailable()`, which returns true when new data is available. We then proceed to get the i, j, k, and real quaternion values along with the accuracy in radians of our measurement using the following lines of code.

    language:c
    float quatI = myIMU.getQuatI();
    float quatJ = myIMU.getQuatJ();
    float quatK = myIMU.getQuatK();
    float quatReal = myIMU.getQuatReal();
    float quatRadianAccuracy = myIMU.getQuatRadianAccuracy();

Printing the rotation vector is then as easy as using a few `Serial.print(quatI, 2)` statements. Uploading the code and opening the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) to a baud rate of **9600** should yield an output similar to the below image.

[![Quaternion Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX1.PNG)

### Example 2 - Accelerometer

Examples 2 deals with pulling the accelerometer values from our sensor to figure out how it is moving. To get started, open up **Example2-Accelerometer** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example2-Accelerometer**. At first glance, you\'ll notice that the way we set up our IMU is nearly identical to the first example. The one difference being in our `setup()`, where we call `myIMU.enableAccelerometer(50);` instead of `myIMU.enableRotationVector(50);` which has the accelerometer report a value every 50 ms. We once again obtain and output our data in our `void loop()` by waiting for data using `myIMU.dataAvailable()`. Once data is available we use the following lines of code to get our x, y, and z acceleration values.

    language:c
    float x = myIMU.getAccelX();
    float y = myIMU.getAccelY();
    float z = myIMU.getAccelZ();

We can then print these values to get our acceleration vector, uploading the code, and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Accelerometer Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX2.PNG)

### Example 3 - Gyro

In example 3, we\'ll pull values from the IMU\'s gyroscope to get a vector for our angular velocity. To get started, open up **Example3-Gyro** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example3-Gyro**. The differences between this example and example 1 are very similar to the differences between examples 1 & 2. We initialize the sensor the exact same way as example 1 only calling `myIMU.enableGyro(50);` instead of `myIMU.enableRotationVector(50);` to have the gyro report it\'s value every 50 ms. We once again obtain and output our data in our `void loop()` by waiting for data using `myIMU.dataAvailable()`. Once data is available, we use the following lines of code to get our x, y, and z gyroscope values.

    language:c
    float x = myIMU.getGyroX();
    float y = myIMU.getGyroY();
    float z = myIMU.getGyroZ();

We can then print these values to get our gyroscope angular velocity vector, uploading the code, and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Gyroscope Serial Monitor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX3-A.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX3-A.PNG)

Also, check out the values in a graph by opening the Serial Plotter to the same baud rate to see the readings from each gyroscope channel plotted against each other. Rotate the IMU and see how the values respond, I got the following output just letting the IMU swing on its cable.

[![Gyroscope Serial Plotter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX3-B.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX3-B.PNG)

### Example 4 - Magnetometer

The following example will get us reading a vector for the magnetic field. To get started, open up **Example4-Magnetometer** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example4-Magnetometer**. The differences between this example and example 1 are very similar to the differences between examples 1 & 2, are you starting to see a pattern here? We initialize the sensor the exact same way as example 1 only calling `myIMU.enableMagnetometer(50);` instead of `myIMU.enableRotationVector(50);` to have the magnetometer report it\'s value every 50 ms. We once again obtain and output our data in our `void loop()` by waiting for data using `myIMU.dataAvailable()`. Once data is available we use the following lines of code to get our x, y, and z magnetometer values. We also obtain the uncertainty in the magnetometer.

    language:c
    float x = myIMU.getMagX();
    float y = myIMU.getMagY();
    float z = myIMU.getMagZ();
    byte accuracy = myIMU.getMagAccuracy();

We can then print these values to get our magnetometer vector, uploading the code, and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Magnetometer Serial Output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-4.PNG)

### Example 5 - Step Counter

The BNO080 has some really neat built in features due to its built in Cortex. One of these is a built in step counter. To get started with this pedometer, open up **Example5-StepCounter** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example5-StepCounter**. The differences between this example and example 1 are very similar to the differences in the previous examples. We initialize our step counter function with a lower sample rate than our previous functions as we don\'t expect steps to happen at as high of a rate. Due to this, we call `myIMU.enableStepCounter(500)` to allow for a half a second in between reports. We once again obtain and output our data in our `void loop()` by waiting for data using `myIMU.dataAvailable()`. Once data is available, we pull the amount of steps from the IMU using `unsigned int steps = myIMU.getStepCount()` to initialize and populate an `unsigned int` with the step count. We then print this value to our serial monitor. Uploading the code and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Step Counter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-5.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-5.PNG)

### Example 6 - Metadata

This example shows us how to retrieve the static metadata from the different sensors in the IMU. To get started, open up **Example6-Metadata** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example6-Metadata**. Notice how this example has an empty `void loop()`? Everything just happens once in our `setup()` loop. To get the metadata for a sensor, we simply pass its corresponding `FRS_RECORD_ID` into `getRange()`, `getResolution()`, `getQ1()`, `getQ2()`, and `getQ3()` to retrieve the metadata for a sensor. The different `FRS_RECORD_ID` variables are shown below.

    language:c
    #define FRS_RECORDID_ACCELEROMETER 0xE302
    #define FRS_RECORDID_GYROSCOPE_CALIBRATED 0xE306
    #define FRS_RECORDID_MAGNETIC_FIELD_CALIBRATED 0xE309
    #define FRS_RECORDID_ROTATION_VECTOR 0xE30B

These are then used like so to print the different parts of each sensors metadata. For a little bit more on metadata, check out page 29 of the [Reference Manual](https://cdn.sparkfun.com/assets/0/4/8/d/1/SH-2-Reference-Manual-v1.2.pdf). Uploading the code and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Metadata](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-6.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-6.PNG)

### Example 7 - Stability Classifier

This example sketch allows us to use the built in stability classifier to figure out how stable the IMU is. To get started, open up **Example7-StabilityClassifier** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example7-StabilityClassifier**. This example is very similar to our first few examples in that we must call `myIMU.enableStabilityClassifier(50);` in our `setup()` function to have the stability classifier report its data every 50 ms. However, we also need to call `myIMU.calibrateGyro()` in our `setup()` function to enable all of our stability classification outputs. We then check if data is available using `myIMU.dataAvailable()`. If it is, we pull the stability classification (a number from 0-5 using `myIMU.getStabilityClassifier()` ) and output the text corresponding to the classification. The code that does this in the `void loop()` is shown below. Also, take note of which number corresponds to which activity.

    language:c
    if (myIMU.dataAvailable() == true)
      

Uploading the code and opening the Serial Monitor to a baud rate of **9600** should yield an output similar to the below image.

[![Stability Classifier](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-7.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-7.PNG)

### Example 8 - Activity Classifier

The activity classifier is somewhat similar to the stability classifier in that it uses the on-board cortex to determine what activity the IMU is doing. To get started, open up **Example8-ActivityClassifier** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example8-ActivityClassifier**. To set up the activity classifier, we need to tell the IMU which activities to look for. We do this using a 32-bit word. There are only 8 possible activities at the moment, so we set our word `enableActivities = 0x1F` to enable everything. The activity classifier also gives a confidence level in each activity. To store these confidences, we create a variable `byte activityConfidences[9]` above our `setup()` function. Then, we can set up the activity classifier in our `setup()` function by calling `myIMU.enableActivityClassifier(50, enableActivities, activityConfidences);`. Using this function enables the activity classifier with 50 ms between reports, activities specified by `enableActivities`, and their confidences are stored in `activityConfidences`. We then check if data is available using `myIMU.dataAvailable()`. If it is, we pull the activity classification (a number from 0-9 using `myIMU.getActivityClassifier()`) and output the text corresponding to the classification. The code that does this is shown below. Take note of which number corresponds to which activity.

    language:c
    void loop()
    

        Serial.println();
      }
    }

    //Given a number between 0 and 8, print the name of the activity
    //See page 73 of reference manual for activity list
    void printActivityName(byte activityNumber)
    

The output of this code should look something like the below image.

[![Activity Classifier](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-8.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-8.PNG)

### Example 9 - Calibrate

When moving between different magnetic environments (different rooms, indoors, outdoors, etc\...), it might be necessary to recalibrate your IMU to obtain the best readings. In order to do this, we\'ll run a calibration function,. To get started, open up **Example9-Calibrate** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example9-Calibrate**. In our setup function, we call the function `myIMU.calibrateAll()` to begin calibration of our sensor. We also need to make sure the we enable our game rotation vector and magnetometer as these are necessary for calculating the calibration of the magnetometer. Go ahead and upload the code to the IMU and open the serial monitor to **9600** baud. Take a look at your output and look for the calibration status. This should probably say `Unreliable`. Make sure you\'re in a clean magnetic environment and go through the calibration steps listed in the [calibration procedure](https://cdn.sparkfun.com/assets/c/6/f/4/9/Sensor-Calibration-Procedure-v1.1.pdf). Once your sensor is calibrated, your accuracy should change from `Unreliable` to `Medium` or `High`. After calibration, send an `s` to your microcontroller over the serial monitor to run the following code and save the calibration.

    language:c
    if(incoming == 's')
    
    }

Your Serial Monitor should look something like the following image when the sensor is being calibrated. Remember, when your confidence levels are satisfactory, send an `s` to save the calibration.

[![Calibration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-9.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-9.PNG)

### Example 10 - Print Packet

Sometimes it\'s easier to look at the raw data coming from the sensor for debugging purposes. This example shows you how to do just that. To get started, open up **Example10-PrintPacket** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example10-PrintPacket**. In our setup, we set up the sensors that we would like to use (in this case, we\'ll set up the magnetometer and accelerometer with 1000 ms sample rates). Since we\'re most likely debugging in this mode, we\'ll also call `myIMU.enableDebugging(Serial)`. Our `void loop()` then simply listens for and prints packets using the below code.

    language:c
    void loop()
    
    }

Your Serial Monitor should look something like the following image with this example code uploaded. Make sure to change the baud rate to **115200** as opposed to 9600 like the previous examples.

[![Print Packet Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/6/4/EX-10.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/EX-10.PNG)

### Example 11 - Advanced Configuration

The final example simply shows us how to configure the sensor on different addresses and I^2^C buses. To get started, open up **Example11-AdvancedConfig** under **File** \> **Examples** \> **SparkFun BNO080 Cortex Based IMU** \> **Example11-AdvancedConfig**. This is simply a matter of setting up the sensor differently. Instead of calling `myIMU.begin()` with no arguments, we call it as `myIMU.begin(0x4A, Wire1)`. If we\'ve pulled the `SI` pin high, the address will be **0x4B**. We can also set up the sensor on a different I^2^C bus if by passing in `Wire2` in place of `Wire1`.

### Bonus Example - Serial Cube Visualizer

**Note:** Processing is a software that enables visual representation of data, among other things. If you\'ve never dealt with Processing before, we recommend you also check out the [Arduino to Processing tutorial](https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing). Follow the below button to go ahead and download and install Processing.\
\

[Download Processing IDE](https://processing.org/download/)

This extra example isn\'t included in the library as it requires Processing. To grab it, go ahead and download or clone the [BNO080 Github Repo](https://github.com/sparkfun/Qwiic_IMU_BNO080).

[Download BNO080 Github Repo (ZIP)](https://github.com/sparkfun/Qwiic_IMU_BNO080/archive/master.zip)

Processing listens for serial data, so we\'ll need to get our Arduino producing serial data that makes sense to Processing. The required Arduino sketch is located in **Qwiic_IMU_BNO080 \> Software \> Serial_Cube_Rotate \> Serial_Cube_Rotate.ino**. This sketch simply prints a list of our quaternions separated by a comma over serial for Processing to listen to.

Once this sketch is uploaded, we need to tell Processing how to turn this data into a visualization. The Processing sketch to do this is located one folder above the Arduino sketch, in **Qwiic_IMU_BNO080 \> Software \> Serial_Cube_Rotate.pde**. Open the **Serial_Cube_Rotate** file in Processing. Before running the sketch, we\'ll need to download ToxicLibs, a library used for computational design. To do this, go to **Sketch \> Import Library\... \> Add Library\...**. Then search for and download **`ToxicLibs`**. Attempting to run the Processing sketch will show us available serial ports in the debug window from this line of code.

    language:c
    myPort = new Serial(this, Serial.list()[0], 115200);

Identify which serial port your Arduino is on. For instance, my RedBoard is on COM6, which corresponds to `[1]` in the image below, so I will need to change 0 to 1 in the following line to ensure Processing is listening to the correct serial port.

[![Serial Ports](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/BONUS-EX-A.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/BONUS-EX-A.PNG)

Once we\'ve done this, we should be able to run the Processing sketch and it will give us a nice visualization of how our IMU is oriented in 3D space as a cube. Try rotating the IMU to see how it responds. You should get a neat little output like the one in the below GIF.

[![Processing Cube Example](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/SerialCube.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/7/6/4/SerialCube.gif)