# Source: https://learn.sparkfun.com/tutorials/gyroscope

## What is a Gyroscope

Gyroscopes, or gyros, are devices that measure or maintain rotational motion. [MEMS](http://en.wikipedia.org/wiki/Microelectromechanical_systems) (microelectromechanical system) gyros are small, inexpensive sensors that measure angular velocity. The units of angular velocity are measured in degrees per second (°/s) or revolutions per second (RPS). Angular velocity is simply a measurement of speed of rotation.

[![breakout board](//cdn.sparkfun.com/assets/f/b/b/4/a/5112d378ce395f8f27000001.jpg)](//cdn.sparkfun.com/assets/0/1/5/c/f/5112d377ce395ffd27000002.jpg)

*The [LPY503](https://www.sparkfun.com/products/11341) gyro on a breakout board.*

Gyros, similar to the one above, can be used to determine orientation and are found in most autonomous navigation systems. For example, if you want to [balance a robot](http://blog.tkjelectronics.dk/2012/03/the-balancing-robot/), a gyroscope can be used to measure rotation from the balanced position and send corrections to a motor. Check out a few of the ones from the [SparkFun catalog](https://www.sparkfun.com/categories/160).

[![SparkFun 9DoF IMU Breakout - ICM-20948 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/6/0/15335-SparkFun_9DoF_IMU_Breakout_-_ICM-20948__Qwiic_-01b.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-icm-20948-qwiic.html)

### [SparkFun 9DoF IMU Breakout - ICM-20948 (Qwiic)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-icm-20948-qwiic.html) 

[ SEN-15335 ]

The SparkFun 9DoF IMU Breakout incorporates all the amazing features of the ICM-20948 into a Qwiic-enabled breakout board.

[ [\$21.95] ]

[![SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/6/1/5/19895_Diag.jpg)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html)

### [SparkFun 9DoF IMU Breakout - ISM330DHCX, MMC5983MA (Qwiic)](https://www.sparkfun.com/sparkfun-9dof-imu-breakout-ism330dhcx-mmc5983ma-qwiic.html) 

[ SEN-19895 ]

The SparkFun 9DoF IMU Breakout combines a high-performance 6DoF IMU with the highly sensitive triple-axis magnetometer in a Q...

[ [\$45.74] ]

[![SparkFun 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/9/4/6/6/6DoFIMU_03a.jpg)](https://www.sparkfun.com/sparkfun-6dof-imu-breakout-ism330dhcx-qwiic.html)

### [SparkFun 6DoF IMU Breakout - ISM330DHCX (Qwiic)](https://www.sparkfun.com/sparkfun-6dof-imu-breakout-ism330dhcx-qwiic.html) 

[ SEN-19764 ]

The SparkFun Qwiic ISM330DHCX 6DoF IMU is a standard-sized, 1\"x1\" breakout featuring a high-performance 3D digital accelerome...

[ [\$25.50] ]

[![SparkFun Triple Axis Accelerometer and Gyro Breakout - MPU-6050](https://cdn.sparkfun.com/r/140-140/assets/parts/6/3/5/5/11028-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-and-gyro-breakout-mpu-6050.html)

### [SparkFun Triple Axis Accelerometer and Gyro Breakout - MPU-6050](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-and-gyro-breakout-mpu-6050.html) 

[ SEN-11028 ]

The MPU-6050 is a serious little piece of motion processing tech! By combining a MEMS 3-axis gyroscope and a 3-axis accelerom...

**Retired**

### Concepts in this tutorial

Before diving into this tutorial, you may want to read up on some of these concepts if you are unfamiliar with them.

- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [SPI Communication](http://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [I2C Communication](https://learn.sparkfun.com/tutorials/i2c)
- [Analog to Digital Conversion](http://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

## How a Gyro Works

When things rotate around an axis they have what's called *angular velocity*. A spinning wheel can be measured in revolutions per second (RPS) or degrees per second (°/s).

[![bike wheel](//cdn.sparkfun.com/assets/d/6/5/6/a/5112ed4ece395f2f2a000003.gif)](//cdn.sparkfun.com/assets/d/6/5/6/a/5112ed4ece395f2f2a000003.gif)

Note that the z axis of the gyro below aligns with the axis of rotation on the wheel.

[![gyro axes](//cdn.sparkfun.com/assets/f/5/a/8/6/5112d376ce395fc826000001.jpg)](//cdn.sparkfun.com/assets/9/9/3/f/b/5112d375ce395ff927000002.jpg)

If you attach the sensor to the wheel shown above, you can measure the angular velocity of the z axis of the gyro. The other two axes would not measure any rotation.

Imagine if the wheel spins once per second. It would have an angular velocity of 360 degrees per second. The spinning direction of the wheel is also important. Is it clockwise around the axis, or is it counter-clockwise?

A triple axis MEMS gyroscope, similar to the one pictured above ([ITG-3200](https://www.sparkfun.com/products/9793)), can measure rotation around three axes: x, y, and z. Some gyros come in single and dual axis varieties, but the triple axis gyro in a single chip is becoming smaller, less expensive, and more popular.

Gyros are often used on objects that are not spinning very fast at all. Aircrafts (hopefully) do not spin. Instead they rotate a few degrees on each axis. By detecting these small changes gyros help stabilize the flight of the aircraft. Also, note that the acceleration or linear velocity of the aircraft does not affect the measurement of the gyro. Gyros only measure angular velocity.

How does the [MEMS](http://en.wikipedia.org/wiki/Microelectromechanical_systems) gyro detect angular velocity?

[![mems explanation](//cdn.sparkfun.com/assets/5/9/3/9/1/5113d811ce395f5c7d000000.jpg)](//cdn.sparkfun.com/assets/5/9/3/9/1/5113d811ce395f5c7d000000.jpg)

Internal operational view of a MEMS gyro sensor

The gyroscope sensor within the MEMS is tiny (between 1 to 100 micrometers, the size of a human hair). When the gyro is rotated, a small resonating mass is shifted as the angular velocity changes. This movement is converted into very low-current electrical signals that can be amplified and read by a host microcontroller.

## How to Connect to a Gyro

The primary hardware connections to use a gyro are *power* and a *communication interface*. As always, refer to the sensor datasheet for all of the information on specifications and example connections.

### Communication Interface

Gyros can have either a *digital* or *analog* communication interface.

- Gyros with a *digital* interface usually use either the [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) or [I2C](https://learn.sparkfun.com/tutorials/i2c) communication protocols. Using these interfaces allow for an easy connection to a host microcontroller. One limitation of a digital interface is max sample rate. I2C has a max sample rate of 400Hz. SPI, on the other hand, can have a much higher sample rate.

- Gyros with an *analog* interface represent rotational velocity by a varying voltage, usually between ground and the supply voltage. An [ADC](http://learn.sparkfun.com/tutorials/analog-to-digital-conversion) on a microcontroller can be used to read the signal. Analog gyros can be less expensive and sometimes more accurate, depending on how you are reading the analog signal.

### Power

MEMS gyros are generally low power devices. Operating currents are in the mA and sometimes &microA range. The supply voltage for gyros is usually 5V or less. Digital gyros can have selectable logic voltages or operate at the supply voltage. For any digital interface, [remember to connect 5V to 5V lines and 3.3V to 3.3V lines](https://learn.sparkfun.com/tutorials/logic-levels). Also, gyros with digital interfaces can have low power and sleep modes that allow them to be used in battery powered applications. Sometimes this is an advantage over an analog gyro.

## How to Select a Gyro

There are many specifications to consider when figuring out what type of gyro to use. Here are a few of the more important useful ones:

### Range

The measurement range, or full-scale range, is the maximum angular velocity that the gyro can read. Think about what you are measuring. Do you need to measure the spin of a record player, which is very slow or a spinning wheel, which could be very fast?

### Sensitivity

The sensitivity is measured in mV per degree per second (mV/°/s). Don't let the weird dimension of this value scare you. It determines how much the voltage changes for a given angular velocity. For example, if a gyro is specified with a sensitivity of 30mV/°/s and you see a 300mV change in the output, you rotated the gyro at 10 °/s.

**A good rule to remember: as the sensitivity increases, the range decreases.** For example, look at the [LPY503 gyro datasheet](http://www.sparkfun.com/datasheets/Sensors/IMU/lpy503al.pdf) or any gyro with a selectable range:

[![alt text](//cdn.sparkfun.com/assets/0/1/f/0/f/5112dad7ce395fe726000000.jpg)](//cdn.sparkfun.com/assets/7/f/0/9/7/5112dacbce395f1c26000000.jpg)

Notice that with a greater range, the sensitivity suffers and you get less resolution.

### Bias

As with any sensor, the values you measure will contain some amount of error or bias. You can see gyro bias by measuring the output when the gyro is still. Though you'd think you would see 0° when the gyro is still, you will always see a slight non-zero error in the output. These errors are sometimes called bias drift or bias instability. The temperature of the sensor greatly affects the bias. To help minimize the source of this error, most gyros have a built in temperature sensor. Thus, you are able to read the temperature of the sensor and correct or any temperature dependent changes. In order to correct for these errors, the gyro must be calibrated. This is usually done by keeping the gyro still and zeroing all of the readings in your code.