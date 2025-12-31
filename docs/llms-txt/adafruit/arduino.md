# Source: https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/arduino.md

# Adafruit Triple Axis Gyro Breakout

## Arduino

The Adafruit L3GD20 Library for the Arduino implements a convenient device class to handle the&nbsp;the low-level device communication with the Gyro module. &nbsp;The programming interface is described below:

# Install Arduino Libraries

Before you can use the L3GD20, you'l need to install the required libraries using the Arduino Library Manager, which you can open via the menu entry shown below:

![](https://cdn-learn.adafruit.com/assets/assets/000/062/537/medium800/sensors_arduno_library_manager.png?1537904340)

You will need to install the&nbsp; **Adafruit Unified Sensor** &nbsp;library ...

![](https://cdn-learn.adafruit.com/assets/assets/000/062/540/medium800/sensors_Screen_Shot_2018-09-25_at_21.42.09.png?1537904546)

... as well as **Adafruit L3GD20 U** :

![](https://cdn-learn.adafruit.com/assets/assets/000/062/538/medium800/sensors_Screen_Shot_2018-09-25_at_21.40.21.png?1537904485)

# **Construction:**
To use the L3GD20 in your sketch, you must first call a constructor to create a device object. &nbsp;There are two forms of the constructor:  

- **Adafruit\_L3GD20(void);**  
- **Adafruit\_L3GD20(int8\_t cs, int8\_t mosi, int8\_t miso, int8\_t clk);&nbsp; &nbsp;&nbsp;**  

The first version takes no parameters and is used for I2C communication. &nbsp;The second version is for SPI communication and requires that you specify the pins to be used.  
  
**I2C Example:** (use with [I2C wiring](http://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/assembly-and-wiring)) ```
// No need to specify pins for I2C
Adafruit_L3GD20 gyro();
```

 **SPI Example:** &nbsp;(use with [SPI wiring](http://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/assembly-and-wiring "Link: http://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/assembly-and-wiring")) ```
// Define the pins for SPI
#define GYRO_CS 4 // labeled CS
#define GYRO_DO 5 // labeled SA0
#define GYRO_DI 6  // labeled SDA
#define GYRO_CLK 7 // labeled SCL
  
Adafruit_L3GD20 gyro(GYRO_CS, GYRO_DO, GYRO_DI, GYRO_CLK);
```

# Initialization:

Before using the device object you constructed, you must initialize it with the sensitivity range you want to use:

- **bool begin(gyroRange\_t rng);**

where " **rng**" can be one of:

- **L3DS20\_RANGE\_250DPS&nbsp;** - for 250 degrees-per-second range (default)
- **L3DS20\_RANGE\_500DPS&nbsp;** - for 500 degrees-per-second&nbsp;range
- **L3DS20\_RANGE\_2000DPS**** &nbsp;**- for 2000 degrees-per-second&nbsp;range

**Example:**

```
void setup() 
{
  Serial.begin(9600);
  
  // Try to initialise and warn if we couldn't detect the chip
  if (!gyro.begin(gyro.L3DS20_RANGE_250DPS))
  {
    Serial.println("Oops ... unable to initialize the L3GD20. Check your wiring!");
    while (1);
  }
}
```

# Sensing Rotation:
To sense rotation, you must first call the "read()" function to take a reading:  

- **void read(void);**

This function takes no parameters. &nbsp;After calling "read()". &nbsp;The raw&nbsp;x, y and z readings can be retrieved from the device object's "data" member.  
  

- **data.x** - x-axis rotation rate in degrees-per-second  
- **data.y** &nbsp;- y-axis rotation rate in degrees-per-second  
- **data.z** &nbsp;- z-axis rotation rate in degrees-per-second  

  
**Example:**  ```
void loop() 
{
  gyro.read();
  Serial.print("X: "); Serial.print((int)gyro.data.x);   Serial.print(" ");
  Serial.print("Y: "); Serial.print((int)gyro.data.y);   Serial.print(" ");
  Serial.print("Z: "); Serial.println((int)gyro.data.z); Serial.print(" ");
  delay(100);
}
```

# Alternate Units:
The values reported by the read() function are in degrees-per-second (dps)&nbsp; For some calculations, it may be more convenient to work in radians. &nbsp;To convert dps to radians-per-second (rad/s), simply multiply by&nbsp;0.017453293 as in the following code: ```
#define SENSORS_DPS_TO_RADS               (0.017453293F)          /**&lt; Degrees/s to rad/s multiplier */

void loop() 
{
  gyro.read();
  Serial.print("X: "); Serial.print((int)gyro.data.x * SENSORS_DPS_TO_RADS);   Serial.print(" ");
  Serial.print("Y: "); Serial.print((int)gyro.data.y * SENSORS_DPS_TO_RADS);   Serial.print(" ");
  Serial.print("Z: "); Serial.println((int)gyro.data.z * SENSORS_DPS_TO_RADS); Serial.print(" ");
  delay(100);
}
```

# Calibration:
The L3GD20 is calibrated at the factory to close tolerances and will provide sufficient accuracy for most applications.   
  
For critical applications where maximum accuracy is required, the gyro should be calibrated for zero-rate and sensitivity. For detailed information on how to calibrate a MEMS gyro, please refer to section 5.3 of this [technical article](http://www.adafruit.com/datasheets/STMEMS.pdf). Danger: 

- [Previous Page](https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/assembly-and-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-triple-axis-gyro-breakout/python-circuitpython.md)

## Featured Products

### L3GD20H Triple-Axis Gyro Breakout Board - L3GD20/L3G4200 Upgrade

[L3GD20H Triple-Axis Gyro Breakout Board - L3GD20/L3G4200 Upgrade](https://www.adafruit.com/product/1032)
A gyroscope is a type of sensor that can sense twisting and turning motions. Often paired with an accelerometer, you can use these to do 3D motion capture and inertial measurement (that is - you can tell how an object is moving!) As these sensors become more popular and easier to manufacture,...

In Stock
[Buy Now](https://www.adafruit.com/product/1032)
[Related Guides to the Product](https://learn.adafruit.com/products/1032/guides)

## Related Guides

- [Adafruit 9-DOF IMU Breakout](https://learn.adafruit.com/adafruit-9-dof-imu-breakout.md)
- [Adafruit 10-DOF IMU Breakout](https://learn.adafruit.com/adafruit-10-dof-imu-breakout-lsm303-l3gd20-bmp180.md)
- [Comparing Gyroscope Datasheets](https://learn.adafruit.com/comparing-gyroscope-datasheets.md)
- [I2C Addresses and Troublesome Chips](https://learn.adafruit.com/i2c-addresses.md)
- [AdaBox 015](https://learn.adafruit.com/adabox015.md)
- [LSM303 Accelerometer + Compass Breakout](https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout.md)
- [micro:bit Lesson 1. Using the Built-in Sensors](https://learn.adafruit.com/micro-bit-lesson-1-using-the-built-in-sensors.md)
- [Mystery Box: Shutterglass Chamber](https://learn.adafruit.com/shutterglass-chamber.md)
- [CircuitPython Libraries on Linux and Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux.md)
- [Using IFTTT with Adafruit IO to Make an IoT Door Detector](https://learn.adafruit.com/using-ifttt-with-adafruit-io.md)
- [itsaSNAP Apple Health Status Board](https://learn.adafruit.com/itssnap-apple-fitness-status-board.md)
- [IoT Filament Sensor](https://learn.adafruit.com/iot-filament-sensor.md)
- [Adafruit Analog Accelerometer Breakouts](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts.md)
- [MLX90393 Wide-Range 3-Axis Magnetometer](https://learn.adafruit.com/mlx90393-wide-range-3-axis-magnetometer.md)
- [Raspberry Pi I2C Clock Stretching Fixes](https://learn.adafruit.com/raspberry-pi-i2c-clock-stretching-fixes.md)
