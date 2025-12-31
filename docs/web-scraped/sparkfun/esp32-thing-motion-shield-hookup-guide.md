# Source: https://learn.sparkfun.com/tutorials/esp32-thing-motion-shield-hookup-guide

## Introduction

The [ESP32 Thing Motion Shield](https://www.sparkfun.com/products/14430) is a versatile addition to our [ESP32 Thing](https://www.sparkfun.com/products/13907). Small movements can be detected with the tried and true LSM9DS1 IMU, large movements and time can be detected with the addition of a GPS sensor. There\'s a port for the [GP-20U7](https://www.sparkfun.com/products/13740) module, and breakout pins for any serial device. Data can be easily logged by adding a microSD card to the slot. *And did I mention there\'s a general purpose LED?* It works quite well to display GPS lock state!

[![SparkFun ESP32 Thing Motion Shield](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/4/5/8/14430-01.jpg)](https://www.sparkfun.com/sparkfun-esp32-thing-motion-shield.html)

### [SparkFun ESP32 Thing Motion Shield](https://www.sparkfun.com/sparkfun-esp32-thing-motion-shield.html) 

[ DEV-14430 ]

The SparkFun ESP32 Thing Motion Shield is a versatile, motion-sensing addition to our ESP32 Thing.

**Retired**

### Required Materials

To fully follow this hookup guide, you would will need the following materials. You may not need everything though, depending on what you have and what you want to do. Add it to your cart, read through the guide, and adjust the cart as necessary depending on what you would like.

**Note:** This list doesn\'t include the Motion Shield. It is all of the *accessories* used to complete this guide.

### Recommended Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

#### Assembly:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

#### Concepts:

[](https://learn.sparkfun.com/tutorials/gps-basics)

### GPS Basics 

The Global Positioning System (GPS) is an engineering marvel that we all have access to for a relatively low cost and no subscription fee. With the correct hardware and minimal effort, you can determine your position and time almost anywhere on the globe.

[](https://learn.sparkfun.com/tutorials/gyroscope)

### Gyroscope 

Gyroscopes measure the speed of rotation around an axis and are an essential part in determines ones orientation in space.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

**How does GPS work?** For more on GPS, check out this excellent article and video, [Adventures in Science: How GPS Works](https://www.sparkfun.com/news/2442).

#### Programming:

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

[](https://learn.sparkfun.com/tutorials/hexadecimal)

### Hexadecimal 

How to interpret hex numbers, and how to convert them to/from decimal and binary.

[](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide)

### ESP32 Thing Hookup Guide 

An introduction to the ESP32 Thing\'s hardware features, and a primer on using the WiFi system-on-chip in Arduino.

## Hardware Overview

The hardware is a conglomeration of an SD card socket, LSM9DS1 IMU, and GPS serial port. There\'s also an LED for general indication.

[![Motion Shield Parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/motion-shield-top_Highlighted_Export2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/motion-shield-top_Highlighted_Export2.png)

*All components are populated on the top of the board. Here, you can see the SD card, IMU, and port. The ESP32 Thing is intended to sit above this board, so no pins are labeled.*

[![Back of Motion Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/motion-shield-bottom.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/motion-shield-bottom.jpg)

*There are no options on the bottom side. Here, you\'ll find labels for all of the pins. The two rows of pins on the side are wired together so that you have one available for prototyping after installing an ESP32 Thing.*

The signals that are used are show here, grouped by function.

  -------------------------------------------------------------------------------
  ESP32 Thing Pin   Direction      Signal         Group          ESP32 Function
  ----------------- -------------- -------------- -------------- ----------------
  GPIO 13           I              LED            LED            GPIO 13

  GPIO 16           I              GPS_TX         GPS UART       Serial 1

  GPIO 17           O              GPS_RX         GPS UART       Serial 1

  GPIO 18           I              SD_SCK         SD Card        SPI SCK

  GPIO 19           O              SD_DO          SD Card        SPI MISO

  GPIO 23           I              SD_DI          SD Card        SPI MOSI

  GPIO 33           I\             SD_CS          SD Card        GPIO 33

  GPIO 38           I\             SD_CD          SD Card        GPIO 38

  GPIO 21           I/O            SDA            IMU            I2C SDA

  GPIO 22           I              SCL            IMU            I2C SCL
  -------------------------------------------------------------------------------

## Hardware Assembly

In this section, we\'ll prepare the shield for a development environment by adding headers. This section also shows what the GPS module, battery, and SD card look like when properly inserted.

[![ESP32 Stacked on ESP32 Thing Motion with GPS and battery ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/jst-battery-gps2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/jst-battery-gps2.jpg)

*The completed stack.*

### Attach the Stackable Headers to the Motion Shield

[Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) a single pin on each header. Make sure the headers are straight, and lined up. You can use perf board, or an already populated ESP32 Thing to help with alignment.

[![ESP32 Thing Motion Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/soldering-headers2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/soldering-headers2.jpg)

Solder the rest of the pins focusing on getting nice, even, conic fillets.

[![Finished Soldering](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/soldering-headers4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/soldering-headers4.jpg)

### Attach the Headers to the ESP32 Thing

Put the pin headers in the shield, and set the ESP32 Thing on top. Then, apply solder and build up nice fillets making sure to not bridge any pins.

[![ESP32 Headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/soldering-headers5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/soldering-headers5.jpg)

### Adding an Optional Sensor

If you\'re using a BME280 to try out the I2C or SPI port, install headers on it as well. See the [BME280 Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-bme280-breakout-hookup-guide) for more information.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/BME280_Tutorial-06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/BME280_Tutorial-06.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/BME280_Tutorial-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/BME280_Tutorial-04.jpg)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/BME280_Tutorial-07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/BME280_Tutorial-07.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

*For generic operation solder both headers (left). If you only need I^2^C (middle), or SPI (right), only attach those headers.*

### 3-Pin JST and microSD Card

Make sure the JST and microSD cards are installed properly.

- If the JST connectors feel like they\'re not going in, don\'t force them, try wiggling them instead. They will hang out a bit when properly seated.

- The microSD card slot is dual position with click feature, and the PCB has a recess. The card should easily click in and out.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/jst-port.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/jst-port.png)   [![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/micro-sd-port.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/micro-sd-port.png)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*The JST connectors are seated properly, protruding slightly from their sockets (left). When the SD card is inserted properly (right), it should be flush with the edge of the board.*

\

### Stack and Connect Additional Parts!

Stack the ESP32 Thing on the ESP32 Thing Motion Shield.

[![Completed Installation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/jst-battery-gps2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/jst-battery-gps2.jpg)

*ESP32 Thing, motion shield, GPS receiver, and battery installed. The ESP32 Thing is ready for code!*

You can also install the stack in a breadboard, letting the antenna hang off the end so you have the most room left to work with when prototyping. If using the BME280, install that on the breadboard as well and wire the sensor as explained in the \"[Using the I2C and SPI Buses](https://learn.sparkfun.com/tutorials/esp32-thing-motion-shield-hookup-guide#using-the-i2c-and-spi-buses)\" example.

## Software

### General Requirements

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

The Motion Shield itself doesn\'t use any special software. It relies on the SD card library from the ESP32 core, and the LSM9DS1 library, plus whatever you attach to it. Make sure you\'ve got the following installed before continuing on to the examples.

- **ESP32 Thing Arduino Core** \-- Follow the [instructions from the ESP32 Thing Hookup Guide](https://learn.sparkfun.com/tutorials/esp32-thing-hookup-guide#installing-the-esp32-arduino-core).
- **Arduino Libraries:**
  - **LSM9DS1** \-- Follow the [LSM9DS1 Hookup Guide](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide#installing-the-arduino-library) or use the library manager.
  - **BME280** \-- Follow the [BME280 Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-bme280-breakout-hookup-guide#installing-the-arduino-library) or use the library manager.
- **Your choice of NMEA parser, or do it yourself!** \-- Examples are contained and need no libraries.

The example code used throughout this tutorial can also be found in the ESP32 Thing Motion Shield\'s GitHub repository.

[ESP32 Thing Motion Shield Example Code](https://github.com/sparkfun/ESP32_Motion_Shield/tree/master/Software)

### General Tips

**Strapping Pins**

The following pins are used to configure the CPU at power up to indicate various booting methods (known as \'strapping\' pins). These are exposed to the user, but should be avoided for beginners. Attaching a device that matches the default state during power up should not interfere with the boot procedure. If it seems like the ESP32 isn\'t booting properly, investigate these pins.

**Proper Usage:** To get full functionality from these pins, attach a tri-state buffer, then enable the buffer with software after the boot has completed. This advanced method is not covered here.

  ESP32 Pin Name   ESP32 Thing Pin Name   Default Pull   Description
  ---------------- ---------------------- -------------- -----------------------------
  MTDI             GPIO12                 High           Internal LDO voltage select
  GPIO0            GPIO0                  High           SPI/Download boot
  GPIO2            GPIO2                  Low            SPI/Download boot
  MTDO             GPIO15                 High           U0TXD toggling mode/timing
  GPIO5            GPIO5                  High           U0TXD timing
  GPIO4            GPIO4                  Low            Unknown

If U0TXD, GPIO2, GPIO5 are floating, GPIO0 determines boot mode.

See the [ESP32 Datasheet](http://espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf) for more information.

**Input-only Pins**

GPIO34 through GPIO39 work only as inputs, with no internal pull capabilities (as of 10/31/2017).

**Standard pin naming**

The pins listed in [Hardware Overview](https://learn.sparkfun.com/tutorials/esp32-thing-motion-shield-hookup-guide#hardware-overview) are also listed here as #defines you can use. Not all are necessary for every application, but it\'s nice to have them all in one place for reference.

    language:c
    #define AUX_LED_PIN 13
    #define GPS_TX_PIN 16
    #define GPS_RX_PIN 17
    #define SD_SCK_PIN 18
    #define SD_DO_PIN 19
    #define SD_DI_PIN 23
    #define SD_CS_PIN 33
    #define SD_CD_PIN 38
    #define IMU_SDA_PIN 21
    #define IMU_SCL_PIN 22

## Using the IMU

The IMU on the shield is the LSM9DS1, which is connected the the ESP32 Thing to the I2C port only. Any of the examples from the LSM9DS1 library should be good to go, as long as you specify the port type to be I2C with default addresses.

There are two examples in this section that will work without modification on the Motion Board.

The first example is a modification of the *LSM9DS1_ESP32_Settings.ino* example, with SPI related information removed. This is a good place to start because it shows all of the API, and you can comment out what you don\'t need.

    language:c
    /*****************************************************************
    LSM9DS1_ESP32_Settings.ino
    SFE_LSM9DS1 Library Settings Configuration Example
    Original Creation: August 13, 2015 by Jim Lindblom
    https://github.com/sparkfun/LSM9DS1_Breakout

    This Arduino sketch demonstrates how to configure every 
    possible configuration value in the SparkFunLSM9DS1 library.

    It demonstrates how to set the output data rates and scales
    for each sensor, along with other settings like LPF cutoff
    frequencies and low-power settings.

    It also demonstrates how to turn various sensors in the
    LSM9DS1 on or off.

    Hardware setup: This library is intended to be used with a 
    ESP32 Motion shield connected directly to the ESP32 Thing.

    Development environment specifics:
    IDE: Arduino 1.8.2
    Hardware Platform: ESP32 Arduion Board

    This code is beerware. If you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, 
    please buy us a round!

    Distributed as-is; no warranty is given.
    *****************************************************************/
    // Include SparkFunLSM9DS1 library and its dependencies
    #include <Wire.h>
    #include <SPI.h>
    #include <SparkFunLSM9DS1.h>

    LSM9DS1 imu;  // Create an LSM9DS1 object

    // Mag address must be 0x1E, would be 0x1C if SDO_M is LOW
    #define LSM9DS1_M   0x1E
    // Accel/gyro address must be 0x6B, would be 0x6A if SDO_AG is LOW
    #define LSM9DS1_AG  0x6B

    // Global variables to keep track of update rates
    unsigned long startTime;
    unsigned int accelReadCounter = 0;
    unsigned int gyroReadCounter = 0;
    unsigned int magReadCounter = 0;
    unsigned int tempReadCounter = 0;

    // Global variables to print to serial monitor at a steady rate
    unsigned long lastPrint = 0;
    const unsigned int PRINT_RATE = 500;

    void setupGyro()
    

    void setupAccel()
    

    void setupMag()
    

    void setupTemperature()
    

    uint16_t initLSM9DS1()
    

    void setup() 
    

    void loop() 
    

    // imu.gyroAvailable() returns 1 if new gyroscope
    // data is ready to be read. 0 otherwise.
    if (imu.gyroAvailable())
    

    // imu.magAvailable() returns 1 if new magnetometer
    // data is ready to be read. 0 otherwise.
    if (imu.magAvailable())
    

    // imu.tempAvailable() returns 1 if new temperature sensor
    // data is ready to be read. 0 otherwise.
    if (imu.tempAvailable())
    

    // Every PRINT_RATE milliseconds, print sensor data:
    if ((lastPrint + PRINT_RATE) < millis())
    
    }

    // printSensorReadings prints the latest IMU readings
    // along with a calculated update rate.
    void printSensorReadings()
    

The second example is more heavily modified example. It outputs CSV data to the serial port (which can be rerouted to a file if you\'re into that). Here, a simple configuration is chosen but more work is done with the output data.

    language:c
    /*****************************************************************
    LSM9DS1_CSV.ino
    Collecting IMU data as CSV for graphing

    Original Creation: August 13, 2015 by Jim Lindblom
    from the LSM9DS1_Basic_I2C.ino library example.
    https://github.com/sparkfun/LSM9DS1_Breakout

    Hardware setup: This library is intended to be used with a 
    ESP32 Motion shield connected directly to the ESP32 Thing.

    Development environment specifics:
    IDE: Arduino 1.8.2
    Hardware Platform: ESP32 Arduion Board

    This code is beerware. If you see me (or any other SparkFun 
    employee) at the local, and you've found our code helpful, 
    please buy us a round!

    Distributed as-is; no warranty is given.
    *****************************************************************/
    // The SFE_LSM9DS1 library requires both Wire and SPI be
    // included BEFORE including the 9DS1 library.
    #include <Wire.h>
    #include <SPI.h>
    #include <SparkFunLSM9DS1.h>

    LSM9DS1 imu;  // Create an LSM9DS1 object

    #define LSM9DS1_M   0x1E // Would be 0x1C if SDO_M is LOW
    #define LSM9DS1_AG  0x6B // Would be 0x6A if SDO_AG is LOW

    #define PRINT_SPEED 250 // 250 ms between prints
    static unsigned long lastPrint = 0; // Keep track of print time

    // Earth's magnetic field varies by location. Add or subtract 
    // a declination to get a more accurate heading. Calculate 
    // your's here:
    // http://www.ngdc.noaa.gov/geomag-web/#declination
    #define DECLINATION -8.58 // Declination (degrees) in Boulder, CO.

    //Internal variables
    float roll;
    float pitch;
    float heading;
    char csvBuffer[300];

    void setup() 
    

    }

    void loop()
    
    if ( imu.accelAvailable() )
    
    if ( imu.magAvailable() )
    

    if ((lastPrint + PRINT_SPEED) < millis())
    
    }

    void calcAttitude(float ax, float ay, float az, float mx, float my, float mz)
    

## Using the MicroSD Card

The microSD card relies on the libraries packaged with the ESP32 Arduino board files. The best way to garner knowledge is to go into the source files and read the various header files, or to use the example sketches.

To use the examples directly, make sure you assign the CS pin to 33.

This example also shows how to setup the CD pin as input, and to us it to detect a card. The program will halt during setup if a card is not detected, or if the card doesn\'t mount properly.

If everything\'s a go, the *SD_Test_Motion_Board.ino* example will report basic information about the card.

    language:c
    /*****************************************************************
    SD_Test_Motion_Board.ino

    This is a modified version of the SD_Test example sketch
    included with the Arduino core for the esp32, from
    https://github.com/espressif/arduino-esp32

    This example:
    * Uses the CD pin to check for a card
    * Mounts the card
    * Prints information about the card.

    Use this for a starting place while working with SD cards.

    Hardware requirements:
    ESP32 Thing attached to Motion Board

    Distributed as-is; no warranty is given.
    *****************************************************************/
    #include "FS.h"
    #include "SD.h"
    #include "SPI.h"

    #define SD_CS_PIN 33
    #define SD_CD_PIN 38

    void setup() else    
        //Call begin with (cs pin, SPI, rate (up to 10MHz), "/sd")
        if(!SD.begin(SD_CS_PIN, SPI, 1000000, "/sd"))
        uint8_t cardType = SD.cardType();

        if(cardType == CARD_NONE)

        Serial.print("SD Card Type: ");
        if(cardType == CARD_MMC) else if(cardType == CARD_SD) else if(cardType == CARD_SDHC) else 

        uint64_t cardSize = SD.cardSize() / (1024 * 1024);
        Serial.printf("SD Card Size: %lluMB\n", cardSize);

    }

    void loop()

To help with development in the *FileSerialExample.ino* example, I\'ve written a little SD extension library that allows writing of sequentially numbered files up to a particular size. It behaves like a serial port, so things like .println() can be used.

**Don\'t run this example!** This example requires **FileSerial.cpp** and **FileSerial.h** to operate. It is here to show how similar the file writing operation of these two included files is to a normal serial object. Get the full project (this example plus code and header) from <https://github.com/sparkfun/ESP32_Motion_Shield/tree/master/Software/FileSerialExample>.

In addition to standard methods such as `print()` and `println()`, the library includes the following functionality.

#### Construction

Create a file writing object with the class name FileSerial. You can construct in two ways:

- `FileSerial ExampleFileSet(&Serial);` \-- Verbose output of data/File IO status to passed serial object.
- `FileSerial ExampleFileSet;` \-- Non-verbose.

#### begin();

`int begin(fs::FS * inputDevice, uint8_t ssPin, SPIClass &spi, uint32_t frequency, const char * mountpoint);`

Call begin to mount the card and start the SPI device.

**Pass**: device, CS pin, port, frequency, and mount point.

**Returns**: 1 if success.

**Example**:`ExampleFileSet.begin(&SD, 33, SPI, 10000000, "/sd")`

**Using Multiple FileSerial Instances:** Calling .begin checks if another FileSerial object has already mounted the card. If so, it doesn\'t re-initialize the microSD card, so multiple files can be written simultaneously. They can even have different paths.

#### setMaxFileSize();

`void setMaxFileSize( int32_t inputSize );`

Call to set the max file size in bytes.

**Default**: 250kB

**Range**:

- 0 \-- No cap.
- 32 to 1000000000 \-- 32 bytes to 1GB

#### setWriteBufferSize();

`void setWriteBufferSize( uint8_t inputSize );`

Call to set buffer size in bytes before performing file write.

**Default**: 100B

**Range**: 1 to 255 \-- 1B to 255B

#### startLog()

`int startLog( const char * inputPath, const char * inputStub );`

Start a batch of log files. Pass directory name and file name. The file name will be appended with *nnnn.txt* where \"*nnnn*\" are sequential numbers.

If directory is a path, parent directories must exist!

- \"\[existing directory\]/\[new directory\]\" is valid
- \"\[new directory\]/\[new directory\]\" is not

**Example**:`ExampleFileSet.startLog("testFiles", "file");`

    language:c
    /******************************************************************************
    FileSerialExample.ino
    Example Serial-like file writer

    Marshall Taylor @ SparkFun Electronics
    original creation date: Nov 6, 2017
    https://github.com/sparkfun/ESP32_Motion_Shield

    This example demonstrates usage of the FileSerial library.

    The FileSerial libary implements the ESP32 SD_Test functions as a class that acts like a
    HardwareSerial device.  It has been modeled from the ESP32 Arduino core's
    HardwareSerial class, but takes no input streams from the user.

    There are a couple extra functions that aren't normally found in a serial device

        int startLog( const char * inputPath, const char * inputStub );
        int stopLog( void );
        void setMaxFileSize( int32_t inputSize );
        void setWriteBufferSize( uint8_t inputSize );

    Construct with an optional serial device address, such as

        FileSerial ExampleFileSet(&Serial);

    Doing so logs SD read/write information plus written data to the passed serial port.

    Resources:
    ESP32 Arduino core

    Development environment specifics:
    Arduino 1.8.2

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).
    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.
    Distributed as-is; no warranty is given.
    ******************************************************************************/

    #include <Arduino.h>
    #include "FileSerial.h"

    //Pass address of serial port to see the file IO debug information
    FileSerial ExampleFileSet(&Serial);

    //...or don't
    //FileSerial ExampleFileSet;

    int loopCount = 0;

    void setup()
        //File name will be appended with file number, ex: filennnn.txt

        //You can set max file size in bytes, set 0 for unchecked.
        //Default is 250kB, range 0, 32 to 1000000000
        ExampleFileSet.setMaxFileSize(10000);

        //You can as set buffer size between file writes.
        //Default is 100B, range is 1 to 255B
        ExampleFileSet.setWriteBufferSize(80);

        //Start a batch of log files with startLog,
        //pass directory name and file name.
        //
        //If directoy is path, parent directories must exist!
        //"[existing directory]/[new directory]" is valid
        //"[new directory]/[new directory]" is not
        ExampleFileSet.startLog("testFiles", "file");
    }

    void loop()
        ExampleFileSet.printf("Loop count: %d\n", loopCount); //Formatting works
        ExampleFileSet.println(2.54321, 3); //standard formatting works
        ExampleFileSet.println(0x2E0A, HEX); //and other types
        loopCount++;
        delay(100);

    }

## Using the I2C and SPI Buses

To demonstrate the attachment of additional I2C and SPI devices, a BME280 is used. This could be any device, but the BME280 has both ports and is pretty easy to work with. There is one catch though, the SPI bus is shared with the microSD card and it will limit in the microSD card\'s data rate to the lowest common speed.

The two examples shown are actually the same program, but with two lines which configure the BME280 for either I2C or SPI mode.

### I2C

Hookup the I2C pins between the BME280 and the ESP32 Thing as shown below.

[![BME280 and I2C Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/fritzing2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/fritzing2.jpg)

*Connect the BME280 I2C port*

To connect the BME280 to the ESP32, wire up as follows:

  -----------------------------------------------------------------------
  BME280 Pin\                         ESP32 Pin\
  ----------------------------------- -----------------------------------
  SCL                                 22

  SDA                                 21

  3.3V                                3.3V

  GND                                 GND
  -----------------------------------------------------------------------

Then, run the following example.

    language:c
    /******************************************************************************
    BME280_I2C_SPI.ino
    BME280 on the ESP32 Thing

    Marshall Taylor @ SparkFun Electronics
    Original creation date: May 20, 2015
    Modified: Nov 6, 2017
    https://github.com/sparkfun/ESP32_Motion_Shield

    This sketch configures a BME280 to produce comma separated values for use
    in generating spreadsheet graphs.

    It has been modified from the original BME280 example to demonstrate I2C and
    SPI operation on the ESP32 Motion board.

    Original source:
    https://github.com/sparkfun/SparkFun_BME280_Arduino_Library

    Resources:
    Uses Wire.h for I2C operation
    Uses SPI.h for SPI operation

    Development environment specifics:
    Arduino IDE 1.8.2

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).
    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.
    Distributed as-is; no warranty is given.
    ******************************************************************************/
    #include <stdint.h>
    #include "SparkFunBME280.h"

    #include "Wire.h"
    #include "SPI.h"

    #define BME280_CS_PIN 17

    //Global sensor object
    BME280 mySensor;

    unsigned int sampleNumber = 0; //For counting number of CSV rows

    void setup()
    

        //***Operation settings*****************************//
        mySensor.settings.runMode = 3; //  3, Normal mode
        mySensor.settings.tStandby = 0; //  0, 0.5ms
        mySensor.settings.filter = 0; //  0, filter off
        //tempOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.tempOverSample = 1;
        //pressOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.pressOverSample = 1;
        //humidOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.humidOverSample = 1;

        Serial.begin(115200);
        Serial.print("Program Started\n");
        Serial.print("Starting BME280... result of .begin(): 0x");
        delay(10);  //Make sure sensor had enough time to turn on. BME280 requires 2ms to start up.
        //Calling .begin() causes the settings to be loaded
        Serial.println(mySensor.begin(), HEX);

        //Build a first-row of column headers
        Serial.print("\n\n");
        Serial.print("Sample,");
        Serial.print("T(deg C),");
        Serial.print("T(deg F),");
        Serial.print("P(Pa),");
        Serial.print("Alt(m),");
        Serial.print("Alt(ft),");
        Serial.print("%RH");
        Serial.println("");

    }

    void loop()
    

### SPI

**SPI Data Rate:** The SPI port is shared with the microSD card. The Arduino Board for the ESP32 doesn\'t allow multiple data rates, so when using the SPI port for your own peripherals, the SD data rate will be constrained to the lowest common speed capability.

Now wire the BME280 up to the ESP32\'s SPI port.

[![BME280 and SPI Example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/fritzing1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/fritzing1.jpg)

*Connect the BME280 SPI port*

Here are the connections in the picture.

  -----------------------------------------------------------------------
  BME280 Pin\                         ESP32 Pin\
  ----------------------------------- -----------------------------------
  CS                                  17\

  SDI\                                23

  SDO                                 19

  SCK\                                18\

  3.3V                                3.3V

  GND                                 GND
  -----------------------------------------------------------------------

To start the BME280 in SPI mode, we switch the configuration by commenting/uncommenting code as shown in the example below. Otherwise, the code is the same.

    language:c
    /******************************************************************************
    BME280_I2C_SPI.ino
    BME280 on the ESP32 Thing

    Marshall Taylor @ SparkFun Electronics
    Original creation date: May 20, 2015
    Modified: Nov 6, 2017
    https://github.com/sparkfun/ESP32_Motion_Shield

    This sketch configures a BME280 to produce comma separated values for use
    in generating spreadsheet graphs.

    It has been modified from the original BME280 example to demonstrate I2C and
    SPI operation on the ESP32 Motion board.

    Original source:
    https://github.com/sparkfun/SparkFun_BME280_Arduino_Library

    Resources:
    Uses Wire.h for I2C operation
    Uses SPI.h for SPI operation

    Development environment specifics:
    Arduino IDE 1.8.2

    This code is released under the [MIT License](http://opensource.org/licenses/MIT).
    Please review the LICENSE.md file included with this example. If you have any questions 
    or concerns with licensing, please contact techsupport@sparkfun.com.
    Distributed as-is; no warranty is given.
    ******************************************************************************/
    #include <stdint.h>
    #include "SparkFunBME280.h"

    #include "Wire.h"
    #include "SPI.h"

    #define BME280_CS_PIN 17

    //Global sensor object
    BME280 mySensor;

    unsigned int sampleNumber = 0; //For counting number of CSV rows

    void setup()
    

        //***Operation settings*****************************//
        mySensor.settings.runMode = 3; //  3, Normal mode
        mySensor.settings.tStandby = 0; //  0, 0.5ms
        mySensor.settings.filter = 0; //  0, filter off
        //tempOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.tempOverSample = 1;
        //pressOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.pressOverSample = 1;
        //humidOverSample can be:
        //  0, skipped
        //  1 through 5, oversampling *1, *2, *4, *8, *16 respectively
        mySensor.settings.humidOverSample = 1;

        Serial.begin(115200);
        Serial.print("Program Started\n");
        Serial.print("Starting BME280... result of .begin(): 0x");
        delay(10);  //Make sure sensor had enough time to turn on. BME280 requires 2ms to start up.
        //Calling .begin() causes the settings to be loaded
        Serial.println(mySensor.begin(), HEX);

        //Build a first-row of column headers
        Serial.print("\n\n");
        Serial.print("Sample,");
        Serial.print("T(deg C),");
        Serial.print("T(deg F),");
        Serial.print("P(Pa),");
        Serial.print("Alt(m),");
        Serial.print("Alt(ft),");
        Serial.print("%RH");
        Serial.println("");

    }

    void loop()
    

## Using the GPS Port

The GPS port is just a pass-through to the serial port, so configuration is easy. Simply start the serial port at the desired baud, usually 9600.

This example simply passes serial monitor data to the GPS port, and GPS data to the serial monitor. Set the serial speeds when calling begin. `Serial` is the USB serial port, and `GPSUART` is the GPS port.

    language:c
    #include <Arduino.h>
    HardwareSerial GPSUART(2);  // Set up GPS UART on pins 16 & 17

    void setup()
    

    void loop() 
      //Pass gps data to the usb
      if (GPSUART.available())
      
    }

[![Different GPS Receivers Connected to GPS port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/8/multiple-hookups.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/multiple-hookups.jpg)

*(left) Connection to the [GP-20U7](https://www.sparkfun.com/products/13740). (right) Connection to the [GP-735](https://www.sparkfun.com/products/13670).*

As for the hardware, either plug in the recommend 3-wire GPS module (rx only), or wire in a 4-wire module (that can be run from **3.3V**) to the provided pin header.

The data that the GPS will emit comes in the form of NMEA messages. See the [NMEA Reference Manual (PDF)](https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf) for information on decoding.

## Logging a Journey

Putting all the concepts from this hookup guide together, a data logger can be built that saves IMU and GPS data. For your consideration, a simple example exists in the software folder of the Motion Shield\'s GitHub repository.

[ESP32_Motion_Shield / Software / GPS_IMU_SD_Logger](https://github.com/sparkfun/ESP32_Motion_Shield/tree/master/Software/GPS_IMU_SD_Logger)

The program collects the GPS data as strings of NMEA data, and the IMU data as CSV. It uses the FileSerial library to create two sets of files, one for GPS data and one for IMU data. What to do with the data is up to you, but let\'s take a look at the GPS data and graph it.

This is what the GPS NMEA messages look like:

- [Example NMEA data](https://github.com/sparkfun/ESP32_Motion_Shield/blob/master/Software/GPS_IMU_SD_Logger/extras/fullGPS.txt)

The data is given to a tool such as the [GPS Visualizer](http://www.gpsvisualizer.com), which can create various types of data. Outputting as GPX format, the data can be passed to a map web application.

- [Example GPX data](https://github.com/sparkfun/ESP32_Motion_Shield/blob/master/Software/GPS_IMU_SD_Logger/extras/fullGPS.gpx)

And finally, the GPS track can be viewed.

[![Example Data Logged on a Map](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/data_track.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/8/data_track.jpg)

*Taking a trip from Denver to SparkFun. Example data logged and mapped with the GPS Visualizer on Google Maps.*

GPS Visualizer can also produce data that can be used in Google Earth, and has a bunch of options. If you\'ve never used GPS data before, it can be super helpful to demystify all the terminology.