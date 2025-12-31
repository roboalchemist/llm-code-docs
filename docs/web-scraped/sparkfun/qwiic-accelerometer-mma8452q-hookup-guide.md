# Source: https://learn.sparkfun.com/tutorials/qwiic-accelerometer-mma8452q-hookup-guide

## Introduction

Freescale\'s [MMA8452Q](https://www.sparkfun.com/products/10953) is a smart, low-power, three-axis, capacitive micro-machined accelerometer with 12 bits of resolution. It\'s perfect for any project that needs to sense orientation or motion. We\'ve taken that accelerometer and stuck it on a [Qwiic-Enabled breakout board](https://www.sparkfun.com/products/14587), in order to make interfacing with the tiny, QFN package a bit easier. It\'s part of SparkFun\'s [Qwiic system](https://www.sparkfun.com/categories/399), so you won\'t have to do any soldering to figure out how things are oriented.

[![SparkFun Triple Axis Accelerometer Breakout - MMA8452Q (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/7/4/0/14587-SparkFun_Accelerometer_Breakout_-_MMA8452Q__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-mma8452q-qwiic.html)

### [SparkFun Triple Axis Accelerometer Breakout - MMA8452Q (Qwiic)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-mma8452q-qwiic.html) 

[ SEN-14587 ]

This breakout board makes it easy to use the tiny MMA8452Q accelerometer communicate over I2C in your project.

**Retired**

The MMA8452Q is a rock-solid, feature rich, 3-axis accelerometer. It supports three, selectable sensing ranges: ± 2g, 4g, or 8g. It also sports features like orientation detection, single and double-tap sensing, and low power modes. It\'s a digital sensor \-- communicating over a Qwiic enabled I^2^C interface \-- so you\'ll get reliable, noise-free data over a Qwiic enabled I^2^C port.

In this hookup guide, we\'ll connect our sensor up to our microcontroller of choice and read the X, Y, and Z accelerometer channels to figure out how we are accelerating in those directions. Then, we\'ll figure out how to use orientation detection to figure out what orientation the sensor is in.

### Required Materials

To get started, you\'ll need a microcontroller to, well, control everything.

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

Now to get into the Qwiic ecosystem, the key will be one of the following Qwiic shields to match your preference of microcontroller:

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

[![SparkFun Qwiic Shield for Photon](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/5/2/6/14477-01.jpg)](https://www.sparkfun.com/products/14477)

### [SparkFun Qwiic Shield for Photon](https://www.sparkfun.com/products/14477) 

[ DEV-14477 ]

The SparkFun Qwiic Shield for Photon is an easy-to-assemble board that provides a simple way to incorporate the Qwiic System ...

**Retired**

You will also need a Qwiic cable to connect the shield to your accelerometer, choose a length that suits your needs.

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

## Hardware Overview 

Let\'s look over a few characteristics of the [MMA8452Q sensor](https://cdn.sparkfun.com/datasheets/Sensors/Accelerometers/MMA8452Q.pdf) so we know a bit more about how it behaves.

  **Characteristic**   **Range**
  -------------------- ---------------------------------------------------------
  Operating Voltage    **1.95V - 3.6V**
  Current              7-165 &microA
  Measurement Range    &plusmn2g, &plusmn4g, &plusmn8g
  I^2^C Address        **0x1D (open jumper, default)** or 0x1C (closed jumper)

### Pins

The characteristics of the available pins on the MMA8452Q are outlined in the table below.

  Pin Label   Pin Function         Input/Output     Notes
  ----------- -------------------- ---------------- ----------------------------------------------------------------------------------------
  3.3V        Power Supply         Input            Should be between 1.95 - 3.6V
  SDA         I^2^C Data Signal    Bi-directional   Bi-directional data line. Voltage should not exceed power supply (e.g. 3.3V).
  SCL         I^2^C Clock Signal   Input            Master-controlled clock signal. Voltage should not exceed power supply (e.g. 3.3V).
  INT2        Interrupt 2          Output           Programmable interrupt --- can indicate data ready, orientation change, tap, and more.
  INT1        Interrupt 1          Output           Programmable interrupt --- can indicate data ready, orientation change, tap, and more.
  GND         Ground               Input            0V/common voltage.

\

### Optional Features

#### Pull-Up Resistors Jumper

The Qwiic Accelerometer has onboard I^2^C pull up resistors; if multiple sensors are connected to the bus with the pull-up resistors enabled, the parallel equivalent resistance will create too strong of a pull-up for the bus to operate correctly. As a general rule of thumb, disable all but one pair of pull-up resistors if multiple devices are connected to the bus. If you need to disconnect the pull up resistors they can be removed by removing the solder on the corresponding jumpers highlighted below.

[![Pull-Up Resistor Jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/4/i2cpu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/4/i2cpu.png)

#### []Address Select Jumper

There is an additional jumper on the back of the board that allows the I^2^C to be changed from the default 0x1D to 0x1C if you have multiple accelerometers on the same I^2^C bus. However, if you have more than 2 accelerometers, you\'ll need the [Qwiic Mux](https://www.sparkfun.com/products/14293) to have them all on the same I^2^C bus. The jumper is highlighted below. Normally open, the jumper sets the I^2^C address to 0x1D. Closing the jumper with solder will give an I^2^C address of 0x1C.

[![Address select jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/4/addr.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/4/addr.png)

#### Axis Reference

Also be sure to check out the labeling on the back of the board that indicates the orientation of the positive X, Y, and Z axes so you know what exactly your data means.

[![Axis Reference](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/4/orient.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/4/orient.png)

## Hardware Assembly 

If you haven\'t yet [assembled your Qwiic Shield](https://learn.sparkfun.com/tutorials/qwiic-shield-for-arduino--photon-hookup-guide), now would be the time to head on over to that tutorial. With the shield assembled, Sparkfun\'s new Qwiic environment means that connecting the sensor could not be easier. Just plug one end of the Qwiic cable into the Accelerometer breakout, the other into the Qwiic Shield of your choice and you\'ll be ready to upload a sketch and figure out how your board is moving around. It seems like it\'s too easy to use, but that\'s why we made it that way!

[![Qwiic Accelerometer connected to Qwiic Arduino Shield and RedBoard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/3/4/Qwiic_Accelerometer_Tutorial-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/3/4/Qwiic_Accelerometer_Tutorial-03.jpg)

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We\'ve written an Arduino library to make interfacing with the MMA8452Q as easy as can be. Click on the button below to download the library. Or you can grab the latest, greatest version over on the [library\'s GitHub repository](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library).

[Download MMA8452Q Arduino Library (ZIP)](https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library/archive/main.zip)

### Load Up the Example Sketch

Once you\'ve installed the *SFE_MMA8452Q* library, restart Arduino. Then go to **File** \> **Examples** \> **SFE_MMA8452Q** \> **MMA8452Q_Basic** to open the example sketch.

[![Opening the example sketch](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/9/opening-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/9/opening-example.png)

Once you\'ve set your Board and Serial Port, upload the sketch to your Arduino. Then **open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics)**. You\'ll begin to see acceleration values stream by, in addition to some information about the sensor\'s orientation.

[![Serial stream example](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/9/serial-monitor-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/4/9/serial-monitor-example.png)

Try moving the sensor around to change those values. If it is motionless, flat on the desk, then an acceleration of 1g should be felt on the z-axis, while the others feel around 0. Test the other axes by rotating the board and making them feel the pull of gravity.

### Using the SFE_MMA8452Q Library

Here are some tips on using the MMA8452Q Arduino library so you can embed it into an Arduino sketch of your own.

#### Include the Library (Global)

To begin, you need to \"include\" the library in your sketch:

    language:c
    #include <Wire.h> // Must include Wire library for I2C
    #include <SFE_MMA8452Q.h> // Includes the SFE_MMA8452Q library

The library also requires that you include `Wire.h` in your sketch. Make sure you include that *before* you include the *SFE_MMA8452Q.h* file.

#### Create an MMA8452Q Object (Global)

Once the library is included, you can create an MMA8452Q object. This line of code will do it for you:

    language:c
    MMA8452Q accel; // Default MMA8452Q object create. (Address = 0x1D)

Optionally, you can define the 7-bit **I^2^C address** of your MMA8452Q in this parameter, using one of these lines of code:

    language:c
    MMA8452Q accel(0x1C); // Initialize the MMA8452Q with an I2C address of 0x1C (SA0=0)
    MMA8452Q accel(0x1D); // Initialize the MMA8452Q with an I2C address of 0x1D (SA0=1)

But if you\'ve left the [address jumper](https://learn.sparkfun.com/tutorials/qwiic-accelerometer-hookup-guide/hardware-overview#address-jumper) untouched (meaning the \"SA0\" pin is connected to VCC), you can call the default (no parameter) constructor shown earlier.

#### Initialize the MMA8452Q (Setup)

Finally, in the `setup()` function of your sketch, you can initialize the accelerometer using the `init()` function. The `init()` function verifies communication with the accelerometer, and sets up the **full-scale range** and **output data rate**.

Again, you have a few options here. You can use a simple declaration like below. This will initialize the accelerometer with range of **±2g** and an output data rate of **800 Hz** (turns the accelerometer up to the max!):

    language:c
    accel.init(); // Default init: +/-2g and 800Hz ODR

If you want to specify the acceleration and output data rate, you can instead use an `init()` function like this:

    language:c
    accel.init([scale], [odr]); // Init and customize the FSR and ODR

Scale can be either `SCALE_2G`, `SCALE_4G`, or `SCALE_8G`. The \"odr\" variable can be either `ODR_800`, `ODR_400`, `ODR_200`, `ODR_100`, `ODR_50`, `ODR_12`, `ODR_6`, or `ODR_1`, respectively setting the data rate to 800, 400, 200, 100, 50, 12.5, 6.25, or 1.56 Hz.

#### Reading and Using Values

Once you\'ve set the accelerometer up, you can immediately start reading the data coming out of the chip. Reading and using the values is a two-step process. First, call the `read()` function to pull in the values.

    language:c
    accel.read(); // Update acceleromter data

*After* you\'ve called the `read()` function, you can use either of two sets of values to use the data. Reading from the `x`, `y`, and `z` class variables will return a signed 12-bit integer read straight out of the accelerometer.

    language:c
    xAcceleration = accel.x; // Read in raw x-axis acceleration data
    Serial.print("Acceleration on the x-axis is ");
    Serial.println(xAcceleration);

Or, if you want a value with physical units, you can use the `cx`, `cy`, and `cz` class variables. These are the **calculated** acceleration values read out of the accelerometer; they\'ll be in units of *g*\'s.

    language:c
    zAcceleration = accel.cz; // Read in calculated z-axis acceleration
    Serial.print("Acceleration on the z-axis is: ");
    Serial.print(zAcceleration);
    Serial.println(" g's");

Remember! Those variables are only updated *after* the `read()` function is called. Make sure that happens before you start using acceleration values.

#### Reading Portrait/Landscape

The MMA8452Q has all sorts of nifty, extra features, one of which is **orientation detection** \-- it can estimate if it\'s being held in landscape mode, portrait mode, or flat.

To read the portrait/landscape data from the accelerometer, use the `readPL()` function. This function returns a byte, which will either be equal to `PORTRAIT_U`, `PORTRAIT_D`, `LANDSCAPE_R`, `LANDSCAPE_L`, or `LOCKOUT`.

    language:c
    byte pl = accel.readPL();
    switch (pl)
    

As in the example above, you can use `if` or `switch` statements to check which orientation your accelerometer is in.