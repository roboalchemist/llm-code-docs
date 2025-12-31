# Source: https://learn.sparkfun.com/tutorials/sparkfun-qwiic-micropressure-hookup-guide

## Introduction

Pressure sensors are used in a wide range of applications. You can find them in the medical field (blood pressure monitoring, negative pressure wound therapy), they have industrial uses (air braking systems, gas and water meters), and have a wide range of consumer uses (coffee machines, humidifiers, air beds, washing machines, dishwashers). Measuring in at 1 square inch, the [SparkFun Qwiic MicroPressure Sensor](https://www.sparkfun.com/products/16476) takes advantage of HoneyWell\'s MPR Series piezoresistive silicone pressure sensor and our plug-and-play [Qwiic System](https://www.sparkfun.com/qwiic) to make pressure measurement easy and portable.

The MPRLS0025PA00001A boasts a small form factor (5 mm x 5 mm), easy to read 24 bit digital I^2^C output, and is calibrated and compensated over a specific temperature range for sensor offset, sensitivity, temperature effects, and non-linearity using an on-board Application Specific Integrated Circuit (ASIC). Add to that ultra-low power consumption (as low as 0.01 mW typ. average power, 1 Hz measurement frequency) and Qwiic ports, you\'ve got yourself a power packed little sensor!

[![SparkFun Qwiic MicroPressure Sensor](https://cdn.sparkfun.com/r/600-600/assets/parts/1/5/3/4/0/16476-SparkFun_Qwiic_MicroPressure_Sensor-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micropressure-sensor.html)

### [SparkFun Qwiic MicroPressure Sensor](https://www.sparkfun.com/sparkfun-qwiic-micropressure-sensor.html) 

[ SEN-16476 ]

The SparkFun Qwiic MicroPressure Sensor is a mini breakout equipped with Honeywell\'s MPR Series piezoresistive silicon 25psi ...

[ [\$37.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  *[Qwiic Connect System](https://www.sparkfun.com/qwiic)*
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[](https://learn.sparkfun.com/tutorials/redboard-qwiic-hookup-guide)

### RedBoard Qwiic Hookup Guide 

This tutorial covers the basic functionality of the RedBoard Qwiic. This tutorial also covers how to get started blinking an LED and using the Qwiic system.

## Hardware Overview

### Micro pressure sensor MPR

Honeywell\'s MPR Series MPRLS0025PA00001A sensor is a very small piezoresistive silicone pressure sensor offering I^2^C ready digital output for reading pressure over the specified full scale pressure span and temperature range. The sensor itself measures 5 mm x 5 mm and has a calibrated pressure sensing range from 1-25 PSI. It is compatible with a variety of liquid media, has a compensated temperature range of 0ºC to 50ºC (32ºF to 122ºF), and has a total error band after customer autozero as low as ±1.25 %FSS. For more information on this little guy, head on over to the [datasheet](https://cdn.sparkfun.com/assets/2/e/8/0/9/honeywell-mpr-datasheet.pdf).

[![MPR Sensor highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_MPR.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_MPR.jpg)

### Power

Ideally, power will be supplied via the Qwiic connectors on either side of the board. Alternatively, power can be supplied through the header along the bottom side of the board labeled `3V3` and `GND`. The input voltage range should be between **1.8**-**3.6V**.

⚡ **Note:** There is no onboard voltage regulation on this board. If you choose to provide power via the plated through holes, ensure that your voltage does not exceed the **3.6V absolute maximum**.

[![3V3 and GND pins highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_PowerPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_PowerPins.jpg)

### Qwiic Connectors

Our Qwiic Ecosystem makes sensors pretty much plug and play. There are two Qwiic connectors on either side of the Qwiic MicroPressure Sensor board to provide power and I^2^C connectivity simultaneously.

[![Qwiic connectors on front side of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_QwiicConnectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_QwiicConnectors.jpg)

### I^2^C Pins

The I^2^C pins break out the functionality of the Qwiic connectors. Depending on your application, you can connect to these pins via the plated through holes for SDA and SCL.

[![GPIO Pins](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_GPIO_fixed.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_GPIO_fixed.jpg)

### Reset and EOC Pins

The reset pin is active low, with an external 2.2 kΩ pull-up resistor on board. While not needed for the board to work, this pin can be pulled low externally to reset the sensor.

The EOC, or End Of Conversion, pin is set high when a measurement and calculation have been completed and the data is ready to be clocked out. Alternatively the status register of the sensor can also be used to check to see when a new measurement is ready.

[![End of Conversion and Reset pins highlighted on the front of the board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_ResetandEOCPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_ResetandEOCPins.jpg)

### Power LED

Located towards the top left of the board, the Power LED gives you visual confirmation that your board is powered and ready to go.

[![Power LED Hightlighted on Front of Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_PowerLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_PowerLED.jpg)

### Jumpers

#### I^2^C Jumpers

Like our other Qwiic boards, the Qwiic MicroPressure Sensor comes equipped with pull-up resistors on the clock and data pins. If you are daisy-chaining multiple Qwiic devices, you will want to cut this jumper; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. To disable the pull up resistors, use an X-acto knife to cut the joint between the two jumper pads highlighted below.

[![Highlighted I2C Jumpers on Back of Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_I2CJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_I2CJumper.jpg)

#### LED Jumper

If power consumption is an issue, cutting this jumper will disable the Power LED on the front of the board.

[![Highlighted LED Jumpers on Back of Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_LEDJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476-SparkFun_Qwiic_MicroPressure_Sensor_LEDJumper.jpg)

### Board Dimensions

[![Dimensions of the Qwiic MicroPressure Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/MicroPressureBoardDimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/MicroPressureBoardDimensions.png)

## Hardware Hookup

With the [Qwiic System](https://www.sparkfun.com/qwiic), hardware hookup is a breeze. Plug one end of the Qwiic cable into the SparkFun Redboard Qwiic port, and the other into the MicroPressure Sensor board\'s Qwiic port as you see below:

[![Hookup Qwiic MicroPressure Sensor to RedBoard Qwiic Port](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/7/5/Micro_Pressure_Sensor_Tutorial-01_Cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/Micro_Pressure_Sensor_Tutorial-01_Cropped.jpg)

## Software Setup and Programming

**Note:** This code/library has been written and tested on Arduino IDE version 1.8.13.\
\
If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

SparkFun has written a library to work with the Qwiic MicroPressure Sensor. You can obtain this library through the Arduino Library Manager by searching for \"MicroPressure\". Find the one written by SparkFun Electronics and install the latest version. If you prefer downloading libraries manually, you can grab them from the GitHub Repository.

[SparkFun MicroPressure Arduino Library GitHub](https://github.com/sparkfun/SparkFun_MicroPressure_Arduino_Library/archive/main.zip)

### Functions

Below is a list of the functions that can be used with the MicroPressure sensor, along with a description of what each function does and how to use it.

- **SparkFun_MicroPressure( int8_t eoc_pin, int8_t rst_pin, uint8_t minimumPSI, uint8_t maximumPSI )** - The constructor has four optional arguments, by default the eoc_pin, and rst_pin are not used, and the MicroPressure sensor used on the board has a pressure range of 0 - 25 PSI.

  - `eoc_pin` - The End Of Conversion pin is set high when a measurement and calculation have been completed and the data is ready to be clocked out. When set to -1, the status register is used to check when a measurement is ready to be clocked out. **Default: -1**
  - `rst_pin` - The Reset pin is active low, and resets the sensor in the begin function. When set to -1, the board will reset after a power cycle. **Default: -1**
  - `minimumPSI` - The minimum PSI value is used in the pressure conversion calculation for the MPR series sensor. **Default: 0 PSI**
  - `maximumPSI` - The minimum PSI value is used in the pressure conversion calculation for the MPR series sensor. **Default: 25 PSI**

- **bool begin(uint8_t deviceAddress, TwoWire &wirePort)** - Call at the beginning of the sketch to intialize the device. This function takes two optional parameters: deviceAddress and wirePort. This function will return `true` when the device is intialized, and `false` if it is unable to communicate with the device.

  - `deviceAddress` - The MPR series sensor has multiple I^2^C addresses that are fixed as shown on [page 7 of the datasheet](https://cdn.sparkfun.com/assets/2/e/8/0/9/honeywell-mpr-datasheet.pdf#page=7), with the most common address being 0x18. **Default: 0x18**
  - `wirePort` - Sets the I^2^C bus the sensor is connected to, such as Wire or Wire1. **Default: Wire**

- **float readPressure (Pressure_Units units)** - returns the pressure sensor reading. The sensor outputs pressure in pounds per square inch, or PSI. If you would prefer a different unit of measurement, this function can convert the reading to one of the following for you by passing the argument:

  - `PSI` - Pounds per Square Inch (default)
  - `PA` - Pascals
  - `KPA` - kilopascals
  - `BAR` - bar (1 bar is equal to 100,000 Pa)
  - `TORR` - torr (1 torr is roughly equal to 133.32 Pa)
  - `INMG` - Inches of Mercury (Mg)
  - `ATM` - Atmospheres

- **uint8_t readStatus( void )** - Reads and returns the status byte of the sensor. For more information about the status byte refer to [page 15 of the datasheet](https://cdn.sparkfun.com/assets/2/e/8/0/9/honeywell-mpr-datasheet.pdf#page=15).

## Example Code

Once the library is installed, go ahead and open up **File**-\>**Examples**-\>**SparkFun MicroPressure Library**-\>**Example1_BasicReadings**. Make sure to select your board (SparkFun RedBoard) and COM port before hitting upload to begin experimenting with the pressure sensor.

Alternatively, you can copy and paste the code below to a shiny new Arduino file:

    language:c
    /*
      Basic test of the Qwiic MicroPressure Sensor
      By: Alex Wende
      SparkFun Electronics
      Date: July 2020
      License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).
      Feel like supporting our work? Buy a board from SparkFun!
      https://www.sparkfun.com/products/16476

      This example demonstrates how to get started with the Qwiic MicroPressure Sensor board, and read pressures in various units.
    */

    // Include the SparkFun MicroPressure library.
    // Click here to get the library: http://librarymanager/All#SparkFun_MicroPressure

    #include<Wire.h>
    #include <SparkFun_MicroPressure.h>

    /*
     * Initialize Constructor
     * Optional parameters:
     *  - EOC_PIN: End Of Conversion (defualt: -1)
     *  - RST_PIN: Reset (defualt: -1)
     *  - MIN_PSI: Minimum Pressure (default: 0 PSI)
     *  - MAX_PSI: Maximum Pressure (default: 25 PSI)
     */
    //SparkFun_MicroPressure mpr(EOC_PIN, RST_PIN, MIN_PSI, MAX_PSI);
    SparkFun_MicroPressure mpr; // Use default values with reset and EOC pins unused

    void setup() 
    }

    void loop() 

Once you have the code, go ahead and click on the upload button, open your serial monitor, and watch the magic happen!

For this particular example, I purchased [uxcell Pneumatic Hose 4mm OD 2.5mm](https://www.amazon.com/gp/product/B077WHF2DS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) from Amazon, but any tubing with an inner diameter of 2.5mm will work.

Attach the tubing over the protruding MPR sensor like so:

[![tubing is attached to the MPR sensor on the breakout board](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/Micro_Pressure_Sensor_Tutorial-02_cropped.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/Micro_Pressure_Sensor_Tutorial-02_cropped.jpg)

[Open up your Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and make sure your baud is at 115200. You should see the average pressure being output in multiple different measurements. If you apply negative pressure to the tubing, you\'ll see the measurements go down, positive pressure will show the measurements going up. Note the output below:

[![Results of average pressure, negative pressure, and positive pressure listed out](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476_PressureReadings_with_Text.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/5/16476_PressureReadings_with_Text.png)

*Output shown with Average, Negative, and Positive pressures applied to the sensor*

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.