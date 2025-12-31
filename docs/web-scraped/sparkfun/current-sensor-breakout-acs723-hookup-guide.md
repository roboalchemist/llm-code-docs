# Source: https://learn.sparkfun.com/tutorials/current-sensor-breakout-acs723-hookup-guide

## Introduction

**Note:** This tutorial is for the ACS723 breakout boards. If you are using either of the ACS712 breakout boards, please refer to the older [ACS712 Low Current Sensor Hookup Guide](https://learn.sparkfun.com/tutorials/acs712-low-current-sensor-hookup-guide).

The ACS723 is a handy little current sensor from Allegro MicroSystems for low to moderate current sensing applications. SparkFun offers two flavors of breakout board, [one with just the sensor](https://www.sparkfun.com/products/13679) and [another with an on-board amplifier](https://www.sparkfun.com/products/14544) to increase the sensitivity.

[![SparkFun Current Sensor Breakout - ACS723](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/1/3/1/13679-SparkFun_Current_Sensor_Breakout_-_ACS723-01.jpg)](https://www.sparkfun.com/sparkfun-current-sensor-breakout-acs723.html)

### [SparkFun Current Sensor Breakout - ACS723](https://www.sparkfun.com/sparkfun-current-sensor-breakout-acs723.html) 

[ SEN-13679 ]

The SparkFun Current Sensor Breakout is a high accuracy board that utilizes the ACS723 for moderate AC and DC current sensing...

[ [\$13.46] ]

[![SparkFun Current Sensor Breakout - ACS723 (Low Current)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/6/6/7/14544-SparkFun_Current_Sensor_Breakout_-_ACS723__Low_Current_-01.jpg)](https://www.sparkfun.com/sparkfun-current-sensor-breakout-acs723-low-current.html)

### [SparkFun Current Sensor Breakout - ACS723 (Low Current)](https://www.sparkfun.com/sparkfun-current-sensor-breakout-acs723-low-current.html) 

[ SEN-14544 ]

The low current version of the SparkFun Current Sensor Breakout is a high accuracy board that utilizes the ACS723 for low to ...

[ [\$19.95] ]

The ACS723 sensor uses a Hall effect sensor to output a voltage relative to the current flowing through the IP+ and IP- pins. The advantage of using a Hall effect sensor is that the circuit being sensed and the circuit reading the sensor are *electrically isolated*. This means that, although your Arduino is running on 5V, the sensed circuit can be operating at higher DC or AC voltages!

The amplified breakout board (Low Current) is capable of sensing very small currents down to around 10mA and large currents up to 5A! However, since the output is analog, your usable readings will be limited by noise and the resolution of the ADC reading the output. This sensor is not recommended for current sensing lower than 10\'s of milliamps.

### Required Materials

Depending on the equipment available to you, you will need some of the following items to follow along with this hookup guide:

### Suggested Reading

Here are some topics related to this hookup guide you may want to review:

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/how-to-power-a-project)

### How to Power a Project 

A tutorial to help figure out the power requirements of your project.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

[](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)

### Series and Parallel Circuits 

An introduction into series and parallel circuits.

[](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Alternating Current (AC) vs. Direct Current (DC) 

Learn the differences between AC and DC, the history, different ways to generate AC and DC, and examples of applications.

[](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)

### How to Use a Multimeter 

Learn the basics of using a multimeter to measure continuity, voltage, resistance and current.

There\'s also a great tutorial from Shawn Hymel explaining electromagnetism and magnets:

## The Hall Effect and Current Sensors

This section provides a quick recap of the electromagnetic concepts that make this current sensor possible. How does this little chip take current from one circuit and produce a proportional output voltage without physically connecting the two circuits?

### Faraday\'s Law of Induction

In the ACS723, sensing current starts with the phenomenon known as Faraday\'s Law of Induction. This phenomenon, first discovered by Michael Faraday in 1831, is one of the foundations of modern radio and electromagnetics. This law describes how an electrical current flowing in a conductor creates a surrounding magnetic field, and how a changing magnetic field can create, or *induce*, a current in a conductor. This is how antennas pick up radio waves!

![Faraday\'s Law](http://www.tesla-institute.com/images/art_004/Faradays%20Law%20of%20Electromagnetic%20Induction_02_TESLA%20Institute.jpg "Faraday's Law Image")

*Illustration of the magnetic field created around a conductor with a current flowing through it (Photo courtesy of the [Tesla Institute](http://www.tesla-institute.com))*

The current pins of the ACS723 are internally connected to a big trace of copper, allowing a lot of electricity to flow through this part of the chip. When current flows through the copper strip, a magnetic field is created around the trace with a strength proportional to the current.

### The Hall Effect

The next step in sensing current is based on the Hall effect - a very useful phenomenon discovered by Edwin Hall in 1879. In basic terms, the Hall effect produces a voltage difference across a conductor in the presence of a magnetic field. This provides a neat way of sensing nearby magnetic fields and has many applications. For example, Hall effect sensors are used in some car engines to detect where in a rotation cycle the camshaft or crankshaft are.

![Hall Effect Animation](http://cdn4.explainthatstuff.com/hall-effect-animation.gif "Hall Effect Animation")

*Animation showing how a magnetic field creates a voltage difference. The blue circles are electrons flowing (Photo courtesy of [Explain that Stuff](http://www.explainthatstuff.com/hall-effect-sensors.html))*

The ACS723 has an internal Hall effect sensor placed next to the aforementioned copper strip. When current flows through this copper strip, a magnetic field is created. This magnetic field is then sensed by the Hall effect sensor and produces a voltage output that is proportional to the input current!

[![Hall Effect current sensor](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/hall-effect-cs.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/hall-effect-cs.jpg)

*Illustration of how the current sensor looks internally (Photo courtesy of [Allegro Micro](https://www.allegromicro.com/))*

This method of sensing allows the sensing circuit to be *electrically isolated* from the sensed circuit. Practically, this means that since the circuits aren\'t physically connected, you can use a low-power Arduino to measure the current going through a high power device, even one that uses AC power!

## Hardware Overview

This section will explore the various segments of the breakout with particular emphasis on the Low Current version.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/13679-SparkFun_Current_Sensor_Breakout_-_ACS723_-03.jpg "ACS 723 Breakout Board closeup")](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/13679-SparkFun_Current_Sensor_Breakout_-_ACS723_-03.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/14544-SparkFun_Current_Sensor_Breakout_-_ACS723__Low_Current_-02.jpg "ACS723 Low Current Breakout Board closeup")](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/14544-SparkFun_Current_Sensor_Breakout_-_ACS723__Low_Current_-02.jpg)\

  *ACS723 Breakout Board closeup*                                                                                                                                                                                                                                        *ACS723 Low Current Breakout Board closeup*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### ACS723 Breakout Details:

Both versions of this breakout board have the following attributes:

- **Analog output** with bandwidth adjustable to 80kHz.
- The bandwidth on the ACS723 Sensor Breakout width filter has been set to 20kHz to reduce noise when using at high gains. The full 80KHz bandwidth that the sensor is capable of can be recovered by closing the JP1 (Bandwidth Select) jumper on the back of the board. See either the [ACS723 schematic](https://cdn.sparkfun.com/assets/c/f/4/a/1/SparkFun_ACS723_Current_Sensor_Breakout.pdf) or the [ACS723 Low Current schematic](https://cdn.sparkfun.com/assets/2/3/c/8/7/ACS723_Low_Current_Sensor.pdf) for more details.
- Measures DC and AC currents from around **10mA up to 5A**
- Full electrical isolation of measured and sensed circuits
- The version without the op-amp has a base sensitivity of 400mV/A

In addition to the above, the Low Current Sensor Board has the following:

- Adjustable sensitivity with on-board amplifier, gain from **2.2** to **22 V/V**

[] **Please Note:** Although the chip itself is rated for up to **2.4kV** (RMS) of isolation, the board has not been designed for such high voltage applications.

Below is a list of all the pins broken out on the ACS723 and their functions.

  Symbol   Description
  -------- --------------------------------------------------------------------
  IP+      High side of current sensor
  IP-      Low side of current sensor
  GND      Must be connected to ground
  Vo       Voltage output proportional to current flowing through IP+ and IP-
  VCC      **5V** power supply

To measure a current using this device, the current must flow through the IP+ terminal and out the IP- terminal (it will work in the other direction, but the measurement will be negative). IE: These terminals must be *in series* with the circuit that the measured current is flowing through. Note that both IP+ and both IP- terminals are connected to each other, you can use either (or both) of them.

### Amplification (Low Current Sensor):

The amplified version of the breakout board [(ACS723-Low Current)](https://www.sparkfun.com/products/14544) has two potentiometers on it: ***Vref*** and ***Gain***.

The **Vref potentiometer** sets the baseline voltage output. In other words, it adjusts the voltage seen at Vo when there is no current flowing through the sensor (0 mA). This allows the sensor to output negative current readings as well as positive.

[![ACS723 Vref Potentiometer](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/Low_Current_Vref2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/Low_Current_Vref2.jpg)

*Vref potentiometer, highlighted*

The **gain potentiometer** sets the sensitivity of the device. For example, if the gain is set high, then a smaller current will cause the voltage output to increase more, giving you higher sensitivity and allowing you to sense smaller currents.

[![ACS723 Gain Potentiometer](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/Low_Current_Gain.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/Low_Current_Gain.jpg)

*Gain potentiometer, highlighted*

**However,** there are a couple caveats:

1.  With higher gain you will see more noise (spikes) on the output, so smaller currents will be harder to measure accurately.
2.  If you are trying to measure larger currents with a high gain setting, your output will **saturate** or **clip** and reach the maximum 5V or 0V.

With that in mind, to get meaningful data from the current sensor, you must configure the *Vref* and *Gain* potentiometers properly.

## Calibration and Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

An example sketch for Arduino is included below to help you get started with the ACS723 Low Current Sensor. It will help you set the potentiometers and perform calculations to convert raw ADC readings into the actual current in mA. While parts are specific to the ACS723 Low Current Sensor, the main body of the sketch should work for the ACS723 Current Sensor as well.

To properly calibrate the ACS723 breakout board, you should first consider what type and range of currents you want to measure.

### Choosing the Range

If you are going to be dealing mainly with DC, positive currents, you can adjust Vref to the lower end of its range. If you are trying to measure AC currents, you will want to keep Vref about in the middle at 2.5V. This lets your output swing equally in the positive and negative directions.

The gain setting will depend on the range of currents you want to measure. If you want to measure a current between 100mA and 500mA, you will want to set the gain so the sensitivity is something like 100mA/250mV (you will learn how to do this in the following steps).

### Setting Vref

To get started, copy and upload the sketch below to your Arduino. You can also find the latest files in the [GitHub repository](https://github.com/sparkfun/Current_Sensor_Breakout-ACS723-Low_Current).

    language:c
    /*  SparkFun ACS712 and ACS723 Demo
        Created by George Beckstein for SparkFun
        4/30/2017
        Updated by SFE
        6/14/2018

        Uses an Arduino to set up the ACS712 and ACS723 Current Sensors
        See the tutorial at: https://learn.sparkfun.com/tutorials/current-sensor-breakout-acs723-hookup-guide

        Parts you may need:
        - 100 Ohm, 1/2W or greater resistor OR two 220 Ohm 1/4 resistors in parallel
        - ACS712 Breakout with on-board amplifier or ACS723 Current Sensor (Low Current)

        Optional equipment:
        - Oscilloscope
        - Multimeter (or two)
        - A power supply with current limiting/constant current would be handy to calibrate the device without using resistors
    */

    const int analogInPin = A0;

    // Number of samples to average the reading over
    // Change this to make the reading smoother... but beware of buffer overflows!
    const int avgSamples = 10;

    int sensorValue = 0;

    float sensitivity = 100.0 / 500.0; //100mA per 500mV = 0.2
    float Vref = 2500; // Output voltage with no current: ~ 2500mV or 2.5V

    void setup() 

    void loop() 

      sensorValue = sensorValue / avgSamples;

      // The on-board ADC is 10-bits -> 2^10 = 1024 -> 5V / 1024 ~= 4.88mV
      // The voltage is in millivolts
      float voltage = 4.88 * sensorValue;

      // This will calculate the actual current (in mA)
      // Using the Vref and sensitivity settings you configure
      float current = (voltage - Vref) * sensitivity;

      // This is the raw sensor value, not very useful without some calculations
      //Serial.print(sensorValue);

      /*************************************************************************************
       * Step 1.)
       * Uncomment and run the following code to set up the baseline voltage 
       * (the voltage with 0 current flowing through the device).
       * Make sure no current is flowing through the IP+ and IP- terminals during this part!
       * 
       * The output units are in millivolts. Use the Arduino IDE's Tools->Serial Plotter
       * To see a plot of the output. Adjust the Vref potentiometer to set the reference
       * voltage. This allows the sensor to output positive and negative currents!
       *************************************************************************************/

      Serial.print(voltage);
      //Serial.print("mV");

      /*************************************************************************************
       * Step 2.)
       * Keep running the same code as above to set up the sensitivity
       * (how many millivolts are output per Amp of current.
       * 
       * This time, use a known load current (measure this with a multimeter)
       * to give a constant output voltage. Adjust the sensitivity by turning the
       * gain potentiometer.
       * 
       * The sensitivity will be (known current)/(Vreading - Vref).
       *************************************************************************************/

        /*************************************************************************************
       * Step 3.)
       * Comment out the code used for the last two parts and uncomment the following code.
       * When you have performed the calibration steps above, make sure to change the 
       * global variables "sensitivity" and "Vref" to what you have set up.
       * 
       * This next line of code will print out the calculated current from these parameters.
       * The output is in mA
       *************************************************************************************/

      //Serial.print(current);
      //Serial.print("mA");

      // -- DO NOT UNCOMMENT BELOW THIS LINE --
      Serial.print("\n");

      // Reset the sensor value for the next reading
      sensorValue = 0;
    }

This sketch reads the voltage on pin A0 and prints it to the [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux). In later steps you will learn how to get actual current readings with this sketch.

To set up Vref, the sensor should have no current flowing through it! For this part, you only need to connect the ACS723\'s GND pin to Ground, VO pin to pin A0 on the SparkFun RedBoard (or equivalent), and 5V to the 5V pin on the RedBoard. If you have one available, it may be useful to also read the output voltage using a [multimeter](https://www.sparkfun.com/products/12966). See the Fritzing diagram below for more information:

[![Adjusting Vref Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/2/ACS723_Low_Current_Sensor_Arduino_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/ACS723_Low_Current_Sensor_Arduino_Fritzing_bb.jpg)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

If you aren\'t using a multimeter to set Vref, open up the Arduino IDE\'s serial plotter by clicking **Tools-\>Serial Plotter**. This will show the voltage reading from the Arduino in real time. The units are in millivolts.

Turn the Vref potentiometer clockwise to increase Vref and counter-clockwise to decrease. Make small adjustments, as the adjustment is very sensitive!

**Note:** Using metal/magnetized screwdrivers may cause the sensor to give false readings. This is because the Hall effect sensor inside is picking up the magnetic fields from the screwdriver. You may want to use a plastic screwdriver to eliminate this effect. I made one out of an old guitar pick with some scissors!

In the Serial Plotter, you should see something like this:

[![Vref Animation](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/vref-animation.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/vref-animation.gif)

*Using the RedBoard and Arduino, you can plot the output voltage as you adjust Vref*

Tune Vref to about where you want it, for example 2500mV.

### Setting Gain and Sensitivity

To set the gain, you need to pass a known current through the sensor and tune the gain pot to achieve the sensitivity your application needs.

For example, if you want to measure between 100mA and 500mA, you should shoot for a sensitivity of around 100mA/250mV. To do this, you can pass 100mA through the sensor, and adjust the gain pot until the output voltage is 250mV above your set Vref.

For those of you who have a benchtop power supply with a current limiter/constant current (CC) mode, getting this 100mA current is easy. In this case, you can simply connect the positive terminal of the power supply to the IP+ pin and the negative terminal of the power supply to the IP- pin. Make sure your current limit is set to something reasonable (**NOT above 5A**), and turn the power on. Adjust the output to a constant 100mA current for use in adjusting the gain.

[] **Make sure your benchtop power supply won\'t be damaged by shorting the outputs! Read your supply\'s user manual for more information.**

If you don\'t have a power supply, all you need are some resistors (like in this [nifty resistor kit](https://www.sparkfun.com/products/10969), or these [power resistors](https://www.sparkfun.com/products/13053) for more power dissipation). To make a fixed, known current, just use [Ohm\'s Law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/ohms-law)!

[![Resistor Kit - 1/4W (500 total)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/1/7/1/10969-Resistor_Kit_-_1_4W__500_total_-01.jpg)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html)

### [Resistor Kit - 1/4W (500 total)](https://www.sparkfun.com/resistor-kit-1-4w-500-total.html) 

[ COM-10969 ]

Nothing stops a project dead in its tracks faster than not having the right resistor. These components are arguably the most ...

[ [\$10.50] ]

[![Power Resistor Kit - 10W (25 pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/0/7/1/10353-01.jpg)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html)

### [Power Resistor Kit - 10W (25 pack)](https://www.sparkfun.com/power-resistor-kit-10w-25-pack.html) 

[ KIT-13053 ]

Holy Wattage, Batman! This Power Resistor Kit comes with 5 each of 5 different 10 Watt resistor values including 1 Ohm, 2 Ohm...

[ [\$9.50] ]

If you want a 100mA current from a 5V source you need (5/0.1) = 50Ω

You should keep in mind how much power your resistors can handle though! If not, they\'ll end up a bit toasty\... With 5V and 100mA, the power would be 500mW or 1/2W. The small resistors in the kit above can only handle 250mW or 1/4W at most. But, wait! A resourceful engineer knows you can still use the 1/4W resistors, you just need to split the power dissipation. By placing equal resistors in [parallel](https://learn.sparkfun.com/tutorials/resistors/series-and-parallel-resistors), you can increase the maximum allowable power dissipation; each resistor just adds their power rating. IE: 1/4W resistor + 1/4W resistor = 1/2W capacity! Keep in mind that the equivalent resistance will be lower though.

500mW is still a lot of power for these 1/4W resistors, so I recommend using only 50mA to tune the gain, unless you have the power resistors linked to above.

To get 50mA from 5V, you need 100Ω. Using parallel resistances, you need double that, or around 220Ω. You may want to use your multimeter to make sure the current flowing through the circuit is indeed 50mA. The tolerances of resistors can alter this current. To measure current with your multimeter, make sure to connect it in series! To see a diagram of how to build the circuit for setting the gain, see the Fritzing diagram below:

[![Adjusting Gain Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/8/2/Config_Gain_Sensitivity_ACS723_Current_Sensor_Arduino_Fritzing_bb.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/7/8/2/Config_Gain_Sensitivity_ACS723_Current_Sensor_Arduino_Fritzing_bb.jpg)

*Having a hard time seeing the circuit? Click on the wiring diagram for a closer look.*

With a known, constant current flowing through the sensor, the gain can be adjusted. The same sketch can be used as last time. Open up the Serial Plotter again. To set the gain, disconnect one of the wires to break the current sensing circuit. When you reconnect it, see how much the output voltage increases. Subtract this from your Vref, to keep the voltage change (also known as delta). So, if you have 50mA flowing in the circuit, you want this change to be about 125mV for the 100mA/250mV sensitivity example. An example is shown below:

[![Gain Adjust Delta Plot](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/4/1/gain-adjust-delta.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/gain-adjust-delta.png)

Adjust the change (Vdelta) to what you need it to be by tuning the gain potentiometer. As mentioned above, this affects the noise (spikiness) you see in the output:

[![Gain Adjust Noise](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/gain-adjust-noise.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/4/4/1/gain-adjust-noise.gif)

*As the gain increases, the spiky noise gets bigger (and the Vref changes slightly)*

**Note:** Adjusting the gain pot also changes the Vref setting slightly; you need to take this into account when you do your calculations. You should measure your final Vref and sensitivity with a multimeter after calibration.

Once you have Vref and the sensitivity settings selected, you can modify the code in the example sketch to print out your current readings in milliamps! Follow step 3 in the code comments to learn how to do this. Make sure to change the sensitivity and Vref variables to what you have set so the code can calculate the current properly.