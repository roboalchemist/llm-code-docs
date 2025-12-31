# Source: https://learn.sparkfun.com/tutorials/sparkfun-pir-breakout-hookup-guide

## Introduction

Looking to add some motion detection to a project you are working on? The [SparkFun PIR Breakout - 170uA (EKMC4607112K)](https://www.sparkfun.com/products/17372) and [SparkFun PIR Breakout - 1uA (EKMB1107112)](https://www.sparkfun.com/products/17373) might be just the thing! These breakouts use two versions of the EKM-series PIR sensors from Panasonic^®^ to offer low profile motion-sensing options for both battery powered and continuously powered applications.

[![SparkFun PIR Breakout - 170uA (EKMC4607112K)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/4/0/4/17372-SparkFun_PIR_Breakout_-_170uA__EKMC4607112K_-01.jpg)](https://www.sparkfun.com/sparkfun-pir-breakout-170ua-ekmc4607112k.html)

### [SparkFun PIR Breakout - 170uA (EKMC4607112K)](https://www.sparkfun.com/sparkfun-pir-breakout-170ua-ekmc4607112k.html) 

[ SEN-17372 ]

Great for detecting motion in a small area & optimized for small movements to offer motion-sensing options for continuously p...

[\$21.50] [ [\$12.90] ]

[![SparkFun PIR Breakout - 1uA (EKMB1107112)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/6/4/0/5/17373-SparkFun_PIR_Breakout_-_1uA__EKMB1107112_-01.jpg)](https://www.sparkfun.com/sparkfun-pir-breakout-1ua-ekmb1107112.html)

### [SparkFun PIR Breakout - 1uA (EKMB1107112)](https://www.sparkfun.com/sparkfun-pir-breakout-1ua-ekmb1107112.html) 

[ SEN-17373 ]

Great for detecting motion in a small area and optimized for small movements to offer motion-sensing options for battery powe...

**Retired**

Passive Infrared (PIR) sensors do not return specific distance data like [distance sensors](https://www.sparkfun.com/distance_sensing). Instead, PIR sensors measure IR light coming from objects to detect motion in their field of view making them perfect for motion-sensing applications such as turning devices like lights, cameras, motors, etc. on automatically. The PIR sensors on these breakouts output a digital signal whenever a moving object is detected in the sensing area. That signal can be monitored by a microcontroller to trigger action on a connected device like those mentioned above.

If you would prefer to use these PIR sensors on an I^2^C bus, check out our Qwiic breakouts of the [170uA PIR](https://www.sparkfun.com/products/17374) and [1uA PIR](https://www.sparkfun.com/products/17375).

### Required Materials

In order to follow along with this tutorial you\'ll need a few items along with your PIR Breakout. First, you\'ll need a microcontroller or Single-Board Computer (SBC) like a Raspberry Pi or Jetson Nano to monitor the PIR\'s signal:

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Raspberry Pi 4 Model B (2 GB)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/2/1/15446-Raspberry_Pi_4_Model_B__2_GB_-01.jpg)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html)

### [Raspberry Pi 4 Model B (2 GB)](https://www.sparkfun.com/raspberry-pi-4-model-b-2-gb.html) 

[ DEV-15446 ]

The 2 GB Raspberry Pi 4 features the ability to run two 4k resolution monitors, to run true Gigabit Ethernet operations, all ...

[ [\$69.75] ]

[![SparkFun RedBoard Artemis](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/0/1/9/15444-SparkFun_RedBoard_Artemis-01.jpg)](https://www.sparkfun.com/sparkfun-redboard-artemis.html)

### [SparkFun RedBoard Artemis](https://www.sparkfun.com/sparkfun-redboard-artemis.html) 

[ DEV-15444 ]

The RedBoard Artemis takes the incredibly powerful Artemis module from SparkFun and wraps it up in an easy to use and familia...

[ [\$24.95] ]

[![NVIDIA Jetson Nano Developer Kit (V3)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/9/4/6/16271-NVIDIA_Jetson_Nano_Developer_Kit__V3_-01.jpg)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html)

### [NVIDIA Jetson Nano Developer Kit (V3)](https://www.sparkfun.com/nvidia-jetson-nano-developer-kit-v3.html) 

[ DEV-16271 ]

The NVIDIA® Jetson Nano™ Developer Kit V3 delivers the performance to run modern AI workloads at a small form factor, low ...

**Retired**

You also may need some wire and headers to connect your breakout to your microcontroller. Depending on your intended connections, you may want to use one or more of the following connection and wire options:

[![Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/7/0/4/11026-Jumper_Wires_Standard_7in._M_M_-_30_AWG__30_Pack_-01.jpg)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html)

### [Jumper Wires Standard 7\" M/M - 30 AWG (30 Pack)](https://www.sparkfun.com/jumper-wires-standard-7-m-m-30-awg-30-pack.html) 

[ PRT-11026 ]

If you need to knock up a quick prototype there\'s nothing like having a pile of jumper wires to speed things up, and let\'s fa...

[ [\$3.50] ]

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Straight Header - Female (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/5/00115-03-L.jpg)](https://www.sparkfun.com/female-headers.html)

### [Straight Header - Female (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/female-headers.html) 

[ PRT-00115 ]

Single row of 40-holes, female header. Can be cut to size with a pair of wire-cutters. Standard .1\" spacing. We use them exte...

[ [\$1.95] ]

[![Jumper Wires Premium 6\" M/F Pack of 10](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/7/09140-02-L.jpg)](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html)

### [Jumper Wires Premium 6\" M/F Pack of 10](https://www.sparkfun.com/jumper-wires-premium-6-m-f-pack-of-10.html) 

[ PRT-09140 ]

This is a SparkFun exclusive! These are 155mm long, 26 AWG jumper wires terminated as male to female. Use these to jumper fro...

[ [\$4.60] ]

Lastly, for easier testing of the range and detection area of your PIR Breakout installation, you may want to have an [LED](https://www.sparkfun.com/categories/89) or sound output like a [buzzer](https://www.sparkfun.com/categories/347) to act as an indicator for when the sensor detects motion.

### Recommended Tools

We recommend soldering to the PTH header on the PIR Breakouts for the best connection. If you do not have soldering tools and accessories, take a look at the following options:

[![Solder Lead Free - 100-gram Spool](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/7/3/09325_9161-Solder_Lead_Free_-_100-gram_Spool-01.jpg)](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html)

### [Solder Lead Free - 100-gram Spool](https://www.sparkfun.com/solder-lead-free-100-gram-spool.html) 

[ TOL-09325 ]

This is your basic spool of lead free solder with a water soluble resin core. 0.031\" gauge and 100 grams. This is a good spoo...

[ [\$15.50] ]

[![Soldering Iron - 60W (Adjustable Temperature)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/4/9/0/14456-01.jpg)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html)

### [Soldering Iron - 60W (Adjustable Temperature)](https://www.sparkfun.com/soldering-iron-60w-adjustable-temperature.html) 

[ TOL-14456 ]

This adjustable-temperature soldering iron is a great tool for when you don\'t want to break the bank but need a reliable iron...

[ [\$25.95] ]

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Weller WLC100 Soldering Station](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/1/7/3/14228-01.jpg)](https://www.sparkfun.com/products/14228)

### [Weller WLC100 Soldering Station](https://www.sparkfun.com/products/14228) 

[ TOL-14228 ]

The WLC100 from Weller is a versatile 5 watt to 40 watt soldering station that is perfect for hobbyists, DIYers and students....

**Retired**

### Suggested Reading

PIR sensors are pretty straight-forward and a great entry point for novices with embedded electronics and sensors but if you aren\'t familiar with the concepts covered in the tutorials linked below, you may want to take a look through them before getting started with the SparkFun PIR Breakout:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-4-kit-hookup-guide)

### Raspberry Pi 4 Kit Hookup Guide 

Guide for hooking up your Raspberry Pi 4 Model B basic, desktop, or hardware starter kit together.

## Hardware Overview

In this section we\'ll cover the characteristics and features of the PIR sensors on these breakouts.

### Panasonic EKM-Series PIR Sensors

The EKMC4607112K and EKMB1107112 from Panasonic are low-profile PIR sensors ideal for things like motion-activated lights, cameras or other electronics. Applications include automatic lighting for energy conservation, motion-activated security or trail cameras or maybe something fun like a [homemade convenience store chime (complete with a 100th customer celebration!)](https://learn.sparkfun.com/tutorials/papa-soundie-audio-player-hookup-guide#hardware-example-project-the-gag). The EKMC4607112K works best in a continuous power installation and has slightly better sensing performance than the EKMB1107112 which is best suited for battery and low-power installations.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![SparkFun PIR Breakout - 1uA Front.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/0/SparkFun_PIR_Breakout-Front.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/SparkFun_PIR_Breakout-Front.jpg)   [![SparkFun PIR Breakout - 1uA Back.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/0/SparkFun_PIR_Breakout_Back.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/SparkFun_PIR_Breakout_Back.jpg)
  *SparkFun PIR Breakout - 1µA Front.*                                                                                                                                                                                                  *SparkFun PIR Breakout - 1µA Back.*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

On each breakout we\'ve broken the sensor\'s three pins (3V3/VDD, Ground and OUT) to a standard 0.1\"-spaced PTH header for users to solder to. Take note that the sensors share the same PCB design and the version (**1µA** or **170µA**) is marked by the solder pads \"North\" of the PIR.

The two PIR sensors have very similar electrical and sensing characteristics with a few specific differences users will want to take note of prior to deciding which sensor is best for their situation. The tables below outline the Electrical and Detection Performance Characteristics to give users a basic overview. For a more detailed look at these two sensors, take a look at their respective specification sheets: [EKMC4607112K](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMC460711xK_Spec.pdf) & [EKMB1107112](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf) along with the [Panasonic PIR Sensors - Product Brief](https://cdn.sparkfun.com/assets/3/f/8/8/1/4541_fileversion.pdf) (EKM-Series sensors are covered on page 8).

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Electrical Characteristics                                                                                                                        |
+===========================+===============+===============+===============+===============+===============+=======================+===============+
|                           |               | EKMC4607112K                                  | EKMB1107112                                           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Characteristic            | Units         | Min           | Typ.          | Max           | Min           | Typ.                  | Max           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Operating Voltage         | VDC           | 3.0           | \-            | 6.0           | 2.3           | \-                    | 4.0           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Current Consumption\      | µA            | \-            | 170           | 300           | \-            | 1^[\[1\]](#PIRnote1)^ | 3             |
| (Sensor Only)             |               |               |               |               |               |                       |               |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Output Current            | µA            | \-            | \-            | 100           | \-            | \-                    | 100           |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Output Voltage            | VDC           | VDD-0.5       | \-            | \-            | VDD-0.5       | \-                    | \-            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Circuit Stability Time\   | secs          | \-            | \-            | 30            | \-            | 25                    | 210           |
| (when voltage is applied) |               |               |               |               |               |                       |               |
+---------------------------+---------------+---------------+---------------+---------------+---------------+-----------------------+---------------+

As we mentioned above, the sensing performances of the PIR Sensors are very similar with a few notable differences you\'ll want to be aware of to decide which one works best for your application. Also take note that PIR sensor performance can vary depending on the environment it is sensing.

Both the EKMC & EKMB have detection areas of 90° Horizontal and Vertical (±45°) and have 32 detection zones. The table below outlines their detection performance in relation to the background temperature:

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

[] [\[1\] Note:](https://learn.sparkfun.com/tutorials/sparkfun-pir-breakout-hookup-guide#PIRnote1) Current consumption for the EKMB1107112 varies depending on the operating mode. Refer to section 4-4 of the [Spec Sheet](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf) for specific values.

### Board Dimensions

The SparkFun PIR Breakout measures 0.50\" x 0.85\" (12.7mm x 21.59mm) and has one mounting hole that fits a [4-40 screw](https://www.sparkfun.com/products/10453).

[![PIR Breakout Board Dimensions](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/0/PIR_Breakout-Dimensions.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/PIR_Breakout-Dimensions.png)

## Hardware Assembly

Assembling the PIR Breakout circuit is pretty straight-forward since the board only has three pins. Recommended setup requires some soldering so if you are not familiar with through-hole soldering or want a refresher, we suggest reading through this tutorial:

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

September 19, 2013

This tutorial covers everything you need to know about through-hole soldering.

The demo circuit we\'ll assemble for the PIR Breakout uses a [standard breadboard](https://www.sparkfun.com/products/12002), [M/M Jumper Wires](https://www.sparkfun.com/products/9387) and a [SparkFun RedBoard Qwiic](https://www.sparkfun.com/products/15123) along with the SparkFun PIR and a set of [breakaway male headers - right angle](https://www.sparkfun.com/products/553).

For permanent installations, we recommend soldering wire directly to the PIR Breakout to create a strong and stable connection to the sensor. For some tips on preparing and soldering wire, take a look at this tutorial:

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

February 8, 2013

How to strip, crimp, and work with wire.

To start off, we break off three pins from the set of breakaway male headers and solder them to the PTH header on the PIR Breakout to have the sensor stand perpendicular to the breadboard for easy testing.

[![Headers soldered to PIR Breakout](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/0/PIR_Breakout_Hookup_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/PIR_Breakout_Hookup_Guide-05.jpg)

Next, we plug the sensor into the breadboard (users connecting directly to their microcontroller can ignore this step) taking care to orient it properly so the pins are not sharing the same rail. After the PIR is in place, select three jumper wires and connect the PIR\'s pins to the matching pins on the microcontroller. **3.3V** to **3.3V**, GND to Ground/GND and OUT to a digital I/O pin.

**Note:** If you choose to not use a dedicated **3.3V** pin for your PIR (e.g an alternate voltage or a digital pin) make sure the voltage it supplies falls within the operating voltage for the sensor:

- EKMC4607112K: **3.0** to **6.0V**
- EKMB1107112: **2.3** to **4.0V**

The OUT signal from the SparkFun PIR can also be used as an external interrupt to trigger an interrupt event on a microcontroller. Users who wish to use the PIR as an external interrupt should note which digital I/O pins on their microcontroller are interrupt-capable and connect the PIR\'s OUT to one of those pins. For this example, we\'ll connect the OUT pin to a digital pin that is also interrupt capable: **D2**.

[![Assembled PIR Breakout circuit with a RedBoard Qwiic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/4/0/0/PIR_Breakout_Hookup_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/PIR_Breakout_Hookup_Guide-04.jpg)

If you are using a Raspberry Pi or other SBC/development-board that uses Python as its primary programming language, follow the above assembly steps for the PIR and connect it to your Pi/SBC\'s GPIO header taking care to make the proper pin connections. Raspberry Pi users looking for a quick GPIO reference can find one [here](https://learn.sparkfun.com/tutorials/raspberry-gpio#gpio-pinout) or you can use the `pinout` command from the [GPIO Zero](https://gpiozero.readthedocs.io/) Python Library in the console to display the pinout there.

## Arduino Examples

Now that our SparkFun PIR Breakout circuit is assembled it\'s time to upload some code to our microcontroller to interact with the sensor. We\'ll cover three examples in this section to demonstrate how to read the signal, stabilize it and use it as an external interrupt to trigger events on a microcontroller.

### Example 1 - Simple Read with Debounce

This quick and dirty example monitors the PIR output signal on D2 and uses the built-in LED on the SparkFun RedBoard as a visual indicator whenever the PIR detects an object in it\'s field of view.

Copy the code below into a blank Arudino sketch, open the **Tools** menu to select your board (in our case, Arduino Uno) and correct Port and click the \"Upload\" button:

    language:c
    #define PIR_PIN 2   // PIR output on D2
    #define LED_PIN  13  // LED to illuminate on motion
    #define DEBOUNCE_TIME 750

    void setup() 
    
      Serial.println("PIR Warmed up.");
    }

    void loop() 
    
      else // Otherwise turn the LED off and print All Clear:
      
    }

After uploading, open the [serial monitor](https://learn.sparkfun.com/tutorials/terminal-basics) and set your baud to **115200** to see the serial data. The code will print out over serial any time the PIR detects motion in it\' field of view and the D13 LED should illuminate.

### Example 2 - Interrupt

The Interrupt Example shows how to set up the output signal from the PIR as an external interrupt to trigger an event on your microcontroller. This is particularly helpful for applications where you do not want to constantly poll the digital pin the PIR\'s output is connected to so you can run other loops in the background.

As we mentioned in the Hardware Assembly, this example assumes a SparkFun RedBoard/Arduino Uno is used and uses D2 as the interrupt pin. If you are using a different microcontroller, adjust the `PIR_PIN` definition to an interrupt-capable pin.

Copy the code below into a blank Arudino sketch, open the **Tools** menu to select your board (in our case, Arduino Uno) and correct Port and click the \"Upload\" button:

    language:c
    #define PIR_PIN 2 //Connect the output of the PIR to this pin
    #define DEBOUNCE_TIME 750

    bool pirStatus = false;
    bool lastPirStatus = pirStatus;

    void interruptRoutine() 

    void setup() 
      Serial.println("PIR Warmed up. Starting readings");
    }

    void loop() 
        else
        
        lastPirStatus = pirStatus;
      }
      delay(DEBOUNCE_TIME);
    }

From here, you can modify the code so the interrupt event triggers whatever behavior you would like. If you find the interrupt is firing too often, modify the code to trigger only on detected events or by modifying the interrupt type to be either `RISING` or `FALLING`.

## Python Example

**Note:** This example assumes you are using the latest version of Python 3. If this is your first time using Python or GPIO hardware on a Raspberry Pi, please read through our [Python Programming with the Raspberry Pi](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi) guide and the [Raspberry Pi GPIO Tutorial](https://learn.sparkfun.com/tutorials/raspberry-gpio/introduction).

If you\'ve assembled your SparkFun PIR Breakout circuit with a Raspberry Pi or other Python-based development board, we\'ve written a quick example to demonstrate how to read the PIR\'s output.

### Example Dependencies

In order to interface with your Pi\'s GPIO ports your user must be a member of the `gpio` group. The `pi` user is a member by default. Users with [**sudo**](https://en.wikipedia.org/wiki/Sudo) privileges can add users manually using the following command:

    language:bash
    sudo usermod -a -G gpio <username>

### Simple Read

This example demonstrates reading the SIG output from the PIR sensor using digital reads. Copy the code below into your preferred Python interpreter or into a blank text file and save it. If you are using an interpreter like Thonny, you can run it from there. Otherwise, open the terminal and run it by entering the following command: `python3 FILENAME.py`

    language:python
    import time
    import RPi.GPIO as GPIO
    import sys

    #Pin Definition
    pir_pin = 4

    #Set up pins and set PIR signal as an input
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_pin, GPIO.IN)

    def run_example():

        #Wait 30 seconds for the PIR to stabilize

        print ("Waiting 30 seconds for PIR to stabilize")
        for i in range(0, 30):
            print(i)
            time.sleep(1)

        print ("Device Stable. Starting readings...")

        #Start monitoring the PIR output. If an object is detected, print "Object Detected" otherwise print "All Clear"

        while True:
            if GPIO.input(pir_pin):
                print("Object Detected")
            else:
                print("All clear")
            time.sleep(1)

    if __name__ == '__main__':
        try:
            run_example()
        except (KeyboardInterrupt, SystemExit) as exErr:
            print("\nEnding Example")
            sys.exit(0)

## Troubleshooting

Hopefully by following the steps in this guide you\'ve got your SparkFun PIR Breakout up and running monitoring motion and reporting data to your preferred microcontroller or single-board computer. In case you run into any issues we\'ve outlined a few tips and tricks for testing the PIR here.

### Hardware Check

Most common problems with the PIR Breakout revolve around the hardware connections. If your PIR Breakout is not powering on or your microcontroller/SBC cannot detect the output signal from the sensor, double-check your solder joints and your wiring to the microcontroller/SBC. The [Hardware Checks](https://learn.sparkfun.com/tutorials/sparkfun-troubleshooting-tips#hardware-checks) section of our Troubleshooting Tips guide can help you diagnose any connection problems.

### Detection Area/Field of View

The effective detection area of both the EKMC4607112K and EKMB1107112 is dependent on a variety of factors. The specifications for measurement range are based on a target concept (area of \~700×250mm) of a human body moving across two detection zones at a speed of 1m/s. The PIR senses objects best when moving across two detection zones on the horizontal (X) or vertical (Y) axes. The PIR may struggle to detect objects moving away or toward the PIR (along the Z axis) unless they also move along the other two axes.

Also note that background IR radiation can influence the PIR\'s ability to detect an object. The PIR can detect objects with a larger temperature difference from the background at a larger range. Refer back to the Hardware Overview section for specific ranges and temperature differences.

Take these detection limitations into consideration when selecting the mounting position of your PIR Breakout. Section 4-7 of the sensors\' spec sheets ([EKMC4607112K](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMC460711xK_Spec.pdf) and [EKMB1107112](https://cdn.sparkfun.com/assets/learn_tutorials/1/4/0/0/EKMB110711x_Spec.pdf)) show diagrams for optimal placement and object motion for sensing.

### General Troubleshooting

If you need technical assistance and more information on this or another SparkFun product that is not working as you expected, we recommend heading on over to the SparkFun Technical Assistance page for some initial troubleshooting:

[SparkFun Technical Assistance Page](https://www.sparkfun.com/technical_assistance)

If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.