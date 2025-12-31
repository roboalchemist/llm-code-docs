# Source: https://learn.sparkfun.com/tutorials/piezo-vibration-sensor-hookup-guide

## Introduction

Piezo sensors are flexible devices that generate electric charge when they're stressed. This characteristic makes piezos an ideal solution for low-power flex, touch, and vibration sensing. In more advanced applications, piezos can be the foundation for energy harvesting. Piezo\'s are the perfect sensor for catching when your fridge is running or as the power source for [energy harvesting](https://www.sparkfun.com/products/9946) shake-lights.

[![Piezo Vibration Sensor - Small Horizontal](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/4/09198-03-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-small-horizontal.html)

### [Piezo Vibration Sensor - Small Horizontal](https://www.sparkfun.com/piezo-vibration-sensor-small-horizontal.html) 

[ SEN-09198 ]

The Minisense 100 from Measurement Specialties is a low-cost cantilever-type vibration sensor loaded by a mass to offer high ...

[ [\$14.95] ]

[![Piezo Vibration Sensor - Large](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/2/09196-Piezo_Vibration_Sensor_-_Large-03.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-large.html)

### [Piezo Vibration Sensor - Large](https://www.sparkfun.com/piezo-vibration-sensor-large.html) 

[ SEN-09196 ]

This basic piezo sensor from Measurement Specialties is often used for flex, touch, vibration and shock measurements. A small...

[ [\$9.95] ]

[![Piezo Vibration Sensor - Large with Mass](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/3/09197-02-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-large-with-mass.html)

### [Piezo Vibration Sensor - Large with Mass](https://www.sparkfun.com/piezo-vibration-sensor-large-with-mass.html) 

[ SEN-09197 ]

This basic piezo sensor from Measurement Specialties is often used for flex, touch, vibration and shock measurements. A small...

[ [\$10.95] ]

[![Piezo Vibration Sensor - Small Vertical](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/5/09199-03-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-small-vertical.html)

### [Piezo Vibration Sensor - Small Vertical](https://www.sparkfun.com/piezo-vibration-sensor-small-vertical.html) 

[ SEN-09199 ]

The Minisense 100 from Measurement Specialties is a low-cost cantilever-type vibration sensor loaded by a mass to offer high ...

[ [\$14.95] ]

Piezo\'s have the potential to produce very large AC voltage spikes \-- ranging upwards of ±50V. Because they produce such high voltages, large resistors are often used to "load down" the piezo sensor in vibration-sensing applications. [Zener diodes](https://www.sparkfun.com/products/10301) can also be used to clamp voltages down to safe levels.

### Suggested Materials

This tutorial serves as a quick primer on piezo vibration sensors, and demonstrates how to hook them up and use them. Beyond the sensor, the following materials are recommended:

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using the Arduino\'s analog-to-digital converter to read in the voltage produced by the piezo sensor. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Resistor Kit](https://www.sparkfun.com/products/10969)** \-- To dampen the piezo sensor\'s AC voltage spikes, a large load resistor \-- somewhere around 1MΩ \-- is used. This resistor kit includes multiple 1MΩ\'s, in case you want to combine a few in series.

**[Breadboard](https://www.sparkfun.com/products/12002) and [Jumper Wires](https://www.sparkfun.com/products/11026)** \-- The piezo sensor\'s legs are spaced by 0.2\" and are breadboard compatible. We\'ll stick them and the resistor into a breadboard, then use the jumper wires to connect from breadboard to Arduino.

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![SparkFun RedBoard - Programmed with Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/7/2/2/13975-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html)

### [SparkFun RedBoard - Programmed with Arduino](https://www.sparkfun.com/sparkfun-redboard-programmed-with-arduino.html) 

[ DEV-13975 ]

The SparkFun RedBoard combines the simplicity of the UNO\'s Optiboot bootloader, the stability of the FTDI, and the shield com...

[ [\$22.50] ]

[![Breadboard - Self-Adhesive (White)](https://cdn.sparkfun.com/r/140-140/assets/parts/8/5/0/3/12002-Breadboard_-_Self-Adhesive__White_-01.jpg)](https://www.sparkfun.com/breadboard-self-adhesive-white.html)

### [Breadboard - Self-Adhesive (White)](https://www.sparkfun.com/breadboard-self-adhesive-white.html) 

[ PRT-12002 ]

This is your tried and true white solderless breadboard. It has 2 power buses, 10 columns, and 30 rows - a total of 400 tie i...

[ [\$6.25] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

### Suggested Reading

Piezos are an great entry-level component for beginners, but there are still a few basic electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/analog-to-digital-conversion)

### Analog to Digital Conversion 

The world is analog. Use analog to digital conversion to help digital devices interpret the world.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Alternating Current (AC) vs. Direct Current (DC) 

Learn the differences between AC and DC, the history, different ways to generate AC and DC, and examples of applications.

## Vibration Sensor Overview

Piezo vibration sensors come in a variety of shapes and sizes. Here is a selection from the SparkFun catalog:

[![Piezo Vibration Sensor - Small Horizontal](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/4/09198-03-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-small-horizontal.html)

### [Piezo Vibration Sensor - Small Horizontal](https://www.sparkfun.com/piezo-vibration-sensor-small-horizontal.html) 

[ SEN-09198 ]

The Minisense 100 from Measurement Specialties is a low-cost cantilever-type vibration sensor loaded by a mass to offer high ...

[ [\$14.95] ]

[![Piezo Vibration Sensor - Large](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/2/09196-Piezo_Vibration_Sensor_-_Large-03.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-large.html)

### [Piezo Vibration Sensor - Large](https://www.sparkfun.com/piezo-vibration-sensor-large.html) 

[ SEN-09196 ]

This basic piezo sensor from Measurement Specialties is often used for flex, touch, vibration and shock measurements. A small...

[ [\$9.95] ]

[![Piezo Vibration Sensor - Large with Mass](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/3/09197-02-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-large-with-mass.html)

### [Piezo Vibration Sensor - Large with Mass](https://www.sparkfun.com/piezo-vibration-sensor-large-with-mass.html) 

[ SEN-09197 ]

This basic piezo sensor from Measurement Specialties is often used for flex, touch, vibration and shock measurements. A small...

[ [\$10.95] ]

[![Piezo Vibration Sensor - Small Vertical](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/4/5/09199-03-L.jpg)](https://www.sparkfun.com/piezo-vibration-sensor-small-vertical.html)

### [Piezo Vibration Sensor - Small Vertical](https://www.sparkfun.com/piezo-vibration-sensor-small-vertical.html) 

[ SEN-09199 ]

The Minisense 100 from Measurement Specialties is a low-cost cantilever-type vibration sensor loaded by a mass to offer high ...

[ [\$14.95] ]

Some piezo sensor\'s include weights at the end to help encourage vibration.

### AC Voltage Source

Piezo sensors are unique because they produce an [alternating current](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc#alternating-current-ac) (AC) voltage when stressed, converting mechanical energy to electrical. If you hooked an [oscilloscope](https://learn.sparkfun.com/tutorials/how-to-use-an-oscilloscope) up to a piezo sensor, you might see waveforms like this when the sensor shakes:

[![Piezo flicked, unloaded](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/5/piezo-screen-2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-screen-2.png)

The signals above were generated by simply inserting a [large, weighted piezo](https://www.sparkfun.com/products/9197) into a breadboard and flicking it a few times. Note the voltage spikes are reaching almost +20V and -12V. Signals at that level have the potential to permanently damage a microcontroller\'s analog-to-digital converter (ADC) pins.

To dampen those voltage spikes, we have a few simple tricks up our sleeve. The easiest fix is to **load the piezo** with a large resistor. By placing a 1MΩ resistor in parallel with the sensor, for example, we can drop the voltage spikes down to safer levels.

[![Piezo sensor loaded with 1M, connected to ADC](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/5/piezo-screen-loaded-adc-1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-screen-loaded-adc-1.png)

In the graph above, the sensor is loaded with a 1MΩ resistor and connected to an Arduino ADC. The voltages spike between -0.5 and +5V are safely within the tolerable range of the ATmega328\'s I/O pins.

More complex piezo damping circuits might include [zener diodes](https://www.sparkfun.com/products/10301) to clamp the voltage or [op amps](https://www.sparkfun.com/products/9456) to buffer a signal, but this simple resistor-loading circuit is a good place to start.

## Example Circuit

Using the 1MΩ load resistor dampening method described above, here\'s a simple example circuit demonstrating how to hook up the vibration sensor:

[![Piezo hookup example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/5/example-circuit_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/example-circuit_bb.png)

The Piezo is grounded on one end, and a generated voltage is routed to the Arduino\'s A0 ADC pin. Reading the voltage at that pin should give us an idea of how much the piezo is moving.

## Example Code

Here is a really simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

    language:c
    /******************************************************************************
    Piezo_Vibration_Sensor.ino
    Example sketch for SparkFun's Piezo Vibration Sensor
      (https://www.sparkfun.com/products/9197)
    Jim Lindblom @ SparkFun Electronics
    April 29, 2016

    - Connect a 1Mohm resistor across the Piezo sensor's pins.
    - Connect one leg of the Piezo to GND
    - Connect the other leg of the piezo to A0

    Vibrations on the Piezo sensor create voltags, which are sensed by the Arduino's
    A0 pin. Check the serial monitor to view the voltage generated.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int PIEZO_PIN = A0; // Piezo output

    void setup() 
    

    void loop() 
    

Once the circuit is set up and code is uploaded, **open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**, and set the baud rate to 9600 bps.

You should be seeing 0.00\'s stream by endlessly. Try shaking the sensor to see the voltages go up.

[![Serial terminal](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-arduino-serial.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-arduino-serial.png)

Your eye\'s probably aren\'t fast enough to catch all of those numbers change. You can either introduce a delay to the end of the loop (e.g. `delay(250);`), or you can view the output in the **serial plotter**, found in newer versions of the Arduino IDE. Open the plotter by going to **Tools** \> **Serial Plotter**.

[![Serial plotter](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-arduino-graph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/5/piezo-arduino-graph.png)

Now, you can create oscilloscope measurements of your own! The graph helps demonstrate the piezo sensor\'s voltage spikes and ringing. Try flicking, shaking, or stomping the ground to see how those movements affect the measurements of the piezo sensor.

Once you\'ve gotten a handle on that, you can find a \"vibration threshold\" that will fit your project needs and have your Arduino look for any measurements above that value to detect vibrations.