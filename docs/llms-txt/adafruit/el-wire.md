# Source: https://learn.adafruit.com/el-wire.md

# EL Wire

## Overview

https://www.youtube.com/watch?v=RJ2xGFfrND0

EL Wire, also known as Electroluminescent wire, is a stiff wire core coated with phosphor and then covered with a protective PVC sheath. When an AC signal is applied to it, it glows an aqua (blue green) color. Sometimes its covered with a colored plastic shell to make it appear another color. It looks a little like thin neon. Very bendable, it keeps its shape and you can curl it around your finger. Its an easy way to add some glow to a project, not as bright as LEDs but uses a lot less power!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/218/medium800/el_wire_tape_panel_Heating_Element.jpeg?1396761297)

It's often used for costuming, decoration, accent lighting, safety vests, bicycle/motorcycle/car/boat/home decoration, signs, etc. It's definitely the most popular wearable electronics we've seen since its so easily to use.

We have two EL project tutorials - the [TRON-inspired bag](http://learn.adafruit.com/tron-bag) and the [EL wire party couch](http://www.adafruit.com/blog/2012/03/19/how-to-el-wire-couch-video/ "Link: http://www.adafruit.com/blog/2012/03/19/how-to-el-wire-couch-video/") !

[You can pick up some high-brightness, long-life EL wire and inverters at the Adafruit shop](http://www.adafruit.com/index.php?main_page=index&cPath=50 "Link: http://www.adafruit.com/index.php?main\_page=index&cPath=50")

## Quickstart FAQ

- EL is 'cold' - the wires generate no heat!
- EL wire requires a driver/inverter that can provide 400-2000 Hz, 60-120VAC (that's RMS not peak-to-peak!)
- Higher frequency/voltage results in a brighter wire
- Running the wire brighter will lead to a reduced lifetime (how many hours it takes until its half-brightness)
- Our high-brightness/long-life EL wire can be driven at 100V/2000Hz for 3000 hours before it is half the original brightness
- EL wire is capacitive, and cannot be PWM'ed or easily dimmed (unless you can adjust the voltage/frequency of the inverter)
- The more wire you connect to an inverter, the more 'loaded' it is and the dimmer it will be
- Our AA pocket driver can drive about 2.5 meters before it starts dimming significantly. 2 meters is a good amount, 3 is OK but wont be as bright.
- If you 'split' and connect more than one piece of EL to an inverter, count the total length of all the pieces
- The AA inverter works best with fresh batteries, but you can use rechargables - it'll just be dimmer because the input voltage is lower.
- The capacitance 'load' of the EL is required to stabilize the inverter so&nbsp; **never run the inverter without at least 1 foot of EL attached!**

Danger: 

- [Next Page](https://learn.adafruit.com/el-wire/soldering-to-el-wire.md)

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
