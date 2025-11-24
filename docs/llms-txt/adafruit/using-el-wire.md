# Source: https://learn.adafruit.com/el-wire/using-el-wire.md

# EL Wire

## Using EL Wire

## Drivers
To power EL, an AC source is required. It is not possible to light up EL with DC such as batteries or a wall-wart adapter! The output of the inverter must be a sine-wave with no DC component. It is not unusual to have an inverter run from batteries, such as this 'pocket' AA driver. The inverting circuitry is inside the box part to the left.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/251/medium800/el_wire_tape_panel_elinverter2AA.jpeg?1396761505)

This pocket inverter can drive approximately 1 to 15 feet (0.3-5 meter) of 'classic' EL wire such as LyTec. Since we are using higher-brightness EL wire in the shop, it can only drive half as much, 1 to 7.5 feet (0.3 to 2.5 meter). We found that 2 meters gives a nice bright glow at good voltage and frequency. At 3 meters, its not as bright, it appears about the same as 'classic' EL.

Each meter of high brightness EL draws about 10-15mA at the high voltage, which means about 1.5 Watt/meter (at 100VAC). 2 AA batteries can provide 9 Watts, so you can drive 1 meter for about 6 hours or 2 meters for 3 hours. This is only approximate, as the voltage changes with the length. The best way to know how long the wire will last is to test it with batteries and time how long it takes to dim!

All EL drivers run at 'audible' frequencies which means that you can hear a squeaking noise emanating from the driver case. This is totally normal, but a little annoying. You can reduce the squeaking by opening up the driver case and padding it with foam tape. You can also try wrapping it in bubble-wrap or foam sheet to reduce the noise. We've usually found people wearing EL wire at parties where it's quite loud already.

## EL Wire Modeling

EL wire is&nbsp; **not** &nbsp;a resistive light (like an incandescent bulb) and it is&nbsp; **not** &nbsp;a diode light (like an LED), it acts more like a capacitor! The stiff inner wire is one 'plate' of the capacitor, the corona wire is the other 'plate' and the phosphor coating being the insulator/dielectric ([for more details on capacitors, see Wikipedia](http://en.wikipedia.org/wiki/Capacitor)). This means you cannot use dimming methods such as triac/chopping for resistive incandescents or PWM for LEDs.

In terms of thinking of how EL wire 'acts' you should model it as a capacitor that increases with the length of the wire. It is not a perfect capacitor, there is also some leakage which we will model as a resistor.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/252/medium800/el_wire_tape_panel_capmodel.png?1396761512)

Adding another meter, we duplicate the RC model in&nbsp; **parallel.** ![](https://cdn-learn.adafruit.com/assets/assets/000/000/253/medium800/el_wire_tape_panel_twometermodel.png?1396761523)

Of course, we can simplify by calculating the new capacitance and resistance. Remember that capacitance _increases_&nbsp;in parallel and resistance&nbsp;_decreases._

![](https://cdn-learn.adafruit.com/assets/assets/000/000/254/medium800/el_wire_tape_panel_twometermodelparr.png?1396761529)

The capacitance and resistance per meter&nbsp; **depends on the 'thickness' of the EL wire, the brand and make, the voltage and frequency applied**

For ELAM Lytec 2.3mm EL wire (which is the most common EL wire) the parallel resistance per meter is:

| Voltage | 200 Hz | 400 Hz | 800 Hz | 1000 Hz | 2000 Hz |
| --- | --- | --- | --- | --- | --- |
| 5 | 1,504 KΩ | 1,043 KΩ | 663 KΩ | 569 KΩ | 314 KΩ |
| 20 | 1428 | 942 KΩ | 592 KΩ | 494 KΩ | 259 KΩ |
| 40 | 1175 KΩ | 691 KΩ | 393 KΩ | 316 KΩ | 165 KΩ |
| 60 | 886 KΩ | 510 KΩ | 280 KΩ | 235 KΩ | 123 KΩ |
| 80 | 709 KΩ | 435 KΩ | 243 KΩ | 200 KΩ | 107 KΩ |
| 100 | 572 KΩ | 374 KΩ | 226 KΩ | 184 KΩ | 101 KΩ |
| 120 | 480 KΩ | 323 KΩ | 210 KΩ | 174 KΩ | 94 KΩ |

And the ELAM Lytec 2.3mm EL wire capacitance per meter is:

| Voltage | 200 Hz | 400 Hz | 800 Hz | 1000 Hz | 2000 Hz |
| --- | --- | --- | --- | --- | --- |
| 5 | 5.1 nF | 5.0 nF | 4.9 nF | 4.9 nF | 4.7 nF |
| 20 | 5.1 nF | 5.0 nF | 4.9 nF | 4.9 nF | 4.8 nF |
| 40 | 5.3 nF | 5.1 nF | 5.0 nF | 5.0 nF | 4.9 nF |
| 60 | 5.6 nF | 5.4 nF | 5.4 nF | 5.3 nF | 5.2 nF |
| 80 | 5.9 nF | 5.8 nF | 5.7 nF | 5.7 nF | 5.6 nF |
| 100 | 6.3 nF | 6.2 nF | 6.1 nF | 6.1 nF | 6.0 nF |
| 120 | 6.4 nF | 6.3 nF | 6.2 nF | 6.2 nF | 6.1 nF |

The 'high brightness, long life' EL wire we carry is about twice as bright and has about twice the capacitance.

## Current Draw
We can use this information to determine the power draw.

Assuming you have LyTec EL wire, 2.3mm diameter 'standard'…if have one meter, that is 6nF and 100KΩ in parallel. The capacitance has an impedance of 1/(2πfC) so at 2000 Hz, the impedence per meter is 12 KΩ, in parallel with 100 KΩ it is 11 KΩ total. For a 100V AC power source, the current draw is 100V/11KΩ&nbsp;= 9mA per meter. 100V \* 9mA/meter = 0.9 Watts/meter!

If you are using our 'high brightness, long life' stuff, its about 1.5 Watts per meter.

Thus an inverter with a 100mA output capability can drive 10 meters&nbsp;or so of LyTec and 5 meter&nbsp;of 'high brightness' EL. The transformer and transistors used in an inverter are a big part of how much current an inverter can provide!

## Inverter / Driver Details
To power EL, an AC source is required. It is not possible to light up EL with DC such as batteries or a wall adapter! The output of the inverter must be a sine-wave with no DC component. It is not unusual to have an inverter run from batteries, such as this 'pocket' AA driver. The inverting circuitry is inside the box part to the left. ![](https://cdn-learn.adafruit.com/assets/assets/000/000/255/medium800/el_wire_tape_panel_elinverter2AA.jpeg?1396761535)

The voltage should be between 50-120V AC RMS (150V-360V peak-to-peak). Higher voltages result in a brighter display (but lower overall wire-life).

The AC frequency can run from 60Hz to 2000Hz, higher frequency results in a brighter display (but lower overall wire-life). Most inverters run at around 100VAC and 2KHz. This will vary a little bit with how much wire is attached, as longer pieces will 'load' the output.

For example, this is the output of our pocket inverter with&nbsp; **no loading**. It is about 7KHz and 120V, the frequency is a bit high because the output is expecting a capacitive load that is not there.**&nbsp;(Don't do this yourself, it can damage the inverter!)**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/256/medium800/el_wire_tape_panel_pocketAAunloaded.jpeg?1396761541)

Attaching 3 meters (10 feet) of high brightness EL wire, the frequency stabilizes at 2KHz and 65V, which means we've about maxed out what this driver can provide.![](https://cdn-learn.adafruit.com/assets/assets/000/000/257/medium800/el_wire_tape_panel_pocketAA3mloaded.jpeg?1396761546)

If you are comfortable using tools and want to optimize your driver and wire, you can do so by 'modeling' your EL wire with a capacitor and resistor and plugging that in, then measuring the frequency across the RC with a multimeter or scope, just watch out you don't zap yourself!

The most important thing to note is that without a load capacitance/resistance, the voltage output can peak very high, up to 400Vpp! This will damage the pass transistors and for this reason&nbsp; **you should never run an EL inverter without EL wire attached**

Another thing is that the more EL you add, the dimmer it will get as the voltage sags.&nbsp;

- [Previous Page](https://learn.adafruit.com/el-wire/soldering-to-el-wire.md)
- [Next Page](https://learn.adafruit.com/el-wire/el-projects.md)

## Featured Products

### EL Wire 12V Sound Activated Pocket Inverter

[EL Wire 12V Sound Activated Pocket Inverter](https://www.adafruit.com/product/832)
A small, portable inverter for EL wire with an audio input! This inverter has a little microphone and will light the connected EL according to the surrounding audio volume. Makes for an easy reactive project.  
  
This inverter requires **12VDC input** (it works great with our 8xAA...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/832)
[Related Guides to the Product](https://learn.adafruit.com/products/832/guides)
### EL Wire Sound Activated Pocket Inverter - 5V USB Power

[EL Wire Sound Activated Pocket Inverter - 5V USB Power](https://www.adafruit.com/product/831)
A small, portable inverter for EL wire with an audio input! This inverter has a little microphone and will light the connected EL according to the surrounding audio volume. Makes for an easy reactive project.

This inverter requires 5V input (it works great with any USB power pack) and it...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/831)
[Related Guides to the Product](https://learn.adafruit.com/products/831/guides)
### EL wire 4xAAA pocket inverter

[EL wire 4xAAA pocket inverter](https://www.adafruit.com/product/564)
A small, portable inverter for EL wire. Powers off of 4 AAA batteries (not included!), it can drive 3-4 meters (10 to 13 feet) of our high-brightness EL wire OR 1 meter (3 feet) of EL tape OR a 10cmx10cm piece of EL panel for about 7 hours.  
  
There is a switch for selecting...

Out of Stock
[Buy Now](https://www.adafruit.com/product/564)
[Related Guides to the Product](https://learn.adafruit.com/products/564/guides)
### 12V EL wire/tape inverter

[12V EL wire/tape inverter](https://www.adafruit.com/product/448)
This is an inverter for EL wire and tape, similar to our pocket inverters, except it is a brick that takes 12V input instead of 2 AA batteries. This means its good for 'fixed' installations since you can just plug it into a 12V wall adapter. It's also good for portable projects...

Out of Stock
[Buy Now](https://www.adafruit.com/product/448)
[Related Guides to the Product](https://learn.adafruit.com/products/448/guides)
### EL wire 2xAA pocket inverter

[EL wire 2xAA pocket inverter](https://www.adafruit.com/product/317)
A small, portable inverter for EL wire. Powers off of 2 AA batteries (not included!), it can drive 1 to 8 feet (about 2.5m) of our high-brightness EL wire for 10 hours. There is a button for selecting steady/blink/off modes. There's a removable clip on the back. Comes with a 2.5mm pitch...

In Stock
[Buy Now](https://www.adafruit.com/product/317)
[Related Guides to the Product](https://learn.adafruit.com/products/317/guides)
### Heat Shrink Pack

[Heat Shrink Pack](https://www.adafruit.com/product/344)
Heat shrink is the duct tape of electronics, it keeps your stuff all safe and kept together. Especially when wiring and soldering, use heat shrink to add mechanical strength to cables. We use this stuff all the time and having a zip-lock bag of all the possible sizes is super...

In Stock
[Buy Now](https://www.adafruit.com/product/344)
[Related Guides to the Product](https://learn.adafruit.com/products/344/guides)

## Related Guides

- [EL Wire Sign](https://learn.adafruit.com/el-wire-sign.md)
- [TRON Hoodie](https://learn.adafruit.com/tron-hoodie.md)
- [Electron Bow](https://learn.adafruit.com/electron-bow.md)
- [EL Bowtie](https://learn.adafruit.com/el-bowtie.md)
- [EL Wire Animal Masks](https://learn.adafruit.com/el-wire-animal-masks.md)
- [Light Up your Costume with Noods](https://learn.adafruit.com/light-up-your-costume-with-noods.md)
- [EL Workshop](https://learn.adafruit.com/el-workshop.md)
- [TRON Bag](https://learn.adafruit.com/tron-bag.md)
- [Glowing Star Chuck Taylor Sneakers](https://learn.adafruit.com/glowing-star-chucks.md)
- [EL Stick Figure](https://learn.adafruit.com/el-stick-figure.md)
- [Glowing Bean Bags with EL Wire](https://learn.adafruit.com/glowing-bean-bags-with-el-wire.md)
- [EL Wire Stocking](https://learn.adafruit.com/el-wire-stocking.md)
