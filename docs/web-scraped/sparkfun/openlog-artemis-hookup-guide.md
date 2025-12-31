# Source: https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- OpenLog Artemis Hookup Guide

# OpenLog Artemis Hookup Guide

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate], [![](https://cdn.sparkfun.com/avatar/814545d7cad2a95dda668529c61c99d0?d=retro&s=20&r=pg) bboyho], [![](https://cdn.sparkfun.com/avatar/ea6398c8ad1d378f523ba26e9c5169ac?d=retro&s=20&r=pg) PaulZC]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1213&name=OpenLog+Artemis+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1213 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=OpenLog+Artemis+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1213&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1213&t=OpenLog+Artemis+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1213&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F1%2F3%2F16832-SparkFun_OpenLog_Artemis-01.jpg&description=OpenLog+Artemis+Hookup+Guide "Pin It")

## Introduction

**Note:** The following tutorial is written with **firmware v1.11** in mind and will be updated as necessary based on the firmware release. For information about the firmware releases, check out the [GitHub repo releases for the OpenLog Artemis](https://github.com/sparkfun/OpenLog_Artemis/releases).

The [SparkFun OpenLog Artemis (OLA)](https://www.sparkfun.com/products/16832) is a versatile, open source data logger that comes preprogrammed to automatically log a wide variety of data from a large number of sensors. And here's the best bit... You can do all of this without writing a single line of code! The OLA automatically detects which sensors are connected to it and logs the data to microSD card in standard Comma Separated Value (CSV) format. The OLA is designed for users who just need to capture a bunch of data and get back to their larger project. We will quickly get you up to speed with the OLA and the Qwiic ecosystem so you can start logging all that data!

[![SparkFun OpenLog Artemis](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/7/5/3/16832-SparkFun_OpenLog_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-openlog-artemis.html)

### [SparkFun OpenLog Artemis](https://www.sparkfun.com/sparkfun-openlog-artemis.html) 

[ DEV-16832 ]

The SparkFun OpenLog Artemis is an open source data logger that comes pre-programmed to automatically log IMU, GPS, serial da...

[ [\$59.95] ]

[![SparkFun OpenLog Artemis (without IMU)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/9/0/6/7/19426-SparkFun_OpenLog_Artemis__no_IMU_-01.jpg)](https://www.sparkfun.com/sparkfun-openlog-artemis-without-imu.html)

### [SparkFun OpenLog Artemis (without IMU)](https://www.sparkfun.com/sparkfun-openlog-artemis-without-imu.html) 

[ DEV-19426 ]

The SparkFun OpenLog Artemis is an open source data logger that comes pre-programmed to automatically log sensor, GPS, serial...

[ [\$48.95] ]

### Required Materials

[] **Battery Polarity:** Please make sure that you use one of our recommended Lithium Ion batteries. Some batteries use the same JST connector as ours but have the [opposite polarity](https://learn.sparkfun.com/tutorials/polarity/all#other-polarized-components). Connecting one of these to your OLA will destroy it. If you are going to use your own battery, it is up to you to ensure it has the correct polarity.

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

- [SparkFun OpenLog Artemis \[DEV-16832\]](https://www.sparkfun.com/products/16832)
- [microSD Card formatted with FAT32 \[COM-15107\]](https://www.sparkfun.com/products/15107)
- A USB-C cable for configuration and LiPo charging
  - Our [USB 2.0 A to C Cable \[CAB-15092\]](https://www.sparkfun.com/products/15092) will do nicely
  - Our [USB 3.1 A to C Cable \[CAB-14743\]](https://www.sparkfun.com/products/14743) is a good choice too
- [Lithium Ion Battery \[PRT-13855\]](https://www.sparkfun.com/lithium-ion-battery-2ah.html)
- At least one Qwiic cable
  - A single [50mm Cable](https://www.sparkfun.com/products/14426) is all you need to get going
  - Our [Qwiic Cable Kit](https://www.sparkfun.com/products/15081) covers all the options
- Any additional sensors you may need

**Note:** Want to quickly add the minimum parts needed to follow along the tutorial? Check out the wishlist below to add the parts to your cart. Depending on your personal preference, you will need at least one Qwiic cable between each Qwiic-enabled sensor that is recognized by the OpenLog Artemis.\
\

### The Sensors

Straight out of the [box] anti-static bag the OLA \[DEV-16832\] is ready to log data from its built-in ICM-20948 Inertial Measurement Unit (IMU) 9-Degrees-Of-Freedom (9-DOF) sensor. Only want to log magnetometer, accelerometer, gyro or temperature data? You're good to go! But the fun is only just beginning...

**Note:** The OpenLog Artemis without IMU \[DEV-19426\] has the ICM-20948 IMU sensor removed. This IC is becoming increasingly difficult to locate. This version still supports auto-detection and logging of over a dozen sensors and GNSS receivers, including the [ISM330DHCX IMU](https://www.sparkfun.com/products/20176), [MMC5983MA Magnetometer](https://www.sparkfun.com/products/19921) and [KX134 64g Accelerometer](https://www.sparkfun.com/products/17589).

The OLA is preprogrammed to automatically log data from all of the following sensors, so you may wish to add one or more of these to your shopping cart too. (More sensors are being added all the time and it is really easy to upgrade the OLA to support them. But we'll get to that in a moment!)

- Global Navigation Satellite System (GNSS) navigation data. The OLA can be linked to any of SparkFun's [u-blox GNSS boards](https://www.sparkfun.com/products/16481) allowing you to log accurate position, velocity and time data from:
  - GPS
  - GLONASS
  - Galileo
  - BeiDou
  - and augmentation services like SBAS\
- Inertial Measurement Unit (Accelerometer and Gyro)
  - [ISM330DHCX](https://www.sparkfun.com/products/19764) IMU\
- Magnetometer
  - [MMC5983MA](https://www.sparkfun.com/products/19921) magnetometer\
- Accelerometer
  - [KX134](https://www.sparkfun.com/products/17589) 64g accelerometer\
- Pressure, Altitude, Humidity and Temperature Data:
  - [BME280](https://www.sparkfun.com/products/15440) atmospheric sensor
  - [LPS25HB](https://www.sparkfun.com/products/14767) absolute pressure sensor
  - [MS8607](https://www.sparkfun.com/products/16298) PHT sensor
  - [MPR0025PA](https://www.sparkfun.com/products/16476) MicroPressure sensor
  - [MS5637](https://www.sparkfun.com/products/14688) barometric pressure sensor
  - [MS5837](https://www.sparkfun.com/products/17709) depth and pressure sensor
  - [AHT20](https://www.sparkfun.com/products/16618) humidity and temperature sensor
  - [SHTC3](https://www.sparkfun.com/products/16467) humidity and temperature sensor
  - [SDP31](https://www.sparkfun.com/products/17874) differential pressure sensor
  - [LPS28DFW](https://www.sparkfun.com/products/21221) barometer\
- Air Quality and Environmental Sensors:
  - [CCS811](https://www.sparkfun.com/products/14193) air quality sensor
  - [VEML6075](https://www.sparkfun.com/products/15089) UV light sensor
  - [SGP30](https://www.sparkfun.com/products/16531) air quality and Volatile Organic Compound (VOC) sensor
  - [SGP40](https://www.sparkfun.com/products/17729) air quality (VOC Index) Sensor
  - [SCD30](https://www.sparkfun.com/products/15112) CO~2~ humidity and temperature sensor
  - [SN-GCJA5](https://www.sparkfun.com/products/17123) particle sensor
  - [VEML7700](https://www.sparkfun.com/products/18981) ambient light sensor\
- Distance:
  - [VL53L1X](https://www.sparkfun.com/products/14722) laser Time of Flight (ToF) sensor
  - [VCNL4040](https://www.sparkfun.com/products/15177) proximity sensor\
- Precision Temperature Sensors:
  - [MCP9600](https://www.sparkfun.com/products/16294) thermocouple amplifier
  - [Qwiic PT100 ADS122C04](https://www.sparkfun.com/products/16770) platinum resistance sensor
  - [TMP117](https://www.sparkfun.com/products/15805) precision temperature sensor\
- Biometric Sensors:
  - [MAX30101](https://www.sparkfun.com/products/15219) pulse oximeter and heart rate sensor\
- Weight:
  - [NAU7802](https://www.sparkfun.com/products/15242) load cell sensor\
- Serial Data:
  - The OLA will automatically log standard 3.3V serial data received on its RX pin
  - The OLA can also stream the sensor data to the serial TX pin (when enabled)\
- Analog Voltage:
  - OLA supports up to four built-in 14-bit Analog to Digital Converter (ADC) pins (2.0V Maximum)
  - [ADS1015](https://www.sparkfun.com/products/15334) 12-bit 4-channel differential ADC
  - The OLA supports differential voltage sensing with the ADS122C04 24-bit ADC found on the [Qwiic PT100](https://www.sparkfun.com/products/16770)\
- Events / Configuration:
  - The OLA supports single or multiple [SparkFun Qwiic Buttons](https://www.sparkfun.com/products/15932), which allow events to be marked or status or configuration information to be logged.\

**Note:** You can find the units for each sensor measurement in the [GitHub repo](https://github.com/sparkfun/OpenLog_Artemis/blob/main/SENSOR_UNITS.md).

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We also recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/gyroscope)

### Gyroscope 

Gyroscopes measure the speed of rotation around an axis and are an essential part in determines ones orientation in space.

[](https://learn.sparkfun.com/tutorials/battery-technologies)

### Battery Technologies 

The basics behind the batteries used in portable electronic devices: LiPo, NiMH, coin cells, and alkaline.

[](https://learn.sparkfun.com/tutorials/accelerometer-basics)

### Accelerometer Basics 

A quick introduction to accelerometers, how they work, and why they\'re used.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/sparkfun-9dof-imu-icm-20948-breakout-hookup-guide)

### SparkFun 9DoF IMU (ICM-20948) Breakout Hookup Guide 

How to use the SparkFun 9DoF ICM-20948 breakout board for your motion sensing projects. This breakout is ideal for wearable sensors and IoT applications.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft1213&name=OpenLog+Artemis+Hookup+Guide "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft1213 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=OpenLog+Artemis+Hookup+Guide&url=http%3A%2F%2Fsfe.io%2Ft1213&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft1213&t=OpenLog+Artemis+Hookup+Guide "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft1213&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F1%2F2%2F1%2F3%2F16832-SparkFun_OpenLog_Artemis-01.jpg&description=OpenLog+Artemis+Hookup+Guide "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/all) [Next Page →\
[Hardware Overview]](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/hardware-overview)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/introduction) [Hardware Overview](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/hardware-overview) [Hardware Hookup](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/hardware-hookup) [Configuration](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/configuration) [Updating Firmware](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/updating-firmware) [Low Power Considerations](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/low-power-considerations) [GNSS Logging](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/gnss-logging) [Seismometry: Geophone Logging](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/seismometry-geophone-logging) [Troubleshooting and FAQs](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/troubleshooting-and-faqs) [Resources and Going Further](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/resources-and-going-further)

[Comments [19]](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/discuss) [Single Page](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/all) [Print]

- **Tags**
- - [Artemis](https://learn.sparkfun.com/tutorials/tags/artemis)
  - [Data Logging](https://learn.sparkfun.com/tutorials/tags/data-logging)
  - [GNSS](https://learn.sparkfun.com/tutorials/tags/gnss)
  - [GPS](https://learn.sparkfun.com/tutorials/tags/gps)
  - [Hookup](https://learn.sparkfun.com/tutorials/tags/hookup)
  - [Logging](https://learn.sparkfun.com/tutorials/tags/logging)
  - [Motion](https://learn.sparkfun.com/tutorials/tags/motion)
  - [Qwiic](https://learn.sparkfun.com/tutorials/tags/qwiic)
  - [Sensors](https://learn.sparkfun.com/tutorials/tags/sensors)
  - [Time](https://learn.sparkfun.com/tutorials/tags/time)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]