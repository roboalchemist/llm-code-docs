# Source: https://learn.sparkfun.com/tutorials/h3lis331dl-accelerometer-breakout-hookup-guide

## Introduction

The [H3LIS331DL](https://www.sparkfun.com/products/14480) is a high-g accelerometer with I2C and SPI interface options. It offers an adjustable output range of 100, 200, or 400g, and an adjustable data rate of up to 1kHz.

[![SparkFun Triple Axis Accelerometer Breakout - H3LIS331DL](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/5/3/2/14480-01.jpg)](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-h3lis331dl.html)

### [SparkFun Triple Axis Accelerometer Breakout - H3LIS331DL](https://www.sparkfun.com/sparkfun-triple-axis-accelerometer-breakout-h3lis331dl.html) 

[ SEN-14480 ]

The SparkFun H3LIS331DL Triple Axis Accelerometer Breakout is a low-power, high-g accelerometer with I2C and SPI interface op...

[ [\$17.10] ]

### Required Materials

Please check the wish list below for items required to follow this tutorial.

### Tools

No special tools are required to follow this tutorial. You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

### Suggested Reading

We suggest reviewing the tutorials below to ensure that you\'re up-to-date with all of the skills necessary to follow this hookup guide.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

### Installing an Arduino Library 

How do I install a custom Arduino library? It\'s easy! This tutorial will go over how to install an Arduino library using the Arduino Library Manager. For libraries not linked with the Arduino IDE, we will also go over manually installing an Arduino library.

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Hardware Overview

The H3LIS331DL breakout is fairly simple.

**H3LIS331DL Sensor IC** - This is the sensor IC. Its operating voltage only extends up to **3.6V**, so to use it with a 5V Arduino or Arduino clone, you\'ll need some kind of [voltage translation](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide)! It is perfectly centered on the PCB.

[![Chip, highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DL_IC.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DL_IC.png)

**I^2^C Pull-up Resistors** - The board includes pull-up resistor so you don\'t need to add them externally.

[![I2C Resistors Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLPullUpResistors.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLPullUpResistors.png)

**I^2^C Pull-up Resistor Isolation Jumper** - If necessary, the I^2^C pull-up resistors can be removed from the circuit by removing the solder from this jumper.

[![I2C Resistor Jumper Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLPullUpResistorJumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLPullUpResistorJumper.png)

**SparkFun Standard I^2^C Header** - Most boards which can be communicated to via I^2^C use this pinout, making it easy to stack them or connect them in a daisy chain.

[![I2C Header Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLI2C.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLI2C.png)

**SA0 Jumper** - Closing this jumper changes the I^2^C address of the sensor from 0x19 to 0x18.

[![SA0 Jumper Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLSA0Jumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLSA0Jumper.png)

**CS Jumper** - Removing the solder from this jumper enables SPI mode. When the part\'s CS line is low at boot, it enables SPI mode.

[![CS Jumper Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLCSJumper.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-02_H3LIS331DLCSJumper.png)

**SA0 Pin** - When the chip is in SPI mode, this goes from being the address select pin to being the MISO pin.

[![SA0 Pin Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLSA0Pin.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLSA0Pin.png)

**CS Pin** - Chip select for SPI mode. Unused in I^2^C mode.

[![CS Pin Highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLCSPin.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLCSPin.png)

**Interrupt Pins** - These pins are tied to interrupts that can be setup by the software library to trigger on various conditions.

[![Interrupt pins highlighted](https://cdn.sparkfun.com/r/300-300/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLINTPins.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/14480-03_H3LIS331DLINTPins.png)

## Library Overview

Here\'s a list of the functions supported by the [Arduino library for the LIS331 family](https://github.com/sparkfun/SparkFun_LIS331_Arduino_Library).

**`begin(comm_mode mode)`** - Sets the communications mode to be used by the library (`LIS331::USE_I2C` or `LIS331::USE_SPI`), sets the power mode to normal, enables the axes, sets the sampling rate to 50Hz, and resets all the other registers to 0.

**`setI2CAddr(address)`** - Sets the I^2^C address. By default this is going to be 0x19. If the SA0 jumper is soldered closed, it is 0x18. **This function must be called before `begin()` so the library knows what address to use for communications.**

**`setSPICSPin(pin)`** - Sets the SPI mode chip select pin. **This function must be called before `begin()` so the library knows which pin to use for communications.**

**`axesEnable(bool enable)`** - Pass `true` to enable the axes or `false` to disable them.

**`setPowerMode(power_mode pmode)`** - Sets the power mode of the chip. This affects the data rate as well. Options are:

- **`LIS331::POWER_DOWN`** - Minimizes chip power usage but no data or communications are possible
- **`LIS331::NORMAL`** - Normal power mode. Data rate is set by the `setODR()` function.
- **`LIS331::LOW_POWER_0_5HZ`** - Low power mode, 0.5Hz data rate.
- **`LIS331::LOW_POWER_1HZ`** - Low power mode, 1Hz data rate.
- **`LIS331::LOW_POWER_2HZ`** - Low power mode, 2Hz data rate.
- **`LIS331::LOW_POWER_5HZ`** - Low power mode, 5Hz data rate.
- **`LIS331::LOW_POWER_10HZ`** - Low power mode, 10Hz data rate.

**`setODR(data_rate drate)`** - Sets the data rate for the part, when in normal power mode only. Options are:

- **`LIS331::DR_50HZ`** - Set the data rate to 50Hz.
- **`LIS331::DR_100HZ`** - Set the data rate to 100Hz.
- **`LIS331::DR_400HZ`** - Set the data rate to 400Hz.
- **`LIS331::DR_1000HZ`** - Set the data rate to 1000Hz.

**`readAxes(int16_t &x, int16_t &y, int16_t &z)`** - Pass three `int16_t` variables to this function and those variables will be populated with the appropriate value from the accelerometer.

**`convertToG(maxScale, reading)`** - Converts from raw data to an actual g-reading. The first parameter is the maximum reading for the current mode, as set by the `setFullScale()` function. Options are 6/12/24g for the LIS331HH and 100/200/400g for the H3LIS331DL.

**`setHighPassCoeff(high_pass_cutoff_freq_cfg hpcoeff)`** - Set the coefficient for the high pass filter. The actual cutoff frequency is dependent upon the data rate set by `setODR()`. The cutoff frequency is (fs)/(6\*Hpc), where fs is the sampling frequency and Hpc is the high pass coefficient as set by these constants:

- **`LIS331::HPC_8`** - Sets coefficient to 8.
- **`LIS331::HPC_16`** - Sets coefficient to 16.
- **`LIS331::HPC_32`** - Sets coefficient to 32.
- **`LIS331::HPC_64`** - Sets coefficient to 64.

**`enableHPF(bool enable)`** - `true` to enable, `false` to disable.

**`HPFOOnIntPin(bool enable, intSource)`** - Does the high pass filter apply to the signal the interrupt is based on? `true` to enable, `false` to disable, and the second parameter is 1 or 2 depending on which interrupt you wish to apply this setting to.

**`intActiveHigh(bool enable)`** - Pass `true` to set the interrupt pin to active high, `false` to set it as active low. Default value is active high.

**`intPinMode(pp_od _pinMode)`** - Are the interrupt pins open-drain or push pull? Pass `LIS331::PUSH_PULL` or `LIS331::OPEN_DRAIN`.

**`intSrcConfig(int_sig_src src, pin)`** - What sort of thing triggers an interrupt, and which pin shows the interrupt. The options are:

- **`LIS331::INT_SRC`** - Interrupt source is the same as the pin number.
- **`LIS331::INT1_2_SRC`** - Either interrupt will be reflected on the pin.
- **`LIS331::DRDY`** - The \"new data ready\" signal will be reflected on the pin.
- **`LIS331::BOOT`** - The boot mode status of the part is reflected on the pin.

**`setFullScale(fs_range range)`** - Sets the range of the part, as listed below:

- **`LOW_RANGE`** - +/-6g for the LIS331HH or +/-100g for the H3LIS331DH.
- **`MED_RANGE`** - +/-12g for the LIS331HH or +/-200g for the H3LIS331DH.
- **`HIGH_RANGE`** - +/-24g for the LIS331HH or +/-400g for the H3LIS331DH.

**`bool newXData()`** - returns `true` if new X data is available since last read of X data register.

**`bool newYData()`** - same as `newXData()` for Y axis.

**`bool newZData()`** - same as `newZData()` for Z axis.

**`enableInterrupt(int_axis axis, trig_on_level trigLevel, interrupt, bool enable)`** - `axis` can be `LIS331::X_AXIS`, `LIS331::Y_AXIS`, or `LIS331::Z_AXIS`. `trigLevel` can be `LIS331::TRIG_ON_HIGH` or `LIS331::TRIG_ON_LOW`, `interrupt` can be 1 or 2, and `enable` is `true` to enable the interrupt and `false` to disable it.

**`setIntDuration(duration, intSource)`** - `duration` can be any value from 0-127, and represents the time in number of samples that the sensor must read above or below the threshold set by the user. `intSource` is 1 or 2.

**`setIntThreshold(threshold, intSource)`** - `threshold` is the absolute magnitude above or below which an interrupt will occur, divided by 16. It can range from 0-127. `intSource` is 1 or 2.

## Examples

### Hardware Hookup

The H3LIS331DL supports I^2^C, SPI, and three-wire SPI data transfer. The library supports I^2^C and SPI mode. Obviously, since SPI requires four wires and I^2^C only requires two, there are different circuit configurations for each mode. Now would be a good time to [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) the female headers to the Arduino Pro 3.3V/8MHz and breakaway headers to the H3LIS331DL sensor before connecting the boards together.

#### I^2^C Mode

The board is labeled for I^2^C mode. Here you can see it connected to a 3.3V Arduino Pro. Note that connecting the board to a 5V Arduino can damage it.

[![I2C Mode circuit diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/8/i2c_circuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/i2c_circuit.png)

#### SPI Mode

In SPI mode, the SDA pin becomes MOSI, the SCL pin becomes clock, the address select pin SA0 become MISO, and the CS pin is used for chip select.

[![SPI Mode circuit diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/9/8/spi_circuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/9/8/spi_circuit.png)

### Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)\
\
You will also need FTDI drivers installed in order to upload code to the Arduino Pro. If this is your first time using an FTDI, make sure to follow our tutorial: [USB Serial Driver Quick Install](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-).

To follow along with the examples, the code requires the LIS331 Arduino library. Make sure that the library has been installed.

[SparkFun LIS331 Arduino Library](https://github.com/sparkfun/SparkFun_LIS331_Arduino_Library)

For the most part, the example code for SPI mode and I^2^C mode is identical. The only part that differs is the intial setup where you configure the pins to be used and the library\'s settings.

#### I^2^C Mode Setup

Here\'s an example of the same section of code from an I^2^C configured system. It\'s important to note that order matters here: `Wire.begin()` and `xl.setI2CAddr()` must be called before `xl.begin()`.

    language:c
    #include "SparkFun_LIS331.h"
    #include <Wire.h>

    LIS331 xl;

    void setup() 
    

    void loop() 
    
      if (digitalRead(9) == HIGH)
      
    }

After placing the code into the Arduino IDE, select the board definition and COM port to upload. Once compiled, check out the sensor readings by opening up a [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux) set to 115200 baud.