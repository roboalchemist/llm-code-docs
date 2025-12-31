# Source: https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide

## Introduction

Passive infrared (PIR) sensors are motion-detecting devices used in security systems across the world \-- even though you may not see them, they probably see you!

[![PIR Motion Sensor (JST)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/0/5/3/5/13285-01.jpg)](https://www.sparkfun.com/pir-motion-sensor-jst.html)

### [PIR Motion Sensor (JST)](https://www.sparkfun.com/pir-motion-sensor-jst.html) 

[ SEN-13285 ]

This is a simple to use motion sensor. Power it up and wait 1-2 seconds for the sensor to get a snapshot of the still room. I...

[ [\$11.50] ]

Using the PIR sensor is simple: power it up, connect a pull-up resistor to the open-collector signal pin, and watch for it to go low. The PIR can sense abrupt changes in scenery as far as 10 feet (\~3m) away. Once your microcontroller is sensing movement, it can trigger a [buzzer](https://www.sparkfun.com/products/7950), [text message](https://www.sparkfun.com/products/13120), [tweet](https://www.sparkfun.com/products/13678), or a [klaxon](https://en.wikipedia.org/wiki/Vehicle_horn#Klaxon).

### Suggested Materials

This tutorial serves as a quick primer on PIR motion sensor and demonstrates how to hook them up and use them. Beyond the sensor itself, the following materials are recommended:

**[Arduino Uno](https://www.sparkfun.com/products/11021)** \-- We\'ll be using a digital pin on the Arduino to read the state of the PIR sensor\'s signal output. Any Arduino-compatible development platform \-- be it a [RedBoard](https://www.sparkfun.com/products/12757), [Pro](https://www.sparkfun.com/products/10914) or [Pro Mini](https://www.sparkfun.com/products/11113) \-- can substitute.

**[Jumper Wires](https://www.sparkfun.com/products/11026)** \-- The PIR sensor is terminated with a 3-pin JST cable one of the easier ways to connect this to an Arduino is to plug a few jumper cables into the connector and run them straight to an Arduino.

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Mini Speaker - PC Mount 12mm 2.048kHz](https://cdn.sparkfun.com/r/140-140/assets/parts/6/2/3/07950-Mini_Speaker_-_PC_Mount_12mm_2.048kHz_-01.jpg)](https://www.sparkfun.com/mini-speaker-pc-mount-12mm-2-048khz.html)

### [Mini Speaker - PC Mount 12mm 2.048kHz](https://www.sparkfun.com/mini-speaker-pc-mount-12mm-2-048khz.html) 

[ COM-07950 ]

We drove it directly from a 5V PIC to generate the tones for our Simon demonstration game.

[ [\$2.50] ]

[![LED Mixed Bag - 10mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/2/0/13326-01.jpg)](https://www.sparkfun.com/led-mixed-bag-10mm.html)

### [LED Mixed Bag - 10mm](https://www.sparkfun.com/led-mixed-bag-10mm.html) 

[ COM-13326 ]

Sometimes when you have too many choices, it\'s hard to make a good decision. In fact, there are times when you just want a ba...

[ [\$10.95] ]

Beyond those two items, you may want to add a buzzer or large LED to make range testing of the PIR sensor more convenient.

### Suggested Reading

PIR sensors are a great entry-level component for beginners, but there are still a few basic electronics concepts you should be familiar with. If any of these tutorial titles sound foreign to you, consider skimming through that content first.

[](https://learn.sparkfun.com/tutorials/pull-up-resistors)

### Pull-up Resistors 

A quick introduction to pull-up resistors - whey they\'re important, and how/when to use them.

[](https://learn.sparkfun.com/tutorials/light)

### Light 

Light is a useful tool for the electrical engineer. Understanding how light relates to electronics is a fundamental skill for many projects.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

## PIR Motion Sensor Overview

At their most fundamental level, PIR sensor\'s are infrared-sensitive light detectors. By monitoring light in the infrared spectrum, PIR sensors can sense subtle changes in temperature across the area they\'re viewing. When a human or some other object comes into the PIR\'s field-of-view, the radiation pattern changes, and the PIR interprets that change as movement.

That white cap dominating most of the top side of the PIR assembly is a lens, which helps focus the PIR sensor\'s field-of-view. The *actual* PIR sensor is hiding under that lens:

[![Under PIR cover](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/uncovered-iso.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/uncovered-iso.jpg)

The back side of the assembly sports amplifiers, voltage regulators and other supporting circuitry to help drive the PIR. All that\'s left for us to connect is three pins: power, ground, and the output signal.

### Power and Signal Pins

The top side of the PIR assembly includes two labels: \"+\" and \"AL\". The \"AL\" pin is the alarm pin \-- don\'t let the black wire fool you, this isn\'t ground! \"+\" is the PIR sensor\'s power supply input, leaving the unlabeled middle pin, with the white wire, as ground.

  Wire Color   Pin      Notes
  ------------ -------- -----------------------------------------------------------------------------------------------------
  Red          Power    5V[^\[1\]^](https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide#min_voltage) to 12V
  White        Ground   
  Black        Alarm    Open-collector output -- active low

The PIR sensor should be powered with at least 5V, but it can work with voltages as high as 12V. Fortunately, even if a PIR is powered higher than 5V, the alarm pin can still connect directly to an input pin because it is designed as an [open-collector](http://en.wikipedia.org/wiki/Open_collector).

When the PIR senses activity in it\'s viewing area, it pulls the alarm pin low. But when the sensor is inactive, the pin is basically floating. To avoid any false-positives, the alarm output should be **pulled high** to 5V. Most microcontroller\'s have internal pull-up resistors on their I/O pins, which can easily accomplish that task. You can also pull it high to 3.3V if you are using it with a 3.3V system (e.g. 3.3V Arduino or Raspberry Pi).

[\[1\]](https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide#min_voltage) **Note:** The PIR motion sensor can work with at least 5V. However, the voltage may not be enough for the L78L05 voltage regulator to work reliably depending on your power supply. The datasheet indicates that the dropout voltage is about *\~1.7V* to *\~2.0V*. Therefore, the PIR motion sensor\'s minimum voltage of about *\~6.7V* to *\~7.0V* is needed.\
\
**Bypass Jumper** - If you only have 5V available (e.g. you are pulling 5V from the Arduino\'s USB, Particle Photon\'s USB, or Raspberry Pi), you could [bypass the voltage regulator by adding a jumper](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces#rerouting-and-green-wire-repair) between the L78L05\'s VIN and VOUT pins. Just make sure that the voltage is regulated and clean. The images below highlightt the pins to bypass the voltage regulator. The pins of the SMD voltage regulator are small so you could also solder wire directly to the \"+\" pin as well.\
\

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![VIN and VOUT Pins Highlighted](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/13285-PIR_Motion_Sensor_Jumper_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/13285-PIR_Motion_Sensor_Jumper_1.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/13285-PIR_Motion_Sensor_Jumper_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/13285-PIR_Motion_Sensor_Jumper_2.jpg)
  *VIN and VOUT Pins Highlighted*                                                                                                                                                                                              *\"+\" and VOUT Pins Highlighted*
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**9V Power Supply** - Otherwise, we recommend using a 9V power supply to power the PIR motion sensor. Assuming that you are using this with an Arduino Uno form factor, you could just insert the 9V into the Arduino Uno\'s barrel jack connector. Then add a jumper between the PIR motion sensor\'s \"+\" pin and the Arduino\'s \"VIN\" pin.\
\

[![Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/7/TOL-15314-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html)

### [Wall Adapter Power Supply - 9VDC, 650mA (Barrel Jack)](https://www.sparkfun.com/wall-adapter-power-supply-9vdc-650ma-barrel-jack.html) 

[ TOL-15314 ]

This is a high quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for SparkFun Elect...

[ [\$9.25] ]

## Example Circuit

The circuit for this example is about as simple as it gets. Grab three jumper wires and insert them into the JST connector. It gets a little tight, but they should all be able to fit in there.

Connect the power (red) and ground (white) wires up to 5V [^\[1\]^](https://learn.sparkfun.com/tutorials/pir-motion-sensor-hookup-guide#min_voltage) and GND respectively. Then connect the **black alarm wire** to Arduino pin 2.

[![PIR sensor hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/1/8/pir_sensor_bb.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/1/8/pir_sensor_bb.png)

We\'ll use the internal pull-up resistor on D2 to complete the circuit. Whenever the sensor is inactive, the pin should read high. When motion is detected, the sensor will pull D2 low.

## Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

Here is a simple Arduino example based on the circuit above. Copy and paste this into your Arduino IDE, then upload!

    language:c
    /******************************************************************************
    PIR_Motion_Detector_Example.ino
    Example sketch for SparkFun's PIR Motion Detector
      (https://www.sparkfun.com/products/13285)
    Jim Lindblom @ SparkFun Electronics
    May 2, 2016

    The PIR motion sensor has a three-pin JST connector terminating it. Connect
    the wire colors like this:
    - Black: D2 - signal output (pulled up internally)
    - White: GND
    - Red: 5V

    Connect an LED to pin 13 (if your Arduino doesn't already have an LED there).

    Whenever the PIR sensor detects movement, it'll write the alarm pin LOW.

    Development environment specifics:
    Arduino 1.6.7
    ******************************************************************************/
    const int MOTION_PIN = 2; // Pin connected to motion detector
    const int LED_PIN = 13; // LED pin - active-high

    void setup() 
    

    void loop() 
    
      else
      
    }

After uploading, have a look at your Arduino\'s pin 13 LED. You can also **open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux)**, and set the baud rate to 9600 bps.

The PIR sensor requires approximately 15 seconds of **motion-free activity**, while it gets a \"snapshot\" of it\'s viewing area. Try not to move until the pin 13 LED turns off, then wave your hands, jump in the air, go crazy!