# Source: https://learn.adafruit.com/multimeters/continuity.md

# Multimeters

## Continuity

## What is Continuity?
You might be asking, "What is continuity?" But don't worry, it's quite simple! Continuity means, are two things electrically connected. So if two electronic parts are connected with a wire, they are continuous. If they are connected with cotton string, they are not: while they are connected, the cotton string is not conductive.

You can always use a resistance-tester (ohmmeter) to figure out if something is connected because the resistance of wires is very small, less than 100 ohms, usually. However, continuity testers usually have a piezo buzzer which beeps. This makes them very useful when you want to poke at a circuit and need to focus on where the probes are instead of staring at the meter display.

For some basic circuits you can just look to see where the wires go to determine continuity but it's always wise to use a multimeter. Sometimes wires break or you're tired and can't easily follow all the PCB traces. I use continuity check all the time!

## What is it good for?
Continuity is one of the most important tests. Here are some things it is good for
- Determine if your soldering is good. If your solder joint it is a&nbsp;_cold solder connection_&nbsp;it will appear connected but in actually it is not! This can be really frustrating if you are not experienced in visually detecting cold solder joints
- Determine if a wire is broken in the middle. Power cords and headphone cables are notorious for breaking inside the shielding, it appears as if the cable is fine but inside the wires have been bent so much they eventually broke.
- Making sure something&nbsp; **isn't** &nbsp;connected. Sometimes a solder joint will&nbsp;_short_&nbsp;two connections.&nbsp;[Or maybe your PCB has mistakes on it and some traces were shorted by accident.](http://s3.amazonaws.com/ladyadanet/make/x0xb0x/shorts_t.jpg "Link: http://s3.amazonaws.com/ladyadanet/make/x0xb0x/shorts\_t.jpg")
- Reverse-engineering or verifying a design back to a schematic

## Remember!
**You can only test continuity when the device you're testing is** &nbsp; **not powered**. Continuity works by poking a little voltage into the circuit and seeing how much current flows, its perfectly safe for your device but if its powered there is already voltage in the circuit, and you will get incorrect readings

**Always** &nbsp;test to make sure your meter is working before starting the test by brushing the two tips together, and verifying you hear the beep. Maybe the battery is low or its not in the right mode.

**Continuity is non-directional** , you can switch probes and it will be the same.

If you are testing two points in a circuit and there is a (big) capacitor between those points&nbsp; **you may hear a quick beep and then quiet**. That's because the voltage the meter is applying to the circuit is charging up the capacitor and during that time the meter 'thinks' its continuous (essentially)

**Small resistors (under 100 ohms or so) and also all inductors will seem like short circuits**&nbsp;to a multimeter because they are very much like wires.

**Likewise, continuity doesn't mean "short"** &nbsp;it just means very very low resistance. For example, if you have a circuit that draws an Amp from a 5V supply, it will appear to be a 5Ω resistor. If you measure that with your meter it will think its a short circuit, but really its just a high-drain circuit.

## Get Into the Mode

## First step is to get your multimeter into the correct mode. Look for the icon that looks sort of like a 'sound wave'

Here are three examples. Note that sometimes the mode is "dual" (or possibly more) usage,

![](https://cdn-learn.adafruit.com/assets/assets/000/001/003/medium800/instruments_conticon2.jpg?1396767723)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/004/medium800/instruments_conticon1.jpg?1396767726)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/005/medium800/instruments_conticon3.jpg?1396767738)

Turn the multimeter knob so that it points to this symbol.## Touch and Go
For a majority of multimeters, you're ready to go, just touch the tips of the probes together so that they make a beeping sound!

Here's a video demonstration:

http://www.youtube.com/watch?v=6BEKj4J2AXw

Here are some examples covering a couple of different multimeters:## Example 1
This meter is very simple. When the probes are not touching, the display shows "1"  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/006/medium800/instruments_mastechopen.jpg?1396767741)

When you touch the tips together, the display changes to a three digit mode (it's displaying resistance, which we will cover later) It also emits a beep.![](https://cdn-learn.adafruit.com/assets/assets/000/001/007/medium800/instruments_mastechcont.jpg?1396767748)

## Example 2
This meter is dual-mode but still very easy to use. Turn the dial to the symbol. When the probes are not touching the display shows "OL" which stands for Open Loop. (Open loop is another way of saying there is no continuity).  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/008/medium800/instruments_wavetekopen.jpg?1396767750)

When you touch the probes, the soundwave icon shows up in the display (upper right) and it also shows a number. The number is not the resistance, actually…its the voltage (look for the V in the right hand side for Volts). This is because this mode is also a&nbsp; **Diode Test** &nbsp;(which will be discussed later).![](https://cdn-learn.adafruit.com/assets/assets/000/001/009/medium800/instruments_wavetekcont.jpg?1396767758)

## Example 3
This meter is triple-mode and requires an extra step to get to the continuity function. Click on the image to get a closer view of the triple-mode. After you dial to this mode you must press the&nbsp; **Mode** &nbsp;button, the wave icon will then appear in the display.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/010/medium800/instruments_extechmode.jpg?1396767761)

You can see the wave icon in the top right as expected. This meter also displays OL (I've noticed that nicer meters do this).![](https://cdn-learn.adafruit.com/assets/assets/000/001/011/medium800/instruments_extechopen.jpg?1396767768)

Unlike the other meter, this one displays Ohms (see the symbol on the right of the display). The resistance is low (4.7Ohms) but not 0 (the ideal value) because the probes and wires act as resistors. Usually with these sorts of meters they will beep whenever resistance is under 100 ohms or so.![](https://cdn-learn.adafruit.com/assets/assets/000/001/012/medium800/instruments_extechcont.jpg?1396767773)

## Probing a PCB
Here is an example of testing a PCB for continuity.The first test shows that the two points are not connected.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/013/medium800/instruments_pcbcheckopen.jpg?1396767779)

The second test shows that these two points are connected.![](https://cdn-learn.adafruit.com/assets/assets/000/001/014/medium800/instruments_pcbcheckcont.jpg?1396767782)

- [Previous Page](https://learn.adafruit.com/multimeters/overview.md)
- [Next Page](https://learn.adafruit.com/multimeters/resistance.md)

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

Out of Stock
[Buy Now](https://www.adafruit.com/product/2034)
[Related Guides to the Product](https://learn.adafruit.com/products/2034/guides)
### Pocket Autoranging Digital Multimeter

[Pocket Autoranging Digital Multimeter](https://www.adafruit.com/product/850)
When we're on the go, we like to keep a multimeter in our purse and this model is by far the best pocket meter we've found. It's so good you'll end up using it as your main multimeter!  
  
First up, this meter can measure nearly everything: it's got DC and AC...

In Stock
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

- [Ladyada's Toolkit](https://learn.adafruit.com/ladyadas-toolkit.md)
- [Energy Budgets](https://learn.adafruit.com/energy-budgets.md)
- [USB-PD Hacks](https://learn.adafruit.com/usb-pd-hacks.md)
- [Collin's Lab: Multimeters](https://learn.adafruit.com/collins-lab-multimeters.md)
