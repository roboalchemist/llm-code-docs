# Source: https://learn.sparkfun.com/tutorials/smart-plant-care-build-a-qwiic-soil-moisture-sensor-system

## Introduction

[![A plant that is happily watered using a remote monitoring system.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-5.jpg)

Have you ever wanted your plants to tell you how they\'re feeling? While we might be a ways away from understanding or communicating with plant consciousness, we can tell if they\'re thirsty or not, and with the [SparkFun Soil Moisture Sensor](https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor-1.html), you can do just that! This tutorial will show you how to take soil moisture readings and then display those readings on an OLED as a happy, meh, or sad face, depending on how wet or dry the soil is.

[![The three types of faces displayed on an OLED depending on how watered your plant is.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-3.jpg)

## Materials

### Required Materials

To follow along with the project at the end of this tutorial, you will need the following. You may not need everything, though, depending on what you already have and which sensor you prefer. Add it all to your cart and modify as necessary.

*Note: The 9V battery isn\'t suitable to keep plugged in for long periods of time. With this current configuration, the project will last plugged in for about a day. We recommend only powering the project when you want to see how your plant is feeling!*

[![SparkFun RedBoard Qwiic](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/9/2/15123-SparkFun_RedBoard_Qwiic-01a.jpg)](https://www.sparkfun.com/sparkfun-redboard-qwiic.html)

### [SparkFun RedBoard Qwiic](https://www.sparkfun.com/sparkfun-redboard-qwiic.html) 

[ DEV-15123 ]

The SparkFun RedBoard Qwiic is an Arduino-compatible development board with a built in Qwiic connector, eliminating the need ...

[ [\$21.95] ]

[![Flexible Qwiic Cable - 100mm](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/2/4/6/17259-Flexible_Qwiic_Cable_-_100mm-01.jpg)](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html)

### [Flexible Qwiic Cable - 100mm](https://www.sparkfun.com/flexible-qwiic-cable-100mm.html) 

[ PRT-17259 ]

This polarized I2C cable insulation is made from silicon making it more flexible than our original Qwiic cable particularly i...

[ [\$1.95] ]

[![SparkFun Micro OLED Breakout (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/2/2/5/5/8/22495-OLED-front.jpg)](https://www.sparkfun.com/sparkfun-micro-oled-breakout-qwiic-lcd-22495.html)

### [SparkFun Micro OLED Breakout (Qwiic)](https://www.sparkfun.com/sparkfun-micro-oled-breakout-qwiic-lcd-22495.html) 

[ LCD-22495 ]

The SparkFun Qwiic Micro OLED Breakout is a Qwiic enabled version of our popular MicroView and micro OLED display!

[ [\$11.25] ]

[![SparkFun Qwiic Soil Moisture Sensor](https://cdn.sparkfun.com/r/140-140/assets/parts/2/4/7/6/8/SEN-24409-Soil-Moisture-Sensor-Qwiic-Feature.jpg)](https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor-1.html)

### [SparkFun Qwiic Soil Moisture Sensor](https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor-1.html) 

[ SEN-24409 ]

A simple breakout for measuring the moisture in soil and similar materials. The exposed pads function together acting as a va...

[ [\$6.95] ]

[![9V Battery Holder](https://cdn.sparkfun.com/r/140-140/assets/parts/5/0/6/2/10512-01.jpg)](https://www.sparkfun.com/9v-battery-holder.html)

### [9V Battery Holder](https://www.sparkfun.com/9v-battery-holder.html) 

[ PRT-10512 ]

This 9V battery holder allows your battery to snap in tight and holds it in place, which is great in situations where you don...

[ [\$3.95] ]

[![9V Alkaline Battery](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/6/2/10218-01.jpg)](https://www.sparkfun.com/9v-alkaline-battery.html)

### [9V Alkaline Battery](https://www.sparkfun.com/9v-alkaline-battery.html) 

[ PRT-10218 ]

These are your standard 9 Volt alkaline batteries from Rayovac. Don\'t even think about trying to recharge these. Use them wit...

[ [\$2.40] ]

[![Unassembled materials for soil moisture sensor project.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-1.jpg)

## Hardware Setup

The hardware setup for this project is super straightforward. Attach the Qwiic Soil Moisture Sensor to the Qwiic OLED via a Qwiic Cable and then attach the OLED to the Redboard. We used a 9V battery and 9V battery holder to power this project so that we could keep it portable, but you could use a portable charger or hook it up straight to your computer depending on your use case and availability of parts on hand. We also used some screws and a 3D-printed base plate to keep the display and sensor together, but that is also not necessary. So simple!

[![Materials assembled for plant soil moisture sensor project connected with Qwiic cables.](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/Soil-Moisture-Sensor-2.jpg)

## Calibration

System Calibration To get any sort of useful data out of your Soil Moisture Sensor, it is advised that you calibrate it to whatever soil you plan to monitor. Different types of soil can affect the sensor, and you may get different readings from one composition tot he next. Before you start storing moisture data or triggering events based on that value, you should see what values you are actually getting from your sensor. Using the sketch above, note what values your sensor outputs when the sensor is completely dry vs when the sensor is completely submerged in a shallow cup of water. Depending on what microcontoller you\'re using, the operating voltage of that microcontoller, and the resolution of its analog-to-digital converter, you\'re results will vary.

For example, using the same circuit above, if I detach the VCC pin from D7 and attach it directly to the 5V supply on the RedBoard, you\'ll see the close to the following values in the serial monitor when the sensor is dry (\~0) and when it is completely saturated with moisture (\~880).

[![Example of soil moisture values.](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/5V_Cal.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/7/0/5/5V_Cal.png)