# Source: https://learn.adafruit.com/multimeters/resistance.md

# Multimeters

## Resistance

## What is Resistance?
Resistance is just what it sounds like, its the characteristic that makes a component fight current flow. The bigger the resistance value (in&nbsp; **ohms** &nbsp; **Ω** ) the more it fights. Most&nbsp;[resistors](http://en.wikipedia.org/wiki/Resistor)&nbsp;you'll see range between 1 ohm and 1 megaohm (1.0 MΩ) they often have 5% tolerance but you can buy 1% or even 0.1% accuracy resistors.

In general, resistence testing is best for measuring resistors, but you may find yourself measuring the resistance of other things, such as sensors and speakers.

## Resistor Coding
Resistors are color coded, at first it seems like a bad way to print the values but with a little time it becomes faster because you dont have to read any numbers and the stripes are visible no matter how it is rotated.&nbsp;[You can use this calculator to play around with resistor color codes](http://www.dannyg.com/examples/res2/resistor.htm "Link: http://www.dannyg.com/examples/res2/resistor.htm").  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/025/medium800/instruments_rescolorcode.jpg?1396768185)

_Resistor color code chart courtesy of&nbsp;[Make Magazine](http://www.makezine.com/ "Link: http://www.makezine.com/")_![](https://cdn-learn.adafruit.com/assets/assets/000/001/027/medium800/instruments_CFR-12JR-1K0.jpg?1396768196)

_Resistor image courtesy of_ _[Digikey](http://www.digikey.com/product-detail/en/CFR-25JR-52-1K/1.0KQTR-ND/11974)_  
  
This image shows a 1.0 kΩ 5% resistor (brown black red gold).  
## What is resistance testing good for?
Resistance-testing is very useful
- If you don't have a continuity tester, it can double as one
- Check resistors whose values are not clear, if you aren't good at [reading color codes](http://en.wikipedia.org/wiki/Electronic_color_code) or if the marking has come off
- Measure input and output resistance of circuits
- Test and characterize [sensors](http://learn.adafruit.com/multimeters/) and [potentiometers](http://learn.adafruit.com/multimeters/) (see below)

## Remember!
**You can only test resistance when the device you're testing is** &nbsp; **not powered**. Resistance testing works by poking a little voltage into the circuit and seeing how much current flows, its perfectly safe for any component but if its powered there is already voltage in the circuit, and you will get incorrect readings

**You can only test a resistor before it has been soldered/inserted into a circuit**. If you measure it in the circuit you will also be measuring everything connected to it. In some instances this is OK but I would say that in the vast majority it is not. If you try, you will get incorrect readings and that's worse than no reading at all.

**You can make sure your meter is working well by having a '**** reference resistor'&nbsp;**to test against. A 1% 1KΩ or 10KΩ resistor is perfect! Low batteries can make your multimeter wonky.

**Resistance is non-directional** , you can switch probes and the reading will be the same.

**If you have a ranging meter** &nbsp;(as most inexpensive ones are), you'll need to keep track of what range you are in. Otherwise, you will get strange readings, like&nbsp; **OL** &nbsp;or similar, or you may think you're in KΩ when really you're in MΩ. This is a big problem for beginners so be careful!

## Get into the mode.
Look for an ohm (Ω) symbol, if its a ranging meter there will be a bunch of subdivided modes. If its auto-ranging there will be only one.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/028/medium800/instruments_wavetek_resmode.jpg?1396768202)

This meter has the Ω symbol and then 7 submodes, ranging from 200Ω to 2000MΩ (wow!)![](https://cdn-learn.adafruit.com/assets/assets/000/001/029/medium800/instruments_mas830_resmode.jpg?1396768203)

This meter has the Ω symbol and then 5 submodes, ranging from 200Ω to 2MΩ![](https://cdn-learn.adafruit.com/assets/assets/000/001/030/medium800/instruments_extech_multimode.jpg?1396768208)

This meter has a multi-mode (you need to press a seperate MODE button to change between capacitor sense, diode test, resistor test and continuity!) It does not, however, have any numbered submodes, as it is auto-ranging.## Ranging vs. Auto-Ranging
As long as it works, it doesn't matter which type you have. But auto-ranging meters are a little slower.&nbsp;  
Compare these two videos as I measure a 1KΩ resistor with an autoranging meter:  
http://www.youtube.com/watch?v=LKjBX1oxcgk

Which takes about 4 seconds to settle on a final value, and a 10KΩ resistor with a ranging meter:http://www.youtube.com/watch?v=AbFhshdswF4

Which gets the first significant digit instantly, the second digit after 1 second and the final digit after 2.

Expensive autoranging meters, like Fluke 73s, will be super fast so it's not a big deal, but if you have a $200 meter you're probably not reading this tutorial.

Ranges will almost always be something like 200Ω, 2KΩ, 20KΩ, 200KΩ, 2MΩ, etc. Why the 2s instead of 100, 1K, 10K etc.? Well, here's my guess.&nbsp;  
Because the vast majority of resistors are 5%, the resistor values are 5% apart (or so). For example, the "standard" 5% values between 1K and 10K are:

1.0K, 1.1K, 1.2K, 1.3K, 1.5K, 1.6K, 1.8K, 2.0K, 2.2K, 2.4K, 2.7K, 3.0K, 3.3K, 3.6K, 3.9K, 4.3K, 4.7K, 5.1K, 5.6K, 6.2K, 6.8K, 7.5K, 8.2K, 9.1K

There are way more values between 1KΩ and 2KΩ than between 2KΩ and 3KΩ, etc. By picking 2KΩ as your max range, you get the best precision for the most probable values.

## Example 1: Testing a Resistor
With an auto-ranging meter, its easy, just put the two probes across the resistor and read the number. For example, this 1KΩ 5% resistor is actually 0.988 Kohm.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/031/medium800/instruments_auto1k2.jpg?1396768214)

And this 10KΩ is really 9.80KΩ. Note that the numbers look similar but the decimal point has moved.![](https://cdn-learn.adafruit.com/assets/assets/000/001/032/medium800/instruments_auto10k2.jpg?1396768215)

This ranged meter requires that you dial in the range. We'll guess that this resistor is under 2KΩ then measure it. We get 0.992 which means its 0.992 KΩ (or, a 1KΩ resistor).![](https://cdn-learn.adafruit.com/assets/assets/000/001/033/medium800/instruments_range1k.jpg?1396768220)

Now testing a different resistor, we will again guess its under 2KΩ. However, this time we get a strange response, a&nbsp; **1.** &nbsp;which means out of range. Some meters will display an&nbsp; **OL** &nbsp;which you may remember from the continuity secion as meaning "open loop" here it means "the measurement is higher than the range".![](https://cdn-learn.adafruit.com/assets/assets/000/001/034/medium800/instruments_range10k.jpg?1396768226)

We try again, changing the range to 20KΩ![](https://cdn-learn.adafruit.com/assets/assets/000/001/035/medium800/instruments_range10k2.jpg?1396768233)

Aha! It is a 9.82 KΩ resistor (10KΩ)

Its a little clumsier than auto-ranging but if you are pretty sure you know about how big the resistance you are expecting is, its very speedy.

## Example 2: Testing a Potentiometer
You can test the max-value of a potentiometer by measuring across the two 'ends' as shown here with a rotational 10KΩ pot. To find the 'range' look at the dial.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/036/medium800/instruments_test10kpot.jpg?1396768237)

You can also use a multimeter to tell whether the potentiometer is a linear or logarithmic (audio) pot. When the pot is centered, if the resistance between the wiper and one end is half of the total value, its linear. (I used clips instead of probles to make it easier to take these photos).

This is a 10KΩ linear potentiometer.

The minimum resistance of the pot, 0Ω (a short) as expected.![instruments_linpotmin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/037/medium640/instruments_linpotmin.jpg?1396768243)

Potentiometer centered, about 5KΩ![instruments_linpotmid.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/038/medium640/instruments_linpotmid.jpg?1396768245)

Maximum value is 9.5KΩ (it should be around 10KΩ)![instruments_linpotmax.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/039/medium640/instruments_linpotmax.jpg?1396768252)

This video shows the resistance of a 10KΩ linear pot as it is adjusted. At the end it is set to approximately the midd, which is measured at 4.7KΩ, pretty close to the 'ideal' of 5KΩ.http://www.youtube.com/watch?v=Yxk6o0RPbsI

Here are photos of a 50KΩ audio potentiometer:Minimum is 0Ω as expected![instruments_logpotmin.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/040/medium640/instruments_logpotmin.jpg?1396768258)

Middle is 8KΩ![instruments_logpotmid.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/041/medium640/instruments_logpotmid.jpg?1396768264)

Maximum is 54.2KΩ, close to the ideal 50KΩ![instruments_logpotmax.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/042/medium640/instruments_logpotmax.jpg?1396768270)

If, when centered, the resistance is more like 85% or 15% of the total resistance, then its a log pot. This is a 50KΩ analog potentiometer. When centered, the resistance is about 8KΩ.http://www.youtube.com/watch?v=ys8EAn0fi48

## Example 3: Testing a Sensor
Potentiometers are resistors that change value when they are moved. A&nbsp;[Light Dependent Resistor (LDR)](http://www.google.com/url?q=http://en.wikipedia.org/wiki/Photocell&revid=245081890&sa=X&oi=revisions_inline&resnum=0&ct=result&cd=1&usg=AFQjCNGRbRFTVwSDdfCPr_9dkdrh-80kjQ)&nbsp;is a resistor that changes value with the amount of light it receives. This one has a range of about 20K max.

First, set the range, in this case 20KΩ seems pretty good. In bright light, it measures about 610 Ω

![](https://cdn-learn.adafruit.com/assets/assets/000/001/043/medium800/instruments_ldrbright.jpg?1396768275)

Slightly shaded it's 5.84KΩ (remember this is still a well-lit photo)![](https://cdn-learn.adafruit.com/assets/assets/000/001/044/medium800/instruments_ldrshade.jpg?1396768282)

After setting the range, I experiment with shading it on video:http://www.youtube.com/watch?v=G8cabfHlpxs

- [Previous Page](https://learn.adafruit.com/multimeters/continuity.md)
- [Next Page](https://learn.adafruit.com/multimeters/voltage.md)

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
