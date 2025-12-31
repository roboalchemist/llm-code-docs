# Source: https://learn.sparkfun.com/tutorials/buck-regulator-hookup-guide

## Introduction

Who doesn\'t occasionally need power regulation? We certainly do, so we\'ve designed the [SparkFun Buck Regulator Breakout](https://www.sparkfun.com/products/18356) and the [SparkFun BabyBuck Regulator Breakout](https://www.sparkfun.com/products/18357) to help us with just such a task.

Starring the AP63203 from Diodes Inc, both breakout boards take advantage of the 2A synchronous buck converter that has a wide input voltage range of 3.8V to 32V and fully integrated 125mΩ high-side power MOSFET/68mΩ lowside power MOSFET to provide high-efficiency step-down DC/DC conversion. All of this snuggled up in a a low-profile, TSOT26 package that\'s integrated into either a 1x1\" or 0.4x0.5\" board. For a wide variety of power management needs - grab yourself a Buck Regulator or Baby Buck Regulator and let\'s dive in!

[![SparkFun Buck Regulator Breakout - 3.3V (AP63203)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/7/0/3/18356-SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203_-01.jpg)](https://www.sparkfun.com/sparkfun-buck-regulator-breakout-3-3v-ap63203.html)

### [SparkFun Buck Regulator Breakout - 3.3V (AP63203)](https://www.sparkfun.com/sparkfun-buck-regulator-breakout-3-3v-ap63203.html) 

[ COM-18356 ]

Featuring the AP63203, this breakout board takes advantage of a 2A synchronous buck converter that has a wide input voltage r...

[ [\$7.50] ]

[![SparkFun BabyBuck Regulator Breakout - 3.3V (AP63203)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/7/7/0/5/18357-SparkFun_BabyBuck_Regulator_Breakout_-_3.3V__AP63203_-01.jpg)](https://www.sparkfun.com/sparkfun-babybuck-regulator-breakout-3-3v-ap63203.html)

### [SparkFun BabyBuck Regulator Breakout - 3.3V (AP63203)](https://www.sparkfun.com/sparkfun-babybuck-regulator-breakout-3-3v-ap63203.html) 

[ COM-18357 ]

Featuring the AP63203, this baby breakout board takes advantage of a 2A synchronous buck converter that has a wide input volt...

[ [\$4.95] ]

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything though depending on what you have. Add it to your cart, read through the guide, and adjust the cart as necessary.

### Tools

You will need a soldering iron, solder, and [general soldering accessories](https://www.sparkfun.com/categories/49).

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

### AP63203

The AP63203 is a 2A, synchronous buck converter from Diodes Inc that has a wide input voltage range (**3.8V** to **32V**) and provides high-efficiency step-down DC/DC conversion to **3.3V**. Frequency Spread Spectrum (FSS) reduces EMI and a proprietary gate driver scheme resists switching node ringing without sacrificing MOSFET turn-on and turn-off times, which further erases high-frequency radiated EMI noise. Full details can be found in the [datasheet](https://cdn.sparkfun.com/assets/e/3/d/9/d/AP63200-AP63201-AP63203-AP63205.pdf).

Features:

- VIN 3.8V to 32V
- Up to 2A Continuous Output Current
- 0.8V ± 1% Reference Voltage
- 22µA Ultralow Quiescent Current
- Switching Frequency - 1.1MHz
- Supports Pulse Frequency Modulation (PFM)
  - Up to 80% Efficiency at 1mA Light Load
  - Up to 88% Efficiency at 5mA Light Load
- Fixed Output Voltage - 3.3V
- Proprietary Gate Driver Design for Best EMI Reduction
- Frequency Spread Spectrum (FSS) to Reduce EMI
- Precision Enable Threshold to Adjust UVLO
- Protection Circuitry
  - Overvoltage Protection
  - Cycle-by-Cycle Peak Current Limit
  - Thermal Shutdown

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-AP63203-Updated1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-AP63203-Updated1.jpg)   [![](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18357-SparkFun-BabyBuck-Regulator-Breakout-AP63203-Updated1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18357-SparkFun-BabyBuck-Regulator-Breakout-AP63203-Updated1.jpg)\

  *AP63203 on the Buck Regulator*                                                                                                                                                                                                                   *AP63203 on the Baby Buck Regulator*
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power

For the Buck Regulator, input power can be supplied in a number of ways. There are screw terminals on the right side of the board, solder pads for a [barrel jack](https://www.sparkfun.com/products/119), which can be mounted on the top or bottom side of the board, and the plated through holes on the left side of the board can all be used as input. Output can be obtained via the screw terminals or the plated through holes.

[![Power options for the Buck Regulator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-PowerOptions.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-PowerOptions.jpg)

The Baby Buck sacrifices flexibility for space. Use the plated through holes for input and output power.

[![Plated through holes on the baby buck used for input and output](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/18357-SparkFun-BabyBuck-Regulator-Breakout-Pins.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18357-SparkFun-BabyBuck-Regulator-Breakout-Pins.jpg)

Both the Buck Regulator as well as the Baby Buck Regulator ratchet the output voltage down to **3.3V**. Be mindful that thermal properties change as Vin increases.

### Thermal Characteristics

One of the benefits of a buck converter over a linear regulator is their superior efficiency at stepping down the voltage. Unfortunately though, heat can still be a problem, particularly as the difference between the input and output voltage increases.

One of the trade-offs of the small size of the BabyBuck is because there is less copper to pull heat away from switching IC, the maximum output current available is reduced due to the thermal protections. Refer to the graphs below to see the how hot you can expect the AP63203 to get at various loads and supply voltages.

[![Baby Buck regulator thermal characteristics](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/BabyBuck_Thermal_Characteristics.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/BabyBuck_Thermal_Characteristics.png)

[![Buck regulator thermal characteristics](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/1x1_Buck_Thermal_Characteristics.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/1x1_Buck_Thermal_Characteristics.png)

To dissipate some of the excess heat, we\'ve added a copper pad for a heat sink on the back of the 1\" x 1\" Buck Regulator Board. Use one of our [small heatsinks](https://www.sparkfun.com/products/11510) and attach it with some [thermal tape](https://www.sparkfun.com/products/17054).

[![Heatsink Pad](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-HeatsinkPad.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-HeatsinkPad.jpg)

### Power LED and Jumper

On the 1\" x 1\" Buck Regulator, there is a power LED available for use.

[![Power LED is on the front of the Buck Regulator, below the AP63203 ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-PwrLED.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-PwrLED.jpg)

To disable this LED, cut the Jumper on the back of the board:

[![LED Jumper is to the left of the heatsink pad on the back of the Buck Regulator board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-LEDJumper.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/18356-SparkFun-Buck-Regulator-Breakout-LEDJumper.jpg)

### Board Outline

#### Buck Board Outline:

[![Outline and measurements of the SparkFun Buck Regulator Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/BuckBoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/BuckBoardOutline.png)

#### Baby Buck Board Outline:

[![Outline and measurements of the SparkFun Baby Buck Regulator Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/BabyBuckBoardOutline.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/BabyBuckBoardOutline.png)

## Hardware Hookup

There are three options when using the 1\" x 1\" Buck Regulator.

### Screw terminals

To use the screw terminals, simply insert the correct wires into the screw terminal opening and gently tighten the screw for that port. Your board should look similar to the following:

[![Screw terminals on the right side of the Buck Regulator Board with wires inserted and screws tightened](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-02.jpg)

### Barrel Jack

To use a barrel jack for input, grab one of our [PTH Mount Barrel Jack Connectors](https://www.sparkfun.com/products/119) and [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) that sucker on. It should look something like what you see here:

[![Barrel Jack fits to the board faceing out](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-01.jpg)

### PTH Pins

To use the plated through holes on either the Buck Regulator or the Baby Buck Regulator, you\'ll need to [solder](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) either [straight headers](https://www.sparkfun.com/products/116) or [angle headers](https://www.sparkfun.com/products/553) to the board.

[![Headers soldered to the PTH pins on both the Buck Regulator and the Baby Buck Regulator](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/8/9/0/SparkFun_Buck_Regulator_Breakout_-_3.3V__AP63203__Hookup_Guide-03.jpg)

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.