# Source: https://learn.adafruit.com/multimeters/voltage.md

# Multimeters

## Voltage

## What is Voltage?
So what is voltage anyhow? Well, its a pretty abstract term but a lot of people like to use the term "potential energy" which is that thing you heard about in high school physics and then forgot immediately.

Some people like to draw an&nbsp;[analogy to water](http://en.wikipedia.org/wiki/Hydraulic_analogy)&nbsp;to describe voltage.&nbsp;[A water pump is like a voltage supply&nbsp;](http://hyperphysics.phy-astr.gsu.edu/hbase/electric/watcir.html#c1)(also known as a&nbsp; **battery** ).&nbsp;  
The pump pushes water through a hydraulic system, and the voltage supply pushes electrons through an electronic system.&nbsp;  
The higher the rated pressure of the pump, the more 'work' the water can do.&nbsp;  
Likewise, the higher the voltage the more 'work' (Watts) the electrons can do.

Voltage is used to provide power (via a battery or wall plug) and its also used as a way of transmitting data. For example, music is recorded from a microphone as an analog voltage signal, if that voltage waveform is applied to a speaker the voltage performs the work of making air move and produces sound.&nbsp;  
Voltage is also used to in digital circuits to talk back and forth in binary, usually 5V or 3.3V is a "1" and 0V is a "0", by alternating the 1's and 0's millions of times a second, data can be moved around rather quickly.

## AC/DC

Not just an 80's hair metal band! Voltage comes in two flavors (yum):&nbsp; **Alternating Current** &nbsp;(AC) and&nbsp; **Direct Current&nbsp;** (DC). Here is a _quick_ tour of the differences.

**Direct current voltage is what comes out of batteries**. The battery is at 9V, and it pretty much keeps that voltage constant, until it dies. The chemical reactions inside the battery creates DC voltage.&nbsp;  
Electronic circuits really like DC voltage.

**Alternating current voltage is what comes out of the wall**. We call it 120 VAC (Volts Alternating Current) because the generator at the US power plant creates a voltage that oscillates (alternates). At the outlet in your home,&nbsp; the voltage is&nbsp;_not constant_ but goes from about -120V to 0 to +120V to 0 again, 60 times a second. In Europe, it's referred to as 240VAC because the voltage goes from about -240V to +240V at 50 times a second.   
_Technically_ the voltage is truly +170V to -170V in the US, which would make 120VAC we're mentioning -\> 340Volts peak to peak. Since multimeters tend to show RMS voltages, its easier to just refer to it as 120VAC and remember that the peak postive and negative voltage are each ~1.5x the RMS voltage and the peak-to-peak is going to be ~3x as what the multimeter is displaying for sinusoidal/wall outlet waveforms! [You can read all about peak to peak vs RMS voltages here](https://en.wikipedia.org/wiki/Amplitude)

AC voltage is great for power plants because its easy to transform AC voltages (using a&nbsp;[transformer](http://en.wikipedia.org/wiki/Transformer)&nbsp;) up to 50KVAC for long distance travel and then down to 240VAC or 120VAC to safely power your home. Those big honking grey things that you see next to buildings that hum are the huge transformers.&nbsp;  
Motors (like your washing machine and refrigerator compressor pump) also like running off of AC voltage.

You can turn AC voltage into DC voltage very easily by using a very small transformer to bring the 120VAC down to a reasonable level like say 16VAC and then [rectify it](http://en.wikipedia.org/wiki/Rectifier). This is basically what's inside a&nbsp;[wall wart plug](http://en.wikipedia.org/wiki/Wall_wart)&nbsp;or your laptop power supply.&nbsp;  
Its much harder to turn DC into AC, you will need an inverter which are more expensive than transformers/rectifiers.

Batteries only supply DC voltage and wall plugs only supply AC voltage. However, it is totally possible to have&nbsp; **both** &nbsp;AC and DC voltage at a certain point:&nbsp;  
If an AC voltage is oscillating between -60V and +60V it has 120Vpp AC and 0V DC because the&nbsp; **average** &nbsp;voltage of -60V and +60V is 0V.&nbsp;  
If an AC voltage is oscilating between 0V and 120V then it has 120Vpp AC and 60V DC because the average voltage of 0V and 120V is 60V.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/045/medium800/instruments_tekx0xacdc.jpg?1396768285)

In the above oscilloscope image, the dashed horizontal line in the center is ground (0V) and each dashed division is 5V. The scope is displaying a signal that has both AC and DC components. There is an alternating voltage (a square wave) that is about 4V high at about 100Hz and a DC (mean average) voltage that is around 7V. Use the dashed divisions to verify for yourself that this is so.## What is voltage testing good for?
Voltage testing is very common, you'll use it a lot
- Test if your power supply is working, are you getting 5V out of that 7805 regulator?
- Verify that your circuit is getting enough power: when all of the blinky lights are on, is the power supply drooping too low?
- Verify signals to and from chips to make sure they are what you expect once the circuit is up and running
- Testing batteries, solar cells, wall plugs, and power outlets (carefully!)
- With a&nbsp; **current sense resistor** &nbsp;you can perform current testing on a project without possibly damaging your meter.

## Remember!
**You can only test voltage when the ciruit is powered** &nbsp;If there is no voltage coming in (power supply) then there will be no voltage in the circuit to test! It must be plugged in (even if it doesn't seem to be working)

**Voltage is always measured between two points** &nbsp;There is no way to measure voltage with only one probe, it is like trying to check continuity with only one probe. You must have two probes in the circuit. If you are told to&nbsp; **test at a point** &nbsp;or&nbsp; **read the voltage at this or that location&nbsp;** what it really means is that you should put the negative (reference, ground, black) probe at&nbsp; **ground** &nbsp;(which you must determine by a schematic or somewhere else in the instructions) and the positive (red) probe at the point you would like to measure.

**If you're getting odd readings** ,&nbsp; **use a** &nbsp; **reference voltage** &nbsp;(even a 9V battery is a reasonable one) to check your voltage readings. Old meter batteries and wonky meters are the bane of your existence but they will eventually strike! Good places to take reference voltages are regulated wall plugs such as those for cell phones. Two meters might also be good :)

**Voltage is directional** &nbsp;If you measure a battery with the red/positive probe on the black/negative contact and the black probe on the positive contact you will read a negative voltage. If you are reading a negative voltage in your ciruit and you're nearly positive (ha!) that this cannot be, then make sure you are putting the black probe on the reference voltage (usually ground)

**DC voltage and AC voltage are very different** &nbsp;Make sure you are testing the right kind of voltage. This may require pressing a mode button or changing the dial.

**Unless otherwise indicated, assume DC voltages** &nbsp;

**Multimeters have different input impedences that affect readings of high impedence circuits** &nbsp;For example, measuring a sensor that has 1Mohm impedence with a 1Mohm impedence meter will give you only half the correct reading

## Get into the right mode.
There are often two seperate modes for AC and DC voltage. Both will have a V but one will have two lines, one dashed and one solid (DC) and one with have a wave next to it (AC).  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/046/medium800/instruments_masdcvoltage.jpg?1396768288)

This meter has the double line for DC voltage, and 5 ranges, from 200mV to 600V. The lightning bolt symbol is a gentle reminder that this voltage is extremely dangerous.![](https://cdn-learn.adafruit.com/assets/assets/000/001/047/medium800/instruments_masacvoltage.jpg?1396768292)

There is also the V-wave symbol for AC, and two ranges since most AC voltages that are measured are power voltages and are pretty big. (For small AC waveforms, a scope is best since you will be able to see the waveform itself).![](https://cdn-learn.adafruit.com/assets/assets/000/001/048/medium800/instruments_extekvoltmode.jpg?1396768294)

This autoranging meter makes it pretty clear which mode you want to be in.![](https://cdn-learn.adafruit.com/assets/assets/000/001/049/medium800/instruments_wavetekvoltmode.jpg?1396768298)

This ranged meter has 5 ranges, the top range is 750 VAC or 1000 VDC, to switch between DC and AC you need to press the DC/AC button on the upper right.

When the probes are not connected to anything, they should display 0V. They might flicker a bit if they pick up ambient voltage (your home is a big radiator of 60Hz voltage which can couple into your meter probes).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/050/medium800/instruments_masstart.jpg?1396768305)

## Example 1: Testing Batteries
Testing batteries is a super useful skill and is one of the best ways to practice with your multimeter

The first battery we'll test is a new 1.5V alkaline. This one is a AAA but a AA, C or D cell will be the same voltage. Set the range to&nbsp; **2V DC**.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/057/medium800/instruments_masaaa_t.jpg?1396768349)

We read 1.588V, which you may think is a mistake, after all its a 1.5V battery so shouldn't it be 1.5V? Not quite, the 1.5V written on the side is just a&nbsp; **nominal voltage** , or the "average" you may expect from the battery.In reality, an alkaline battery starts out higher, and then slowly drifts down to 1.3V and then finally to 1.0V and even lower.&nbsp;[Check out this graph from Duracell's page about alkaline battery voltage](http://ww2.duracell.com/en-US/Global-Technical-Content-Library/Product-Data-Sheets.jspx).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/058/medium800/instruments_alkdischarge.gif?1447976726)

Using this graph you can easy tell how fresh your battery is and how long you can expect it to last.

Next, we measure a 9V alkaline battery. If we still have the range set to 2VDC we will get a mysterious " **1.** &nbsp;" display, indicating is it over-range.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/059/medium800/instruments_mas9vover_t.jpg?1396768364)

Fix the range so that it's 20V, and try again.![](https://cdn-learn.adafruit.com/assets/assets/000/001/060/medium800/instruments_mas9vrange.jpg?1396768374)

For this new battery we get 9.6V. Remember that battery voltage is&nbsp;_nominal_, which means that the "9V" is just the&nbsp; **average voltage** &nbsp;of the battery. In reality, it starts out as high as 9.5V and then drops down to 9 and then slowly drifts to 7V.&nbsp;[You can check out the discharge curve in the Duracell 9V datasheet](http://ww2.duracell.com/en-US/Global-Technical-Content-Library/Product-Data-Sheets.jspx)

If we want to check a rechargeable AA battery, and it's set to a 20VDC range, we will read 1.3V, which is about what a fully charged NiMH battery will measure.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/061/medium800/instruments_masnimhrange1.jpg?1396768380)

If we fix the range so it's&nbsp; **2VDC** , we can get an extra digit of precision. This meter probably isnt more than 0.5% accurate so the precision may not mean much.![](https://cdn-learn.adafruit.com/assets/assets/000/001/062/medium800/instruments_masnimhrange2.jpg?1396768389)

Finally, I test a lithium 3V coin cell, its at 2.7V which means it's getting near the end of it's life.![](https://cdn-learn.adafruit.com/assets/assets/000/001/063/medium800/instruments_deadcoin.jpg?1396768396)

## Example 2: Testing wall wart (adapter) plugs
Testing wall adapters is also very handy, especially when you build your own circuits.

The first kind we will test is a&nbsp; **transformer-based&nbsp;** adapter.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/064/medium800/instruments_wart.jpg?1396768405)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/065/medium800/instruments_1280805698_c6de4d8107.jpg?1396768410)

Note that the label says&nbsp; **Transformer** , its also blocky and heavy which indicates a transformer as well. It requires 120VAC input, US power only. The nominal output is 9VDC at 300mA. The polarity symbol shows that the middle is positive, the outside is negative, thus we place the ground (black) probe on the outside and the positive (red) probe on the inside.![](https://cdn-learn.adafruit.com/assets/assets/000/001/066/medium800/instruments_maswart.jpg?1396768416)

Yow! 14V? That's not anything like the 9V on the package, is this a broken wall wart? Turns out, its totally normal. Transformer-based wall adaptors are (almost always)&nbsp; **unregulated** , which means that the output is not guaranteed to be a particular value, only that it will be&nbsp; **at least** &nbsp;what is printed on the box. For example, with this adapter it means that when drawing 300mA, the voltage is guaranteed to be higher than 9V.

Since the output is unregulated, the voltage supplied will droop as more current is pulled from it, which means that open-circuit (connected to nothing) the measured output can be as high as 14V. [Our power supply tutorial on transformer-based wall adapters covers this in detail](http://learn.adafruit.com/power-supplies)

Next, lets check out a&nbsp; **Switch-mode** &nbsp;adapter.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/067/medium800/instruments_smps.jpg?1396768423)

Notice that it's not square, its much thinner and although you cant feel it, its quite light for its size: There is no big honking transformer inside!![](https://cdn-learn.adafruit.com/assets/assets/000/001/068/medium800/instruments_1280805810_4c07b2f938.jpg?1396768428)

Note that it says Switching (not Transformer) on the label, and you can input US or European power. Like the transformer adapter, it is center-positive polarity.![](https://cdn-learn.adafruit.com/assets/assets/000/001/069/medium800/instruments_massmps.jpg?1396768436)

Switch-mode wall adapters are&nbsp; **regulated** &nbsp;which means that the output doesn't droop from open-circuit to full load. Its not an ultra-high quality supply, the voltage is 12.2V which is less than 5% error. Still, its much better than the transformer's 50% error!

Lastly, we'll test a 9VAC adaptor, which outputs AC voltage instead of DC. Basically this means that there's still a transformer inside, but no rectifier. This is also an unregulated supply.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/070/medium800/instruments_9vactrans.jpg?1396768445)

Note that is is similar to the transformer-based DC supply we checked out first.![](https://cdn-learn.adafruit.com/assets/assets/000/001/071/medium800/instruments_1282113408_72a8fd1ad5.jpg?1396768446)

Note again that the label says transformer. It requires 120VAC input, US power only. The nominal output is 9VAC at 300mA. The output is indicated twice, once at the top "AC/AC" and then again in the output designator "9V AC"&nbsp;  
There is no polarity because AC adaptors are not polarized: AC power oscillates between positive and negative voltages.

We test the output, but get 0V! That's when we remember that the multimeter has to be in AC voltage mode.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/072/medium800/instruments_9vactestdc.jpg?1396768451)

Switching over to AC, we get a good reading, 10.5VAC. This is an unregulated supply so again we are going to get a voltage higher than 9V.![](https://cdn-learn.adafruit.com/assets/assets/000/001/073/medium800/instruments_9vactestac.jpg?1396768454)

## Bonus Example: Testing a circuit with AC and DC
If you're trying to measure something that is just DC or just AC its very easy, just get into the right mode and measure away! The hardest thing to do is measure a circuit with both AC and DC voltages.

For example, here is a few attempts to measure the VCO output of a x0xb0x as seen in the oscilloscope output shown here (its the same one from above).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/075/medium800/instruments_tekx0xacdc.jpg?1396768477)

The DC portion is the easy part to measure, most multimeters just average out the input measurement.![](https://cdn-learn.adafruit.com/assets/assets/000/001/076/medium800/instruments_masx0xdc.jpg?1396768480)

We read 6.75V DC, which is about right.

However, when trying to measure AC, this multimeter gives us a seemingly random number. (Maybe the DC voltage \* 2 ?).

![](https://cdn-learn.adafruit.com/assets/assets/000/001/077/medium800/instruments_masx0xac.jpg?1396768488)

The Extech meter reads 1.65V![](https://cdn-learn.adafruit.com/assets/assets/000/001/078/medium800/instruments_extekx0xac.jpg?1396768495)

The Wavetek does the same![](https://cdn-learn.adafruit.com/assets/assets/000/001/079/medium800/instruments_wavex0xac.jpg?1396768503)

The lesson? You can't depend on your multimeter to measure AC voltages when there is a DC component!- [Previous Page](https://learn.adafruit.com/multimeters/resistance.md)
- [Next Page](https://learn.adafruit.com/multimeters/current.md)

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
