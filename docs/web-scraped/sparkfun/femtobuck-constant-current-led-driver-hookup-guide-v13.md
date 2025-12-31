# Source: https://learn.sparkfun.com/tutorials/femtobuck-constant-current-led-driver-hookup-guide-v13

## Introduction

**Note:** This tutorial is for the latest version of the FemtoBuck, V12. If you have an older version of the FemtoBuck, please consult [this guide](https://learn.sparkfun.com/tutorials/retired---femtobuck-constant-current-led-driver-hookup-guide).

The [FemtoBuck](https://www.sparkfun.com/products/13716) is a small-size, single-output constant current [LED](https://www.sparkfun.com/leds) driver. By default, the FemtoBuck is driven at 330mA. That current can be reduced by either presenting an analog voltage or a PWM signal to the board. It can be increased to 660mA by closing a solder jumper on the board, as described later in this tutorial.

[![FemtoBuck LED Driver](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/2/1/0/13716-01.jpg)](https://www.sparkfun.com/femtobuck-led-driver.html)

### [FemtoBuck LED Driver](https://www.sparkfun.com/femtobuck-led-driver.html) 

[ COM-13716 ]

This is the FemtoBuck, a small-size single-output constant current LED driver. Each FemtoBuck has the capability to dim a sin...

[ [\$8.95] ]

### Suggested Reading

Here are some topics you should know before using the FemtoBuck. Have a look if you need more information.

[](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)

### Voltage, Current, Resistance, and Ohm\'s Law 

Learn about Ohm\'s Law, one of the most fundamental equations in all electrical engineering.

[](https://learn.sparkfun.com/tutorials/pulse-width-modulation)

### Pulse Width Modulation 

An introduction to the concept of Pulse Width Modulation.

[](https://learn.sparkfun.com/tutorials/resistors)

### Resistors 

A tutorial on all things resistors. What is a resistor, how do they behave in parallel/series, decoding the resistor color codes, and resistor applications.

[](https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds)

### Light-Emitting Diodes (LEDs) 

Learn the basics about LEDs as well as some more advanced topics to help you calculate requirements for projects containing many LEDs.

[](https://learn.sparkfun.com/tutorials/electric-power)

### Electric Power 

An overview of electric power, the rate of energy transfer. We\'ll talk definition of power, watts, equations, and power ratings. 1.21 gigawatts of tutorial fun!

## FemtoBuck Overview

### Connecting the FemtoBuck

For the version 1.2 of the FemtoBuck, we\'ve increased the voltage ratings on the parts to allow the input voltage to cover the **full 36V range** of the AL8860. Note that the supply voltage must be at least 6.0V, and should be at least 2-3V higher than the forward voltage of the LED(s) to be driven. You can use the board to drive any high power LED like the ones listed below. Keep in mind that you would need 3x FemtoBucks to control each channel on the triple output high power RGB LED.

[![Triple Output High Power RGB LED](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/6/2/4/15200-Triple_Output_High_Power_RGB_LED-01.jpg)](https://www.sparkfun.com/triple-output-high-power-rgb-led.html)

### [Triple Output High Power RGB LED](https://www.sparkfun.com/triple-output-high-power-rgb-led.html) 

[ COM-15200 ]

This 3W per channel, Triple Output High Power RGB LED is sure to shed a lot of light on any project you add it to.

[ [\$6.95] ]

[![LED - 3W Aluminum PCB (5 Pack, Warm White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/3/13104-00.jpg)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-warm-white.html)

### [LED - 3W Aluminum PCB (5 Pack, Warm White)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-warm-white.html) 

[ COM-13104 ]

So much power and light from such a small package. This 5 pack of \"Warm\" white 3 Watt aluminum backed PCBs is sure to shed a ...

[ [\$12.45] ]

[![LED - 3W Aluminum PCB (5 Pack, Cool White)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/4/13105-00.jpg)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html)

### [LED - 3W Aluminum PCB (5 Pack, Cool White)](https://www.sparkfun.com/led-3w-aluminum-pcb-5-pack-cool-white.html) 

[ COM-13105 ]

So much power and light from such a small package. This 5 pack of \"Cool\" white 3 Watt aluminum backed PCBs is sure to shed a ...

[ [\$12.45] ]

[![LED - 3W Aluminum PCB (5 Pack, Red)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/5/13106-00.jpg)](https://www.sparkfun.com/products/13106)

### [LED - 3W Aluminum PCB (5 Pack, Red)](https://www.sparkfun.com/products/13106) 

[ COM-13106 ]

So much power and light from such a small package. This 5 pack of red 3 Watt aluminum backed PCBs is sure to shed a lot of li...

**Retired**

[![LED - 3W Aluminum PCB (5 Pack, Blue)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/1/5/6/13107-00.jpg)](https://www.sparkfun.com/products/13107)

### [LED - 3W Aluminum PCB (5 Pack, Blue)](https://www.sparkfun.com/products/13107) 

[ COM-13107 ]

So much power and light from such a small package. This 5 pack of blue 3 Watt aluminum backed PCBs is sure to shed a lot of l...

**Retired**

[![LED - 3W Aluminum PCB (5 Pack, Green)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/3/2/2/13185-01.jpg)](https://www.sparkfun.com/products/13185)

### [LED - 3W Aluminum PCB (5 Pack, Green)](https://www.sparkfun.com/products/13185) 

[ COM-13185 ]

So much power and light from such a small package. This 5 pack of green 3 Watt aluminum backed PCBs is sure to shed a lot of ...

**Retired**

Since the FemtoBuck is a constant current driver, the current drawn from the supply will drop as supply voltage rises. In general, efficiency of the FemtoBuck is around 95%, depending on the input voltage.

[![Labeled picture](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/13716-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/13716-02.png)

One signal input is provided for dimming control. A ground pin (DGND) is provided to reference against the controlling module for accuracy. Dimming can be done by an analog voltage (20%-100% of max current by varying voltage from .5V-2.5V) or by PWM (so long as PWM minimum voltage is less than .4V and maximum voltage is more than 2.4V) for a full 0-100% range.

Another ground (PGND) pin is available next to the power supply pin to provide a high-current return path. The spacing on the four holes on the input side is 0.1\" for [standard headers](https://www.sparkfun.com/products/553).

[![Straight Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/6/00116-02-L.jpg)](https://www.sparkfun.com/break-away-headers-straight.html)

### [Straight Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-straight.html) 

[ PRT-00116 ]

A row of headers - break to fit. 40 pins that can be cut to any size. Used with custom PCBs or general custom headers.

[ [\$1.95] ]

[![Long Header - Male (PTH, 0.1in., 40-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/4/4/5/2/10158-01.jpg)](https://www.sparkfun.com/break-away-headers-long.html)

### [Long Header - Male (PTH, 0.1in., 40-Pin)](https://www.sparkfun.com/break-away-headers-long.html) 

[ PRT-10158 ]

These are a longer version of our \[standard\](http://www.sparkfun.com/commerce/product_info.php?products_id=116) break away he...

[ [\$3.50] ]

[![Screw Terminals 2.54mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/5/2/0/4/10571-01.jpg)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html)

### [Screw Terminals 2.54mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-2-54mm-pitch-2-pin.html) 

[ PRT-10571 ]

These are simple 2-position screw terminals with 2.54mm pitch pins. Rated up to 150V @ 6A, this terminal can accept 30 to 18A...

[ [\$0.95] ]

The output side has a 0.1\" spaced hole pair as well as a 3.5mm spaced hole pair, to allow the user to attach our [3.5mm screw terminals](https://www.sparkfun.com/products/8084).

[![Screw Terminals 3.5mm Pitch (2-Pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/6/5/7/08084-01.jpg)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html)

### [Screw Terminals 3.5mm Pitch (2-Pin)](https://www.sparkfun.com/screw-terminals-3-5mm-pitch-2-pin.html) 

[ PRT-08084 ]

Screw Terminal 3.5mm pitch pins with slide-locking together to form any size you need. Rated up to 125V @ 6A, and can accept ...

[ [\$1.25] ]

The notches on either end of the board allow you to use a zip tie to secure the wires to the board after soldering them down.

[![Closing the solder jumper](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/FemtoBuck_Image.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/FemtoBuck_Image.jpg)

The most recent revision has a small solder jumper, highlighted above, that can be closed with a glob of solder to double the output current from 330mA to 660mA. We suggest closing this jumper *before* soldering headers, terminals, or wires to the nearby holes. **Note that it\'s very likely that you\'ll get some solder on the adjacent resistor pads. That\'s perfectly okay.** Those pads will be shorted together when you\'re done anyway.

Finally, take note of the size of the FemtoBuck. If desired, the entire board can be slid into a piece of 9mm [heat shrink tubing](https://www.sparkfun.com/products/9353) to provide insulation and strain relief.

[![Heat Shrink Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/2/3/09353-01.jpg)](https://www.sparkfun.com/heat-shrink-kit.html)

### [Heat Shrink Kit](https://www.sparkfun.com/heat-shrink-kit.html) 

[ PRT-09353 ]

We love heat shrink! We use it for all sorts of handy projects. Use it to reinforce connections, protect devices, and electri...

[ [\$10.95] ]

## Connecting to an Arduino or Compatible Board

If you have only one or two LEDs, you can connect the FemtoBuck directly to the VIN pin on your Arduino. **You will need to power the board from an external supply**, as the 5V provided by USB isn\'t high enough to power the FemtoBuck (the FemtoBuck won\'t turn on below 6V).

[![Connected to Arduino Uno](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__1_.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__1_.png)

If you want more than one FemtoBuck, or if you\'ve closed the solder jumper to increase the drive current, you\'ll need to add an external power supply. It\'s not good to try to run too much current through the traces on the Arduino. **Note that the LEDs are wired separately to each FemtoBuck!** This is very important; the output of each FemtoBuck must be completely isolated from any other! That means that RGB LEDs with \"common\" pins (common anode or common cathode) cannot be used with the FemtoBuck!

[![Multiple FemtoBucks or high current mode](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__2_.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__2_.png)

**Note:** When using an external supply for the Femtobuck, the grounds of the two boards must be connected! If the power supply is 12V or less, the Arduino can be powered from it as well, but do not attempt to power the Femtobuck from the Arduino if you are using anything higher! Below are a few power options and accessories that can be used with the FemtoBuck.\
\

[![DC Barrel Jack Adapter - Female](https://cdn.sparkfun.com/r/140-140/assets/parts/4/6/8/4/10288-02.jpg)](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html)

### [DC Barrel Jack Adapter - Female](https://www.sparkfun.com/dc-barrel-jack-adapter-female.html) 

[ PRT-10288 ]

This adapter allows you to connect a barrel jack connector to bare wires. One end has screw terminals and the other has a 5.5...

[ [\$3.75] ]

[![Wall Adapter Power Supply - 9VDC 650mA](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/5/00298-01a.jpg)](https://www.sparkfun.com/products/298)

### [Wall Adapter Power Supply - 9VDC 650mA](https://www.sparkfun.com/products/298) 

[ TOL-00298 ]

High quality switching \'wall wart\' AC to DC 9V 650mA wall power supply manufactured specifically for Spark Fun Electronics. T...

**Retired**

[![Power Supply - 24V (5A)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/1/2/2/0/13758-Power_supply_24V_5A-01.jpg)](https://www.sparkfun.com/products/13758)

### [Power Supply - 24V (5A)](https://www.sparkfun.com/products/13758) 

[ TOL-13758 ]

This 5A power supply outputs both 24VDC and is terminated with a center-positive 5.5 x 2.1mm barrel connector.

**Retired**

[![Global Power Supply - 15V 4.34A](https://cdn.sparkfun.com/r/140-140/assets/parts/1/2/3/1/4/14338-01.jpg)](https://www.sparkfun.com/global-power-supply-15v-4-34a.html)

### [Global Power Supply - 15V 4.34A](https://www.sparkfun.com/global-power-supply-15v-4-34a.html) 

[ PRT-14338 ]

This isn\'t your ordinary power supply. The Global Power Supply is a 15V, 4.34A power device specifically designed to work wit...

[\$34.95] [ [\$19.95] ]

[![SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/2/5/0/15701-SparkFun_ATX_Power_Connector_Breakout_Kit_-_12V_5V__4-pin_-01.jpg)](https://www.sparkfun.com/products/15701)

### [SparkFun ATX Power Connector Breakout Kit - 12V/5V (4-pin)](https://www.sparkfun.com/products/15701) 

[ KIT-15701 ]

The ATX power connector breaks out the standard 4-pin computer peripheral port for you 12V & 5V devices from one wall adapter...

**Retired**

Multiple LEDs can be connected in series, as shown, and the supply voltage should be at least 2-3V higher than the sum of the forward voltages of the LEDs.

[![Multiple LEDs in series](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__3_.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/3/0/femtobuck_one_LED_arduino__3_.png)

For instance, our [blue 3W LEDs](https://www.sparkfun.com/products/13107) have a forward voltage of 3.2V to 3.8V. To be on the safe side, use the highest voltage in the range. If you want to connect four of them, you\'d need a power supply of \~17V or greater (3.8V + 3.8V + 3.8V + 3.8V = 15.2V; add 2V of \"head room\").

Since 17V is greater than the Arduino can tolerate on its input, we have to provide an external supply for the Arduino as well. This can be the standard 5V USB supply.

**[] Tip:** If you have three FemtoBucks together, you can mix colors with the RGB high power LED. Try using [Arduino.cc\'s Color Cross Fader example](https://www.arduino.cc/en/Tutorial/ColorCrossfader) to mix the colors like a rainbow using the Arduino\'s analog pins.\
\

[![](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/1/0/TertiaryColorWheel_Chart.png)

\
Try checking the example that was used in the [LilyPad ProtoSnap Plus Activity Guide for custom color mixing with tertiary colors](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing). Just make sure to update the pin definitions.\
\

[![LilyPad ProtoSnap Plus Activity Guide: Custom Color Mixing](https://cdn.sparkfun.com/r/480-270/assets/learn_tutorials/7/1/0/ProtoSnap_PingPongBall.jpg)](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing)\
\
*RGB LED Lighting Up from [Experiment 3: Custom Color Mixing](https://learn.sparkfun.com/tutorials/lilypad-protosnap-plus-activity-guide/3-custom-color-mixing)*

\
Or try using the code from the [Non-Addressable RGB LED Strip Hookup Guide](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide). While the code was written for RGB strips with transistors, the code functions the same with the the PickBuck.\
\

[](https://learn.sparkfun.com/tutorials/non-addressable-rgb-led-strip-hookup-guide)

### Non-Addressable RGB LED Strip Hookup Guide 

February 19, 2020

Add color to your projects with non-addressable LED strips! These are perfect if you want to control and power the entire strip with one color for your props, car, fish tank, room, wall, or perhaps under cabinet lighting in your home.

## Further Increasing Current Drive Strength

If even 660mA isn\'t enough current for you, it is possible to increase the maximum current of the FemtoBuck board up to 1A per channel. To do so, replace the current sense resistors with smaller values. To calculate the new value for the resistor, use this formula:

**I~LED~ = 0.1 / R~set~**

\
Thus, for a 1A current, you\'d want a 0.1Ω resistor. Don\'t forget to be wary of current ratings; at 1A, the sense resistor will be dissipating 1/10W, so you probably want a resistor of at least 1/8W rating. The package is a standard 0805.