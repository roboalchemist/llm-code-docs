# Source: https://learn.sparkfun.com/tutorials/accelerometer-basics

## What is an Accelerometer?

Accelerometers are devices that measure [acceleration](http://en.wikipedia.org/wiki/Acceleration), which is the rate of change of the [velocity](http://en.wikipedia.org/wiki/Velocity) of an object. They measure in meters per second squared (m/s^2^) or in G-forces (g). A single G-force for us here on planet Earth is equivalent to 9.8 m/s^2^, but this does vary slightly with elevation (and will be a different value on different planets due to variations in gravitational pull). Accelerometers are useful for sensing vibrations in systems or for orientation applications.

[![Accelerometer breakout board](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/accel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/3/accel.jpg)

*[ADXL345 Breakout Board](https://www.sparkfun.com/products/9836)*

### Suggested Reading

If you are unfamiliar with any of the topics below, you may want to read up on those before moving ahead with accelerometers.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

------------------------------------------------------------------------

## How an Accelerometer Works

Accelerometers are electromechanical devices that sense either static or dynamic forces of acceleration. Static forces include gravity, while dynamic forces can include vibrations and movement.

[![Accelerometer axes of measurement](https://cdn.sparkfun.com/r/600-600/assets/6/7/e/5/a/516c6b6ece395f0f49000000.jpeg)](https://cdn.sparkfun.com/assets/6/7/e/5/a/516c6b6ece395f0f49000000.jpeg)

*Axes of measurement for a triple axis accelerometer*

Accelerometers can measure acceleration on one, two, or three axes. 3-axis units are becoming more common as the cost of development for them decreases.

Generally, accelerometers contain capacitive plates internally. Some of these are fixed, while others are attached to minuscule springs that move internally as acceleration forces act upon the sensor. As these plates move in relation to each other, the [capacitance](https://learn.sparkfun.com/tutorials/capacitors) between them changes. From these changes in capacitance, the acceleration can be determined.

Other accelerometers can be centered around piezoelectric materials. These tiny crystal structures output electrical charge when placed under mechanical stress ( e.g. acceleration).

[![Representation of How an Accelerometer Works](https://cdn.sparkfun.com/assets/a/9/1/1/7/516daf84ce395f411e000001.gif)](https://cdn.sparkfun.com/assets/a/9/1/1/7/516daf84ce395f411e000001.gif)

*An example of the inside of a piezoelectric accelerometer*

------------------------------------------------------------------------

## How to Connect to an Accelerometer

For most accelerometers, the basic connections required for operation are power and the communication lines. As always, read the datasheet to ensure proper connections are made.

### Communication Interface

Accelerometers will communicate over an analog, digital, or pulse-width modulated connection interface.

- **Analog** - Accelerometers with an analog interface show accelerations through varying voltage levels. These values generally fluctuate between ground and the supply voltage level. An [ADC](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion) on a microcontroller can then be used to read this value. These are generally less expensive than digital accelerometers.

- **Digital** - Accelerometers with a digital interface can either communicate over [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi) or [I^2^C](https://learn.sparkfun.com/tutorials/i2c) communication protocols. These tend to have more functionality and be less susceptible to noise than analog accelerometers.

- **Pulse-Width Modulation (PWM)** - Accelerometers that output data over [pulse-width modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) output square waves with a known period, but a duty cycle that varies with changes in acceleration.

### Power

Accelerometers are generally low-power devices. The required current typically falls in the micro (µ) or milli-amp range, with a supply voltage of 5V or less. The current consumption can vary depending on the settings (e.g., power saving mode versus standard operating mode). These different modes can make accelerometers well suited for battery powered applications.

Make sure that proper [logic levels](https://sparkle.sparkfun.com/sparkle/learn_tutorials/62#tab-attributes) are matched, especially with the digital interfaces.

------------------------------------------------------------------------

## How to Select an Accelerometer

When choosing which accelerometer to use, several features are important to consider including power requirements and communication interfaces as discussed previously. Additional features for consideration are below.

### Range

Most accelerometers will have a selectable range of forces they can measure. These ranges can vary from ±1g up to ±250g. Typically, the smaller the range, the more sensitive the readings will be from the accelerometer. For example, to measure small vibrations on a tabletop, using a small-range accelerometer will provide more detailed data than using a 250g range (which is more suited for rockets).

[![ADXL362](https://cdn.sparkfun.com/assets/8/f/f/e/b/51703cbfce395f3e3b000000.jpg)](https://cdn.sparkfun.com/assets/8/f/f/e/b/51703cbfce395f3e3b000000.jpg)

*The [ADXL362 Triple Axis Accelerometer](https://www.sparkfun.com/products/11446) can measure ±2g, ±4g, and ±8g.*

### Additional Features

Some accelerometers include features such as tap detection (useful for low-power applications), free-fall detection (used for [Active Hard Drive Protection](http://en.wikipedia.org/wiki/Active_hard-drive_protection)), temperature compensation (to increase accuracy in [dead reckoning](http://en.wikipedia.org/wiki/Dead_reckoning) situations ) and 0-g range sensing, which are other features to take into consideration when purchasing an accelerometer. The need for these types of features on the accelerometer will be determined by the application in which the accelerometer is incorporated.

There are also IMUs ([Inertial Measurement Units](http://en.wikipedia.org/wiki/Inertial_measurement_unit)) available, which can include accelerometers, gyroscopes and even, occasionally, magnetometers into a single IC package or board. Some examples of this include the [MPU6050](https://www.sparkfun.com/products/11028) and [MPU9150](https://www.sparkfun.com/products/11486). These are commonly used in [motion tracking applications](https://dev.qu.tu-berlin.de/projects/sf-razor-9dof-ahrs/wiki/Tutorial) and [UAV guidance systems](https://www.sparkfun.com/news/947), where location and orientation of an object is important.

------------------------------------------------------------------------

## Purchasing an Accelerometer

Now that you\'ve learned the abc\'s of the x\'s, y\'s, and z\'s, take a look at our recommended [accelerometers from the SparkFun catalog](https://www.sparkfun.com/categories/80)

### Our Recommendations:

[![SparkFun Triple Axis Accelerometer Breakout - ADXL335](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/6/8/09269-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-adxl335.html)

### [SparkFun Triple Axis Accelerometer Breakout - ADXL335](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-adxl335.html) 

[ SEN-09269 ]

Breakout board for the 3 axis ADXL335 from Analog Devices. This is the latest in a long, proven line of analog sensors - the ...

[ [\$22.27] ]

[![SparkFun Micro 6DoF IMU Breakout - LSM6DSV16X (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/1/4/4/21336_Micro6DOF_3.jpg)](https://www.sparkfun.com/sparkfun-micro-6dof-imu-breakout-lsm6dsv16x-qwiic.html)

### [SparkFun Micro 6DoF IMU Breakout - LSM6DSV16X (Qwiic)](https://www.sparkfun.com/sparkfun-micro-6dof-imu-breakout-lsm6dsv16x-qwiic.html) 

[ SEN-21336 ]

The SparkFun LSM6DSV16X Micro 6DoF IMU is a Qwiic-enabled, AI-featured, breakout based on the LSM6DSV16X from STMicroelectron...

[ [\$25.50] ]

[![SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/9/7/1/21208_SEN-_01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - BMA400 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-bma400-qwiic.html) 

[ SEN-21208 ]

he SparkFun Qwiic BMA400 Triple Axis Accelerometer Breakout offers a 3-axis acceleration sensor perfect for ultra-low-power a...

[ [\$10.50] ]

[![SparkFun Triple Axis Accelerometer Breakout - LIS3DH](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/6/8/0/13963-02.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-lis3dh.html)

### [SparkFun Triple Axis Accelerometer Breakout - LIS3DH](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-lis3dh.html) 

[ SEN-13963 ]

The LIS3DH Breakout is a smart, low-power, three-axis, capacitive micro-machined accelerometer with 12 bits of resolution tha...

[ [\$7.75] ]

[![SparkFun Triple Axis Digital Accelerometer Breakout - ADXL313 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/2/4/17241-SparkFun_3-Axis_Digital_Accelerometer_Breakout_-_ADXL313__Qwiic_02.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-digital-accelerometer-breakout-adxl313-qwiic.html)

### [SparkFun Triple Axis Digital Accelerometer Breakout - ADXL313 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-digital-accelerometer-breakout-adxl313-qwiic.html) 

[ SEN-17241 ]

The SparkFun ADXL313 Breakout is a low power, high resolution (up to 13-bits) 3-axis accelerometer for measurement up to ±4g...

[ [\$22.10] ]

[![SparkFun Triple Axis Accelerometer Breakout - KX132 (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/0/6/0/17871-SparkFun_Triple_Axis_Accelerometer_Breakout_-_KX132__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx132-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - KX132 (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-kx132-qwiic.html) 

[ SEN-17871 ]

This SparkFun Triple-Axis Accelerometer Breakout is a simple Qwiic breakout for the KX132 digital accelerometer from Kionix.

[ [\$15.50] ]

*For a more in-depth look at choosing an accelerometer, take a look at our [**buying guide**](https://www.sparkfun.com/pages/accel_gyro_guide) to find the right fit for your project.*

[View Accelerometer Buying Guide](https://www.sparkfun.com/pages/accel_gyro_guide)

------------------------------------------------------------------------