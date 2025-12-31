# Source: https://learn.adafruit.com/li-ion-and-lipoly-batteries/proper-charging.md

# Li-Ion & LiPoly Batteries

## Proper Charging

Now that you know how best to use your lithium ion/polymer battery, we'll finish up by making sure you know how to charge the battery. We'll have a longer tutorial for our chargers at some point but we want to get people started with how to best use our chargers!

As we mentioned before,&nbsp; **you must use a proper lithium ion/polymer&nbsp;** battery charger. The good news is that nearly all batteries you will encounter are going to be 4.2V. And you can use a 4.2V charger for both lithium ion and lithium ion polymer. If you ever encounter a 4.35V battery, you can always use a 4.2V charger: it'll charge it up to 4.2V which is perfectly safe.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/000/medium800/components_chargers.gif?1447976688)

We carry two chargers in our store (at this time). A USB charger and a USB/DC charger. The USB charger is meant for charging single cells from a USB port that can provide 500mA or so. The USB/DC charger is meant for charging batteries from a USB port&nbsp; **or** &nbsp;a DC power supply up to 12V. The latter is more flexible, but more expensive because of the added circuitry.

You'll note that both have battery ports on the bottom (Labeled Battery In and Out) and charging ports at the top (USB on the left and USB + DC on the right)

To connect the battery, simply plug it into the&nbsp; **BATTERY IN** &nbsp;slot.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/001/medium800/components_battplug.gif?1447976698)

If you want to use the battery while also having it connected to the charger (less plugging and unplugging that way) you can simply use the&nbsp; **BATTERY OUT** &nbsp;connecion on the right. The&nbsp; **IN&nbsp;** and&nbsp; **OUT** &nbsp;ports are connected together on the circuit board so it acts as a&nbsp;_pass-through_

To charge, connect a power supply to the top of the board.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/002/medium800/components_charging.gif?1447976708)

The **PWR** red LED on either board will light up to let you know its powered properly. While charging, an LED will also be lit. For the USB only charger, a green done LED will light when the battery is full. For the USB/DC charger, the charging LED will blink slowly (once every few seconds).

You can change the charge rate of each charger by soldering a resistor into slot **R4** (for the USB charger) or **RPROG** (the USB/DC charger).

**The max charge rate of the USB charger is about 1000 mA**. To acheive this charge rate, you can either solder a **2.0K** resistor on top of **R4** (default 2K) - this will make the total parallel restance 1.0K or you can remove **R4** by desoldering it or cutting the trace to it and solder a 1.0K resistor in its place.

**The max charge rate of the USB/DC charger is about 1200 mA**. To acheive this charge rate, you should solder a wire (short) on top of **RPROG** (default 4.7K). You can also change the rate to a different value by either soldering a resistor on top of **RPROG** (and calculating the parallel resistance) or removing the resistor and soldering a different one in its place. [See the schematic for what values result in what charge rates](http://www.adafruit.com/datasheets/mcp73861.png).

[For other values, use a parallel resistor calculator such as this one.](http://www.sengpielaudio.com/calculator-paralresist.htm "Link: http://www.sengpielaudio.com/calculator-paralresist.htm") Put the desired resistance in **Rtotal** and the current resistance on the board into **R1** and then solder **R2** on top.

Info: 

- [Previous Page](https://learn.adafruit.com/li-ion-and-lipoly-batteries/multi-battery-packs.md)
- [Next Page](https://learn.adafruit.com/li-ion-and-lipoly-batteries/conclusion.md)

## Featured Products

### Adafruit Micro Lipo - USB LiIon/LiPoly charger

[Adafruit Micro Lipo - USB LiIon/LiPoly charger](https://www.adafruit.com/product/1304)
Oh so adorable, this is the tiniest little lipo charger, so handy you can keep it any project box! Its also easy to use. Simply plug in the gold plated contacts into any USB port and a 3.7V/4.2V lithium polymer or lithium ion rechargeable battery into the JST plug on the other end. There are...

In Stock
[Buy Now](https://www.adafruit.com/product/1304)
[Related Guides to the Product](https://learn.adafruit.com/products/1304/guides)
### USB LiIon/LiPoly charger

[USB LiIon/LiPoly charger](https://www.adafruit.com/product/259)
This is a Lithium Ion and Lithium Polymer battery charger based on the [MCP73833](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en027785). It uses a USB mini-B for connection to any computer or 'USB wall adapter'. Charging is performed in three stages: first a...

In Stock
[Buy Now](https://www.adafruit.com/product/259)
[Related Guides to the Product](https://learn.adafruit.com/products/259/guides)
### USB/DC  Lithium Polymer battery charger 5-12V

[USB/DC  Lithium Polymer battery charger 5-12V](https://www.adafruit.com/product/280)
Charge your single-cell lithium ion/polymer battery any which way you like with this board. Have a USB connection? No problem, just plug into the miniUSB connector. Only have a wall adapter? Any standard 2.1mm DC adapter which puts out 5 to 12VDC will work fine. If both are plugged in, the...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/280)
[Related Guides to the Product](https://learn.adafruit.com/products/280/guides)
### Lithium Ion Battery Pack - 3.7V 6600mAh

[Lithium Ion Battery Pack - 3.7V 6600mAh](https://www.adafruit.com/product/353)
Need a massive battery for your project? This lithium-ion pack is made of 3 balanced 2200mAh cells for a total of 6600mA capacity! The cells are connected in parallel and spot-welded to a protection circuit that provides over-voltage, under-voltage, and over-current protection.

Each cell...

In Stock
[Buy Now](https://www.adafruit.com/product/353)
[Related Guides to the Product](https://learn.adafruit.com/products/353/guides)
### Lithium Ion Battery Pack - 3.7V 4400mAh

[Lithium Ion Battery Pack - 3.7V 4400mAh](https://www.adafruit.com/product/354)
Need a big battery for your project? This lithium-ion pack is made of 2 balanced 2200mAh cells for a total of 4400mA capacity! The cells are connected in parallel and spot-welded to a protection circuit that provides over-voltage, under-voltage, and over-current protection.

Each cell can...

In Stock
[Buy Now](https://www.adafruit.com/product/354)
[Related Guides to the Product](https://learn.adafruit.com/products/354/guides)
### Lithium Ion Polymer Battery - 3.7v 2500mAh

[Lithium Ion Polymer Battery - 3.7v 2500mAh](https://www.adafruit.com/product/328)
Lithium-ion polymer (also known as 'lipo' or 'lipoly') batteries are thin, light, and powerful. The output ranges from 4.2V when completely charged to 3.7V. This battery has a capacity of **2500mAh** for a total of about 10 Wh. If you need a smaller battery, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/328)
[Related Guides to the Product](https://learn.adafruit.com/products/328/guides)
### Lithium Ion Polymer Battery - 3.7v 1200mAh

[Lithium Ion Polymer Battery - 3.7v 1200mAh](https://www.adafruit.com/product/258)
Lithium-ion polymer (also known as 'lipo' or 'lipoly') batteries are thin, light, and powerful. The output ranges from 4.2V when completely charged to 3.7V. This battery has a capacity of 1200mAh for a total of about 4.5 Wh. If you need a larger battery, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/258)
[Related Guides to the Product](https://learn.adafruit.com/products/258/guides)
### Lithium Ion Polymer Battery - 3.7v 500mAh

[Lithium Ion Polymer Battery - 3.7v 500mAh](https://www.adafruit.com/product/1578)
Lithium-ion polymer (also known as 'lipo' or 'lipoly') batteries are thin, light, and powerful. The output ranges from 4.2V when completely charged to 3.7V. This battery has a capacity of 500mAh for a total of about 1.9 Wh. If you need a larger (or smaller!) battery, <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/1578)
[Related Guides to the Product](https://learn.adafruit.com/products/1578/guides)

## Related Guides

- [Steven Universe Wearable, Fusable Gem](https://learn.adafruit.com/steven-universe-wearable-fusable-gem.md)
- [Gemma 3D Printed Tree Topper](https://learn.adafruit.com/gemma-3d-printed-tree-topper.md)
- [LOVE Light](https://learn.adafruit.com/love-light.md)
- [Make a Snow Globe with Circuit Playground Express & MakeCode](https://learn.adafruit.com/make-a-snowglobe-with-circuit-playground-makecode.md)
- [NeoPixel Basketball Hoop](https://learn.adafruit.com/neopixel-mini-basketball-hoop.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Easy Sparkle Pocket T-Shirt](https://learn.adafruit.com/easy-sparkle-pocket-t-shirt.md)
- [Haptic Headband](https://learn.adafruit.com/haptic-headband.md)
- [SNES EZ Key Bluefruit Game Pad](https://learn.adafruit.com/snes-ez-key-bluefruit-game-pad.md)
- [Chirping Plush Owl Toy](https://learn.adafruit.com/chirping-plush-owl-toy.md)
- [3D Printed Camera LED Ring](https://learn.adafruit.com/3d-printed-camera-led-ring.md)
- [Cartoon Network and Make Code - Rose Quartz Shield Umbrella](https://learn.adafruit.com/cartoon-network-and-make-code-rose-quartz-shield-umbrella.md)
- [Heart Rate Badge](https://learn.adafruit.com/heart-rate-badge.md)
- [Flora+NeoPixel LED Skateboard Upgrade](https://learn.adafruit.com/flora-neopixel-led-skateboard-upgrade.md)
- [Drama Piñata](https://learn.adafruit.com/customizable-reusable-pinata.md)
