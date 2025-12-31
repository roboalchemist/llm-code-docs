# Source: https://learn.adafruit.com/li-ion-and-lipoly-batteries/protection-circuitry.md

# Li-Ion & LiPoly Batteries

## Protection Circuitry

Lithium ion/polymer batteries are extremely power dense. This makes them great for reducing size and weight of projects. However, they are not 'safe' batteries and require extra care. Charging or using the batteries incorrectly can cause explosion or fire (as shown by this and many other youtube videos).

http://www.youtube.com/watch?v=YCWdnjLqVWw&amp;feature=player_embedded

There are five main things to watch for when charging and using batteries:

- Do not charge them **above** their maximum safe voltage (say 4.2V) - usually taken care of by any on-cell protection circuit  
- Do not discharge them **below** their minimum safe voltage (say 3.0V) - usually taken care of by any on-cell protection circuit
- Do not **draw more current** than the battery can provide (say about 1-2 **C** ) - usually taken care of by any on-cell protection circuit
- Do not **charge them with more current** than the battery can take (say about 1 **C** ) - usually taken care of by any on-cell protection circuit but also set with the charger by adjusting the charge rate  
- Do not charge the batteries **above or below** certain temperatures (usually about 0-50 degrees C) - sometimes handled by the charger, but often not an issue as long as the charge rate is reasonable.  

For specifics on each battery you must look at the datasheet to know what the safe voltages, currents and temperatures are - they can vary from cell to cell.

For the first 3 items, a circuit board attached to the battery can monitor the battery voltage and the current going out. These are often referred to simply as **protection circuits**. They are very common on standard batteries but **you must check the datasheet**  **or product image** to verify that a protection circuit is attached

On the batteries we sell, the protection circuit is soldered onto the battery and then taped into the little cavity at the top of the battery. This is very common for lipoly cells.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/981/medium800/components_protcells.jpg?1396767563)

If you don't see any taped circuit board, the cell may be 'raw' - these raw cells&nbsp; **are not** &nbsp;protected!![](https://cdn-learn.adafruit.com/assets/assets/000/000/982/medium800/components_Lipo-3-7V-3000mah-30125-1.jpg?1396767570)

Danger: 

- [Previous Page](https://learn.adafruit.com/li-ion-and-lipoly-batteries/voltages.md)
- [Next Page](https://learn.adafruit.com/li-ion-and-lipoly-batteries/rc-type-batteries.md)

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
