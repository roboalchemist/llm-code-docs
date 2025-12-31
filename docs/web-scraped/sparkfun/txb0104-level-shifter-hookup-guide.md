# Source: https://learn.sparkfun.com/tutorials/txb0104-level-shifter-hookup-guide

## Introduction

The [TXB0104](https://www.sparkfun.com/products/11771) is a bi-directional signal level shifter made by Texas Instruments. It features four channels of input/output signals and an output enable line that allows the signal lines to be placed in a high impedance mode when they are unneeded.

[![SparkFun Voltage-Level Translator Breakout - TXB0104](https://cdn.sparkfun.com/r/600-600/assets/parts/8/0/0/6/11771-01.jpg)](https://www.sparkfun.com/sparkfun-voltage-level-translator-breakout-txb0104.html)

### [SparkFun Voltage-Level Translator Breakout - TXB0104](https://www.sparkfun.com/sparkfun-voltage-level-translator-breakout-txb0104.html) 

[ BOB-11771 ]

This is a breakout board for the Texas Instruments TXB0104 module. The TXB0104 is a 4-bit bidirectional voltage-level transla...

[ [\$5.95] ]

Depending on the high and low side voltages, the bandwidth on the individual signal channels can range from 20Mbps up to 100Mbps, making the TXB0104 suitable for higher speed signals such as SPI.

SparkFun\'s [TXB0104 breakout board](https://www.sparkfun.com/products/11771) makes it easy to use this powerful chip in your projects.

#### Suggested Reading

Before going further with this guide, you should be familiar with the topics covered in these tutorials:

[](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)

### Serial Peripheral Interface (SPI) 

SPI is commonly used to connect microcontrollers to peripherals such as sensors, shift registers, and SD cards.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

## TXB0104 BOB Overview

[![Labeled image of the TXB0104 BOB](https://cdn.sparkfun.com/r/600-600/assets/6/4/4/b/5/522e1872757b7ff85a8b4569.png)](https://cdn.sparkfun.com/assets/6/4/4/b/5/522e1872757b7ff85a8b4569.png)

The TXB0104 breakout board is pretty simple. There are two rows of pin headers, one down each side of the board; one side for the high voltage signals and one for the low voltage signals.

- The **output enable jumper** (1) is closed by default, causing the signals on both sides to be driven at all times. It\'s up to the user to ensure (as is usually the case) that the system avoid bus contention states where the high side and low side of the same signal are being driven to opposite levels.
- **B-side signals** (2) are the high voltage signals. VccB *must* be at a higher voltage than VccA to avoid total protonic reversal (or at least, to avoid possible damage to the chip). The voltage range for VccB is 1.65 to 5.5V. If driving the OE pin from the high-voltage device, please insert a 1k resistor in series with the drive signal.
- **A-side signals** (3) are the low voltage signals. VccA *must* be at a lower voltage than VccB. The voltage range for VccA is 1.2V to 3.6V.

## Example: Connecting ADXL345 to Arduino

[![Example hook-up diagram](https://cdn.sparkfun.com/r/600-600/assets/8/7/1/2/b/522e274b757b7f78358b4569.png)](https://cdn.sparkfun.com/assets/8/7/1/2/b/522e274b757b7f78358b4569.png)

The image above shows how to use the TXB01014 BOB to connect an Arduino Uno to SparkFun\'s [ADXL345 breakout board](https://www.sparkfun.com/products/9836). The ADXL345 board is a 3.3V system, and the Arduino Uno is a 5V system, so some level shifting is required.

In this case, we\'re leaving the OE pin tied high as it defaults; there\'s no real need to make the pins high impedance for this application.

There is no need for changes in software to support the TXB0104; the chip will automatically detect the signal direction and pass the data through accordingly.