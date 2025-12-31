# Source: https://learn.sparkfun.com/tutorials/mpu-9250-hookup-guide

## Introduction

The [MPU-9250](https://www.sparkfun.com/products/13762) is the latest 9-axis MEMS sensor from InvenSense®. This replaces the popular EOL\'d [MPU-9150](https://www.sparkfun.com/products/retired/11486). InvenSense® lowered power consumption and decreased the size by 44% compared to the MPU-9150. \"Gyro noise performance is 3x better, and compass full scale range is over 4x better than competitive offerings.\" The MPU-9250 uses 16-bit analog-to-digital converters (ADCs) for digitizing all 9 axes.

[![SparkFun IMU Breakout - MPU-9250](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/0/6/13762-SparkFun_IMU_Breakout_-_MPU-9250-00.jpg)](https://www.sparkfun.com/products/13762)

### [SparkFun IMU Breakout - MPU-9250](https://www.sparkfun.com/products/13762) 

[ SEN-13762 ]

The SparkFun MPU-9250 IMU Breakout features the latest 9-axis MEMS sensor from InvenSense.

**Retired**

The **S**ystem **i**n **P**ackage ([SiP]) combines two chips: the MPU-6500, which contains a 3-axis gyroscope, a 3-axis accelerometer, and the AK8963, a 3-axis magnetometer.

### Suggested Reading

Before getting started, you may find the following links useful:

- [I^2^C Protocol](https://learn.sparkfun.com/tutorials/i2c)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [What are Pull-up Resistors?](https://learn.sparkfun.com/tutorials/pull-up-resistors)
- [How to use a Breadbaord](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)

## Board Overview

[![MPU-9250 \<abbr title=](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/13762-01a.jpg)PCB\" /\>](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/13762-01a.jpg)

*The MPU-9250 Breakout as you will receive it*

The board is designed to be smaller than some of our other offerings to fit in smaller projects. To achieve this, the [PTH]s are wrapped around the boarder of the [PCB] in three rows of three or four. The top row ([J1](https://cdn.sparkfun.com/datasheets/Sensors/IMU/SparkFun_MPU-9250_Breakout.pdf)) is all one need to get most of the functionality of the IMU. These include the I^2^C and power interface. If space were really tight, one could take a saw and carefully remove all of the other [PTH]s.

The second most likely to be used set of [PTH]s are found along the bottom ([J3](https://cdn.sparkfun.com/datasheets/Sensors/IMU/SparkFun_MPU-9250_Breakout.pdf)). This includes the address pin, the interrupt pin, and the IO voltage supply for easy interface with a more modern 1.8V processor.

The third, non-breadboard-compatible row ([J2](https://cdn.sparkfun.com/datasheets/Sensors/IMU/SparkFun_MPU-9250_Breakout.pdf)) is used for features like running other I^2^C devices as slaves to this one. For prototyping with these connections, throw your connections on top like you would with an [Arduino Pro Mini](https://www.sparkfun.com/products/11114) or similar product.

### PTH Connections

The following table summarizes all of the plated through hole ([PTH]) connections on the breakout board in order found on the board stating in the upper-left corner and wrapping clockwise:

  --------------------------------------------------------------------------------------------------------------------
  Pin Label               Pin Function                Notes
  ----------------------- --------------------------- ----------------------------------------------------------------
  **SCL**                 I^2^C serial clock\         100 or 400 kHz I^2^C\
                          SPI serial port clock       Up to 1 MHz SPI (20 MHz in certain cases)

  **SDA**                 I^2^C serial data           Can also be used for SPI serial data input (SDI)

  **VDD**                 Power supply                +2.4V to +3.6V

  **GND**                 Ground reference            +0V

  **AUXDA**               Ground reference            I^2^C master serial data, for connecting to external sensors

  **FSYNC**               Ground reference            Frame synchronization digital input. Connect to GND if unused.

  **AUXCL**               Ground reference            I^2^C Master serial clock, for connecting to external sensors

  **INT**                 Interrupt signal            Interrupt digital output (totem pole or open-drain)

  **CS**                  Chip select                 Chip select (SPI mode only)

  **AD0/\                 Address selection           I^2^C Slave Address LSB (AD0):\
  SDO**                                                  Low: 0b1101000 ➫ 0x68\
                                                         High: 0b1101001 ➫ 0x69\
                                                      SPI serial data output (SDO)

  **VDDIO**               Power supply for I/O pins   +1.71V up to VDD
  --------------------------------------------------------------------------------------------------------------------

### Jumpers

The MPU-9250 Breakout has two solder jumpers, [SJ1](https://cdn.sparkfun.com/datasheets/Sensors/IMU/SparkFun_MPU-9250_Breakout.pdf) and [SJ2](https://cdn.sparkfun.com/datasheets/Sensors/IMU/SparkFun_MPU-9250_Breakout.pdf).

SJ1 comes pre-soldered to short V~DD~ and V~DDIO~. This reduces the number of power supplies to one with out requiring an external jumper. If the core and IO need to be supplied with different voltages, remove the solder from SJ1.

SJ2 is a two way jumper that comes pre-soldered to connect AD0 to ground. This sets the I^2^C address to 0x68. It also leaves the [PTH] for AD0 disconnected and floating. If the solder is moved to connect the center pad with the pad on the left, then the AD0 [PTH] needs to be connected high or low to chose the I^2^C address.

### Reducing size

As stated earlier, one of the design goals for this breakout was to make the board small. Some projects will require mounting holes, so we threw them on the right side of some v-score on this board. Since the board is only ⅔\" wide and there isn\'t enough mass to the left of the mounting holes, there isn\'t much of a bending moment.

If you plan to use a breadboard, or secure the IMU securely to a project with something like epoxy, the mounting holes can be snapped off. As shown in the following image. The pliers I had on hand made super easy work of this. The edge of a table should work fine too.

[![PCB held in pliers ready to be snapped](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/breakingPCB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/breakingPCB.jpg)

*Board was held with pliers and easily broken by pressing the other side*

[![PCB snapped in two parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/splitPCB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/splitPCB.jpg)

*[PCB] snapped in two parts*

## Hardware Connections

The MPU-9250 breakout board runs on 3.3 [VDC], so a 3.3V USB to UART bridge such as the [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/products/9873) or the [SparkFun Beefy 3 - FTDI Basic Breakout](https://www.sparkfun.com/products/13746) can be used to power and bridge communication with a micro controller. In this case an [Arduino Pro Mini 328 - 3.3V/8MHz](https://www.sparkfun.com/products/11114) was chosen so logic level translation isn\'t needed.

[![Fritzing Diagram of MPU-9450 Connected to Arduino ](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/MPU-9250_Hookup_Arduino_Fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/MPU-9250_Hookup_Arduino_Fritzing.jpg)

*Fritzing diagram of setup*

Only 4 connections are needed for I^2^C communication.

[![Snapped PCB next to 0.1\" header](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/PCBPreSolder.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/PCBPreSolder.jpg)

*Minimum parts for a breadboard compatible setup*

For stability in the breadboard, another four pins were soldered on: V~DDIO~, AD0/SDO, [CS], and INT.

[![PCB with breadboard compatible male headers soldered on](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/solderedPCB.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/solderedPCB.jpg)

*PCB with breadboard compatible male headers soldered on*

Here is the final setup used for testing.

[![Setup used for testing](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/inBreadboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/inBreadboard.jpg)

*Setup used for testing*

## Library and Example Code

**Note:** The example sketch and library are **HEAVILY** based on the work of Kris Winer. His original work can be found in his [GitHub repository](https://github.com/kriswiner/MPU-9250).\
\

[kriswiner\'s MPU-9250 GitHub Repo](https://github.com/kriswiner/MPU-9250)

\
For more information on the algorithms Kris used for the **A**ttitude and **H**eading **R**eference **S**ystem ([AHRS]), check out the [open source IMU and AHRS algorithms](http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms/)\
\

[Open Source IMU and AHRS Algorithms](http://www.x-io.co.uk/open-source-imu-and-ahrs-algorithms)

Our version is mostly a conversion to make it follow the Arduino library format. You can use the Arduino IDE\'s library manager by searching for \"**SparkFun MPU-9250**\" as detailed in [this tutorial](https://learn.sparkfun.com/tutorials/installing-an-arduino-library). Or you can manually install the library from the [GitHub repository](https://github.com/sparkfun/MPU-9250_Breakout_Arduino_Library) by downloading the **\*.zip** linked below:

[SparkFun MPU-9250 Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MPU-9250_Breakout_Arduino_Library/archive/master.zip)

**Heads up!** The code provided in this tutorial compiles for Arduino v1.8.8. However, if you are using an older version like v1.6.5, you will need to include the following at the top of the example code:\
\

``` c
#include <Wire.h>
#include <SPI.h>
```

    language:c
    /* MPU9250 Basic Example Code
     by: Kris Winer
     date: April 1, 2014
     license: Beerware - Use this code however you'd like. If you
     find it useful you can buy me a beer some time.
     Modified by Brent Wilkins July 19, 2016

     Demonstrate basic MPU-9250 functionality including parameterizing the register
     addresses, initializing the sensor, getting properly scaled accelerometer,
     gyroscope, and magnetometer data out. Added display functions to allow display
     to on breadboard monitor. Addition of 9 DoF sensor fusion using open source
     Madgwick and Mahony filter algorithms. Sketch runs on the 3.3 V 8 MHz Pro Mini
     and the Teensy 3.1.

     SDA and SCL should have external pull-up resistors (to 3.3V).
     10k resistors are on the EMSENSR-9250 breakout board.

     Hardware setup:
     MPU9250 Breakout --------- Arduino
     VDD ---------------------- 3.3V
     VDDI --------------------- 3.3V
     SDA ----------------------- A4
     SCL ----------------------- A5
     GND ---------------------- GND
     */

    #include "quaternionFilters.h"
    #include "MPU9250.h"

    #ifdef LCD
    #include <Adafruit_GFX.h>
    #include <Adafruit_PCD8544.h>

    // Using NOKIA 5110 monochrome 84 x 48 pixel display
    // pin 9 - Serial clock out (SCLK)
    // pin 8 - Serial data out (DIN)
    // pin 7 - Data/Command select (D/C)
    // pin 5 - LCD chip select (CS)
    // pin 6 - LCD reset (RST)
    Adafruit_PCD8544 display = Adafruit_PCD8544(9, 8, 7, 5, 6);
    #endif // LCD

    #define AHRS false         // Set to false for basic data read
    #define SerialDebug true  // Set to true to get Serial output for debugging

    // Pin definitions
    int intPin = 12;  // These can be changed, 2 and 3 are the Arduinos ext int pins
    int myLed  = 13;  // Set up pin 13 led for toggling

    #define I2Cclock 400000
    #define I2Cport Wire
    #define MPU9250_ADDRESS MPU9250_ADDRESS_AD0   // Use either this line or the next to select which I2C address your device is using
    //#define MPU9250_ADDRESS MPU9250_ADDRESS_AD1

    MPU9250 myIMU(MPU9250_ADDRESS, I2Cport, I2Cclock);

    void setup()
    ;

      // Set up the interrupt pin, its set as active high, push-pull
      pinMode(intPin, INPUT);
      digitalWrite(intPin, LOW);
      pinMode(myLed, OUTPUT);
      digitalWrite(myLed, HIGH);

    #ifdef LCD
      display.begin(); // Ini8ialize the display
      display.setContrast(58); // Set the contrast

      // Start device display with ID of sensor
      display.clearDisplay();
      display.setTextSize(2);
      display.setCursor(0,0); display.print("MPU9250");
      display.setTextSize(1);
      display.setCursor(0, 20); display.print("9-DOF 16-bit");
      display.setCursor(0, 30); display.print("motion sensor");
      display.setCursor(20,40); display.print("60 ug LSB");
      display.display();
      delay(1000);

      // Set up for data display
      display.setTextSize(1); // Set text size to normal, 2 is twice normal etc.
      display.setTextColor(BLACK); // Set pixel color; 1 on the monochrome screen
      display.clearDisplay();   // clears the screen and buffer
    #endif // LCD

      // Read the WHO_AM_I register, this is a good test of communication
      byte c = myIMU.readByte(MPU9250_ADDRESS, WHO_AM_I_MPU9250);
      Serial.print(F("MPU9250 I AM 0x"));
      Serial.print(c, HEX);
      Serial.print(F(" I should be 0x"));
      Serial.println(0x71, HEX);

    #ifdef LCD
      display.setCursor(20,0); display.print("MPU9250");
      display.setCursor(0,10); display.print("I AM");
      display.setCursor(0,20); display.print(c, HEX);
      display.setCursor(0,30); display.print("I Should Be");
      display.setCursor(0,40); display.print(0x71, HEX);
      display.display();
      delay(1000);
    #endif // LCD

      if (c == 0x71) // WHO_AM_I should always be 0x71
      

        // Get magnetometer calibration from AK8963 ROM
        myIMU.initAK8963(myIMU.factoryMagCalibration);
        // Initialize device for active mode read of magnetometer
        Serial.println("AK8963 initialized for active data mode....");

        if (SerialDebug)
        

    #ifdef LCD
        display.clearDisplay();
        display.setCursor(20,0);  display.print("AK8963");
        display.setCursor(0,10);  display.print("ASAX ");
        display.setCursor(50,10); display.print(myIMU.factoryMagCalibration[0], 2);
        display.setCursor(0,20);  display.print("ASAY ");
        display.setCursor(50,20); display.print(myIMU.factoryMagCalibration[1], 2);
        display.setCursor(0,30);  display.print("ASAZ ");
        display.setCursor(50,30); display.print(myIMU.factoryMagCalibration[2], 2);
        display.display();
        delay(1000);
    #endif // LCD

        // Get sensor resolutions, only need to do this once
        myIMU.getAres();
        myIMU.getGres();
        myIMU.getMres();

        // The next call delays for 4 seconds, and then records about 15 seconds of
        // data to calculate bias and scale.
    //    myIMU.magCalMPU9250(myIMU.magBias, myIMU.magScale);
        Serial.println("AK8963 mag biases (mG)");
        Serial.println(myIMU.magBias[0]);
        Serial.println(myIMU.magBias[1]);
        Serial.println(myIMU.magBias[2]);

        Serial.println("AK8963 mag scale (mG)");
        Serial.println(myIMU.magScale[0]);
        Serial.println(myIMU.magScale[1]);
        Serial.println(myIMU.magScale[2]);
    //    delay(2000); // Add delay to see results before serial spew of data

        if(SerialDebug)
        

    #ifdef LCD
        display.clearDisplay();
        display.setCursor(20,0); display.print("AK8963");
        display.setCursor(0,10); display.print("ASAX "); display.setCursor(50,10);
        display.print(myIMU.factoryMagCalibration[0], 2);
        display.setCursor(0,20); display.print("ASAY "); display.setCursor(50,20);
        display.print(myIMU.factoryMagCalibration[1], 2);
        display.setCursor(0,30); display.print("ASAZ "); display.setCursor(50,30);
        display.print(myIMU.factoryMagCalibration[2], 2);
        display.display();
        delay(1000);
    #endif // LCD
      } // if (c == 0x71)
      else
      
    }

    void loop()
     // if (readByte(MPU9250_ADDRESS, INT_STATUS) & 0x01)

      // Must be called before updating quaternions!
      myIMU.updateTime();

      // Sensors x (y)-axis of the accelerometer is aligned with the y (x)-axis of
      // the magnetometer; the magnetometer z-axis (+ down) is opposite to z-axis
      // (+ up) of accelerometer and gyro! We have to make some allowance for this
      // orientationmismatch in feeding the output to the quaternion filter. For the
      // MPU-9250, we have chosen a magnetic rotation that keeps the sensor forward
      // along the x-axis just like in the LSM9DS0 sensor. This rotation can be
      // modified to allow any convenient orientation convention. This is ok by
      // aircraft orientation standards! Pass gyro rate as rad/s
      MahonyQuaternionUpdate(myIMU.ax, myIMU.ay, myIMU.az, myIMU.gx * DEG_TO_RAD,
                             myIMU.gy * DEG_TO_RAD, myIMU.gz * DEG_TO_RAD, myIMU.my,
                             myIMU.mx, myIMU.mz, myIMU.deltat);

      if (!AHRS)
      

    #ifdef LCD
          display.clearDisplay();
          display.setCursor(0, 0); display.print("MPU9250/AK8963");
          display.setCursor(0, 8); display.print(" x   y   z  ");

          display.setCursor(0,  16); display.print((int)(1000 * myIMU.ax));
          display.setCursor(24, 16); display.print((int)(1000 * myIMU.ay));
          display.setCursor(48, 16); display.print((int)(1000 * myIMU.az));
          display.setCursor(72, 16); display.print("mg");

          display.setCursor(0,  24); display.print((int)(myIMU.gx));
          display.setCursor(24, 24); display.print((int)(myIMU.gy));
          display.setCursor(48, 24); display.print((int)(myIMU.gz));
          display.setCursor(66, 24); display.print("o/s");

          display.setCursor(0,  32); display.print((int)(myIMU.mx));
          display.setCursor(24, 32); display.print((int)(myIMU.my));
          display.setCursor(48, 32); display.print((int)(myIMU.mz));
          display.setCursor(72, 32); display.print("mG");

          display.setCursor(0,  40); display.print("Gyro T ");
          display.setCursor(50,  40); display.print(myIMU.temperature, 1);
          display.print(" C");
          display.display();
    #endif // LCD

          myIMU.count = millis();
          digitalWrite(myLed, !digitalRead(myLed));  // toggle led
        } // if (myIMU.delt_t > 500)
      } // if (!AHRS)
      else
      

    // Define output variables from updated quaternion---these are Tait-Bryan
    // angles, commonly used in aircraft orientation. In this coordinate system,
    // the positive z-axis is down toward Earth. Yaw is the angle between Sensor
    // x-axis and Earth magnetic North (or true North if corrected for local
    // declination, looking down on the sensor positive yaw is counterclockwise.
    // Pitch is angle between sensor x-axis and Earth ground plane, toward the
    // Earth is positive, up toward the sky is negative. Roll is angle between
    // sensor y-axis and Earth ground plane, y-axis up is positive roll. These
    // arise from the definition of the homogeneous rotation matrix constructed
    // from quaternions. Tait-Bryan angles as well as Euler angles are
    // non-commutative; that is, the get the correct orientation the rotations
    // must be applied in the correct order which for this configuration is yaw,
    // pitch, and then roll.
    // For more see
    // http://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles
    // which has additional links.
          myIMU.yaw   = atan2(2.0f * (*(getQ()+1) * *(getQ()+2) + *getQ()
                        * *(getQ()+3)), *getQ() * *getQ() + *(getQ()+1)
                        * *(getQ()+1) - *(getQ()+2) * *(getQ()+2) - *(getQ()+3)
                        * *(getQ()+3));
          myIMU.pitch = -asin(2.0f * (*(getQ()+1) * *(getQ()+3) - *getQ()
                        * *(getQ()+2)));
          myIMU.roll  = atan2(2.0f * (*getQ() * *(getQ()+1) + *(getQ()+2)
                        * *(getQ()+3)), *getQ() * *getQ() - *(getQ()+1)
                        * *(getQ()+1) - *(getQ()+2) * *(getQ()+2) + *(getQ()+3)
                        * *(getQ()+3));
          myIMU.pitch *= RAD_TO_DEG;
          myIMU.yaw   *= RAD_TO_DEG;

          // Declination of SparkFun Electronics (40°05'26.6"N 105°11'05.9"W) is
          //    8° 30' E  ± 0° 21' (or 8.5°) on 2016-07-19
          // - http://www.ngdc.noaa.gov/geomag-web/#declination
          myIMU.yaw  -= 8.5;
          myIMU.roll *= RAD_TO_DEG;

          if(SerialDebug)
          

    #ifdef LCD
          display.clearDisplay();

          display.setCursor(0, 0); display.print(" x   y   z  ");

          display.setCursor(0,  8); display.print((int)(1000 * myIMU.ax));
          display.setCursor(24, 8); display.print((int)(1000 * myIMU.ay));
          display.setCursor(48, 8); display.print((int)(1000 * myIMU.az));
          display.setCursor(72, 8); display.print("mg");

          display.setCursor(0,  16); display.print((int)(myIMU.gx));
          display.setCursor(24, 16); display.print((int)(myIMU.gy));
          display.setCursor(48, 16); display.print((int)(myIMU.gz));
          display.setCursor(66, 16); display.print("o/s");

          display.setCursor(0,  24); display.print((int)(myIMU.mx));
          display.setCursor(24, 24); display.print((int)(myIMU.my));
          display.setCursor(48, 24); display.print((int)(myIMU.mz));
          display.setCursor(72, 24); display.print("mG");

          display.setCursor(0,  32); display.print((int)(myIMU.yaw));
          display.setCursor(24, 32); display.print((int)(myIMU.pitch));
          display.setCursor(48, 32); display.print((int)(myIMU.roll));
          display.setCursor(66, 32); display.print("ypr");

        // With these settings the filter is updating at a ~145 Hz rate using the
        // Madgwick scheme and >200 Hz using the Mahony scheme even though the
        // display refreshes at only 2 Hz. The filter update rate is determined
        // mostly by the mathematical steps in the respective algorithms, the
        // processor speed (8 MHz for the 3.3V Pro Mini), and the magnetometer ODR:
        // an ODR of 10 Hz for the magnetometer produce the above rates, maximum
        // magnetometer ODR of 100 Hz produces filter update rates of 36 - 145 and
        // ~38 Hz for the Madgwick and Mahony schemes, respectively. This is
        // presumably because the magnetometer read takes longer than the gyro or
        // accelerometer reads. This filter update rate should be fast enough to
        // maintain accurate platform orientation for stabilization control of a
        // fast-moving robot or quadcopter. Compare to the update rate of 200 Hz
        // produced by the on-board Digital Motion Processor of Invensense's MPU6050
        // 6 DoF and MPU9150 9DoF sensors. The 3.3 V 8 MHz Pro Mini is doing pretty
        // well!
          display.setCursor(0, 40); display.print("rt: ");
          display.print((float) myIMU.sumCount / myIMU.sum, 2);
          display.print(" Hz");
          display.display();
    #endif // LCD

          myIMU.count = millis();
          myIMU.sumCount = 0;
          myIMU.sum = 0;
        } // if (myIMU.delt_t > 500)
      } // if (AHRS)
    }

*Full demo sketch*

Some configuration can be found at the beginning of the sketch. Here is where you can turn on or off [AHRS] calculations, and serial debugging:

    language:c
    #define AHRS true         // Set to false for basic data read
    #define SerialDebug true  // Set to true to get Serial output for debugging

*Some of the settings used by library exposed in the sketch*

### Magnetic Declination

The [AHRS] needs to know where you are located to convert magnetic north to true north. I used the combination of two services to find the current declination of our offices; Google, and [NOAA]. This may or may not be ideal in your country.

The first thing I needed were the latitude and longitude of the office. Searching for SparkFun in [Google Maps](https://www.google.com/maps/place/Spark+Fun+Electronics/) shows a red pin on our building. Clicking near the front door, but not on the existing pin dropped a new pin which also made a card appear bottom center. The bottom of this card contains a link to a search of the latitude and longitude marked by the new pin.

[![Screenshot of Google Maps showing the latitude and longitude of SparkFun Electronics](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/droppedPin.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/droppedPin.png)

*Google Maps showing the latitude and longitude of SparkFun Electronics*

Clicking on the link in the card brings up a page showing the latitude and longitude in both the **d**ecimal **d**egrees ([DD]) and **d**egrees **m**inutes **s**econds ([DMS]) forms. I find sign errors easier to avoid by using [DMS] form Google provides with the since I\'m not intimately familiar with the WGS 84 **c**oordinate **r**eference **s**ystem (CRS). The included cardinal directions are handy and required by the next tool.

[![Search for SparkFun Electronics\' coordinates](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/Geolocation.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/Geolocation.png)

*Search for SparkFun Electronics\' coordinates*

The second tool is the default [magnetic field calculator](http://www.ngdc.noaa.gov/geomag-web/#declination) on [NOAA]\'s website. Enter the coordinates found in the previous step into the latitude and longitude inputs. The *Calculate* button will trigger a dialog box with the results to appear. If the results appear on the Google map where you are expecting them, then you chose the correct directions with the radio inputs!

[![Magnetic declination of SparkFun Electronics Colorado office](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/5/0/Geomagnetism.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/5/0/Geomagnetism.png)

*Magnetic declination of SparkFun Electronics\' Colorado office*

Note that the declination here is currently 8˚ 30\' E. Also note that the image on the map shows magnetic north to be east of true north. The provided [DM] format needs to be converted to [DD] format for the code. There are 60 minutes per degree, 30 of them is ^30^⁄~60~ of a degree, or 0.5˚. The declination in [DD] format is thus 8.5˚ E. Update the code in the example sketch around line 391 with the declination for your desired location.

    language:c
    myIMU.yaw   -= 8.5;

### What You Should See

The library left a lot of the math in the example sketch in part to make things like this easier to access. Here is an example of what the output of the demo sketch should look like:

    language:bash
    MPU9250 I AM 71 I should be 71
    MPU9250 is online...
    x-axis self test: acceleration trim within : 2.4% of factory value
    y-axis self test: acceleration trim within : 0.5% of factory value
    z-axis self test: acceleration trim within : -0.0% of factory value
    x-axis self test: gyration trim within : -0.3% of factory value
    y-axis self test: gyration trim within : -1.0% of factory value
    z-axis self test: gyration trim within : 0.5% of factory value
    MPU9250 initialized for active data mode....
    AK8963 I AM 48 I should be 48
    AK8963 initialized for active data mode....
    X-Axis sensitivity adjustment value 1.21
    Y-Axis sensitivity adjustment value 1.22
    Z-Axis sensitivity adjustment value 1.17
    ax = -70.19 ay = -70.56 az = 931.03 mg
    gx = 0.02 gy = 0.00 gz = 0.02 deg/s
    mx = -189 my = 355 mz = 127 mG
    q0 = 0.97 qx = -0.04 qy = 0.03 qz = 0.22
    Yaw, Pitch, Roll: 16.45, 4.22, -4.14
    rate = 140.15 Hz