# Source: https://learn.sparkfun.com/tutorials/ccs811bme280-qwiic-environmental-combo-breakout-hookup-guide

## Introduction

The [CCS811/BME280 (Qwiic) Environmental Combo Breakout](https://www.sparkfun.com/products/14348) work together to take care of all of your atmospheric quality sensing needs with the CCS811 and BME280 ICs. The CCS811 is an exceedingly popular sensor, providing readings for equivalent CO~2~ (or eCO~2~) in the parts per million (PPM) and total volatile organic compounds in the parts per billion (PPB). The CCS811 also has a feature that allows it to fine tune its readings if it has access to the current humidity and temperature. Luckily for us, the BME280 provides humidity, temperature, and barometric pressure! This allows the sensors to work together to give us more accurate readings than they\'d be able to provide on their own. We also made it easy to interface with them via I^2^C.

[![SparkFun Environmental Combo Breakout - CCS811/BME280 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/3/2/9/14348-01.jpg)](https://www.sparkfun.com/products/14348)

### [SparkFun Environmental Combo Breakout - CCS811/BME280 (Qwiic)](https://www.sparkfun.com/products/14348) 

[ SEN-14348 ]

The SparkFun CCS811/BME280 Environmental Combo Breakout takes care of all your atmospheric-quality sensing needs with the pop...

**Retired**

### Required Materials

To get started, you\'ll need a microcontroller or single board computer to control everything.

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

Now to get into the Qwiic ecosystem, the key will be one of the following stackable Qwiic boards to match your preference of microcontroller or single board computer:

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

[![Qwiic Shield for ESP32](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/4/3/Qwiic_ESP32_Shield_04.jpg)](https://www.sparkfun.com/products/14203)

### [Qwiic Shield for ESP32](https://www.sparkfun.com/products/14203) 

[ SPX-14203 ]

\*\*The product has been retired.\*\* We recommend you solder a \[Qwiic breadboard cable\](https://www.sparkfun.com/products/14425)...

**Retired**

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

You will also need a Qwiic cable to connect the shield to your CCS811/BME280, choose a length that suits your needs.

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

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide)

### Qwiic Shield for Arduino & Photon Hookup Guide 

Get started with our Qwiic ecosystem with the Qwiic shield for Arduino or Photon.

For more information on TVOC and eCO2 readings, check out the following blog post.

[](https://news.sparkfun.com/2369 "April 26, 2017: Wherein we seek to answer the age old question: What the heck is a VOC?")

### Hardware Hump Day: Air Quality Measurements with the CCS811 

[April 26, 2017]

Read Post

If the concepts of pressure are weighing on you, check out these links.

- [(external) Air Pressure Altitude Calculator](http://www.mide.com/products/slamstick/air-pressure-altitude-calculator.php) \-- Play around to get a feel for what the pressures are at different altitudes.
- [Wikipedia: Atmospheric_pressure](https://en.wikipedia.org/wiki/Atmospheric_pressure) \-- Has a nice equation for conversion of pressure and altitude (referenced for library code).
- [MPL3115A2 Pressure Sensor Hookup Guide: Pressure vs Altimeter Setting](https://learn.sparkfun.com/tutorials/mpl3115a2-pressure-sensor-hookup-guide#pressure-vs-altimeter-setting) \-- Confused why the reading pressure doesn\'t match the reported pressure from your local weather station? Read this section.

## Hardware Overview

### Power & Features

Together the sensors can consume 13 mA of current. It takes 12 mA to power the CCS811 while 1 mA to power the BME280.

  **Characteristic**   **Range**
  -------------------- ---------------------------------------------------------------------------------------------
  Operating Voltage    3.3V: **Regulated to 1.8V - 3.6V**
  tVOC                 0 - 1187 PPB
  eCO~2~               400 - 8192 PPM
  Temperature          -40&degC - 85&degC
  Humidity             0 - 100% RH, &plusmn3% from 20 - 80%
  Pressure             30 - 110 kPa, relative accuracy of 12 Pa, absolute accuracy of 100 Pa
  Altitude             0 - 30,000ft (9.2km), relative accuracy of 3.3ft (1M) at sea level, 6.6ft (2M) at 30,000ft.

### Communication via I^2^C

The CCS811+BME280 communicates exclusively via I^2^C, utilizing our handy Qwiic system. The Qwiic System utilizes the 4-pin polarized Qwiic connectors highlighted below.

[![i2cconn](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/i2cconn.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/i2cconn.png)

The I^2^C address can also be changed using the jumpers on the back of the board if you are using another device with the same I^2^C address. ADR1 can be used to change the I^2^C address of the CCS811 from 0x5B to 0x5A by adding solder to close the jumper. The ADR2 jumper can be used to change the I^2^C address of the BME280 from 0x77 to 0x76. The I^2^C bus has pull-up resistors enabled by default. If not desired, these can be removed by separating the \"I^2^C PU\" triple jumper on the bottom side with a hobby knife. The locations of these jumpers are shown in the picture below.

[![Jumpers](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/JumperGimp.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/JumperGimp.png)

### Pins

Below is a list of pins made available for the CCS811 and BME280 environmental combo breakout.

  Pin                                        Description                      Direction
  ------------------------------------------ -------------------------------- -----------
  [RST]   Reset (active low, CCS811)       In
  [INT]   Interrupt (active low, CCS811)   Out
  [WAK]   Wake (active low, CCS811)        In
  SCL                                        Clock                            In
  SDA                                        Data                             In
  3.3V                                       Power                            In
  GND                                        Ground                           In

#### Optional Control Lines for the CCS811

Additionally, the three control lines [RST], [INT], and [WAK] can be used to further the degree of control over the CCS811.

- [RST] \-\-- Pull this line low to reset the IC.
- [INT] \-\-- After configuring the sensor to emit interrupt requests, read this line to determine the state of the interrupt.
- [WAK] \-\-- Pull this line high to put the sensor to sleep. This can be used to save power but is not necessary if power is not an issue.

## Hardware Assembly

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/arduino-shields#installing-headers-preparation), now would be the time [solder the headers to the shield](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the CCS811+BME280 breakout (either I^2^C connector will do) and the other into the Qwiic Shield. You\'ll be ready to upload a sketch and start taking air quality measurements once connected. It seems too easy, but thats why we made it this way! We show the [SparkX](https://www.sparkfun.com/sparkx) version of the Qwiic shield below, but the shield is now sold in [SparkFun Red](https://www.sparkfun.com/products/14352)!

[![Combo Sensor to Qwiic Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/7/CCS811_BME280_hookup_guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/CCS811_BME280_hookup_guide-02.jpg)

## Library Overview

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

**Use the Arduino Library Manager!** SparkFun has written libraries to control both the CCS811 and the BME280. You can obtain these libraries through the Arduino Library Manager. Search for **SparkFun CCS811** and **SparkFun BME280** and you should be able to install the latest version. Never installed a library before? That\'s ok! Checkout our tutorial on [installing Arduino Libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library/using-the-library-manager). If you prefer downloading the libraries you can grab them here to manually install:

[Download the SparkFun BME280 Library (ZIP)](https://github.com/sparkfun/SparkFun_BME280_Arduino_Library/archive/master.zip)

[Download the SparkFun CCS811 Library (ZIP)](https://github.com/sparkfun/SparkFun_CCS811_Arduino_Library/archive/master.zip)

Before we get started on a sketch, lets take a look at the libraries used.

### BME280 Library

#### Construction

In the global scope, construct your sensor object (such as `mySensor` or `pressureSensorA`) without arguments.

Example:

`BME280 mySensor;`

#### Object Parameters and setup()

Rather that passing a bunch of data to the constructor, configuration is accomplished by setting the values of the BME280 type in the `setup()` function. They are exposed by being `public:` so use the `myName.aVariable = someValue;` syntax.

*Settable variables of the class BME280:*

//Main Interface and mode settings\
uint8_t commInterface;\
uint8_t I2CAddress;\
uint8_t chipSelectPin;\
\
uint8_t runMode;\
uint8_t tStandby;\
uint8_t filter;\
uint8_t tempOverSample;\
uint8_t pressOverSample;\
uint8_t humidOverSample;\

*An example configuration of the BME280 type in `setup()`:*

    language:c
    #include <stdint.h>
    #include "SparkFunBME280.h"

    #include "Wire.h"
    #include "SPI.h"

    //Global sensor object
    BME280 mySensor;

    void setup()
    

- `uint8_t begin( void )` \-\-- In the above example, begin is used to start the sensor. The basic routine it follows is like this:

  - Starts up the wiring library if necessary, though `#include "Wire.h"` may be needed in your sketch.
  - Concatenates the calibration words as specified by Bosch.
  - Applies user settings to the configuration registers in the BME280.
  - Returns the ID register (should read 0x60).    

  To use it, call `mySensor.begin();` or assign the output to something like `uint8_t myReturnedValue = mySensor.begin();`

  ::: 
  **.begin() Needs to be run once during the setup**, or after any settings have been modified. In order to let the sensor\'s configuration take place, the BME280 requires a minimum time of about 2 ms in the sketch before you take data.
  :::

- `void reset( void )` \-\-- Send the reset word to the BME280. Afterwards, you\'ll have to run begin() again.

- `float readTempC( void )` \-\-- Use to get the temperature in Celsius, as a float.

- `float readTempF( void )` \-\-- Use to get the temperature in Fahrenheit, as a float. Takes no arguments.

- `float readFloatPressure( void )` \-\-- Use to get pressure in units of kiloPascals, as a float.

- `float readFloatAltitudeMeters( void )` \-\-- Use to get altitude in units of meters, as a float.

- `float readFloatAltitudeFeet( void )` \-\-- Use to get altitude in units of feet, as a float. This function calculates based off the measured pressure.

- `float readFloatHumidity( void )` \-\-- Use to get humidity in % relative, as a float.

### CCS811 Library

The library is fairly normal to use compared with our other sensors. You\'ll have to include the library, create a sensor object in the global space, and then use functions of that object to begin and control the sensor. With this one, you must pass the I^2^C address to the object during construction.

**CCS811 Burn-in Time:** Please be aware that the CCS811 datasheet recommends a burn-in of 48 hours and a run-in of 20 minutes (i.e. you must allow 20 minutes for the sensor to warm up and output valid data).

To include the library and to take care of all the gritty compiler stuff, place the following at the beginning of the sketch before `void setup()` function.

    language:c
    #include <SparkFunCCS811.h>

    #define CCS811_ADDR 0x5B //Default I2C Address
    //#define CCS811_ADDR 0x5A //Alternate I2C Address

    CCS811 myCCS811(CCS811_ADDR);

Now functions of the object named `myCCS811` can be called to set up and get data, while all the I^2^C stuff is kept under the hood.

To get the sensor ready during program boot, `myCCS811.begin()` must be called. Here\'s an example of the minimal usage of begin.

    language:c
    void setup()
    

**Error Status:** The .begin() function has a special feature: it returns the status of the function call! If there was a problem during begin, it will return a non-zero code indicating what happened. It\'s optional, and is described in the \"Custom Types and Literals\" section below.

Then in the main `loop()` of the program, calls to the sensor functions such as `mySensor.readAlgorithmResults()` are needed to read the sensor. The following snippet shows a simple check for data by calling the sensor to calculate values, output data, and save the data in variables. However, it doesn\'t do anything with the data! Check out the examples for fully functional code to make use of the sensor data.

    language:c
    void loop()
    
      else if (myCCS811.checkForStatusError())
      

      delay(1000); //Wait for next reading
    }

### Function Reference

The following functions exist for the `CCS811` object. Functions with scoped return type `CCS811Core::status` report an error state as defined in the literals section below. It is optional and can be used to determine success or failure of call.

- `CCS811Core::status begin( void )` \-\-- This starts `wire`, checks the ID register, checks for valid app data, starts the app, and establishes a drive mode.

- `CCS811Core::status readAlgorithmResults( void )` \-\-- Call to cause the sensor to read its hardware and calculate TVOC and eCO~2~ levels.

- `bool checkForStatusError( void )` \-\-- Returns `true` if there is an error pending. This checks the status register.

- `bool dataAvailable( void )` \-\-- Returns `true` if a new sample is ready and hasn\'t been read.

- `bool appValid( void )` \-\-- Returns `true` if there is a valid application within the internal CCS811 memory.

- `uint8_t getErrorRegister( void )` \-\-- Returns the state of the ERROR_ID register.

- `uint16_t getBaseline( void )` \-\-- Returns the baseline value.

- `CCS811Core::status setBaseline( uint16_t )` \-\-- Apply a saved baseline to the CCS811.

- `CCS811Core::status enableInterrupts( void )` \-\-- Enables the interrupt pin for data ready.

- `CCS811Core::status disableInterrupts( void )` \-\-- Disables the interrupt pin.

- `CCS811Core::status setDriveMode( uint8_t mode )` \-\-- Sets the drive mode where `mode` can be 0 through 4:

  - 0: Measurement off
  - 1: Measurement every 1 second
  - 2: Measurement every 10 seconds
  - 3: Measurement every 60 seconds
  - 4: Measurement every 0.25 seconds \-\-- for use with external algorithms\

- `CCS811Core::status setEnvironmentalData( float relativeHumidity, float temperature )` \-\-- Sets the environmental conditions for compensation.

  - relativeHumidity in units of %, 0.00 through 100.0
  - temperature in degrees C, -25.0 through 50.0\

- `void setRefResistance( float )` \-\-- If you\'ve changed the thermistor pull-up, call this to give the sensor the new resistor value. Otherwise, it will be 10000.

- `uint16_t getTVOC( void )` \-\-- Collect the last calculated TVOC value, in parts per billion (ppb).

- `uint16_t getCO2( void )` \-\-- Collect the last calculated eC0~2~ value, in parts per million (ppm).

- `float getResistance( void )` \-\-- Collect the last calculated resistance value of the NTC terminals.

- `float getTemperature( void )` \-\-- Collect the last calculated temperature.

### Custom Types and Literals

The CCS811 library defines a special data type to deal with error states of functions. In most places, the library can be used without paying attention to the function return types, but here are the values the data type `status` can hold if they are needed:

    language:c
    // Return values 
    typedef enum
     status;

To avoid the possibility of multiple libraries using the same `status` name, the enum is actually inside the scope of the CCS811 object, buried in the CCS811Core, which is the base class. *Phew*, don\'t worry about that too much; just place `CCSCore::` before the status name when you want to use it, and use it like a regular enum (e.g., `CCS811Core::status myLocalReturnStatus;`). This just tells the compiler that the variable name is in a specific place. You\'ll also have to add the scope operator to the enum names.

Here\'s an example that shows how the status enum can be used:

    language:c
    CCS811Core::status returnCode = mySensor.beginCore();
    Serial.print("beginCore exited with: ");
    switch ( returnCode )
    

The library also defines names for CCS811 registers, if you\'re using direct read and write functions. These are globally scoped and can be used anywhere.

    language:c
    //Register addresses
    #define CSS811_STATUS 0x00
    #define CSS811_MEAS_MODE 0x01
    #define CSS811_ALG_RESULT_DATA 0x02
    #define CSS811_RAW_DATA 0x03
    #define CSS811_ENV_DATA 0x05
    #define CSS811_NTC 0x06
    #define CSS811_THRESHOLDS 0x10
    #define CSS811_BASELINE 0x11
    #define CSS811_HW_ID 0x20
    #define CSS811_HW_VERSION 0x21
    #define CSS811_FW_BOOT_VERSION 0x23
    #define CSS811_FW_APP_VERSION 0x24
    #define CSS811_ERROR_ID 0xE0
    #define CSS811_APP_START 0xF4
    #define CSS811_SW_RESET 0xFF

## Example Code

For the following examples, which can be found [here](https://github.com/sparkfun/Qwiic_BME280_CCS811_Combo/tree/master/Firmware), we will use our libraries along with a few functions to view our data. Our code\'s preamble, `setup()`, and function definitions will all be the same. However, the `void loop()` will change between the examples. To get started, we first have to initialize our sensors with our preamble, `setup()`, and `loop()` as shown below.

    language:c
    #include <SparkFunBME280.h>
    #include <SparkFunCCS811.h>

    #define CCS811_ADDR 0x5B //Default I2C Address
    //#define CCS811_ADDR 0x5A //Alternate I2C Address

    //Global sensor objects
    CCS811 myCCS811(CCS811_ADDR);
    BME280 myBME280;

    void setup()
    
      else
      

      //Initialize BME280
      //For I2C, enable the following and disable the SPI section
      myBME280.settings.commInterface = I2C_MODE;
      myBME280.settings.I2CAddress = 0x77;
      myBME280.settings.runMode = 3; //Normal mode
      myBME280.settings.tStandby = 0;
      myBME280.settings.filter = 4;
      myBME280.settings.tempOverSample = 5;
      myBME280.settings.pressOverSample = 5;
      myBME280.settings.humidOverSample = 5;

      //Calling .begin() causes the settings to be loaded
      delay(10);  //Make sure sensor had enough time to turn on. BME280 requires 2ms to start up.
      byte id = myBME280.begin(); //Returns ID of 0x60 if successful
      if (id != 0x60)
      
      else
      
    }

Our `void loop` will call a few functions that are not included in our libraries, so we must define them after our `void loop`. Don\'t worry about defining prototypes, the Arduino IDE does this for us. Paste the below code below your `void loop` to define the necessary functions to print data and errors.

    language:c
    void printData()
    

    void printDriverError( CCS811Core::status errorCode )
    
    }

### Example 1 - Basic Readings

The `void loop` shown below will get you up and running taking readings of CO~2~, tVOC(total volatile organic compounds), temperature, pressure, and humidity. Once this sketch is uploaded, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with a baud rate of **9600** to display the air quality data from the sensor.

    language:c
    void loop()
    
      else if (myCCS811.checkForStatusError()) //Check to see if CCS811 has thrown an error
      

      delay(2000); //Wait for next reading
    }

The output of this example should look something like the photo below.

[![example 1 output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/7/e11screencap.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/e11screencap.PNG)

### Example 2 - Calibrated Readings

The `void loop` shown below will get you started taking calibrated readings from the CCS811. When humidity and temperature are known by the CCS811, it is able to refine it\'s tVOC and CO~2~ readings. This sketch feeds the temperature and humidity from the BME280 to the CCS811 in order to attain greater accuracy.

**The BME280 is unable to compensate for the heat produced by the CCS811** This can cause the displayed temperature to be up to 15° higher than the actual ambient temperature. To compensate for this take the difference between an initial temperature reading (with a cold sensor) and a final temperature reading (after letting the sensor warm up). Then subtract this value from \`BMEtempC\` to ensure the proper calibration is taking place.

    language:c
    void loop()
    
      else if (myCCS811.checkForStatusError())
      

      delay(2000); //Wait for next reading
    }

The output for this example is shown below.

[![example 2 output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/7/e_2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/7/e_2.PNG)