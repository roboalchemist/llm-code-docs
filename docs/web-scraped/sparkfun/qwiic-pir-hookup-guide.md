# Source: https://learn.sparkfun.com/tutorials/qwiic-pir-hookup-guide

## Introduction

Passive Infrared (PIR) sensors are great for detecting motion in a specific area around the sensor. The [SparkFun Qwiic PIR - 170uA (EKMC4607112K)](https://www.sparkfun.com/products/17374) and [SparkFun Qwiic PIR - 1uA (EKMB1107112)](https://www.sparkfun.com/products/17375) use two versions of the EKM-series PIR sensors from Panasonic^®^ to offer low profile motion-sensing options over I^2^C for both battery powered and continuously powered applications.

[![SparkFun Qwiic PIR - 170uA (EKMC4607112K)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/4/0/6/17374-SparkFun_Qwiic_PIR_-_170uA__EKMC4607112K_-01A.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pir-170ua-ekmc4607112k.html)

### [SparkFun Qwiic PIR - 170uA (EKMC4607112K)](https://www.sparkfun.com/sparkfun-qwiic-pir-170ua-ekmc4607112k.html) 

[ SEN-17374 ]

Great for detecting motion in a small area & optimized for small movements to offer motion-sensing options for continuously p...

[ [\$22.50] ]

[![SparkFun Qwiic PIR - 1uA (EKMB1107112)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/4/0/7/17375-SparkFun_Qwiic_PIR_-_1uA__EKMB1107112_-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-pir-1ua-ekmb1107112.html)

### [SparkFun Qwiic PIR - 1uA (EKMB1107112)](https://www.sparkfun.com/sparkfun-qwiic-pir-1ua-ekmb1107112.html) 

[ SEN-17375 ]

Great for detecting motion in a small area and optimized for small movements to offer motion-sensing options for battery powe...

**Retired**

PIR sensors do not return specific distance data like [distance sensors](https://www.sparkfun.com/distance_sensing). Instead, the sensors measure IR light coming from objects in their detection area making them perfect for applications such as controlling power to devices like lights, cameras, screens, etc. automatically when motion is detected.

The Qwiic versions of these PIR breakouts feature an ATTiny84 with firmware that handles monitoring the sensor\'s output signal, debouncing that signal along with a configurable interrupt and translates it all to the I^2^C interface; making it easy to add a PIR to an existing Qwiic/I^2^C project.

In this guide we\'ll cover the hardware present on the Qwiic PIRs, how to connect them to your circuit and we\'ll finish things up covering both the Arduino Library and Python Package we have written for these sensors along with the examples included in both code packages.

If you would prefer to monitor the output of the sensors directly, check out our basic breakouts of the [170uA PIR](https://www.sparkfun.com/products/17372) and [1uA PIR](https://www.sparkfun.com/products/17373).

### Required Materials

In order to follow along with this tutorial you\'ll need a few items along with your Qwiic PIR. First, you\'ll need a microcontroller to communicate with the board. Below are a few options that come Qwiic-enabled out of the box:

[![SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/4/1/15663-SparkFun_Thing_Plus_-_ESP32_WROOM-01.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html)

### [SparkFun Thing Plus - ESP32 WROOM (Micro-B)](https://www.sparkfun.com/sparkfun-thing-plus-esp32-wroom-micro-b.html) 

[ WRL-15663 ]

The SparkFun ESP32 Thing Plus is the next step to get started with Espressif IoT ideations while still enjoying all the ameni...

[ [\$24.95] ]

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![SparkFun Qwiic Micro - SAMD21 Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/0/15423-SparkFun_Qwiic_Micro_-_SAMD21-01b.jpg)](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html)

### [SparkFun Qwiic Micro - SAMD21 Development Board](https://www.sparkfun.com/sparkfun-qwiic-micro-samd21-development-board.html) 

[ DEV-15423 ]

The SparkFun Qwiic Micro is molded to fit our standard 1\" x 1\" Qwiic board size which makes it our smallest SAMD21 micro-cont...

[ [\$22.95] ]

We also have a Python package available for the Qwiic PIRs so you can use a single-board computer (SBC) like a Raspberry Pi or Jetson Nano as your controller as well.

[![Raspberry Pi 4 Model B (2 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/1/15446-Raspberry_Pi_4_Model_B__2_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html)

### [Raspberry Pi 4 Model B (2 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html) 

[ DEV-15446 ]

The 2 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$69.75] ]

[![NVIDIA Jetson Nano Developer Kit (V3)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/4/6/16271-NVIDIA_Jetson_Nano_Developer_Kit__V3_-01.jpg)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html)

### [NVIDIA Jetson Nano Developer Kit (V3)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html) 

[ DEV-16271 ]

The NVIDIA® Jetson Nano™ Developer Kit V3 delivers the performance to run modern AI workloads at a small form factor, low ...

**Retired**

[![SparkFun DLI Kit for Jetson Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/0/1/1/16308-SparkFun_DLI_Kit_for_Jetson_Nano_V3-01.jpg)](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano.html)

### [SparkFun DLI Kit for Jetson Nano](https://www.sparkfun.com/sparkfun-dli-kit-for-jetson-nano.html) 

[ KIT-16308 ]

With the release of the Jetson Nano™ Developer Kit, NVIDIA® empowers developers, researchers, students, and hobbyists to e...

**Retired**

[![SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/0/3/16386-Raspberry_Pi_4_Desktop_Kit_-_4GB-01b.jpg)](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html)

### [SparkFun Raspberry Pi 4 Desktop Kit - 4GB](https://www.sparkfun.com/sparkfun-raspberry-pi-4-desktop-kit-4gb.html) 

[ KIT-16386 ]

The SparkFun Raspberry Pi 4 Desktop Kit (4GB) includes everything you need to turn any monitor with an HDMI port into a deskt...

**Retired**

If your preferred microcontroller or SBC does not have a Qwiic connector, you can add one using one of the following products:

[![SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/5/8/8/15945-SparkFun_Qwiic_pHAT_V3.0_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html)

### [SparkFun Qwiic pHAT v2.0 for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-phat-v2-0-for-raspberry-pi.html) 

[ DEV-15945 ]

The SparkFun Qwiic pHAT V2 for Raspberry Pi is the quickest and easiest way to make your way into the Qwiic ecosystem and sti...

[ [\$7.95] ]

[![SparkFun Qwiic Shield for Arduino](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/4/3/14352-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html)

### [SparkFun Qwiic Shield for Arduino](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino.html) 

[ DEV-14352 ]

The SparkFun Qwiic Shield is an easy-to-assemble board that provides a simple way to incorporate the Qwiic Connect System wit...

[ [\$7.75] ]

[![SparkFun Qwiic Shield for Arduino Nano](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/6/16789-SparkFun_Qwiic_Shield_for_Arduino_Nano-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html)

### [SparkFun Qwiic Shield for Arduino Nano](https://www.sparkfun.com/sparkfun-qwiic-shield-for-arduino-nano.html) 

[ DEV-16789 ]

The SparkFun Qwiic Shield for Arduino Nano makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards...

[ [\$5.50] ]

[![SparkFun Qwiic Shield for Thing Plus](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/9/7/16790-SparkFun_Qwiic_Shield_for_Thing_Plus-05.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html)

### [SparkFun Qwiic Shield for Thing Plus](https://www.sparkfun.com/sparkfun-qwiic-shield-for-thing-plus.html) 

[ DEV-16790 ]

The SparkFun Qwiic Shield for Thing Plus makes it so you can use SparkFun\'s Qwiic connect ecosystem with development boards t...

[ [\$5.10] ]

Finally, you\'ll need at least one Qwiic cable to connect your Qwiic PIR to your microcontroller:

[![Flexible Qwiic Cable - 50mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/7/17260-Flexible_Qwiic_Cable_-_50mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html)

### [Flexible Qwiic Cable - 50mm](https://www.sparkfun.com/flexible-qwiic-cable-50mm.html) 

[ PRT-17260 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.50] ]

[![Flexible Qwiic Cable - 500mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/4/17257-Flexible_Qwiic_Cable_-_500mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-500mm.html)

### [Flexible Qwiic Cable - 500mm](https://www.sparkfun.com/flexible-qwiic-cable-500mm.html) 

[ PRT-17257 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$2.75] ]

[![Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/3/14427-Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/qwiic-cable-100mm.html)

### [Qwiic Cable - 100mm](https://www.sparkfun.com/qwiic-cable-100mm.html) 

[ PRT-14427 ]

This is a 100mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

[![Qwiic Cable - 200mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/5/4/14428-Qwiic_Cable_-_200mm-01.jpg)](https://www.sparkfun.com/products/14428)

### [Qwiic Cable - 200mm](https://www.sparkfun.com/products/14428) 

[ PRT-14428 ]

This is a 200mm long 4-conductor cable with 1mm JST termination. It's designed to connect Qwiic enabled components together...

**Retired**

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic):

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with the concepts covered in them:

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/terminal-basics)

### Serial Terminal Basics 

This tutorial will show you how to communicate with your serial devices using a variety of terminal emulator applications.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

## Hardware Overview

In this section we\'ll cover the characteristics and features of the PIR sensors and other hardware included on the Qwiic PIR boards.

### Panasonic EKM-Series PIR Sensors

The EKMC4607112K and EKMB1107112 from Panasonic are low-profile PIR sensors ideal for things like motion-activated lights, cameras or other electronics. Applications include automatic lighting for energy conservation, motion-activated security or trail cameras or maybe something fun like a [homemade convenience store chime](https://learn.sparkfun.com/tutorials/papa-soundie-audio-player-hookup-guide#hardware-example-project-the-gag). The EKMC4607112K works best in a continuous power installation and has slightly better sensing performance than the EKMB1107112 which is best suited for battery and low-power installations.

[![Photo of the Qwiic PIR with the Panasonic EKM PIR Sensor Highlighted.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Sensor.jpg)

*The version (1µA or 170µA) is marked by one of two solder pads \"East\" of the PIR sensor.*

\
Input voltage (normally **3.3V**) for the Qwiic PIR is provided either via the Qwiic connectors or through the **3.3V** pin on the PTH header. The Output (OUT) pin is connected to a digital pin on the ATTiny84. Take note that both versions of the Qwiic PIR share the same PCB design and the version (**1µA** or **170µA**) are marked by the solder pads \"East\" of the PIR sensor.

The two PIR sensors have very similar electrical and sensing characteristics with a few specific differences users will want to take note of prior to deciding which sensor best suits their needs. The tables below outline the Electrical and Detection Performance Characteristics to give users a basic overview. For a more detailed look at these two sensors, take a look at their respective specification sheets ([EKMC4607112K](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMC460711xK_Spec.pdf) & [EKMB1107112](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf)) along with the [Panasonic PIR Sensors - Product Brief](https://cdn.sparkfun.com/assets/3/f/8/8/1/4541_fileversion.pdf) (EKM-Series sensors are covered on page 8).

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Electrical Characteristics                                                                                                                         |
+===========================+===============+===============+===============+===============+===============+========================+===============+
|                           |               | EKMC4607112K                                  | EKMB1107112                                            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Characteristic            | Units         | Min           | Typ.          | Max           | Min           | Typ.                   | Max           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Operating Voltage         | VDC           | 3.0           | \-            | 6.0           | 2.3           | \-                     | 4.0           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Current Consumption\      | µA            | \-            | 170           | 300           | \-            | 1^[\[1\]](#QwiicPIR1)^ | 3             |
| (Sensor Only)             |               |               |               |               |               |                        |               |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Output Current            | µA            | \-            | \-            | 100           | \-            | \-                     | 100           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Output Voltage            | VDC           | VDD-0.5       | \-            | \-            | VDD-0.5       | \-                     | \-            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+
| Circuit Stability Time\   | secs          | \-            | \-            | 30            | \-            | 25                     | 210           |
| (when voltage is applied) |               |               |               |               |               |                        |               |
+---------------------------+---------------+---------------+---------------+---------------+---------------+------------------------+---------------+

As mentioned above, the sensing performances of the PIR Sensors are very similar with a few notable differences. Also take note that PIR sensor performance can vary depending on the environment it is monitoring.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Detection Performance Characteristics                                                                                                                             |
+=================+========================+===============+========================+===============+===============================================================+
|                 | EKMC4607112K                           | EKMB1107112                            | Notes                                                         |
+-----------------+------------------------+---------------+------------------------+---------------+---------------------------------------------------------------+
|                 | Temperature Difference | Value         | Temperature Difference | Value         | Target Conditions                                             |
+-----------------+------------------------+---------------+------------------------+---------------+---------------------------------------------------------------+
| Detection Range | 8°C (14.4°F)           | up to 7m      | 4°C (7.2°F)            | up to 7m      | 1\. Movement speed: 1 m/s\                                    |
|                 |                        |               |                        |               | 2. Target concept is human body (Object size:Around700×250mm) |
|                 +------------------------+---------------+------------------------+---------------+                                                               |
|                 | 4°C (7.2°F)            | up to 5m      | 2°C (3.6°F)            | up to 5m      |                                                               |
+-----------------+------------------------+---------------+------------------------+---------------+---------------------------------------------------------------+

[\[1\] Note:](https://learn.sparkfun.com/tutorials/qwiic-pir-breakout-hookup-guide#QwiicPIR1) Current consumption for the EKMB1107112 varies depending on the operating mode. Refer to section 4-4 of the [EKMB Spec Sheet](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf) for specific values.

### ATTiny84 IC

The ATTiny84 on this board comes pre-programmed with firmware to act as an intermediary between the PIR sensor and the microcontroller via Qwiic/I^2^C. The firmware handles monitoring the raw sensor output to detect objects entering or leaving the sensing area, automatically debouncing the output, triggering an interrupt whenever motion is detected and even storing a queue of sensing events you can pull from and clear.

[![Qwiic PIR with the ATTiny84 IC Highlighted.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-ATTiny.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-ATTiny.jpg)

The default I^2^C address for the Qwiic PIR is **0x12** but can be switched to **0x13** by adjusting the ADR jumper. Alternatively, users can alter the address to a custom value using functions from the libraries or direct writes to the address register. Software setting of the I^2^C address is covered in more detail in the Arduino and Python library sections.

Finally, a 2x3 header broken out on the back of the board allows for programming the ATTiny84. This is primarily used for programming during manufacturing but can be used re-program the IC with custom firmware. You can download and modify the firmware from the [Hardware GitHub Repository](https://github.com/sparkfun/Qwiic_PIR).

[]Need help re-programming your Qwiic PIR? Take a look through these tutorials for instructions and tips:

- [Tiny AVR Programmer Hookup Guide](https://learn.sparkfun.com/tutorials/tiny-avr-programmer-hookup-guide)
- [Re-Programming the LilyTiny/LilyTwinkle](https://learn.sparkfun.com/tutorials/re-programming-the-lilytiny--lilytwinkle)

### Qwiic/I^2^C Interface and Interrupt Pin

The easiest way to use the Qwiic PIR is with the Qwiic connect system. Connect it to your microcontroller or SBC with a [Qwiic Cable](https://www.sparkfun.com/products/14427) to start communicating with it via I^2^C. For users who prefer a soldered connection, the I^2^C pins for the Qwiic PIR are broken out to a standard 0.1\"-spaced PTH header.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Highlighting the Qwiic connectors on the front of the Qwiic PIR](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Qwiic.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Qwiic.jpg)   [![Highlighting the Qwiic PIR\'s PTH Header for I2C and Interrupt pin.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-I2C_PTH_Header.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-I2C_PTH_Header.jpg)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Having trouble viewing the detail in these photos? Click on them for a larger view.*

We\'ve also included a dedicated Interrupt pin users can connect to an interrupt-capable pin on their microcontroller to trigger interrupt events based on the activity detected by the Qwiic PIR. Read on to the Arduino and Python sections for more information on how to configure and use this pin.

### Solder Jumpers

If you have never worked with solder jumpers and PCB traces before or would like a quick refresher, check out our [How to Work with Solder Jumpers and PCB Traces](https://learn.sparkfun.com/tutorials/how-to-work-with-jumper-pads-and-pcb-traces) tutorial for detailed instructions and tips.

There are four solder jumpers on the Qwiic PIR boards labeled **PWR**, **I2C**, **INT** and **ADR**. Let\'s briefly cover each jumper\'s functionality and default state.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Highlighting the Power LED Jumper on the Qwiic PIR](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Power_LED.jpg)   ![Highlighting the I2C, Interrupt and Address Jumpers on the back of the Qwiic PIR](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/SparkFun_Qwiic_PIR-Jumpers.jpg)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Power Jumper

The Power (PWR) Jumper controls the power LED on the board and is **closed** by default. It ties the anode of the Power LED to **3.3V** via a **1KΩ** resistor. Open the jumper and disable the LED by severing the trace between the two pads. Disabling the Power LED helps to reduce the total current draw of the Qwiic PIR.

#### I^2^C Jumper

The I^2^C Jumper pulls the ATTiny84\'s SDA and SCL lines to **3.3V** via a pair of **2.2kΩ** resistors. The default state is **closed**. Open the jumper by severing the trace connecting the three pads to disable the pull-up resistors.

If you have more than one device on a single I^2^C bus, it is recommended to only maintain a single pair of pullup resistors to avoid creating too strong of a parallel resistance. A strong parallel resistance can lead to communication issues on the bus. If you have multiple devices using a single set of pull-up resistors on your I^2^C bus make sure all devices operate at the same [logic level](https://learn.sparkfun.com/tutorials/logic-levels) or are properly shifted to avoid damage to the device(s).

#### Interrupt Jumper

The Interrupt (INT) Jumper pulls the ATTiny84\'s Interrupt pin to **3.3V** via a **10kΩ** resistor. The default state of the Interrupt jumper is **closed**. The Interrupt Pin on the ATTiny84 is configured as an active LOW interrupt and must be pulled to logic HIGH (**3.3V**) to function properly. Disable the Interrupt pin by opening the jumper.

#### Address Jumper

The Address (ADR) Jumper sets the I^2^C address of the ATTiny84. The jumper is **closed** by default. Open the jumper by severing the trace between the two pads to change the I^2^C address from its default value (**0x12**) to **0x13**.

### Board Dimensions

The Qwiic PIR matches the standard 1\" x 1\" (24.5mm x 24.5mm) form-factor for most Qwiic breakouts and has two mounting holes that fit a [4-40 screw](https://www.sparkfun.com/products/10453).

[![Qwiic PIR Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-Dimensions.png)

## Hardware Assembly

With the Qwiic system, assembling your SparkFun Qwiic PIR incredibly easy. We\'ll cover the basics of hardware assembly here along with a couple of tips for using the Interrupt pin.

### Connecting Qwiic Cables

Assuming you are using a Qwiic-enabled development board like the [RedBoard Qwiic](https://www.sparkfun.com/products/15123) shown below or you have a Qwiic shield or Qwiic adapter attached to your development board or Raspberry Pi/SBC, all you need to do to connect the Qwiic PIR to your circuit is to plug one end of your Qwiic cable into the Qwiic PIR and the other end into the Qwiic connector on your development board/shield.

[![Qwiic PIR connected to RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-RedBoard_Connection.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-RedBoard_Connection.jpg)

Alternatively, you can use one of our adapter cables ([male](https://www.sparkfun.com/products/14425) and [female](https://www.sparkfun.com/products/14988)) to convert the Qwiic system to a standard jumper wire assembly. If you use one of these adapter cables, make sure you match the signals correctly:

- **Black = GND**
- **Red = 3.3V**
- **Blue = SDA**
- **Yellow = SCL**

If you prefer to not use the Qwiic connectors you can [solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering) wire or header pins to the PTH header to make your connections.

### Connecting Everything Up

If you do not plan to use the Interrupt pin on the Qwiic PIR go ahead and connect your development board to your computer via USB or if you are using a Raspberry Pi or other SBC, power it up.

If you want to use the Interrupt pin, a bit more assembly is required. In order to use the Interrupt pin we need to either solder to it or, for quick prototyping, you can connect it to your development board/SBC using IC hooks like [these](https://www.sparkfun.com/products/9741) that terminate in a standard male jumper wire connection.

After you have made your connection to the Qwiic PIR\'s Interrupt Pin, run that wire to a digital pin available for external interrupts. If you are not sure which pins are interrupt-capable, refer to your board\'s documentation for clarification. Since we\'re using the RedBoard Qwiic we can set up D2 or D3 as an interrupt pin. In the circuit below and the Interrupt Example in the Arduino library, the Interrupt pin is connected to D2:

[![The completed Qwiic PIR circuit with Interrupt Pin connected.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-Interrupt_Assembly.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/9/8/Qwiic_PIR-Interrupt_Assembly.jpg)

Now that the Qwiic PIR circuit is fully assembled, connect the RedBoard to your PC via USB (or if using a Raspberry Pi or other SBC, power it on) and we can move on to uploading code and monitoring motion.

## Qwiic PIR Arduino Library

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please read our [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library) tutorial.

We\'ve written an Arduino library to make it easy to get started and interact with the Qwiic PIR. Before we jump into the examples for reading data from the sensor, we need to install the library and we\'ll take a closer look at the available functions in the library. The Arduino Library Manager is the easiest way to install the library. Open the Library Manager, search for **\"SparkFun Qwiic PIR Arduino Library\"** and click the \"Install\" button to download the latest version. If you prefer manually installing the library from the [GitHub repository](https://github.com/sparkfun/SparkFun_Qwiic_PIR_Arduino_Library), you can download it here:

[Download the SparkFun Qwiic PIR Arduino Library](https://github.com/sparkfun/SparkFun_Qwiic_PIR_Arduino_Library/archive/master.zip)

### Library Functions

The list below outlines all of the functions available in the SparkFun Qwiic PIR Arduino Library along with quick descriptions of what they do. The examples cover nearly all the functions on this list so refer to them to get started or for demonstrations on how to integrate them into your own code.

#### Class

In the global scope, construct your sensor object (such as `mySensor` or `myPIR`) without arguments.

- `QwiicPIR mySensor;`

#### Device Setup & Settings

- `bool begin(uint8_t address = DEFAULT_ADDRESS, TwoWire &wirePort = Wire);` - Initializes the Qwiic PIR on the I^2^C bus. Users can specify an alternate address if it has been changed as well as choose which I^2^C port used to communicate with the PIR.
- `bool isConnected();` - Returns true if the PIR will acknowledge over I^2^C and false otherwise.
- `uint8_t deviceID();` - Returns the 8-bit device ID.
- `bool checkDeviceID();` - Returns true if the device ID matches the Qwiic PIR ID.
- `uint8_t getDeviceType();` - Returns `1` if a Qwiic PIR is attached to the bus and `0` if no device is attached.
- `uint16_t getFirmwareVersion();` - Returns the Qwiic PIR firmware version as a 16-bit integer. Major Revision Number = leftmost (high) byte. Minor Revision Number = rightmost (low) byte.
- `bool setI2Caddress(uint8_t address);` - Configures the attached Qwiic PIR to initialize to the bus using the specified address.
- `uint8_t getI2Caddress();` - Returns the I^2^C address of the attached Qwiic PIR.

#### PIR Status and Debounce Configuration

These functions are the primary ways to read whether or not an object is detected in the sensing area as well as how to customize the debounce time from the PIR to reduce noise and false detections and how to manipulate the detection queues.

- `bool rawPIRReading();` - Returns `1` when PIR is outputting a signal, `0` when not. This is the raw output from the PIR with no debouncing.
- `bool objectDetected();` - Returns `1` if a debounced object detection event occurs in the sensing area. The debounce time `objectDetected();` waits for is set by the `setDebounceTime(uint16_t time);`.
- `bool ojbectRemoved()`; - Returns `1` if a debounced object removal event occurs in the sensing area. The debounce time `objectRemoved();` waits for is set by the `setDebounceTime(uint16_t time);`.
- `uint16_t getDebounceTime();` - Returns the debounce time set for the PIR reading to settle (in milliseconds).
- `uint8_t setDebounceTime(uint16_t time);` Sets the time the Qwiic PIR waits for the raw reading from the sensor to settle. The default value for debounce time is 750ms.

#### Interrupt Status and Configuration

- `uint8_t enableInterrupt();` - When called, the interrupt pin is configured to trigger on all PIR events (detection & removal).
- `uint8_t disableInterrupt();` - When called, the interrupt pin is no longer configured to trigger on PIR events.
- `bool available();` - Returns the `eventAvailable` bit.
- `uint8_t clearEventBits();` - Sets `objectDetected`, `objectRemoved` and `eventAvailable` bits to zero.
- `uint8_t resetInterruptConfig();` - Resets any configured interrupt functions to defaults (OFF).

#### Queue Manipulation

- `bool isDetectedQueueFull();` - Returns true if queue of object detections timestamps is *full* and false if not. This queue stores ten timestamp values.
- `bool isDetectedQueueEmpty();` - Returns true if the queue of object detections timestamps is *empty* and false otherwise.
- `unsigned long timeSinceLastDetect();` - Returns the time (in milliseconds) since the `objectDetected();` function last returned `1`.
- `unsigned long timeSinceFirstDetect();` - Returns the time (in milliseconds) for the oldest value stored in the Detected Queue.
- `unsigned long popDetectedQueue();` - Returns the oldest value stored in the Detected Queue and removes it.
- `bool isRemovedQueueFull();` - Returns true if the object removals queue is *full* and false if not. This queue stores ten timestamp values.
- `bool isRemovedQueueEmpty();` - Returns true if the object removals queue is *empty* and false otherwise.
- `unsigned long timeSinceLastRemove();` - Returns the time (in milliseconds) since the `objectRemoved();` function last returned `1`.
- `unsigned long timeSinceFirstRemove();` - Returns the time (in milliseconds) for the oldest value stored in the Removed Queue.
- `unsigned long popRemovedQueue();` - Returns the oldest value stored in the Removed Queue and removes it.

## Arduino Examples

The SparkFun Qwiic PIR Arduino Library includes five examples to help users get started with the board and library. In this section we\'ll go over a few of the examples and highlight how they work.

### Example 1 - Print Raw PIR Status

The first example demonstrates how to set up the Qwiic PIR on your I^2^C bus and then retrieve raw data readings from the Qwiic PIR using the `rawPIRReading();` function. Open the first example by navigating to **File \> Examples \> SparkFun Qwiic PIR Arduino Library \> Example1_PrintRawPIRStatus**. Next, open the Tools menu and select your board (in our case, Arduino Uno) and the correct Port your board enumerated on. Upload the code and open your [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) with the baud set to **115200**.

The example first sets up the Qwiic PIR object and debounce time (in milliseconds):

    language:c
    QwiicPIR pir;

    #define DEBOUNCE_TIME 750

Next it initializes the sensor and then waits 30 seconds for the PIR to warm up and stabilize.

    language:c
    if (pir.begin() == false) 

      Serial.println("PIR acknowledged. Waiting 30 Seconds while PIR warms up");
      for (uint8_t seconds = 0; seconds < 30; seconds++)
      

The code will freeze if the Qwiic PIR does not acknowledge on the I^2^C bus at the default address. A bad connection or a different I^2^C address are the most common causes of this failure.

Once the PIR warms up the main loop checks whether `rawPIRReading();` returns `TRUE` or `FALSE` and waits to update again for the value set for `DEBOUNCE_TIME`. The code prints out objects detected or removed via serial. Take note when using the `rawPIRReading();` any debouncing of the signal must be done manually.

### Example 2 - Print PIR Status

The second example is very similar to the first but uses the `objectDetected();` and `objectRemoved();` functions instead of `rawPIRReading();`. The primary difference between these functions is where debouncing the PIR signal happens. Instead of manually debouncing the PIR signal each time it occurs, the `objectDetected();` and `objectRemoved();` functions refer to the value stored for `setDebounceTime(uint16_t time);` and will automatically debounce the signal for that time. The default value for `setDebounceTime();` is 750ms.

Open the example, upload it and open a serial terminal set to **115200** baud. After initializing the sensor and waiting for 30 seconds for the PIR to warm up, the code will start polling the PIR for events and prints what they are over serial:

    language:c
    if (pir.available())     
        if (pir.objectRemoved()) 
        pir.clearEventBits();
    }

### Example 3 - Queue Usage

The third example included with the library shows how to read and manipulate the Object Detected and Object Removed queues. After uploading the example, open a serial terminal with the baud set again to **115200**. After initializing the Qwiic PIR, the main loop checks if either the Detected or Removed queues have values stored for either time (in seconds) since first detect/remove or time since last detect/remove and prints them over serial. If no values are present in either queue, the code prints out which queue is empty:

    language:c
    if(pir.isDetectedQueueEmpty() == false) 

    if(pir.isDetectedQueueEmpty() == true)  

    if(pir.isRemovedQueueEmpty() == false) 
    if(pir.isRemovedQueueEmpty() == true) 

Along with printing values from each queue, this example also shows how to manipulate and pop values from any queue:

    language:c
    if(Serial.available()) 

        if(data == 'r' || data == 'R') 
    }
    delay(20);

With a serial terminal open, send the letter \"D\" (capitalized or not) to pop a value off the Detected Queue. Similarly, send the letter \"R\" to pop a value off the Removed Queue.

### Example 4 - External Interrupt

Example 4 - ExtInterrupt demonstrates how to use the Interrupt pin on the Qwiic PIR.

Along with setting up the Qwiic PIR in the global class, the code defines the interrupt pin and creates an interrupt flag:

    language:c
    int interruptPin = 2;

    bool interruptEntered = false;

Adjust the value for your interrupt pin as needed. This example assumes a SparkFun RedBoard/Arduino Uno is used and sets D2 as the interrupt pin. In the setup, the code initializes the Interrupt pin as an input and attaches it as a falling-edge interrupt to a custom function called `pirHandler`:

    language:c
    pinMode(interruptPin, INPUT);
    attachInterrupt(digitalPinToInterrupt(interruptPin), pirHandler, FALLING);

After initializing the Qwiic PIR on the bus and waiting for 30 seconds for the PIR to warm up, the code calls the `enableInterrupt();` and `clearEventBits();` functions to tell the Qwiic PIR to trigger the pin on object events and clears any event bits to toggle the Interrupt pin `HIGH`:

    pir.enableInterrupt();
    pir.clearEventBits();

The main loop checks for motion events and if any are detected it will fire the interrupt pin:

    language:c
    void loop() 
        pir.clearEventBits();
        interruptEntered = false;
        delay(10);
      }
    }

    void pirHandler()
    

From here, you can modify this example or insert it into more complex code to trigger whatever interrupt event you would like using the Qwiic PIR.

## Qwiic PIR Python Package

**Note:** This tutorial assumes you are using the latest version of Python 3. If this is your first time using Python or I^2^C hardware on a Raspberry Pi these tutorials will help you get started:

- [Python Programming with the Raspberry Pi](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)
- [Raspberry Pi SPI and I2C Tutorial](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)

We\'ve written a Python package for the Qwiic PIR for users who prefer to use something like a Raspberry Pi with their sensor. The package can be installed with the all inclusive SparkFun Qwiic Python package or independently.

We recommend installing the entire SparkFun Qwiic Package as it also installs the required I^2^C driver.

**Note:** Don\'t forget to double check that the hardware I^2^C connection is enabled on your Raspberry Pi or other single board computer. Make sure to reboot your Pi after enabling the I^2^C bus for changes to take effect.

### SparkFun Qwiic Package

This repository is hosted on PyPi as the `sparkfun-qwiic` package. On systems that support PyPi installation via `pip3` (use `pip` for Python 2) is simple using the following commands:

For **all users** (Note: the user must have [**sudo**]() privileges):

    language:bash
    sudo pip3 install sparkfun-qwiic

For the **current user**:

    language:bash
    pip3 install sparkfun-qwiic

### Independent Qwiic PIR Py Package Installation

If you prefer to only install the Qwiic PIR package, you can download the `sparkfun-qwiic-pir` Python package hosted by PyPi via `pip3` following the instructions below. Alternatively, if you prefer to manually download and build the libraries you can grab them from the [Qwiic PIR Py GitHub Repository](https://github.com/sparkfun/Qwiic_PIR_Py) or by clicking the button below:

[Download the Qwiic PIR Py Repository](https://github.com/sparkfun/Qwiic_PIR_Py/archive/main.zip)

#### PyPi Installation

This repository is hosted on PyPi as the `sparkfun-qwiic-PIR` package. On systems that support PyPi, install the `sparkfun-qwiic-PIR` package via `pip3` (use `pip` for Python 2) using the following commands:

For **all users** (Note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install sparkfun-qwiic-PIR

For the **current user**:

    language:bash
    pip3 install sparkfun-qwiic-PIR

#### Local Installation

To install, make sure the `setuptools` package is installed on the system.

Direct installation at the command line (use `python` for Python 2):

    language:bash
    python3 setup.py install

To build a package for use with `pip3`:

    language:bash
    python3 setup.py sdist

A package file is built and placed in a subdirectory called dist. This package file can be installed using `pip3`.

    language:bash
    cd dist
    pip3 install sparkfun_qwiic_PIR-<version>.tar.gz

### Qwiic PIR Python Package Operation

Let\'s take a quick look at the functions available in the Python package. For more details on how the package works, take a look at the [source code](https://github.com/sparkfun/Qwiic_PIR_Py/blob/main/qwiic_pir.py) and package documentation hosted on [ReadTheDocs](https://qwiic-pir-py.readthedocs.io/en/latest/?).

#### Dependencies

This Python package has a few dependencies in the code, listed below:

    language:python
    import time
    import sys

#### Default Variables

    language:python
    # Define the device name and I2C addresses. These are set in the class definition
    # as class variables, making them available without having to create a class instance.
    # This allows higher level logic to rapidly create an index of qwiic devices at runtime.

    # This is the name of the device
    _DEFAULT_NAME = "Qwiic PIR"

    # Some devices have  multiple available addresses - this is a list of these addresses.
    # NOTE: The first address in this list is considered the default I2C address for the 
    # device.
    _AVAILABLE_I2C_ADDRESS = [0x12]

**Note:** This package differs from other SparkFun packages as the register values are declared in the object class.

    language:python
    # Constructor
    device_name = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    # Device ID for all Qwiic PIRs
    DEV_ID = 0x72

    # Registers
    ID = 0x00
    FIRMWARE_MINOR = 0x01
    FIRMWARE_MAJOR = 0x02
    EVENT_STATUS = 0x03
    INTERRUPT_CONFIG = 0x04
    EVENT_DEBOUNCE_TIME = 0x05
    DETECTED_QUEUE_STATUS = 0x07
    DETECTED_QUEUE_FRONT = 0x08
    DETECTED_QUEUE_BACK = 0x0C
    REMOVED_QUEUE_STATUS = 0x10
    REMOVED_QUEUE_FRONT = 0x11
    REMOVED_QUEUE_BACK = 0x15
    I2C_ADDRESS = 0x19

    # Status Flags
    eventAvailable = 0
    objectRemove = 0
    objectDetect = 0
    rawObjectDetected = 0

    # Interrupt Configuration Flags
    interruptEnable = 0

    # Queue Status Flags
    popRequest = 0
    isEmpty = 0
    isFull = 0

#### Class

**`QwiicPIR()`** or **`QwiicPIR(address)`**

This Python package operates as a class object, allowing new instances of that type to be made. An `__init__()` constructor is used that creates a connection to an I^2^C device over the I^2^C bus using the default or specified I^2^C address.

**Note:** If the Qwiic PIR\'s address has been altered from the default (**0x12**), create the Qwiic PIR object with the new address. For example, if the address jumper is opened create the Qwiic PIR object using this format: `QwiicPIR(0x13)`.

##### The Constructor

A constructor is a special kind of method used to initialize (assign values to) the data members needed by the object when it is created.

**`__init__(address=None, i2c_driver=None):`**

Input: value

The value of the device address. If not defined, the Python package will use the default I^2^C address (**0x12**) stored under `_AVAILABLE_I2C_ADDRESS` variable.

Input: *i2c_driver*

Loads the specified I^2^C driver; by default the [Qwiic I^2^C driver](https://github.com/sparkfun/Qwiic_I2C_Py) is used: `qwiic_i2c.getI2CDriver()`. Users should use the default I^2^C driver and leave this field blank.

#### Functions

A function is an attribute of the class, which defines a method for instances of that class. In simple terms, they are objects for the operations (or methods) of the class. For a complete list of all the available functions, head over to the [API Reference page](https://qwiic-pir-py.readthedocs.io/en/latest/apiref.html) of ReadtheDocs for the [Qwiic PIR Py Python Package](https://github.com/sparkfun/Qwiic_PIR_Py).

### Upgrading the Package

Updating the installed packages has to be done individually for each package (i.e. sub-modules and dependencies won\'t update automatically and must be updated manually). For the `sparkfun-qwiic-pir` Python package, use the following command (use `pip` for Python 2):

For **all users** (note: the user must have [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges):

    language:bash
    sudo pip3 install --upgrade sparkfun-qwiic-pir

For the **current user**:

    language:bash
    pip3 install --upgrade sparkfun-qwiic-pir

## Python Examples

The SparkFun Qwiic PIR Python Library includes four examples to help users get started with the board and library. In this section we\'ll go over the examples and highlight how they work.

To use the examples, open them from the Python library\'s location or copy the code into your preferred Python interpreter.

### Example 1 - Simple Example (Raw PIR Readings)

The first example shows how to set up the Qwiic PIR on the I^2^C bus and retrieve raw data from the PIR\'s output signal. Because we are reading raw PIR output the code manually sets up a debounce time (in milliseconds) to wait for the PIR output signal to stabilize. Adjust the debounce time by changing this value:

    language:python
    debounce_time = .20

The main example loop sets up the PIR object, attempts to initialize it on the I^2^C bus and, if successful, waits 30 seconds for the PIR to stabilize:

    language:python
    def run_example():

            print("\nSparkFun Qwiic PIR Example1\n")
            my_PIR = qwiic_pir.QwiicPIR()

            if my_PIR.begin() == False:
                    print("The Qwiic PIR isn't connected to the system. Please check your connection", \ file=sys.stderr)

                    return
            print ("Waiting 30 seconds for PIR to stabilize")
            for i in range(0,30):
                    print(i)
                    time.sleep(1)

            print("Device Stable")

Once the PIR has initialized and stabilized, the code begins to take readings and print out whether an object was detected or removed, pausing for the value set for `debounce_time` after each reading:

    language:python
    while True:
            if my_PIR.raw_reading() is True:
                    print("Object Detected")
            else:
                    print("Object Removed")
            time.sleep(debounce_time)

### Example 2 - Debounced Readings

The second example demonstrates how to read the debounced output signals from the Qwiic PIR using the `object_detected()` and `object_removed()` functions. Just like with the Arduino library, the Qwiic PIR Python Library includes functions for both raw PIR readings as well as automatically debounced readings.

Using the `object_detected()/removed()` functions allows you to set a debounce time with the `set_debounce_time()` function and the PIR will always wait for that amount of time before taking another reading. The default value for `set_debounce_time()` is 750ms.

The code initializes the Qwiic PIR on the bus and waits for 30 seconds for the PIR to stabilize prior to taking readings for object detections:

    language:python
    while True:
            if my_PIR.available() is True:
                    if my_PIR.object_detected():
                            print("Object Detected")
                    if my_PIR.object_removed():
                            print("Object Removed")
                    my_PIR.clear_event_bits()
            time.sleep(1)

### Example 3 - Queue Usage

The third example shows how to read values stored for the Object Detected and Object Removed queues. After initializing the sensor and waiting for it to stabilize the code then prints out values stored in Detected Queue & Removed Queue for both time (in seconds) since the last (most recent) object detection or removal event as well as the time since the oldest stored object detection or removal event. If either queue is empty, the code prints out which queue is empty.

    language:python
    while True:
            if my_PIR.is_detected_queue_empty() is False:
                    last_detect = my_PIR.time_since_last_detect() / 1000.0
                    first_detect =  my_PIR.time_since_first_detect() / 1000.0
                    print(last_detect)
                    print("s since last PIR detect   ")
                    print(first_detect)
                    print("s since first PIR detect   ")
            else:
                    print("Detected queue is empty")

            if my_PIR.is_removed_queue_empty() is False:
                    last_remove = my_PIR.time_since_last_remove() / 1000.0
                    first_remove =  my_PIR.time_since_first_remove() / 1000.0
                    print(last_remove)
                    print("s since last PIR detect   ")
                    print(first_remove)
                    print("s since first PIR detect   ")
            else:
                    print("Removed queue is empty")

### Example 4 - Pop Queue

Example 4 demonstrates how to pop values from both the `object_detected()` and `object_removed()` queues by sending the appropriate characters over serial.

Just like the other examples, the Qwiic PIR is initialized on the I^2^C bus and the code waits for 30 seconds for the PIR to stabilize it\'s readings. After waiting, the code prints out to enter either \"d\" or \"r\" to pop values from either the detected (d) or removed (r) queues:

    language:python
    while True:
        print("\mType 'd' to pop from the detected queue.")
        val = raw_input("Type 'r' to pop from the removed queue: ")
        # If the character is 'd' or 'D', then pop a value off the detected queue
        if val == 'd' or val == 'D':
            print("\nPopped detected queue! The first timestamp in detected queue was: ")
            print(str(my_PIR.pop_detected_queue() / 1000.0))

        # If the character is 'r' or 'R', then pop a value off the removed queue
        if val == 'r' or val == 'R':
            print("\nPopped removed queue! The first timestamp in removed queue was: ")
            print(str(my_PIR.pop_removed_queue90 / 1000.0))

        time.sleep(debounce_time)

If the correct value is entered the code prints out over serial the respective queue has been popped and prints out the timestamp for the removed value in seconds.

## Troubleshooting

Assembling and testing the Qwiic PIR is fairly straight-forward but in case you run into any issues we\'ve outlined a few tips and tricks for testing the PIR here.

### Detection Area/Field of View

The effective detection area of both the EKMC4607112K and EKMB1107112 is dependent on a variety of factors. The specifications for measurement range are based on a target concept (area of \~700×250mm) of a human body moving across two detection zones at a speed of 1m/s. The PIR senses objects best when moving across two detection zones on the horizontal (X) or vertical (Y) axes. The PIR may struggle to detect objects moving away or toward the PIR (along the Z axis) unless they also move along the other two axes.

Also note that background IR radiation can influence the PIR\'s ability to detect an object. The PIR can detect objects with a larger temperature difference from the background at a larger range. Refer back to the Hardware Overview section for range specifications at different temperature differences.

Take these detection factors into consideration when selecting the mounting position of your Qwiic PIR. Section 4-7 of the sensors\' spec sheets ([EKMC4607112K](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMC460711xK_Spec.pdf) and [EKMB1107112](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf)) show diagrams for optimal sensor placement and object motion for sensing performance.

### Qwiic PIR Not Recognized on I^2^C Bus

The examples included in both the Arduino and Python libraries will freeze if the Qwiic PIR does not acknowledge on the I^2^C bus. The most common cause of this is a poor or incomplete connection either using the Qwiic connectors or PTH header. Check your Qwiic cables for a secure connection to the Qwiic connectors or for damage. If using the PTH header, double check your [solder joints and wires](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips#loose-wires) to make sure they are complete and secure.

Another common cause for this error is if the Qwiic PIR is set to an alternate address. The examples assume the PIR uses the default I^2^C address (**0x12**) and will freeze if the code is not adjusted to reflect a change in address. For example, if the ADR jumper is set to switch the address to **0x13**, the `begin();` function in the Arduino Library can be adjusted as follows:

    language:c
    pir.begin(0x13);

Similarly, the Qwiic PIR object can be created in the Python package at an alternate address using the following code:

    language:python
    QwiicPIR(0x13)

Finally, Raspberry Pi users encountering this error should check to make sure the I^2^C bus is enabled. Refer to [this section](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial#i2c-on-pi) of our Raspberry Pi SPI & I^2^C tutorial for detailed instructions on enabling the bus.

### General Troubleshooting

If you need technical assistance and more information on this or another SparkFun product that is not working as you expected, we recommend heading on over to the SparkFun Technical Assistance page for some initial troubleshooting:

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.