# Source: https://learn.sparkfun.com/tutorials/buck-boost-hookup-guide

## Introduction

We got tha powah! The [Buck-Boost Converter](https://www.sparkfun.com/products/15208) is the latest breakout from SparkFun that allows you to fine tune the amount of power your project receives. It can take an input voltage of anywhere from **3-16V** which can then be regulated to an output voltage between **2.5-9V**. With the switch on the bottom of the board, you can set the common output voltages of 3.3V and 5V, but we\'ve also broken out a custom setting that allows you to populate a resistor based on your custom voltage needs. What\'s more, we have broken out the GPIO pins along the top of the board for even more control. Get your boost on!

[![SparkFun Buck-Boost Converter](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/6/3/9/15208-SparkFun_Buck-Boost_Converter-01.jpg)](https://www.sparkfun.com/sparkfun-buck-boost-converter.html)

### [SparkFun Buck-Boost Converter](https://www.sparkfun.com/sparkfun-buck-boost-converter.html) 

[ COM-15208 ]

The SparkFun Buck-Boost Converter is a handy power accessory board that allows you to fine tune the amount of power your proj...

[ [\$13.21] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You may also need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

### Suggested Reading

If you aren't familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/logic-levels)

### Logic Levels 

Learn the difference between 3.3V and 5V devices and logic levels.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

## Hardware Overview

The Buck-Boost board is centered around the TPS63070 Buck-Boost converter, which will take your input power and either regulate the output voltage up or down to your set output voltage. In this section we\'ll take a closer look at how the converter works and how you can incorporate into your next project.

[![Buck-Boost board](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-01.jpg)

### Power Pins

[![Power connections highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Power_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Power_Highlight.jpg)

The Buck-Boost board has an input voltage range of **3-16V**. You can supply power by either soldering wires directly to the board or by using our [3.5mm screw terminals](https://www.sparkfun.com/products/8084).

[![Buck-Boost with screw terminals](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-01.jpg)

The output is adjustable from **2.5-9V** using the single-pole-triple-throw switch. The board is configured with two of the more common voltages you might use, **3.3V** and **5V**, but there\'s a unpopulated PTH resistor to allow for setting a specific voltage.

### Setting The Output Voltage

[![Highlight of voltage selection switch](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Voltage_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Voltage_Switch.jpg)

The output voltage of the Buck-Boost is set by voltage divider connected to the feedback pin. The Buck-Boost board has one fixed resistor at 68.1kΩ and the switch changes the second resistor between VOUT and the feedback pin. To change the output voltage, move the switch to one of the three positions for 3.3V, 5V, or CUST. The CUST position is there to allow you to set the voltage to whatever you need by soldering a resistor to the PTH resistor pads highlighted below.

[![Custom resistor highlight](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Custom_Voltage_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_Custom_Voltage_Highlight.jpg)

Use the equation below to determine the resistor value needed based on the desired output voltage.

[![Equation to calculate resistor value](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/ResistorEquation.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/ResistorEquation.gif)

### I/O pins

The Buck-Boost board will work out of the box, but if you need a little bit more control, most of the extra pins have been broken out, as shown below.

[![Highlight of I/O pins](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_IO_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_IO_Highlight.jpg)

  Pin        Description
  ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **VIN**    Supply voltage for power stage. Can be used to pass power to the rest of the project, or used to set the logic level.
  **EN**     Enable input. Pull high to enable the device. Pull Low to disable the device. **Default: HIGH** through 10kΩ pull-up resistor to VIN.
  **GND**    Ground. Can be used to set I/O pin low.
  **PS**     Power Save. Pull low for forced PWM. Pull high for power save mode. In power save mode, the switching frequency will adjust to the most efficient frequency. You can also apply a clock signal to synchronize to an external frequency. **Default: HIGH** through 10kΩ pull-up resistor to VIN.
  **PG**     Power good open drain output.
  **VOUT**   Additional buck-boost converter output.

### PWR LED

[![Highlight of power LED](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_PWR_LED_Highlight.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/15208-SparkFun_Buck-Boost_Converter-04_PWR_LED_Highlight.jpg)

The power LED indicates red when voltage is present on the output pins. Because the LED has a fixed 1k current limiting resistor in series, the brightness of the LED will vary depending on the output voltage. The LED can be disabled by cutting the jumper on the back of the board as shown below.

[![Cutting LED jumper](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-02-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-02-03.jpg)

## Buck-Boost Tips and Tricks

### Maximum Output Current VS Input Voltage

One of the benefits of the Buck-Boost, aside from boosting the output voltage up from a lower input voltage, is it uses a switching DC/DC converter, which is more efficient than a linear regulator. More efficiency means less energy is wasted in the form of heat. However, that doesn\'t mean the TPS63070 doesn\'t get hot under load. The TPS63070 has an operating die temperature range of -40 to +125°C, using the graphs below should provide a good rule of thumb for the maximum output current available at various output voltages as a function of the input voltage.

The temperature was recorded using a FLIR camera with an air temperature of 25°C, with a maximum case temperature of 100°C. Each output voltage graph has a showing the maximum output current both with and without a [heatsink](https://www.sparkfun.com/products/11510).

[![Maximum Output Current Graphs](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Maximum_Output_Current_Graphs.png)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Maximum_Output_Current_Graphs.png)

**Click on the photo for full resolution**

### Adding a Heatsink

In the maximum output current section, the graphs are shown both with and without a heatsink. The benefit of a heatsink is it provides more surface area for the air to dissipate the heat, which will allow the Buck-Boost board to output the maximum amount of current across a wider input voltage range. To add a heatsink you\'ll need two of our products: a [heatsink (of course)](https://www.sparkfun.com/products/11510), and our [thermal tape](https://www.sparkfun.com/products/9771).

To add a heatsink first cut the thermal tape to rough size:

[![Thermal tape cut to rough size](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-04.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-04.jpg)

Peel off one of the protective coverings and attach heatsink to thermal tape:

[![Heatsink connected to thermal tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-05.jpg)

With a [hobby knife](https://www.sparkfun.com/products/9200), follow the perimeter of the heatsink to cut the tape to it\'s final size:

[![Cutting thermal tape](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-08.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-08.jpg)

Remove the remaining protective covering of the tape and attach the heatsink to the TPS63070, trying to center the heatsink over the IC:

[![Heatsink attached to board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/9/5/Buck_-_Boost_Hook_Up_Guide-09.jpg)

### Connecting your Load

Depending on the size of the load connected to the output, you may need to wait between when the enable pin is pulled high and the load is connected to the board. The time delay is relatively short (\~10ms), but it shouldn\'t be a problem if the load is **\<800mA at 3.3V**, or **\<700mA at 5.0V**. If the custom resistor is populated to output a voltage **greater than 5V**, you should be able to leave the load connected if the load is **\<650mA**.