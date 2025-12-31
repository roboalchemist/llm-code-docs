# Source: https://learn.sparkfun.com/tutorials/imu-data-to-motion-tutorial-for-translating-sensor-data-into-real-world-movement

## Introduction

[![Setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/7/3/MotionToMovementSetup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/7/3/MotionToMovementSetup.jpg)

~*A\ Qwiic\ cable,\ some\ jumper\ wires,\ a\ couple\ of\ servos,\ and\ you\'re\ good\ to\ go.\ (3D\ printed\ rig\ optional)*~

Over the Years, we've carried quite a number of IMUs. And why not? Inertial Motion Units are used in an incredibly broad array of products, from robots to rockets, smart watches to structural components, electronic stabilization systems to exoskeletons. IMUs combine several sensors to provide data about movement and orientation in three-dimensional space, utilizing an accelerometer and gyroscope in the case of a 6DoF sensor (six degrees of freedom), or an accelerometer, gyroscope, and magnetometer in the case of a 9DoF (nine degrees of freedom).

[Confused by IMUs? Learn more here](https://www.sparkfun.com/pages/accel_gyro_guide)

## The Challenge: Translating Measured Movement to Motion

Monitoring and measuring this incoming data is simple, especially with our Qwiic sensors and example sketches. But let's face it, we want to do more with our incoming motion data than just read the results on a screen. So I decided to revisit an old project build that I quickly threw together for a new product demo. Since I'll only be using the measurements from one of the three possible sensors on a 9D0F IMU, for this project I'm going to be using one of our newer, smaller magnetometer boards to control a pair of servos, and then toss out some ideas to upgrade to a much bigger, cooler project.

[![SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/5/3/19921_03.jpg)](https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html)

### [SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://www.sparkfun.com/sparkfun-micro-magnetometer-mmc5983ma-qwiic.html) 

[ SEN-19921 ]

The SparkFun Qwiic Micro MMC5983MA Magnetometer is a micro-sized 0.75in. by 0.30in. sensor that utilizes a highly sensitive t...

[ [\$18.50] ]

[![SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/6/1/5/19895_Diag.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html)

### [SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html) 

[ SEN-19895 ]

The SparkFun 9DoF IMU Breakout combines a high-performance 6DoF IMU with the highly sensitive triple-axis magnetometer in a Q...

[ [\$45.74] ]

[View the Full Hookup Guide](https://learn.sparkfun.com/tutorials/qwiic-micro-magnetometer---mmc5983ma-hookup-guide)

## Components Required

You can opt for a number of different servos, or a number of different microcontrollers, but here are some suggestions for a fast and simple demo.

**The magnetometer -** [SparkFun Micro Magnetometer - MMC5983MA (Qwiic)](https://www.sparkfun.com/products/19921)

**A microcontroller -** [SparkFun Redboard Qwiic](https://www.sparkfun.com/products/15123)

**2 Servos (anything from sub-micro to giant) -** [Generic sub-micro servo](https://www.sparkfun.com/products/9065)

**Power Supply for Servos (optional).** [Power Supplies](https://www.sparkfun.com/categories/28)

**SparkFun Qwiic Connectors -** [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/products/15081)

## The Project

I've always been a fan of flying, and eventually of flight simulators. So of course, I've always wanted to build a chair frame that would move in concert with the movements of my onscreen plane, whether it's a Cessna 172 or a Airbus H225 helicopter. So in order to do this, I want to read the movement or position of our yolk or stick. Note: I know that when it actually comes to creating a chair frame that moves based on the movement of the flight stick, the movements will need to be measured from local axes, and a magnetometer, like I'm using in this example, bases its measurements on global axes. This is just a broad look at how to translate sensor data into motion, and can then be tailored to fit the needs of each project. Planes use cables to control the ailerons and elevator, and if you're planning on building an experimental aircraft, I'm going to suggest not using this method., but if something goes wrong on a Flight Sim build, a catastrophic control failure would, at worst, toss toss onto the floor.

[![Lego Pilot in the cockpit of a Cessna Citation](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/7/3/MotionToMovementCockpit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/7/3/MotionToMovementCockpit.jpg)

For testing the concept, I'm going to translate the sensor data to a pair of small servos. I 3D printed a small rig and a tiny chair for my little lego fly-boy. The initial concept worked just fine, I only needed to tweak the limits of the servo travel.

## Hardware Setup

**Connecting the MMC5983MA Sensor:** Connect the MMC5983MA sensor to the Arduino using the SparkFun Qwiic Connectors. Plug the Qwiic connector on the MMC5983MA into one of the Qwiic ports on the Qwiic Shield or directly on a Qwiic-compatible Arduino board.

**Connecting the Servos:** Servo 1 Signal to Pin 8 on Arduino Servo 2 Signal to Pin 9 on Arduino Servo Power (VCC) to an external 5V power supply (opt) Servo Ground (GND) to Arduino GND

[![Layout of Components](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/5/7/3/MotionToMovementLayout.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/5/7/3/MotionToMovementLayout.jpg)

*^The\ basic\ layout\ is\ fast\ and\ simple,\ getting\ you\ to\ the\ testing\ phase\ quickly.^*

## Arduino Sketch

    /*
      Movement to Motion: Using the SparkFun Micro Magnetometer (MMC5983MA) to control servo motors
      By: Rob Reynolds
      SparkFun Electronics
      Date: September 19th, 2024
      Based on original code by Nathan Seidle and Ricardo Ramos
      License: SparkFun code, firmware, and software is released under the MIT License(http://opensource.org/licenses/MIT).

      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/19921

      This example demonstrates how to take raw X/Y/Z readings from the sensor over Qwiic
      and translate them to movement through servo motors on the X and Y axes

      Hardware Connections:
      Plug a Qwiic cable into the sensor and a RedBoard
      If you don't have a platform with a Qwiic connection use the SparkFun Qwiic Breadboard Jumper
      (https://www.sparkfun.com/products/17912) Open the serial monitor at 115200 baud to see the output
    */

    #include <Wire.h>

    #include <SparkFun_MMC5983MA_Arduino_Library.h> //Click here to get the library: http://librarymanager/All#SparkFun_MMC5983MA

    SFE_MMC5983MA myMag;

    // Here's where we set up the servos

    #include <Servo.h>
    Servo servoPitchX; //Create object on X access
    Servo servoRollY; //Create object on Y access

    // initiate variables for servo positions
    int rollYVal;
    int pitchXVal;

    void setup()
    

        myMag.softReset();

        Serial.println("MMC5983MA connected");

        servoPitchX.attach(8);
        servoRollY.attach(9);
    }

    void loop()
    

\

## Explanations

**1. Libraries:** Wire.h: For I2C communication. SparkFunLSM6DSV16X.h: To interface with the LSM6DSV16X sensor via Qwiic. Servo.h: To control the servos.

**2. Setup Function:** Initializes serial communication for debugging. Initializes the IMU sensor and checks if it\'s detected. Attaches servos to their respective pins and sets initial positions.

**3. Loop Function:** Reads magnetometer data (x, y, z). Maps x and y positional values to servo angles. Constrains angles to valid ranges (for this, 15-165 and 35-135 degrees). Updates servo positions based on mapped angles. Includes a small delay for stability.

**Testing and Calibration:**

**Upload the Sketch:** Connect your Arduino to your computer and upload the sketch using the Arduino IDE.

**Power the Servos**: Ensure the servos are powered correctly with an external power supply. (Small servos with light lode might be able to get away with using power from teh board.)

**Observe Movement:** Tilt or move the IMU sensor and watch how the servos react. The servos should adjust their positions based on the x and y acceleration data from the sensor.

## Troubleshooting

**Troubleshooting:**

**IMU Not Detected:** Ensure the Qwiic connections are secure and that the sensor is properly connected to the I2C bus. Check if the Qwiic shield or board is functioning correctly.

**Servo Movement Issues:** Verify that the mapping and constraints are correct. Make sure the servo power supply is adequate. By following this tutorial, you should be able to easily interface the SparkFun Micro 6DoF IMU Breakout - LSM6DSV16X with your Arduino using Qwiic connectors and control servos based on the sensor's motion data.