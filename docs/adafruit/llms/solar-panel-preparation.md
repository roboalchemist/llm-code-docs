# Source: https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/solar-panel-preparation.md

# USB, DC & Solar Lipoly Charger

## Solar Panel Preparation

## Splice or Adapt?

The first verison of the solar charger came with a 4mm DC barrel jack on it. On older versions (4mm) it would come with a converter cable.

- If you have a newer v2 charger (June 2013+), connect a [2.1mm Terminal Block Adapter](http://www.adafruit.com/products/369 "Link: http://www.adafruit.com/products/369") onto the panel using basic wires, or a&nbsp;[1.3mm to 2.1mm adapter cable](https://www.adafruit.com/products/2788) then plug that into the 2.1mm adapter. This is the fastest method

- If you have an older v1 charger, you can use the terminal block method above OR cut the adapter cable in half and splice the 4mm connector onto the panel. The panel will plug right into the board but its more work.

# Voltaic Panels with 1.3mm Connectors

[Grab one of our adapter cables, it will let you plug in the solar panel directly](https://www.adafruit.com/products/2788)

![](https://cdn-learn.adafruit.com/assets/assets/000/028/817/medium800/projects_2788-00.jpg?1448988501)

# Other 6V Solar Panels

If you have a panel with something other than 2.1mm or 1.3mm connector, you'll need to remove any existing connector. Cut off whatever connector is on

![](https://cdn-learn.adafruit.com/assets/assets/000/001/494/medium800/projects_cutconnector.jpeg?1396773442)

Gently remove the outer casing without nipping the inner wires.![](https://cdn-learn.adafruit.com/assets/assets/000/001/495/medium800/projects_strippanel.jpeg?1396773450)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/496/medium800/projects_solarstripped.jpeg?1396773451)

Strip and tin the inner wires.![](https://cdn-learn.adafruit.com/assets/assets/000/001/497/medium800/projects_solarstrip2.jpeg?1396773456)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/498/medium800/projects_solartin.jpeg?1396773463)

## Method 1
For this you'll need a [2.1mm Terminal Block Adapter](http://www.adafruit.com/products/369) but its really simple. Just open up the screw terminals, slide the red wire into the + hole and the black wire into the - hole and retighten! Now you can just plug it directly into the charger (or adapter cable).  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/499/medium800/projects_21mmterm_t.jpeg?1396773469)

# If You Have a Pre-2013 Solar Charger

This method is a little tougher, but results in a nicer cable. You'll need some heatshrink as well as some item with a 2.1mm DC barrel plug (like the 2.1mm adapter)

Cut off anything on the opposite end.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/500/medium800/projects_deconnect.jpeg?1396773477)

And carefully strip off the outer sheath.![](https://cdn-learn.adafruit.com/assets/assets/000/001/501/medium800/projects_solarstripping.jpeg?1396773484)

You'll want some longer wires on this side, maybe 1.5" (3-4 cm).![](https://cdn-learn.adafruit.com/assets/assets/000/001/502/medium800/projects_solarsheath.jpeg?1396773492)

Strip just the ends of the wires and tin them.![](https://cdn-learn.adafruit.com/assets/assets/000/001/503/medium800/projects_solarstrip.jpeg?1396773499)

Place a big piece of heatshrink onto the cable, and then two shorter and smaller pieces on each of the wires.![](https://cdn-learn.adafruit.com/assets/assets/000/001/504/medium800/projects_solartinned.jpeg?1396773506)

Solder red to red and black to black, keep the heatshrink away from your soldering iron since it may shrink too fast!![](https://cdn-learn.adafruit.com/assets/assets/000/001/505/medium800/projects_jig.jpeg?1396773514)

![](https://cdn-learn.adafruit.com/assets/assets/000/001/506/medium800/projects_splice.jpeg?1396773522)

After the solder cools off, pull the smaller shrink onto the wires and heatshrink them!![](https://cdn-learn.adafruit.com/assets/assets/000/001/507/medium800/projects_minisolarshrink.jpeg?1396773531)

Then pull the big piece over everything!![](https://cdn-learn.adafruit.com/assets/assets/000/001/508/medium800/projects_bigheatshrink.jpeg?1396773538)

And heatshrink it (with a hot air gun if you have one, or carefully with a lighter if you don't).![](https://cdn-learn.adafruit.com/assets/assets/000/001/509/medium800/projects_shrinking.jpeg?1396773546)

That's it! Check with a multimeter, in the sun, to verify that you have a open circuit voltage on the plug.![](https://cdn-learn.adafruit.com/assets/assets/000/001/510/medium800/projects_done_t.jpeg?1396773551)

- [Previous Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/solar-charger-preparation.md)
- [Next Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/using-the-charger.md)

## Featured Products

### Lithium Ion Battery Pack - 3.7V 4400mAh

[Lithium Ion Battery Pack - 3.7V 4400mAh](https://www.adafruit.com/product/354)
Need a big battery for your project? This lithium-ion pack is made of 2 balanced 2200mAh cells for a total of 4400mA capacity! The cells are connected in parallel and spot-welded to a protection circuit that provides over-voltage, under-voltage, and over-current protection.

Each cell can...

In Stock
[Buy Now](https://www.adafruit.com/product/354)
[Related Guides to the Product](https://learn.adafruit.com/products/354/guides)
### USB / DC / Solar Lithium Ion/Polymer charger

[USB / DC / Solar Lithium Ion/Polymer charger](https://www.adafruit.com/product/390)
Make your projects to go green this summer with our specialized USB/Solar Lithium Ion Polymer Battery charger! This charger is a very unique design, perfect for outdoor projects, or DIY iPod chargers. We've spent over a year testing and tinkering with this charger to come up with a plug...

In Stock
[Buy Now](https://www.adafruit.com/product/390)
[Related Guides to the Product](https://learn.adafruit.com/products/390/guides)
### Lithium Ion Polymer Battery - 3.7v 1200mAh

[Lithium Ion Polymer Battery - 3.7v 1200mAh](https://www.adafruit.com/product/258)
Lithium-ion polymer (also known as 'lipo' or 'lipoly') batteries are thin, light, and powerful. The output ranges from 4.2V when completely charged to 3.7V. This battery has a capacity of 1200mAh for a total of about 4.5 Wh. If you need a larger battery, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/258)
[Related Guides to the Product](https://learn.adafruit.com/products/258/guides)
### Male DC Power adapter - 2.1mm plug to screw terminal block

[Male DC Power adapter - 2.1mm plug to screw terminal block](https://www.adafruit.com/product/369)
If you need to connect a battery pack or wired power supply to a board that has a DC jack - this adapter will come in very handy! There is a 2.1mm DC plug on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/369)
[Related Guides to the Product](https://learn.adafruit.com/products/369/guides)
### MintyBoost Kit

[MintyBoost Kit](https://www.adafruit.com/product/14)
The world's first and only open-source hardware charger: The MintyBoost®!  
  
**New version!** Works with the new iPhone 4 & 5 and more! **Please review the [Minty Boost project page(s)](//learn.adafruit.com/minty-boost) before purchase and...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/14)
[Related Guides to the Product](https://learn.adafruit.com/products/14/guides)
### 10K Precision Epoxy Thermistor

[10K Precision Epoxy Thermistor](https://www.adafruit.com/product/372)
Need to measure something damp? This epoxy-coated precision 1% 10K thermistor is an inexpensive way to measure temperature in weather or liquids. The resistance in 25 °C is 10K (+- 1%). The resistance goes down as it gets warmer and goes up as it gets cooler. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/372)
[Related Guides to the Product](https://learn.adafruit.com/products/372/guides)
### Large 6V 3.7W Solar Panel

[Large 6V 3.7W Solar Panel](https://www.adafruit.com/product/417)
Harness even more power from the sun with this nice big solar panel. We had these custom made for us when customers let us know they needed more than what our 2W panel could provide. This panel is a 12-cell (6V) assembly mounted onto a fiberglass PCB and covered with PET plastic which protects...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/417)
[Related Guides to the Product](https://learn.adafruit.com/products/417/guides)
### Large 6V 3.5W Solar panel

[Large 6V 3.5W Solar panel](https://www.adafruit.com/product/500)
These panels come to us from Voltaic Systems, makers of fine solar-powered bags and packs. These are waterproof, scratch resistant, and UV resistant. They use a high efficiency monocrystalline cell. They output 6V at 530 mA via 3.5mm x 1.1mm DC jack connector - a nice upgrade to the 2W panels...

Out of Stock
[Buy Now](https://www.adafruit.com/product/500)
[Related Guides to the Product](https://learn.adafruit.com/products/500/guides)

## Related Guides

- [Collin's Lab: Solar](https://learn.adafruit.com/collins-lab-solar.md)
- [Compost Friend!](https://learn.adafruit.com/compost-optimization-machine.md)
- [Portable Solar Charging Tracker](https://learn.adafruit.com/portable-solar-charging-tracker.md)
- [Mailbox Notification Service](https://learn.adafruit.com/mailbox-notification-service.md)
- [Solar Charging Handbag](https://learn.adafruit.com/solar-charging-handbag.md)
- [Solar Boost Bag](https://learn.adafruit.com/solar-boost-bag.md)
- [Adafruit MCP4728 I2C Quad DAC](https://learn.adafruit.com/adafruit-mcp4728-i2c-quad-dac.md)
- [Adafruit LiIon or LiPoly Charger BFF Add-On for QT Py](https://learn.adafruit.com/adafruit-qt-py-charger-bff.md)
- [Adafruit TPS61169 Constant Current Boost Converter for LEDs](https://learn.adafruit.com/adafruit-tps61169-constant-current-boost-converter-for-leds.md)
- [Adafruit MAX17048 LiPoly / LiIon Fuel Gauge and Battery Monitor](https://learn.adafruit.com/adafruit-max17048-lipoly-liion-fuel-gauge-and-battery-monitor.md)
- [Magical Light-up Dreidel](https://learn.adafruit.com/magical-light-up-dreidel.md)
- [Adafruit USB Type C Power Delivery Switchable Breakout](https://learn.adafruit.com/adafruit-usb-type-c-power-delivery-switchable-breakout.md)
- [Controlling Devices with RFID Wiz](https://learn.adafruit.com/controlling-devices-with-rfid-wiz.md)
- [Adafruit INA23x DC Current Voltage Power Monitor](https://learn.adafruit.com/adafruit-ina237-dc-current-voltage-power-monitor.md)
- [Adafruit TPL5110 Power Timer Breakout](https://learn.adafruit.com/adafruit-tpl5110-power-timer-breakout.md)
