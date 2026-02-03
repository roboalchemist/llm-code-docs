# Source: https://learn.adafruit.com/multimeters/current.md

# Multimeters

## Current

# What is current? &nbsp;
Current is the rate of electricity flow in a circuit. &nbsp;Using the same water analogy as before, higher pressure (voltage) and a bigger pipe (lower resistance)&nbsp;means a greater volume of water per second (current) will flow. &nbsp;This simple relationship&nbsp;is represented by the equation known as "Ohm's Law":  
  

## &nbsp; &nbsp; I = V/R
  
Where: 'I' is current, 'V' is voltage and 'R' is resistance.  
  
Another important equation is the one for power.  
  

## &nbsp; &nbsp;&nbsp;P = I x&nbsp;V
  
Where 'P' is power (measured in Watts), 'I' is current and&nbsp;'V' is voltage.  
  
Watts is a measure of work, or the conversion of electrical energy into some other form such as&nbsp;heat, light or motion. &nbsp;As the equation implies, it takes both voltage and current to do work.  
  

# Why Measure Current?
  
If there is not enough current, your circuit may not be able to do the work it was&nbsp;designed&nbsp;to do. &nbsp;Logic circuits&nbsp;may not function reliably, displays may be dim,&nbsp;motors&nbsp;may stall. &nbsp;  
  
On the other hand, if there is too much current, things will heat up and&nbsp;components may be damaged. In extreme cases there may even be&nbsp;smoke or flames.  
  
Reasons for measuring current in a circuit include:  

- Determining circuit power requirements  
- Verifying correct circuit operation  
- Testing power supply performance
- Verify that batteries are charging or discharging at a safe rate  
- Estimating battery life or recharge time  
- Diagnosing circuit problems  

![](https://cdn-learn.adafruit.com/assets/assets/000/001/696/medium800/instruments_Wavetek.jpg?1396775437)

# Pick a safe range.
Most meters have several current measuring ranges. &nbsp;Choose one that is good for AT LEAST the maximum current you expect to be measuring. &nbsp;If in doubt, choose the next higher range. &nbsp;There is usually overlap between the ranges and you can always go back to a lower one after you have verified that it is safe to do so. &nbsp;  
  
Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/697/medium800/instruments_wavetek_dial.jpg?1396775442)

This meter has 4 ranges from 200 microamps to 200 milliamps. &nbsp;In addition, the 20 milliamp setting can be used to measure up to 20 amps when used with a special high-current probe jack.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/699/medium800/instruments_Extech_dial.jpg?1396775454)

This is an 'auto-ranging' meter and has just 3 very wide range&nbsp;settings. &nbsp;It will automatically adjust the range to give you the best precision measurement within those settings:

- microamps (uA)  
- milliamps (mA)  
- amps (A)  

# Choose the right connections.
  
Multimeters contain sensitive circuits capable of precision measurements of tiny currents and voltage. &nbsp;These circuits can be damaged or destroyed by high current flow.&nbsp; That is why most meters have a separate jack for high current measurements. &nbsp;This jack is fused for safety. &nbsp;If you are using the high-current setting, be sure to use the right jack. &nbsp;  
Info: 

Info: 

![](https://cdn-learn.adafruit.com/assets/assets/000/001/701/medium800/instruments_Wavetek_jacks.jpg?1396775475)

This meter has a separate jack for measuring voltage and resistance. &nbsp;And two jacks for different ranges of&nbsp;current measurement. &nbsp;One&nbsp;current measurement jack is safe for currents up to 200mA. &nbsp;The other can be used to measure currents up to 20 amps.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/705/medium800/instruments_Extech_jacks.jpg?1396775514)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/704/medium800/instruments_Mastech_jacks.jpg?1396775508)

These two meters use the same jack for all measurements except high current measurements.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/703/medium800/instruments_Wavetek_low.jpg?1396775498)

Here we are using the&nbsp;0-200mA jack to make a measurement in the 2mA range.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/706/medium800/instruments_2012_08_12_IMG_0423.jpg?1396775543)

This is the correct jack and range to use for measurements above 200mA on this meter.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/710/medium800/instruments_Extech_high.jpg?1396775503)

On this meter, the correct jack and range selections&nbsp;for high-current measurement are clearly indicated in yellow. &nbsp;  
  
Also note the warning labels indicating maximum safe levels for each jack.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/711/medium800/instruments_Mastech_High.jpg?1396775568)

But with all meters, use care when choosing range and connections to avoid damage to the meter. &nbsp;Most meters have internal fuses to protect the circuitry, but they are not always&nbsp;readily accessible for easy replacement.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/716/medium800/instruments_Fuse.jpg?1396775605)

# Get in the loop!
To measure the current, you have to make it flow through the meter. &nbsp;To do that you need to make your meter part of the circuit. &nbsp;You need to break the circuit at the point where you want to measure the current and insert your meter in the middle. &nbsp;Before connecting your meter to the circuit, double check your range and make sure you have the leads plugged into the right jacks.&nbsp;  
  
For this example, we are going to measure the battery supply current going into a MintyBoost:![](https://cdn-learn.adafruit.com/assets/assets/000/001/712/medium800/instruments_MintyBoost.jpg?1396775576)

## Breaking the circuit:
  
First we need to break the circuit so we can insert our meter. &nbsp;In this case we will just unsolder the battery wire from the Mintyboost circuit board  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/713/medium800/instruments_Disconnect_Lead.jpg?1396775584)

Then we will attach a temporary lead to make it easier to connect the meter.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/714/medium800/instruments_Add_Jumper.jpg?1396775591)

## Closing the loop
Now we connect the meter between the battery lead and our temporary lead. &nbsp;We'll use some alligator clips to hold it all together.  
  
The positive meter probe is connected to the positive battery lead. &nbsp;The negative probe connects to the&nbsp;temporary&nbsp;lead we soldered to the Mintyboost circuit board. &nbsp;This closes the loop and makes the battery current flow through the meter.![](https://cdn-learn.adafruit.com/assets/assets/000/001/719/medium800/instruments_Connections.jpg?1396775627)

We'll start with the high-current range and probe connection to be safe:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/717/medium800/instruments_HiRange.jpg?1396775612)

We see that the current is 0.23A (230mA). &nbsp;This is well within the 400mA safe limit for the low-current probe jack, so we set the meter to the milliamp range and use the low current jack for a more precise measurement.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/715/medium800/instruments_Current_MEasurement.jpg?1396775599)

Using the milliamp range, we can see that there is 226.9 mA of current going from the battery to the mintyboost.

- [Previous Page](https://learn.adafruit.com/multimeters/voltage.md)

## Featured Products

### Extech EX330 12-function autoranging multimeter

[Extech EX330 12-function autoranging multimeter](https://www.adafruit.com/product/308)
 **Discontinued** - [you can grab this&nbsp;Digital Multimeter - Model 9205B+&nbsp;instead!](https://www.adafruit.com/product/2034)

If you're looking for one of the best multimeters, we're proud to now offer our personal favorite! The Extech EX330 "12...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/308)
[Related Guides to the Product](https://learn.adafruit.com/products/308/guides)
### Digital Multimeter

[Digital Multimeter](https://www.adafruit.com/product/71)
This is a basic multimeter, I've played with it a bunch and I think its a great addition to a toolbox. It's low cost and simple to use with a big clear display and all the measurements you need:

- AC/DC Voltage measurement
- Current measurement, from 1uA up to...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/71)
[Related Guides to the Product](https://learn.adafruit.com/products/71/guides)
### Digital Multimeter - Model 9205B+

[Digital Multimeter - Model 9205B+](https://www.adafruit.com/product/2034)
This massive multimeter has everything but the kitchen sink included. It's a great addition to any workbench or toolbox. &nbsp;It's low cost, simple to use, and has a big clear display with all the measurements you need and more!

The multimeter includes:

- AC/DC Voltage...

In Stock
[Buy Now](https://www.adafruit.com/product/2034)
[Related Guides to the Product](https://learn.adafruit.com/products/2034/guides)
### Pocket Autoranging Digital Multimeter

[Pocket Autoranging Digital Multimeter](https://www.adafruit.com/product/850)
When we're on the go, we like to keep a multimeter in our purse and this model is by far the best pocket meter we've found. It's so good you'll end up using it as your main multimeter!  
  
First up, this meter can measure nearly everything: it's got DC and AC...

Out of Stock
[Buy Now](https://www.adafruit.com/product/850)
[Related Guides to the Product](https://learn.adafruit.com/products/850/guides)
### Multi-Meter! - Skill badge, iron-on patch

[Multi-Meter! - Skill badge, iron-on patch](https://www.adafruit.com/product/502)
You can use a multi-meter! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many ways to show and share.  
  
This is...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/502)
[Related Guides to the Product](https://learn.adafruit.com/products/502/guides)
### Multi-Meter! - Sticker!

[Multi-Meter! - Sticker!](https://www.adafruit.com/product/646)
You can use a multi-meter! Adafruit offers a fun and exciting stickers to celebrate achievements in electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a great sticker is just one of the many ways to show and share.  
<br...></br...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/646)
[Related Guides to the Product](https://learn.adafruit.com/products/646/guides)

## Related Guides

- [USB-PD Hacks](https://learn.adafruit.com/usb-pd-hacks.md)
- [Energy Budgets](https://learn.adafruit.com/energy-budgets.md)
- [Ladyada's Toolkit](https://learn.adafruit.com/ladyadas-toolkit.md)
- [Collin's Lab: Multimeters](https://learn.adafruit.com/collins-lab-multimeters.md)
