# Source: https://learn.sparkfun.com/tutorials/vl6180-hookup-guide

## Introduction

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/7/Combined_ISO.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/Combined_ISO.png)

The [VL6180](https://www.sparkfun.com/products/12785) is a Time of Flight (TOF) distance sensor with an I^2^C (\"Wire\") interface. This Hookup Guide will cover two boards. The [VL6180 Breakout](https://www.sparkfun.com/products/12784) and the [VL6180 Sensor](https://www.sparkfun.com/products/12785). These boards are very similar in function though the [VL6180 Sensor](https://www.sparkfun.com/products/12785) has additional hardware for level shifting and voltage regulation.

Many distance sensors rely on reflected light intensity or reflected angles to determine range. This sensor uses a precise clock to measure the time it takes light to bounce back from a surface. This is a great benefit over other methods because it can be much more accurate and more immune to noise. This sensor is commonly found in cellphones as the sensor that detects when the caller is holding their phone to their ear.

### Covered in this Tutorial

We will show you how to connect this sensor to an Arduino microcontroller and use the included software library to get measurements out of the sensor. (If you\'re using a different type of microcomputer these instructions and source code may still help.)

### Suggested Reading

This part is easy to use. But before you start, we recommend the following background knowledge:

- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)
- [Working with Wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [Logic Levels](https://learn.sparkfun.com/tutorials/logic-levels)
- [What is an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [\"Wire\" (I^2^C) Communications](https://learn.sparkfun.com/tutorials/i2c)

## Board Overview - VL6180 Breakout

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/BreakoutAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/BreakoutAnnotated.png)

*VL6180 Breakout Diagram*

The VL6180 Breakout is as simple as it gets. Only the required passives are populated to give users the smallest, most cost effective way to use multiple sensors in a project.

- Pull-up Enable - Defaulted to enable, two required pull-up resistors are attached to the I^2^C lines. Remove solder jumper on all but one unit if using multiple sensors on the same bus.
- VL6180 Sensor - The sensor by itself is very small, only passive components are necessary to complete the circuit.

*NOTE: This device only accepts 2.8V input and logic. You must provide a 2.8V voltage source and level shifting to 3.3V and 5V devices.*

## Board Overview - VL6180 Sensor

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/7/SensorBlockDiagramAnnotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorBlockDiagramAnnotated.png)

*VL6180 Sensor Diagram*

The VL6180 Sensor is very similar to the VL6180 Breakout with some noted additions.

- 2.8V Regulator - Provides the required 2.8V for the sensor
- I^2^C level shifter - Provides logic level conversion from 2.8V to VCC (provided by the user)
- Pull-up Enable - Defaulted to enable, two required pull-up resistors are attached to the I^2^C lines. Remove solder jumper if using multiple sensors on the same bus.
- VL6180 Sensor

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorComparison_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorComparison_1.png)

*VL6180 Sensor and [Sharp GP2Y0A41SK0F](https://www.sparkfun.com/products/12728) Comparison*

Another thing to note is the form factor of the sensor itself. Many small robotics platforms have integrated hole patterns for the long time favorite Sharp IR sensor line. This allows the VL6180 Sensor to be a near drop-in replacement for most Sharp sensors.

## Connecting the Hardware

### Using the VL6180 Breakout

To use the VL6180 Breakout, follow the diagram below. One important thing to note is you **MUST** use a [3.3v Pro-Mini](https://www.sparkfun.com/products/11114) for this to work. We are cheating the 2.8v Level shifting rules in this hookup. Since I^2^C is an active low signal, we will use the pull-up resistors on the breakout to provide our logic voltage. We have a great [I^2^C tutorial](https://learn.sparkfun.com/tutorials/i2c) that explains this in more detail. To provide the required 2.8V we are using an [LM317 regulator](https://www.sparkfun.com/products/527). The output voltage is tuned to 2.8V with the two resistors shown.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/WiringDiagramBreakout.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/WiringDiagramBreakout.png)

*Wiring Diagram for VL6180 Breakout and 3.3v Pro-Mini*

NOTE: To use this diagram make sure the two pull-up resistors on the Pro-Mini are NOT populated.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/7/pro-mini_annotated.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/pro-mini_annotated.png)

*Unpopulated Pro-Mini Pull-ups*

### Using the VL6180 Sensor

To use the Sensor version of the VL6180, things are much simpler. The board carries its own level shifting and regulation. The VL6180 Sensor can work with 3.3-5V Logic and power.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorHookupDiagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorHookupDiagram.png)

## Library Install and Sample Sketch

To use either the VL6180 Sensor or Breakout, you will need some supporting software. If you are using an Arduino, then you are in luck! We created an Arduino library that makes the VL6180 easy to use. Click the button below to download the latest version of the VL6180 Library.

[Download the Arduino Library!](https://github.com/sparkfun/SparkFun_VL6180_Time_of_Flight_Library/archive/master.zip)

Unzip the downloaded file and navigate to \\\\SparkFun_VL6180_Time_of_Flight_Library-master.zip\\SparkFun_VL6180_Time_of_Flight_Library-master\\Libraries.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/5/7/LibraryInstall.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/LibraryInstall.PNG)

Follow [this guide on installing Arduino libraries](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) to install the files within the SFE_VL6180x directory as an Arduino library.

There is a sample sketch associated with the Library. VL6180X_demo reads the distance and light outputs and reports them to the screen.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/Demo.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/Demo.png)

*Demo Program Found in Examples*

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorExampleProgram.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/2/5/7/SensorExampleProgram.PNG)

*Demo Program Output*