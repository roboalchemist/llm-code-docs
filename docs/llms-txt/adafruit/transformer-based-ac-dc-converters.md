# Source: https://learn.adafruit.com/power-supplies/transformer-based-ac-dc-converters.md

# Power Supplies

## Transformer-based AC/DC converters

The most common and inexpensive plugpack power supply type you'll see is the chunky transformer based plug. Whenever you buy some consumer electronics you'll be getting one of these:![](https://cdn-learn.adafruit.com/assets/assets/000/001/088/medium800/components_wart_t.jpg?1396768575)

These guys are&nbsp; **everywhere** &nbsp;- all sorts of voltage and current ratings. They're available for sale at any store just about, but there are some big things to watch out for! One is that the output voltage is not going to be 9V (for example) out of the box, that voltage rating is just the minimum output for the current rating (200mA for example). And also, the output is going to have a lot of ripple on it!

Before we talk precisely about these guys, lets go back in time to when engineers had to build their power supplies with their bare hands!

## The good old days!
Back a couple decades ago, the only way to build a power supply was to start a big chunky 120VAC/12VAC transformer. The transformer was used to bring the high voltage from the wall down to a less dangerous level. Then diodes and capacitors were used to turn the AC into DC.  
## Transformers
![](https://cdn-learn.adafruit.com/assets/assets/000/001/089/medium800/components_df7f2a3b388d92926e7fd84487c350f0.media.500x385.jpg?1396768578)

We aren't going to get into the heavy detail of the electromagnetic theory behind transformers except to say that they are made of two coils of wire around a chunk of iron. If the number of coils are the same on both sides then the AC voltage is the same on both sides. If one side has twice the coils, it has twice the voltage. They can be used 'backwards' or 'forwards'! For more detailed information, be sure to&nbsp;[check out the wikipedia page](http://en.wikipedia.org/wiki/Transformer). ![](https://cdn-learn.adafruit.com/assets/assets/000/001/090/medium800/components_xformpri_t.jpg?1396768580)

To use it, one half would get wired up to the wall (the 'primary' 'high side')![](https://cdn-learn.adafruit.com/assets/assets/000/001/091/medium800/components_xformsec_t.jpg?1396768586)

and the other half would output 12V AC (the 'secondary' 'low side'). The transformer functioned in two ways: one it took the dangerous high voltage and&nbsp; **transformed** &nbsp;it to a much safer low voltage, second it **isolated** &nbsp;the two sides. That made it even safer because there was no way for the hot line to show up in your electronics and possibly electrocute you.

We'll use a schematic symbol to indicate a transformer, its two coils inside which are drawn out, the schematic symbol will have the same number of coils on either side so use common sense and any schematic indicators to help you out in figuring which is primary and which is secondary!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/093/medium800/components_xformsch.png?1396768597)

## Half wave rectification
Now that the voltage is at a non-electrocutey level of around 12VAC it can be converted into DC. The easiest and cheapest way to convert (also called&nbsp; **rectify** ) AC to DC is to use a single diode. A diode is a simple electronic 'valve' - it only lets current flow one way. Since AC voltage cycles from positive to negative and we only want positive, we can connect it up so that the circuit only receives the&nbsp; **positive half** of the AC cycle.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/094/medium800/components_1n4001.jpg?1396768602)

You'll want to use a&nbsp;[power diode such as a 1N4001](http://www.adafruit.com/partfinder/diodes#power_blocking)&nbsp;, they're extremely common and can put up with a lot of abuse. The side with the silver stripe matches the schematic symbol side that the 'arrow' in the diode symbol is pointing to. That's the only direction that current can flow. The output is then chopped in half so that the voltage only goes positive.![](https://cdn-learn.adafruit.com/assets/assets/000/001/095/medium800/components_halfsch.png?1396768628)

This will convert![](https://cdn-learn.adafruit.com/assets/assets/000/001/096/medium800/components_ac.png?1396768656)

into![](https://cdn-learn.adafruit.com/assets/assets/000/001/097/medium800/components_halfwave.png?1396768684)

What we have now isnt really AC and isn't really DC, its this lumpy wave. The good news is that it's only positive voltage'd now, which means its safe to put a capacitor on it.

This is a 2200 microFarad (0.0022 Farad) capacitor, one leg has (-) signs next to it, this is the negative side. The other side is positive, and there should never be a voltage across is so that the negative pin is 'higher' than the positive pin or it'll go POOF!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/098/medium800/components_2200uf.jpg?1396768690)

A capacitor&nbsp; **smooths** &nbsp;the voltage out, taking out the lumps, sort of how spring shocks in car or mountain bike reduce the bumpiness of the road. Capacitors are great at this, but the big capacitors that are good at this (electrolytic) can't stand negative voltages - they'll explode!![](https://cdn-learn.adafruit.com/assets/assets/000/001/099/medium800/components_halfwavecapsch.png?1396768711)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/100/medium800/components_halfwavecap.png?1396768739)

Because the voltage is very uneven (big ripples), we need a really big electrolytic-type capacitor. How big? Well, [there's a lot of math behind it which you can read about](http://en.wikipedia.org/wiki/Ripple_%28electrical%29) but the rough formula you'll want to keep in mind is:

**Ripple voltage = Current draw / ( (Ripple frequency) \* (Capacitor size) )**

or written another way

**Capacitor size = Current draw / ( (Ripple frequency) \* (Ripple Voltage) )**

For a half wave rectifier (single diode) the frequency is 60 Hz (or 50 Hz in europe). The current draw is how much current your project is going to need, maximum. The ripple voltage is how much rippling there will be in the output which you are willing to live with and the capacitor size is in Farads.

So lets say we have a current draw of 50 mA and a maximum ripple voltage of 10mV we are willing to live with. For a half wave rectifier, the capacitor should be **at least** = 0.05 / (60 \* 0.01) = 0.085 Farads = **85,000 uF**! This is a **massive** and expensive capacitor. For that reason, its rare to see ripple voltages as low as 10mV. Its more common to see maybe 100mV of ripple and then some other technique to reduce the ripple, such as a linear regulator chip.

You don't have to memorize that formula, but you should keep the following in mind: When the current goes **up** and the capacitor stays the same, the ripple goes **up**. If the current goes **up** and you want the ripple the same, the capacitor must also **increase**.

## Full wave rectifiers
One thing that can be done to reduce the ripple/capacitor size by half is to use a full wave rectifier instead of a half wave. A full wave rectifier uses 4 diodes arranged in a peculiar way so that it both lets the positive voltage through&nbsp; **and** &nbsp;manages to 'flip over' the negative voltages into positive.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/101/medium800/components_fullsch.png?1396768764)

So now we get:![](https://cdn-learn.adafruit.com/assets/assets/000/001/102/medium800/components_fullwave.png?1396768790)

As you can see, there are twice as many humps - there isnt that "half the time, no voltage" thing going on. This means we can divide the calculated capacitor size to half of what it was in the previous.![](https://cdn-learn.adafruit.com/assets/assets/000/001/103/medium800/components_fullwavecap.png?1396768818)

Basically, a full wave rectifier is way better than a half wave! So why even talk about half-wave type rectifiers? Well, because they're useful for a few other purposes. In general, you're unlikely to see an AC/DC converter that uses a half wave as the cost of the diodes makes up for the saving in capacitor size and cost!## The transformer AC/DC in practice
![](https://cdn-learn.adafruit.com/assets/assets/000/001/104/medium800/components_9v200ma_t.jpg?1396768824)

OK now that we've reviewed transformers, diodes when used as rectifiers and big capacitors, lets look at a chunky plugpack again. This time, we'll look inside by cutting it in half! This power supply is rated at **9VDC @ 200mA.**

![](https://cdn-learn.adafruit.com/assets/assets/000/001/105/medium800/components_xformerpack_t.jpg?1396768827)

We can pull it out completely to see the circuit board parts.![](https://cdn-learn.adafruit.com/assets/assets/000/001/106/medium800/components_xformerpack2_t.jpg?1396768832)

Wow so this looks really familiar, right? From left to right, you can see the wires that come into the transformer from the wall plug, the transformer output has two power diodes on it and a big capacitor (2,200uF). You might be a little puzzled at the&nbsp; **two** &nbsp;diodes - shouldn't there be&nbsp; **four** &nbsp;for a full-wave rectifier? It turns out that&nbsp;[if you have a special transformer made with a 'center tap' (a wire that goes to the center) you can get away with using only two diodes](http://en.wikipedia.org/wiki/Full_wave_rectifier#Full-wave_rectification)&nbsp;. So it really is a full wave rectifier, just one with a center-tap transformer.

These transformer-based plug-packs are&nbsp; **really cheap** &nbsp;to make - like on the order of under $1!

## Testing the 9V supply
So now we will take a fresh power supply (don't use one you sawed in half, of course) and measure the output voltage with a multimeter.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/107/medium800/components_maswart_t.jpg?1396768835)

Yow! 14V? That's not anything like the 9V on the package, is this a broken wall wart? No! Its totally normal! Transformer-based wall adapters are not designed to have precision outputs. For one thing, the transformer, if you remember, is made of coils of wire. The coils for the most part act like inductors but they still have some small resistance. For example, if the coil is 10 ohms of resistance, then 200 mA of current will cause V = I \* R = (0.2 Amps) \* (10 ohms) = 2 Volts to be lost just in the copper winding! Another thing that causes losses is the metal core of the transformer becomes less efficient as the amount of current being transformed increases. Altogether, there are many inefficiencies that will make the output fluctuate. In general, the output can be as high as&nbsp; **twice** &nbsp;the 'rated' voltage when there is less than 10mA of current being drawn.## Let's look in detail
Lets look on an oscilloscope, that way we can see in detail what is going on.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/108/medium800/components_9vopen.jpg?1396768838)

With no current being drawn on the supply, the voltage output is about 14V![](https://cdn-learn.adafruit.com/assets/assets/000/001/109/medium800/components_150ohm.jpg?1396768847)

When I connected a 100 ohm resistor (110 mA draw) from the positive pin to the negative pin, it dropped to 11.2V![](https://cdn-learn.adafruit.com/assets/assets/000/001/110/medium800/components_100ohm.jpg?1396768851)

Connecting a 60 ohm resistor (~160 mA draw), it goes down to 10.3V![](https://cdn-learn.adafruit.com/assets/assets/000/001/111/medium800/components_60ohm.jpg?1396768857)

With 35 ohms (230 mA draw) the voltage plummets to 7.7V!

As the resistance gets smaller and smaller, the current draw gets higher and higher and the voltage&nbsp; **droops** &nbsp;(that's the technical term for it!) You can also see the ripple increase as the current goes up.

Now we can at least understand the thinking behind saying "9V 200mA" on the label. As long as we are drawing&nbsp; **less than 200mA** &nbsp;the voltage will be&nbsp; **higher than 9V.**

## What does this mean for you?

OK so after all that work, you're wondering why does this even matter? The reason it matters is that everywhere you look are these wall warts that are 'unregulated' and thus extremely suspicious. You simply can't trust 'em to give you the voltage you want!

For example, let's say you have a microcontroller project and it requires 5V power as many DIY projects do. You shouldn't go out and buy a 5V transformer supply like the one above and just stick the power output into your microcontroller - you'll destroy it! Instead, you will need to build a 5V regulator like the common LM7805 that will take the somewhere-around-9V from the transformer and convert it to a nice steady 5V with almost no ripple.

So here is what you should always do:

1. Always check your power supply brick with a multimeter to see what the maximum voltage is
2. Assume that the voltage can be twice as high as you expect
3. Assume that the voltage will droop as you draw more and more current
4. If you're using a brick for low-power usage, say your circuit draws 100mA max, find one that has a very similar current rating.

You might be wondering well why on earth doesn't someone make a power plug that takes a transformer and some diodes and a LM7805 and that will give you a nice 5V output instead of having everyone build it into the project circuit? While it's an interesting idea there are a few reasons they don't do that. One is that the enclosed wall adapter would overheat. Another is that some projects need more than one voltage, say 5V and 3.3V both. But in the end, its probably for manufacturing simplicity. The factory that makes the wall plugs makes 100's of thousands in predictable sizes and rates, each country has plenty of factories to make the right plug packs for the wall voltage and plug style. The designers of, say, the DVD player have an easier time of it when they can just say "anything above 7V and below 20V input will work for us" and the plug-pack maker matches them up with the closest thing they already make.

Nowadays, there are switch-mode power plugs that solve much of this problem. They are thinner and lighter than transformers and have almost no heating problems so they can have precise outputs that don't fluctuate. However, circuit-wise they are much more complex which means they're also much more expensive than transformer-supplies, perhaps 5-10x the price, and have a downside that they're 'noisier' electrically. But, because the parts and assembly cost is going down, they're much more popular than they were even 10 years ago.

- [Previous Page](https://learn.adafruit.com/power-supplies/overview.md)

## Featured Products

### 12V 5A switching power supply

[12V 5A switching power supply](https://www.adafruit.com/product/352)
This is a beefy switching supply, for when you need a lot of power! It can supply 12V DC up to 5 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard 'figure-8'...

Out of Stock
[Buy Now](https://www.adafruit.com/product/352)
[Related Guides to the Product](https://learn.adafruit.com/products/352/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)
### 5V 1A (1000mA) USB port power supply - UL Listed

[5V 1A (1000mA) USB port power supply - UL Listed](https://www.adafruit.com/product/501)
Need a USB jack for charging or powering a project, but don't want to lug around a computer? This switching supply gives a clean regulated output at up to 1000mA! 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but...

In Stock
[Buy Now](https://www.adafruit.com/product/501)
[Related Guides to the Product](https://learn.adafruit.com/products/501/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 9 VDC 1000mA regulated switching power adapter - UL listed

[9 VDC 1000mA regulated switching power adapter - UL listed](https://www.adafruit.com/product/63)
This is a really nice power supply. It's a switching DC supply so it's small and light and efficient. It is thin so it fits in power strips without blocking other outlets. The output is regulated so you'll get a steady 9V up to 1000mA (1 Amp) of current draw. 5.5mm/2.1mm barrel...

Out of Stock
[Buy Now](https://www.adafruit.com/product/63)
[Related Guides to the Product](https://learn.adafruit.com/products/63/guides)

## Related Guides

- [Adafruit 16 Channel Servo Driver with Raspberry Pi](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi.md)
- [Adafruit PCA9548 8-Channel STEMMA QT / Qwiic I2C Multiplexer](https://learn.adafruit.com/adafruit-pca9548-8-channel-stemma-qt-qwiic-i2c-multiplexer.md)
- [Adafruit Motor Selection Guide](https://learn.adafruit.com/adafruit-motor-selection-guide.md)
- [Boomy Pi Airplay Boombox](https://learn.adafruit.com/boomy-pi-airplay.md)
- [Digital Circuits 3: Combinational Circuits](https://learn.adafruit.com/combinational-logic.md)
- [Digital Circuits 6: An EPROM Emulator](https://learn.adafruit.com/digital-circuits-6-eprom-emulator.md)
- [Adafruit TPS65131 Split Power Supply Boost Converter](https://learn.adafruit.com/adafruit-tps65131-split-power-supply-boost-converter.md)
- [Digital Circuits 4: Sequential Circuits](https://learn.adafruit.com/digital-circuits-4-sequential-circuits.md)
- [Piezo Ring Tones with Raspberry Pi](https://learn.adafruit.com/piezo-ring-tones-with-raspberry-pi.md)
- [All About Stepper Motors](https://learn.adafruit.com/all-about-stepper-motors.md)
- [Motion-Activated Solder Fume Extractor With Lamp](https://learn.adafruit.com/motion-activated-solder-fume-extractor-with-lamp.md)
- [Adafruit bq25185 USB / DC / Solar Charger with 5V Boost Board](https://learn.adafruit.com/adafruit-bq25185-usb-dc-solar-charger-with-5v-boost-board.md)
- [Secret Knock Activated Drawer Lock](https://learn.adafruit.com/secret-knock-activated-drawer-lock.md)
- [All About Batteries](https://learn.adafruit.com/all-about-batteries.md)
- [Adafruit SPI FRAM Breakouts](https://learn.adafruit.com/adafruit-spi-fram-breakout.md)
