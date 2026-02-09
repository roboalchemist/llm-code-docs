# Source: https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/using-the-charger.md

# USB, DC & Solar Lipoly Charger

## Using the Charger

## Solar Charging
![](https://cdn-learn.adafruit.com/assets/assets/000/034/576/medium800/projects_batt_solar.jpg?1470259447)

Solar charging is easy,&nbsp;[don't forget to prepare your solar panel and solder in the electrolytic capacitor beforehand!](http://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/solar-charger-preparation "Link: http://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/solar-charger-preparation")

Once you've done that, you can simply plug in the solar panel into the DC jack - look for the&nbsp; **PWR GOOD** LED to indicate that the solar panel is providing power and then plug the battery into the&nbsp; **BATT** slot in the left. Use only 3.7V/4.2V lithium ion/polymer batteries.

W[e have a tutorial about the batteries in case you have some questions about how to use them.](http://learn.adafruit.com/li-ion-and-lipoly-batteries)

When the **CHRG&nbsp;** charging light is lit, the battery is being charged. Make sure to have the panel facing direct sunlight&nbsp; **not** &nbsp;shaded and not behind any glass or plastic! when the battery is full, you'll see the green&nbsp; **DONE&nbsp;** LED light up.

## USB & DC Charging
Of course, sometimes is just really dark out and you can't solar charger, so there's a USB port on the board as well. Use any mini-B cable to plug in and charge.  
  
If there is something connected to the DC jack, it will mechanically disconnect the mini USB connector so be sure to unplug the solar panel when USB charging  
![](https://cdn-learn.adafruit.com/assets/assets/000/034/577/medium800/projects_usb_DC.jpg?1470259456)

You can also connect a DC wall plug adapter directly into the jack, just make sure its a 5.5mm/2.1mm inner diameter connector, which is very common!

![](https://cdn-learn.adafruit.com/assets/assets/000/001/514/medium800/projects_chumbypsp_MED.jpeg?1396773592)

If you need the DC power for something else, you can also connect to the DC input via the 0.1" breakout. While you can feed power into the breakout pins as well, it's not polarity protected so make sure you use a schottky diode or just be really careful.## Indicator LEDs
There are three status LEDs on the charger, which you'll find very handy!

The red&nbsp; **PWR** &nbsp;LED indicates that there is good power connected to the charger. If this LED is not lit, something is wrong with the power supply

The orange&nbsp; **CHRG** &nbsp;LED indicates current charging status. When this LED is lit, the charger is working to charge up a battery! It also acts as a low battery indicator (fixed at 3.1V) when no power is connected. So, if you don't have USB/Solar wired up, when the battery voltage drops below 3.1V, the orange LED will come on.

The green&nbsp; **DONE** &nbsp;LED is pretty easy to understand as well - when it's lit the battery is charged up! Very handy for when you want to know that everything is done.

If you need to connect larger LEDs or a microcontroller up to these status pins, you can us the STATUS 0.1" breakout on the bottom edge of the PCB. The pins are open drain, so they will short to ground when 'active' and float when 'inactive' - you'll want to use a pullup resistor if you need a digital signal or connect LEDs just like shown below on the schematic, if you want bigger lights.

![](https://cdn-learn.adafruit.com/assets/assets/000/001/515/medium800/projects_statLED.gif?1447864286)

# Load Sharing
The MCP73871 chip in the usb/solar charger has a very nifty feature called 'load sharing.' Say you have an every day lipoly charger and you want to use the battery _while_ its charging. To do this, you might connect the project directly to the battery output. This means, however, that the charger is both charging a battery and driving your project at the same time. The charger is working extra hard and the battery is being charged and discharged constantly.  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/516/medium800/projects_loadshare.gif?1447864287)

As an improvement, this design has a pass transistor inside the chip, connected to the output load from the input voltage, so that you dont lose efficiency from charging/discharging the battery. When the USB/Solar charger is powered from a USB port or panel, the load current goes directly from the input voltage to the output. If the current required is higher than what the panel or USB port can provide, the current is supplemented by the lipo battery, up to 1.8ADanger: 

![](https://cdn-learn.adafruit.com/assets/assets/000/034/578/medium800/projects_batt_load.jpg?1470259469)

This is all managed at the same time as the solar current maximization. Simply plug in the lipoly battery on the left into the&nbsp; **BATT** &nbsp;port and connect your project up thru the&nbsp; **LOAD** &nbsp;port on the right.## Temperature Monitoring
If you plan to have your project outside or unattended, we suggest adding temperature sensing to keep the charger from overheating the battery or attempting to charge when the battery is too hot or cold.  
![](https://cdn-learn.adafruit.com/assets/assets/000/034/579/medium800/projects_therm.jpg?1470259476)

Simply remove the 10K surface mount resistor from the&nbsp; **THERM** &nbsp;pads (or cut the trace going to it), and&nbsp;[solder in a 10K NTC thermistor](http://www.adafruit.com/products/372). Test out the system by trying to charge while you place the thermistor in a freezer or against some ice, as well as in a cup of \> 50°C hot water. The charger should stop charging the battery. Once you are sure it is working, attach the sensing element (the epoxy bulb in this case) so it is resting against the battery.## Adjusting the Max Charge Current
The USB/Solar charger comes with a preset rate of 500mA which will work great for USB ports, USB wall adapters and solar panels up to 3 Watts. If you have a project that uses a larger panel, or perhaps some other sort of setup, you can easily adjust the current by soldering a resistor into the&nbsp; **PROG** &nbsp;pads.  
![](https://cdn-learn.adafruit.com/assets/assets/000/034/580/medium800/projects_alt_progresistor.jpg?1470259496)

The current is set by 1000/ **RPROG** &nbsp;Amps, where&nbsp; **RPROG** &nbsp;is the resistance. So for 2 Kohms, that would make it 1000/2000 = 0.5 A = 500 mA. If you want 1A, you would use a 1K ohm resistor. If you want to_&nbsp;increase the current_, you need to&nbsp;_decrease the resistance_, so you can just solder&nbsp; **over** &nbsp;the existing 2K. So for example, soldering another 2K resistor into&nbsp; **RPROG&nbsp;** will give you 1K total resistance and 1000 mA current draw. See above for a 2.2K resistor soldered for about 950mA of max current draw. If you want to set the max current draw lower, you'll need to remove the 2K resistor.

# Adding External LEDs
  
If you are placing the charger in a box, you may want to have external LEDs for indicating charge state. This is easy! Simply use any 3mm, 5mm or 10mm LEDs you wish and 1K resistors and wire them like so:  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/537/medium800/projects_Charger_LEDs.png?1396773118)

- [Previous Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/solar-panel-preparation.md)
- [Next Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/design-notes.md)

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
