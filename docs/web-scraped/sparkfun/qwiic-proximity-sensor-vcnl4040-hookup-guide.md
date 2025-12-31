# Source: https://learn.sparkfun.com/tutorials/qwiic-proximity-sensor-vcnl4040-hookup-guide

## Introduction

The [Qwiic Proximity Sensor](https://www.sparkfun.com/products/15177) is a simple IR presence and ambient light sensor utilizing the [VCNL4040](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf). This sensor is excellent for detecting if something has appeared in front of the sensor; detecting objects qualitatively up to **20cm** away. This means you can detect if something is there, and if it is closer or further away since the last reading, but it's difficult to say it is 7.2cm away. If you need quantitative distance readings for exact distances, check out the SparkFun [2 meter](https://www.sparkfun.com/products/14539) and [4 meter](https://www.sparkfun.com/products/14722) Time of Flight (ToF) sensors with mm accuracy.

[![SparkFun Proximity Sensor Breakout - 20cm, VCNL4040 (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/9/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-proximity-sensor-breakout-20cm-vcnl4040-qwiic.html)

### [SparkFun Proximity Sensor Breakout - 20cm, VCNL4040 (Qwiic)](https://www.sparkfun.com/sparkfun-proximity-sensor-breakout-20cm-vcnl4040-qwiic.html) 

[ SEN-15177 ]

The SparkFun Proximity Sensor Breakout is a simple IR presence and ambient light sensor utilizing the VCNL4040.

[ [\$4.95] ]

We often see this type of sensor on automatic towel dispensers, automatic faucets, etc. However, the VCNL4040 has **no dead zone** and can read all the way up to the face of the sensor. The SparkFun Proximity VCNL4040 sensor is a great digital alternative to the popular analog [PIR sensors](https://www.sparkfun.com/products/13968). The [Qwiic Proximity Sensor](https://www.sparkfun.com/products/15177) also has an ambient light sensor built it which is excellent if you need a digital light sensor for your next glitter cannon.

This board is one of our many Qwiic compatible boards! Simply plug and go. No soldering, no figuring out which is SDA or SCL, and no voltage regulation or translation required!

### Required Materials

The Qwiic Proximity Sensor does need a few additional items for you to get started. *You may already have a few of these items, so feel free to modify your cart as necessary.*

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

### Suggested Reading

If you\'re unfamiliar with jumper pads or I^2^C be sure to checkout some of these foundational tutorials.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces)

### How to Work with Jumper Pads and PCB Traces 

Handling PCB jumper pads and traces is an essential skill. Learn how to cut a PCB trace, add a solder jumper between pads to reroute connections, and repair a trace with the green wire method if a trace is damaged.

[![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)

The Qwiic Proximity Sensor utilizes the [Qwiic connect system](https://www.sparkfun.com/qwiic). We recommend familiarizing yourself with the **Logic Levels** and **I^2^C** tutorials (above) before using it. Click on the banner above to learn more about our [Qwiic products](https://www.sparkfun.com/categories/399).

## Hardware Overview

**Note:** If you want to do anything outside of what is covered in this tutorial or the example code, please refer to the [VCNL4040 datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf) for exact details on the sensor functionality.

### Power LED

There is a power status LED to help make sure that your Qwiic Joystick is getting power. You can power the board either through the *polarized* **Qwiic connector** system or the **breakout pins** (**PWR** and **GND**) provided. This Qwiic system is meant to use **3.3V**, be sure that you are **NOT** using another voltage when using the Qwiic system.

[![Power LED](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/PowerLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/PowerLED.jpg)

### VCNL4040 Sensor

The VCNL4040 is a **proximity sensor** (PS), **ambient light sensor** (ALS), and a high power **IR emitter** (IRED) integrated into a single package. The ambient light sensor and proximity sensor operate in a parallel structure. The combination of the two sensors along with the IR emitter form the proximity detector.

[![VCNL4040 Sensor](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/VCNL4040Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/VCNL4040Sensor.jpg)

The sensor has an operating voltage range from **2.5V** to **3.6V**. It is recommended that you use this board with the intended **3.3V** of the Qwiic connect system. The VCNL4040 also includes excellent temperature compensation. For any details not covered in this guide, please refer to the [datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf).

**Note:** This sensor is excellent for detecting qualitative changes (if an object is there or moved since the last reading). If you need quantitative distance readings, like exact distances, check out the SparkFun [2 meter](https://www.sparkfun.com/products/14539) and [4 meter](https://www.sparkfun.com/products/14722) Time of Flight (ToF) sensors with mm accuracy.

#### IR Emitter

The IR emmiter is immune to red glow with a **940 nm** wavelength (for those discrete applications) and the sink current is programmable (**200 mA default**). For more details on the IR emitter, please refer to the [datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf).

#### Ambient Light Sensor (ALS)

The VCNL4040 offers a **16-bit** high resolution ALS with ±10 % accuracy and is immune to fluorescent light flicker. With an ambient light sensing capability down to 0.01 lux/step, the VCNL4040 works well under a low transmittance lens design (dark lens). In addition, the patented FiltronTM technology offers great background light cancellation capability (including sunlight) without utilizing microcontroller resources.

#### Proximity Sensor (PS)

The proximity sensor features smart persistence, which prevents the misjudgment of proximity sensing but also keeps a fast response time. In active force mode, a single measurement can be requested for more design flexibility and/or power saving.

### Qwiic or I^2^C

#### I^2^C Address

The sensor has a single slave address **0x60** (HEX) of 7-bit addressing, following I^2^C protocol.

#### Connections

The simplest way to use the Qwiic Proximity Sensor is through the Qwiic connect system. The connectors are polarized for the I^2^C connection and power. (*\*They are tied to their corresponding breakout pins.*)

[![Qwiic Connectors](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/QwiicConnectors.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/QwiicConnectors.jpg)

However, the board also provides five labeled breakout pins. You can connect these lines to the I^2^C bus of your microcontroller and power pins (**3.3V** and **GND**), if it doesn\'t have a Qwiic connector. The interrupt pin is broken out to use for triggered events.

[![Breakout Pins](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/BreakoutPins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/BreakoutPins.jpg)

#### Interrupt Pin

High and low interrupt thresholds can be programmed for both the ambient light sensor and proximity sensor, allowing the component to use a minimal amount of the microcontrollers resources. Adjustable persistence sets up the amount of consecutive hits required before an interrupt event occurs, to prevent false triggers.\
\
The VCNL4040 also supports an easy to use proximity detection logic mode, that triggers when the PS high threshold is exceeded and automatically resets the interrupt pin when the proximity reading falls beneath the PS low threshold.\
\
An interrupt can be cleared by reading data out from the **INT_Flag register** (resetting it to \"0\") and the INT pin is then reset to high. For more details on the interrupt, please refer to the [datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf).

##### Interrupt Jumper

Cutting the **INT** jumper will remove the **10 kΩ** pull-up resistor from the INT pin.

[![Interrupt Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/InterruptJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/InterruptJumper.jpg)

#### I^2^C Pull-up Jumper

Cutting the **I^2^C** jumper will remove the **2.2 kΩ** pull-up resistors from the I^2^C bus. If you have many devices on your I^2^C bus you may want to remove these jumpers. Not sure how to cut a jumper? [Read here!](https://learn.sparkfun.com/tutorials/how-to-work-w-jumper-pads-and-pcb-traces/cutting-a-trace-between-jumper-pads)

[![Pull-up Jumper](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/PullupJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/PullupJumper.jpg)

## Hardware Assembly

With the Qwiic connector system, assembling the hardware is simple. All you need to do is connect your Qwiic Proximity Senor to the RedBoard Qwiic with a Qwiic cable. Otherwise, you can use the I^2^C pins, if you don\'t have a Qwiic connector on your microcontroller board. Just be aware of your input voltage and any logic level shifting you may need to do.

[![Hardware connection](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/4/Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Assembly.jpg)

## Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

We've written an Arduino library to flex every feature of this sensor. You can grab it from the Arduino Library Manager by searching for **\'SparkFun VCNL4040\'**. Otherwise you can get it from the [GitHub repository](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library) or use the download button below.

[DOWNLOAD THE VCNL4040 LIBRARY (ZIP)](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library/archive/master.zip)

### Library Functions

The Arduino library is commented and the functions should be self-explanatory. However, below is a detailed list of the available library functions.

**Note:** It is recommended that users begin with the examples in the following section before diving head first into the library functions. The library examples demonstrate how to setup the more basic features of the VCNL4040 without having to dig through the datasheet. Once users have become familiar with the basic setups and have gone through the [datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf) thoroughly, it should be easier to follow the [library functions](https://github.com/sparkfun/SparkFun_VCNL4040_Arduino_Library/blob/master/src/SparkFun_VCNL4040_Arduino_Library.cpp) below.

`.begin` - Check communication with sensor and set it to default I^2^C Wire library settings\

`.isConnected` - Checks connection

`.setLEDCurrent` - Sets the IR LED sink current to one of 8 settings (75, 100, 120, 140, 160, 180, and 200 mA).

`.setIRDutyCycle` - Sets duty cycle of the IR LED (40 max.)

`.setProxInterruptPersistance` - Sets the Prox interrupt persistance value.\
[The PS persistence function (PS_PERS, 1, 2, 3, 4) helps to avoid false trigger of the PS INT. It defines the amount of consecutive hits needed in order for a PS interrupt event to be triggered.] `.setAmbientInterruptPersistance` - Sets the Ambient interrupt persistance value\
[The ALS persistence function (ALS_PERS, 1, 2, 4, 8) helps to avoid false trigger of the ALS INT. It defines the amount of consecutive hits needed in order for a ALS interrupt event to be triggered.]

`.setProxIntegrationTime` - Sets the integration time for the proximity sensor\
`.setAmbientIntegrationTime` - Sets the integration time for the ambient light sensor

`.powerOnProximity` - Power on the prox sensing portion of the device\
`.powerOffProximity` - Power off the prox sensing portion of the device

`.powerOnAmbient` - Power on the ALS sensing portion of the device\
`.powerOffAmbient` - Power off the ALS sensing portion of the device

`.setProxResolution` - Sets the proximity resolution to 12 or 16 bit

`.enableAmbientInterrupts` - Enables ALS interrupt\
`.disableAmbientInterrupts` - Disables ALS interrupt

`.enableSmartPersistance` - Turn on smart presistance\
`.disableSmartPersistance` - Turn off smart presistance\
[To accelerate the PS response time, smart persistence prevents the misjudgment of proximity sensing, but also keeps a fast response time.]

`.enableActiveForceMode` - Enables active force mode\
`.disableActiveForceMode` - Disable active force mode\
[An extreme power saving way to use PS is to apply PS active force mode. Anytime host would like to request one proximity measurement, enable the active force mode. This triggers a single PS measurement, which can be read from the PS result registers. VCNL4040 stays in standby mode constantly.]

`.takeSingleProxMeasurement` - Sets trigger bit so sensor takes a force mode measurement and returns to standby.

`.enableWhiteChannel` - Enables the white measurement channel\
`.disableWhiteChannel` - Disables the white measurement channel

`.enableProxLogicMode` - Enables the proximity detection logic output mode\
`.disableProxLogicMode` - Disables the proximity detection logic output mode\
[When this mode is selected, the INT pin is pulled low when an object is close to the sensor (value is above high threshold) and is reset to high when the object moves away (value is below low threshold). Register: PS_THDH / PS_THDL define where these threshold levels are set.]

`.setProxCancellation` - Sets the proximity sensing cancellation value - helps reduce cross talk with ambient light

`.setALSHighThreshold` - Value that ALS must go above to trigger an interrupt\
`.setALSLowThreshold` - Value that ALS must go below to trigger an interrupt

`.setProxHighThreshold` - Value that Proximity Sensing must go above to trigger an interrupt\
`.setProxLowThreshold` - Value that Proximity Sensing must go below to trigger an interrupt

`.getProximity` - Read the Proximity value\
`.getAmbient` - Read the Ambient light value\
`.getWhite` - Read the White light value\
`.getID` - Read the sensors ID

`.setProxInterruptType` - Enable four proximity interrupt types\
[ `.isClose` - Interrupt flag: True if prox value greater than high threshold\
`.isAway` - Interrupt flag: True if prox value lower than low threshold\
`.isLight` - Interrupt flag: True if ALS value higher than high threshold\
`.isDark` - Interrupt flag: True if ALS value lower than low threshold ]

`.readCommand` - Reads two consecutive bytes from a given \'command code\' location\
`.writeCommand` - Write two bytes to a given command code location (8 bits)

## Arduino Examples

**Note:** This section is an example of using the Qwiic Proximity Sensor and the RedBoard Qwiic with the Arduino IDE. It is not intended to be a guide for using I^2^C devices with the Arduino IDE.\
\
Please use the following links and the internet for a better understanding of I^2^C and how it works in the Arduino IDE:

- A [tutorial on I^2^C](https://learn.sparkfun.com/tutorials/i2c/all).
- An [in-depth overview](https://playground.arduino.cc/Main/WireLibraryDetailedReference) of the [Wire (I^2^C) library](https://www.arduino.cc/en/reference/wire).

### Example 1: Proximity Readings

This example outputs the IR Proximity Value from the VCNL4040 sensor in the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics).

[![Serial output of proximity values](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example1.PNG)

Despite being a qualitative sensor, you will notice that the output does vary with the distance of the object, surface color, and reflectivity. You can also use this setting to estimate the field of view of the sensor. The maximum output value is 65535, closest to the sensor, and the minimum (0-1) being the furthest the sensor can read.

### Example 2: Is Something There

This example takes an initial reading at power on. If the reading changes by a significant amount the sensor prints that something is present in the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics).

[![Serial output of proximity detection](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example2.PNG)

This example also allows the proximity sensor to work as a dual purpose *photogate*.

[![Hot wheels car triggering proximity sensor](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/RaceCarDemo.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/RaceCarDemo.gif)

*A Hot Wheels^TM^ car triggering proximity sensor.*\
*(\*The speed of the Gif is slowed down for you to see the output in the Serial Monitor.)*

There is a slight delay in the serial output from the microcontroller (few frames); however, this is exaggerated due to how the image is slowed down.

### Example 3: Ambient Light

This example outputs ambient light readings to the [terminal](https://learn.sparkfun.com/tutorials/terminal-basics).

[![Serial output of ambient light values](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example3.PNG)

Again the sensor is qualitative, but you can test how the angle of incident from the light source affects the sensor readings.

### Example 4: All Readings

This example outputs IR, ambient and white light readings to the terminal. Along with proximity and ambient light sensing the VCNL4040 has a \'white light\' sensor as well.

[![Serial output of all values](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/4/Example4.PNG)

### Example 5: Advanced Settings

This example shows how to use different Wire ports, fast I^2^C, and various advanced settings that are supported by the library. Please, refer to the [datasheet](https://cdn.sparkfun.com/assets/2/3/8/f/c/VCNL4040_Datasheet.pdf) and library functions listed above for more details.