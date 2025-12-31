# Source: https://learn.sparkfun.com/tutorials/getting-started-with-load-cells

## Introduction

Have you ever wanted to know the weight of something? How about knowing the change in weight over time? Do you want your project to sense the presence of something by measuring strain or a load on some surface? If so, you\'re in the right place. This tutorial is here to help you get started in the world of load cells and their variants.

[![SparkFun bar load cell](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/13329-01Crop.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/13329-01Crop.jpg)

*One of many kinds of load cells.*

### Suggested readings:

Before jumping into load cells and all of their awesomeness, we suggest you familiarize yourself with some basic concepts if you haven\'t already:

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/voltage-dividers)

### Voltage Dividers 

Turn a large voltage into a smaller one with voltage dividers. This tutorial covers: what a voltage divider circuit looks like and how it is used in the real world.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)

### Series and Parallel Circuits 

An introduction into series and parallel circuits.

[](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic)

### How to Read a Schematic 

An overview of component circuit symbols, and tips and tricks for better schematic reading. Click here, and become schematic-literate today!

## Load Cell Basics

### Types of Load Cells

A load cell is a physical element (or transducer if you want to be technical) that can translate pressure (force) into an electrical signal.

So what does that mean? There are three main ways a load cell can translate an applied force into a measurable reading.

#### Hydraulic Load Cells

Hydraulic load cells use a conventional piston and cylinder arrangement to convey a change in pressure by the movement of the piston and a diaphragm arrangement which produces a change in the pressure on a Bourdon tube connected with the load cells.

[![Diagram of a Hydraulic Load Cell](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/hyd_dia3.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/hyd_dia3.gif)

*Diagram of a Hydraulic Load Cell from [Nikka\'s Rocketry](http://www.nakka-rocketry.net/hydlc.html)*

#### Pneumatic Load Cells

Pneumatic load cells use air pressure applied to one end of a diaphragm, and it escapes through the nozzle placed at the bottom of the load cell, which has a pressure gauge inside of the cell.

[![Diagram of a pneumatic load cell](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/Pneumatic-Load-Cell.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/Pneumatic-Load-Cell.jpg)

*Diagram of a pneumatic load cell from [Instrumentation Today](http://www.instrumentationtoday.com/force-transducers/2011/07/)*

#### Strain Gauge Load Cells

And lastly (though there are many other less common load cell set ups), there is a strain gauge load cell, which is a mechanical element of which the force is being sensed by the deformation of a (or several) strain gauge(s) on the element.

[![Strain gauge load cell diagram](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/loadcell.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/loadcell.gif)

*Strain gauge load cell diagram from [Scalenet.com](http://www.scalenet.com/applications/glossary.html)*

In bar strain gauge load cells, the cell is set up in a \"Z\" formations so that torque is applied to the bar and the four strain gauges on the cell will measure the bending distortion, two measuring compression and two tension. When these four strain gauges are set up in a wheatstone bridge formation, it is easy to accurately measure the small changes in resistance from the strain gauges.

[![Diagram of strain gauges on bar load cells](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/img0054.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/img0054.png)

*More in depth diagram of strain gauges on bar load cells when force is applied*

In this tutorial, we will be focusing on strain gauge load cells like the [ones SparkFun carries](https://www.sparkfun.com/categories/143):

[![Load Cell - 5kg, Straight Bar (TAL220B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/5/6/14729-Mini_Load_Cell_-_5kg__Straight_Bar__TAL220B_-01.jpg)](https://www.sparkfun.com/load-cell-5kg-straight-bar-tal220b.html)

### [Load Cell - 5kg, Straight Bar (TAL220B)](https://www.sparkfun.com/load-cell-5kg-straight-bar-tal220b.html) 

[ SEN-14729 ]

This straight bar load cell (sometimes called a strain gauge) can translate up to 5kg of pressure (force) into an electrical ...

[ [\$15.50] ]

[![Load Cell - 10kg, Straight Bar (TAL220)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/2/9/13329-01.jpg)](https://www.sparkfun.com/load-cell-10kg-straight-bar-tal220.html)

### [Load Cell - 10kg, Straight Bar (TAL220)](https://www.sparkfun.com/load-cell-10kg-straight-bar-tal220.html) 

[ SEN-13329 ]

This straight bar load cell (sometimes called a strain gauge) can translate up to 10kg of pressure (force) into an electrical...

[ [\$12.95] ]

[![Mini Load Cell - 500g, Straight Bar (TAL221)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/5/5/14728-Mini_Load_Cell_-_500g__Straight_Bar__TAL221_-01.jpg)](https://www.sparkfun.com/mini-load-cell-500g-straight-bar-tal221.html)

### [Mini Load Cell - 500g, Straight Bar (TAL221)](https://www.sparkfun.com/mini-load-cell-500g-straight-bar-tal221.html) 

[ SEN-14728 ]

This straight bar load cell (sometimes called a strain gauge) can translate up to 500g of pressure (force) into an electrical...

[ [\$15.50] ]

[![Mini Load Cell - 100g, Straight Bar (TAL221)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/9/5/4/14727-Mini_Load_Cell_-_100g__Straight_Bar__TAL221_-01.jpg)](https://www.sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html)

### [Mini Load Cell - 100g, Straight Bar (TAL221)](https://www.sparkfun.com/mini-load-cell-100g-straight-bar-tal221.html) 

[ SEN-14727 ]

This straight bar load cell (sometimes called a strain gauge) can translate up to 100g of pressure (force) into an electrical...

[ [\$14.50] ]

[![Load Cell - 200kg, S-Type (TAS501)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/2/3/8/14282-01.jpg)](https://www.sparkfun.com/load-cell-200kg-s-type-tas501.html)

### [Load Cell - 200kg, S-Type (TAS501)](https://www.sparkfun.com/load-cell-200kg-s-type-tas501.html) 

[ SEN-14282 ]

This S-Type load cell (sometimes called a strain gauge) can translate up to 200kg of pressure (force) into an electrical sign...

[ [\$96.95] ]

[![Load Cell - 50kg, Disc (TAS606)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/3/1/13331-01.jpg)](https://www.sparkfun.com/load-cell-50kg-disc-tas606.html)

### [Load Cell - 50kg, Disc (TAS606)](https://www.sparkfun.com/load-cell-50kg-disc-tas606.html) 

[ SEN-13331 ]

This single disc load cell (sometimes called a strain gauge) can translate up to 50kg of pressure (force) into an electrical ...

[ [\$99.95] ]

[![Load Cell - 200kg, Disc (TAS606)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/3/2/13332-01.jpg)](https://www.sparkfun.com/load-cell-200kg-disc-tas606.html)

### [Load Cell - 200kg, Disc (TAS606)](https://www.sparkfun.com/load-cell-200kg-disc-tas606.html) 

[ SEN-13332 ]

This disc load cell (sometimes called a strain gauge) can translate up to a whopping 200kg of pressure (force) into an electr...

[ [\$99.95] ]

[![Load Cell - 10kg, Straight Bar with Hook](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/4/9/8/21669-_SEN-_01.jpg)](https://www.sparkfun.com/load-cell-10kg-straight-bar-with-hook.html)

### [Load Cell - 10kg, Straight Bar with Hook](https://www.sparkfun.com/load-cell-10kg-straight-bar-with-hook.html) 

[ SEN-21669 ]

This straight bar load cell (sometimes called a strain gauge) can translate up to 10kg of pressure (force) into an electrical...

[ [\$19.95] ]

Most strain gauge load cells work in very similar ways, but may vary in size, material, and mechanical setup, which can lead to each cell having different max loads and sensitivities that they can handle. For a few possible load cell mechanical setups, check out the hookup guide with the [load cell setup](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#load-cell-setup).

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Bar-Type Load Cell in Between Two Plates](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/3/HX711_and_Combinator_board_hook_up_guide-02.jpg)](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#load-cell-setup)
  *[One Possible Load Cell Setup with the Bar-Type Load Cell](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#load-cell-setup)*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Strain Gauge Basics

A strain gauge is a device that measures electrical resistance changes in response to, and proportional of, strain (or pressure or force or whatever you so desire to call it) applied to the device. The most common strain gauge is made up of very fine wire, or foil, set up in a grid pattern in such a way that there is a linear change in electrical resistance when strain is applied in one specific direction, most commonly found with a base resistance of 120Ω, 350Ω, and 1,000Ω.

### Gauge Factor

Each strain gauge has a different sensitivity to strain, which is expressed quantitatively as the **gauge factor (GF)**. The gauge factor is defined as the ratio of fractional change in electrical resistance to the fractional change in length (strain). (The gauge factor for metallic strain gauges is typically around 2.)

### Small Changes in Strain

We set up a strain gauge load cell and measure that change in resistance and all is good, right? Not so fast. Strain measurements rarely involve quantities larger than a few millistrain [![](http://latex.codecogs.com/gif.latex?(e&space;\cdot&space;10%5E%7B-3%7D) "(e \cdot 10^)")](http://www.codecogs.com/eqnedit.php?latex=(e&space;\cdot&space;10%5E%7B-3%7D)) (fancy units for strain, but still very small).

So lets take an example: suppose you put a strain of 500µε. A strain gauge with a gauge factor of 2 will have a change in electrical resistance of only:\

[![](http://latex.codecogs.com/gif.latex?2&space;*&space;(500&space;*&space;10%5E-%5E6)&space;=&space;0.1% "2 * (500 * 10^-^6) = 0.1%")](http://www.codecogs.com/eqnedit.php?latex=2&space;*&space;(500&space;*&space;10%5E-%5E6)&space;=&space;0.1%)

For a 120Ω gauge, this is a change of only 0.12Ω. 0.12Ω is a very small change, and, for most devices, couldn\'t actually be detected, let alone detected accurately. So we are going to need another device that can either accurately measure super small changes in resistance (spoiler: they are very expensive) or a device that can take that very small change in resistance and turn it into something that we can measure accurately.

### Amplifiers and Wheatstone Bridge

This is where an amplifier, such as the [HX711](https://www.sparkfun.com/products/13879) or the [NAU7802](https://www.sparkfun.com/products/15242) comes in handy.

[![SparkFun Load Cell Amplifier - HX711](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/5/1/0/13879-SparkFun_Load_Cell_Amplifier_-_HX711-01.jpg)](https://www.sparkfun.com/sparkfun-load-cell-amplifier-hx711.html)

### [SparkFun Load Cell Amplifier - HX711](https://www.sparkfun.com/sparkfun-load-cell-amplifier-hx711.html) 

[ SEN-13879 ]

The SparkFun Load Cell Amplifier is a small breakout board for the HX711 IC that allows you to easily read load cells to meas...

[ [\$11.50] ]

[![SparkFun Qwiic Scale - NAU7802](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/7/0/0/15242-SparkFun_Qwiic_Scale_-_NAU7802-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-scale-nau7802.html)

### [SparkFun Qwiic Scale - NAU7802](https://www.sparkfun.com/sparkfun-qwiic-scale-nau7802.html) 

[ SEN-15242 ]

The SparkFun Qwiic Scale - NAU7802 is a small breakout board for the NAU7802 that allows you to easily read load cells to mea...

[ [\$18.50] ]

A good way of taking small changes in resistance and turning it into something more measurable is using a [wheatstone bridge](http://en.wikipedia.org/wiki/Wheatstone_bridge). A wheatstone bridge is a configuration of four resistors with a known voltage applied like this:

[![Wheatstone Bridge](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/wheatstone_bridge.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/wheatstone_bridge.gif)

where Vin is a known constant voltage, and the resulting Vout is measured. If [![](http://latex.codecogs.com/gif.latex?R1/R2&space;=&space;R3/R4 "R1/R2 = R3/R4")](http://www.codecogs.com/eqnedit.php?latex=R1/R2&space;=&space;R3/R4), then Vout is 0, but if there is a change to the value of one of the resistors, Vout will have a resulting change that can be measured and is governed by the following equation using Ohm\'s law:

[![](https://latex.codecogs.com/gif.image?\dpi%7B110%7DV_%7Bout%7D&space;=&space;%5BR3/(R3+R4)&space;-&space;R1/(R1+R2)%5D\times&space;V_%7Bin%7D "https://latex.codecogs.com/gif.image?\dpiV_ = [R3/(R3+R4) - R1/(R1+R2)]\times V_")](https://editor.codecogs.com/)

***or***

[![](https://latex.codecogs.com/gif.image?\dpi%7B110%7DV_%7Bout%7D&space;=&space;%5BR2/(R1+R2)&space;-&space;R4/(R3+R4)%5D\times&space;V_%7Bin%7D "https://latex.codecogs.com/gif.image?\dpiV_ = [R2/(R1+R2) - R4/(R3+R4)]\times V_")](https://editor.codecogs.com/)

By replacing one of the resistors in a wheatstone bridge with a strain gauge, we can easily measure the change in Vout and use that to assess the force applied.

[![Wheatstone Bridge with Strain Gauges](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/00431.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/2/00431.png)

*Bar load cell wheatstone bridge example From [All About Circuits](http://www.allaboutcircuits.com/textbook/direct-current/chpt-9/strain-gauges/)*

## Combinator Basics

But what happens when you don\'t have a load cell with four strain gauges? Or you want to measure something really heavy on something scale like? You can combine four single strain gauge load cells (sometimes referred to as [Load sensors](https://www.sparkfun.com/products/10245)) using the [load sensor combinator breakout board](https://www.sparkfun.com/products/13878)!

[![Load Sensors from a Bathroom Scale](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/3/HX711_and_Combinator_board_hook_up_guide-09.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/3/HX711_and_Combinator_board_hook_up_guide-09.jpg)

*Bathroom scale using the [Load Sensor Combinator](https://www.sparkfun.com/products/13281) to combine twelve wires into one wheatstone bridge*

Using the same wheatstone bridge principle, you can use the combinator to combine the single strain gauge load cells into a wheatstone bridge configuration where the force applied to all four single strain gauge load cells is added to give you a higher maximum load, and better accuracy than just one. The combinator can be hooked up to the same amplifier for easier measuring.

[![Four Load Cells Connected to Combinator and HX711 Amplifier](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/3/HX711_and_Combinator_board_hook_up_guide-11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/3/HX711_and_Combinator_board_hook_up_guide-11.jpg)

*Load cells connected to combinator and HX711 amplifier*

This is the same layout that you would find in say your home scale. There would be four single strain gauge load cells hooked up to a [combinator](https://www.sparkfun.com/products/13281) and an [amplifier](https://www.sparkfun.com/products/13230) to give you your weight reading. For more information about setting up the four single strain gauges with the combinator, check out the [combinator\'s hardware hookup for the HX711](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#combinator). This setup can also be used with the NAU7802.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Singe Strain Load Sensors Connected in Wheatstone Bridge Configuration using Combinator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/4/6/Wheatstone_Bridge_Load_Sensor_bb_Fritzing.jpg)](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#combinator)
  *[Four Single Strain Gauges Arranged in a Wheatstone Bridge with the Combinator](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide#combinator)*
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------