# Source: https://learn.sparkfun.com/tutorials/photon-imu-shield-hookup-guide

## Introduction

Does your [Photon](https://www.sparkfun.com/products/13774) project need an accelerometer? What about a gyroscope or a magnetometer? With the [SparkFun Photon IMU Shield](https://www.sparkfun.com/products/13629?_ga=1.205770074.890988720.1429644996), you can get *all three*, thanks to the LSM9DS1 IC module.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.54.19_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.54.19_PM.png)

The SparkFun Photon IMU (Inertial Measurement Unit) Shield is a versatile motion-sensing add-on board for your Photon device that houses a 3-axis accelerometer, 3-axis gyroscope, and 3-axis magnetometer. That's right, 9 degrees of freedom (9DOF) from a single IC!

Each sensor in the LSM9DS1 supports a large variety of ranges: the accelerometer's scale can be set to ± 2, 4, 6, 8, or 16 g, the gyroscope supports ± 245, 500, and 2000 °/s, and the magnetometer has full-scale ranges of ± 2, 4, 8, or 12 gauss. As a bonus, the SparkFun Photon IMU Shield comes with the headers already soldered on, so you can plug your Photon (or Core) in and get started!

**Please Note:** All SparkFun shields for the Photon are also compatible with the [Core](https://store.particle.io/?product=spark-core) from Particle. The WKP, DAC and VBT pins on the Photon will be labeled A7, A6 and 3V3\*, respectively, on the Core, but will not alter the functionality of any of the Shields.

### Covered in this tutorial

This tutorial will cover the functionality of the IMU shield, how to hook it up in your project, and how to program with it using the SparkFun LSM9DS1 Library from the online Particle build environment.

### Required Materials

To get started with the Photon IMU Shield you\'ll want a Photon, a micro-USB cable, and of course the shield itself. You\'ll also want to sign up for an account on [particle.io](http://particle.io) and register your Photon. Instructions on how to do this can be found at [docs.particle.io](http://docs.particle.io/photon/).

[![SparkFun Photon IMU Shield](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/0/1/6/13629-01a.jpg)](https://www.sparkfun.com/sparkfun-photon-imu-shield.html)

### [SparkFun Photon IMU Shield](https://www.sparkfun.com/sparkfun-photon-imu-shield.html) 

[ DEV-13629 ]

This is the SparkFun Photon IMU Shield, a versatile motion-sensing add-on board for your Photon device. Each IMU shield is eq...

**Retired**

[![Particle Photon (Headers)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/3/2/8/13774-01.jpg)](https://www.sparkfun.com/products/13774)

### [Particle Photon (Headers)](https://www.sparkfun.com/products/13774) 

[ WRL-13774 ]

Particle\'s IoT (Internet of Things) hardware development board, the Photon, provides everything you need to build a connected...

**Retired**

### Suggested Reading

Here\'s a few things you may want to brush up on or dive into if you plan on making the most of your IMU Shield.

- [Accelerometer Basics](https://learn.sparkfun.com/tutorials/accelerometer-basics) \-- It\'s always a good idea to know what you\'re measuring, what\'s possible, and what is not.
- [Gyroscopes!](https://learn.sparkfun.com/tutorials/gyroscope) \-- Learn what makes a gyro tick\...er, rotate.
- [Magnetometers](http://en.wikipedia.org/wiki/Magnetometer) \-- Magnetometers\...how do they work!?
- [I^2^C](https://learn.sparkfun.com/tutorials/i2c) \-- I^2^C is the preferred method used to control the IMU. It uses less wires, but is quite a bit slower than, for instance, SPI.
- [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) \-- SPI is another method of communication with the IMU. Refer to the section on jumpers if you\'d like to use this board in SPI mode.

## IMU Shield Overview

### Pin Descriptions

Since the shield does all of the work for you, there\'s no need to actually wire these connections - but in case you\'re looking at datasheets, or code examples, this table will give you a clue as to what the shield is doing. As always, you can check the schematic for more info.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.55.41_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.55.41_PM.png)

  IMU Shield Pin   Photon Pin   Function
  ---------------- ------------ -------------------
  GND              GND          Ground
  VDD              3.3V         Regulated 3.3V in
  SCL              D1           SCL Serial clock
  SDA              D0           Serial Data in

\

We also broke out a few pins at the top of the board that some of you may wish to make use of. From left to right in the picture above, they are:

IMU Shield Pin

Function

DEN AG

Data Enable Accel/Gyro

INT2 AG

Programmable Interrupt Accel/Gyro

INT1 AG

Programmable Interrupt Accel/Gyro

INT M

Programmable Interrupt Magnetometer

DRDY M

Magnetic sensor data ready

\

### Setting the Jumpers

With the board flipped over, you\'ll notice there are six jumpers. The majority of these jumpers are used to **switch between SPI and I^2^C mode**. As the board ships, these jumpers are set to configure the IMU in **I^2^C mode**.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.54.48_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_3.54.48_PM.png)

The SDO M-MISO and SDO A/G-MISO jumpers can be used to set the I^2^C addresses (In I^2^C mode) or, if open, can be used either to set I^2^C address or for SPI control. The default out of the box has both jumpers pulled high for I^2^C mode.

I^2^C Address Table

SDOM /AG

AG Addr.

M Addr.

0

0x6A

0x1C

1

0x6B

0x1E

\

The CS A/G-SS2 and CS M-SS are the chip select jumpers for the accelerometer/gyro and the magnetometer, respectively. The board ships with them both pulled high to enable I^2^C mode. Close the jumpers and cut the former traces to enable SPI mode.

The same story holds true for the SDA-MOSI and SCL-SCK jumpers. They are pulled high to enable I^2^C communication. Close the jumpers in the other direction and cut the former traces to enable SPI mode.

## Using the LSM9DS1 Library

Now that we understand the IMU hardware, let\'s put some code on this thing and see what it can do. Using the Particle library we\'ve written, you\'ll be able to capture acceleration, angular rotation, and magnetic field strength with ease!

### Getting the Particle LSM9DS1 Library

For this page we\'ll be using the [online Particle environment](https://build.particle.io). If you\'re using the Particle Dev environment instead, you can get the library and code examples from the [GitHub repository](https://github.com/sparkfun/SparkFun_LSM9DS1_Particle_Library).

[Download the Particle IMU Library](https://github.com/sparkfun/SparkFun_LSM9DS1_Particle_Library/archive/master.zip)

### Load the Demo Example

If you haven\'t created a Particle user account and claimed your board, you\'ll need to do that now. Starting [here](http://docs.particle.io/) is a great idea if you\'re having trouble.

Once you\'re logged into build.particle.io and have a device selected (all this is covered at the link above), you\'ll want to click on the `create new app` button in the sidebar \-- it\'s big and blue, you can\'t miss it. Call your app something like \'IMU_test\'.

Next \-- this is the important part \-- we include the `LSM9DS1` library. To do this:

- Click on the icon that looks like a bookmark (it\'s all the way to the left on the black skinny sidebar, 4th up from the bottom)
- In the text box under \'community libraries\', search for \'SparkFunLSM\' and you\'ll see \'SparkFunLSM9DS1\' come up (though it might be cut off a little bit, don\'t worry).

It should look something like this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_4.03.06_PM.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/9/9/Screen_Shot_2015-06-30_at_4.03.06_PM.png)

- Click on the library name, and a bunch of stuff will pop up, including all the library files as well as a few options of what to do with the library.
- In this case, we just want to use the library in our app, so click on the \'include in app\' button.
- This will lead you to list of all your apps - click on the name of the app you just created, and you should see a statement like `#include "SparkFunLSM9DS1/SparkFunLSM9DS1.h"` at the top of your app.

Now that we\'ve included the library in our app, let\'s give it some code - just copy the demo code below and **paste it into your app, below the include statements**. NOTE: this example uses I^2^C - check out the \"LSM9DS1_BASIC_SPI.CPP\" file in the Particle library for and SPI example.

    language:cpp
    /*****************************************************************
    LSM9DS1_Basic_I2C.ino
    SFE_LSM9DS1 Library Simple Example Code - I2C Interface
    Jim Lindblom @ SparkFun Electronics
    Original Creation Date: April 30, 2015
    https://github.com/sparkfun/SparkFun_LSM9DS1_Particle_Library

    The LSM9DS1 is a versatile 9DOF sensor. It has a built-in
    accelerometer, gyroscope, and magnetometer. Very cool! Plus it
    functions over either SPI or I2C.

    This Photon sketch is a demo of the simple side of the
    SFE_LSM9DS1 library. It'll demo the following:
    * How to create a LSM9DS1 object, using a constructor (global
      variables section).
    * How to use the begin() function of the LSM9DS1 class.
    * How to read the gyroscope, accelerometer, and magnetometer
      using the readGryo(), readAccel(), readMag() functions and 
      the gx, gy, gz, ax, ay, az, mx, my, and mz variables.
    * How to calculate actual acceleration, rotation speed, 
      magnetic field strength using the calcAccel(), calcGyro() 
      and calcMag() functions.
    * How to use the data from the LSM9DS1 to calculate 
      orientation and heading.

    Hardware setup: This library supports communicating with the
    LSM9DS1 over either I2C or SPI. This example demonstrates how
    to use I2C. 

    If you have the Photon IMU shield, no extra wiring is required.
    If you're using a breakout, the pin-out is as follows:
        LSM9DS1 --------- Photon
         SCL -------------- D1 (SCL)
         SDA -------------- D0 (SDA)
         VDD ------------- 3.3V
         GND ------------- GND
    (CSG, CSXM, SDOG, and SDOXM should all be pulled high. 
    Jumpers on the breakout board will do this for you.)

    Development environment specifics:
        IDE: Particle Build
        Hardware Platform: Particle Photon
                           SparkFun Photon IMU Shield

    This code is released under the MIT license.

    Distributed as-is; no warranty is given.
    *****************************************************************/
    #include "SparkFunLSM9DS1/SparkFunLSM9DS1.h"
    #include "math.h"

    //////////////////////////
    // LSM9DS1 Library Init //
    //////////////////////////
    // Use the LSM9DS1 class to create an object. [imu] can be
    // named anything, we'll refer to that throught the sketch.
    LSM9DS1 imu;

    ///////////////////////
    // Example I2C Setup //
    ///////////////////////
    // SDO_XM and SDO_G are both pulled high, so our addresses are:
    #define LSM9DS1_M   0x1E // Would be 0x1C if SDO_M is LOW
    #define LSM9DS1_AG  0x6B // Would be 0x6A if SDO_AG is LOW

    ////////////////////////////
    // Sketch Output Settings //
    ////////////////////////////
    #define PRINT_CALCULATED
    //#define PRINT_RAW
    #define PRINT_SPEED 250 // 250 ms between prints

    // Earth's magnetic field varies by location. Add or subtract 
    // a declination to get a more accurate heading. Calculate 
    // your's here:
    // http://www.ngdc.noaa.gov/geomag-web/#declination
    #define DECLINATION -8.58 // Declination (degrees) in Boulder, CO.

    void setup() 
    
    }

    void loop()
    

    void printGyro()
    

    void printAccel()
    

    void printMag()
    

    // Calculate pitch, roll, and heading.
    // Pitch/roll calculations take from this app note:
    // http://cache.freescale.com/files/sensors/doc/app_note/AN3461.pdf?fpsp=1
    // Heading calculations taken from this app note:
    // http://www51.honeywell.com/aero/common/documents/myaerospacecatalog-documents/Defense_Brochures-documents/Magnetic__Literature_Application_notes-documents/AN203_Compass_Heading_Using_Magnetometers.pdf
    void printAttitude(
    float ax, float ay, float az, float mx, float my, float mz)
    

Now hit the \'flash\' button (the one that looks like a lightning bolt) and wait for the magic to begin!